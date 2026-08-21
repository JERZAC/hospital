from pydantic import BaseModel, EmailStr, Field


# ==========================================
# AUTH
# ==========================================

class RegisterRequest(BaseModel):

    full_name: str = Field(
        min_length=2,
        max_length=120
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=100
    )

    role: str = "usuario"


class LoginRequest(BaseModel):

    email: EmailStr

    password: str


class UserResponse(BaseModel):

    id: int

    full_name: str

    email: EmailStr

    role: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):

    access_token: str

    token_type: str


# ==========================================
# TICKETS
# ==========================================

class TicketCreate(BaseModel):

    title: str = Field(
        min_length=3,
        max_length=150
    )

    description: str = Field(
        min_length=5
    )

    department: str = Field(
        min_length=2,
        max_length=100
    )

    impact: int = Field(
        ge=1,
        le=3
    )

    urgency: int = Field(
        ge=1,
        le=3
    )


class TicketResponse(TicketCreate):

    id: int

    category: str

    priority: str

    recommendation: str

    status: str

    owner_id: int

    class Config:
        from_attributes = True