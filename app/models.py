from sqlalchemy import (
    String,
    Integer,
    Text,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from .database import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    full_name: Mapped[str] = mapped_column(
        String(120)
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        index=True
    )

    password_hash: Mapped[str] = mapped_column(
        String(255)
    )

    role: Mapped[str] = mapped_column(
        String(30),
        default="usuario"
    )

    tickets = relationship(
        "Ticket",
        back_populates="owner"
    )


class Ticket(Base):

    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        String(150)
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    department: Mapped[str] = mapped_column(
        String(100)
    )

    impact: Mapped[int] = mapped_column(
        Integer
    )

    urgency: Mapped[int] = mapped_column(
        Integer
    )

    category: Mapped[str] = mapped_column(
        String(50)
    )

    priority: Mapped[str] = mapped_column(
        String(30)
    )

    recommendation: Mapped[str] = mapped_column(
        Text
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="abierto"
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="tickets"
    )