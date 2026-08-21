# app/main.py
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


from .auth import (
    create_access_token,
    get_current_user,
    get_db,
    hash_password,
    verify_password,
)
from .database import Base, engine
from .models import Ticket, User
from .schemas import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    TicketCreate,
    TicketResponse,
    UserResponse,
)
from .services import (
    calculate_priority,
    classify_ticket,
    recommend_solution,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HospitalTech AI",
    description="Sistema inteligente de soporte técnico hospitalario",
    version="2.0.0",
)

app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)


@app.get("/web")
def web():

    return FileResponse(
        "frontend/login.html"
    )

@app.get("/")
def root():
    return {
        "message": "HospitalTech AI funcionando"
    }


# =====================================================
# AUTH - REGISTER
# =====================================================

@app.post(
    "/auth/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing = db.query(User).filter(
        User.email == payload.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="El correo ya está registrado"
        )

    role = payload.role

    if role not in {"usuario", "tecnico"}:
        role = "usuario"

    user = User(
        full_name=payload.full_name,
        email=payload.email,
        password_hash=hash_password(
            payload.password
        ),
        role=role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# =====================================================
# AUTH - LOGIN
# =====================================================

@app.post(
    "/auth/login",
    response_model=TokenResponse
)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == payload.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )

    if not verify_password(
        payload.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )

    token = create_access_token(user.id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# =====================================================
# AUTH - USUARIO ACTUAL
# =====================================================

@app.get(
    "/auth/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(
        get_current_user
    )
):

    return current_user


# =====================================================
# TASK / TICKET - CREAR
# =====================================================

@app.post(
    "/tickets",
    response_model=TicketResponse,
    status_code=201
)
def create_ticket(
    payload: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    # Inteligencia

    category = classify_ticket(
        payload.title,
        payload.description
    )

    priority = calculate_priority(
        payload.impact,
        payload.urgency
    )

    recommendation = recommend_solution(
        category
    )

    # Crear ticket

    ticket = Ticket(
        **payload.model_dump(),

        category=category,

        priority=priority,

        recommendation=recommendation,

        status="abierto",

        owner_id=current_user.id
    )

    db.add(ticket)

    db.commit()

    db.refresh(ticket)

    return ticket


# =====================================================
# TASKS - LISTAR
# =====================================================

@app.get(
    "/tickets",
    response_model=list[TicketResponse]
)
def list_tickets(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    # Técnicos pueden ver todos

    if current_user.role in {
        "admin",
        "tecnico"
    }:

        return db.query(
            Ticket
        ).order_by(
            Ticket.id.desc()
        ).all()

    # Usuario normal solamente sus tickets

    return db.query(
        Ticket
    ).filter(
        Ticket.owner_id == current_user.id
    ).order_by(
        Ticket.id.desc()
    ).all()


# =====================================================
# TASK - OBTENER POR ID
# =====================================================

@app.get(
    "/tickets/{ticket_id}",
    response_model=TicketResponse
)
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    ticket = db.get(
        Ticket,
        ticket_id
    )

    if not ticket:

        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado"
        )

    # Seguridad

    if (
        current_user.role
        not in {"admin", "tecnico"}
        and ticket.owner_id
        != current_user.id
    ):

        raise HTTPException(
            status_code=403,
            detail="No tienes permiso"
        )

    return ticket