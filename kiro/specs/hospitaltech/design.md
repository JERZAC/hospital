# HospitalTech - Design

## 1. Descripción general

HospitalTech utiliza una arquitectura cliente-servidor.

El sistema está dividido en:

1. Frontend.
2. API Backend.
3. Servicios de negocio.
4. Capa de autenticación.
5. Capa de persistencia.
6. Base de datos.

---

# 2. Arquitectura

```text
┌──────────────────────────────┐
│          FRONTEND            │
│                              │
│ HTML / CSS / JavaScript      │
└──────────────┬───────────────┘
               │
               │ HTTP / JSON
               │
               ▼
┌──────────────────────────────┐
│           FASTAPI            │
│                              │
│       API REST               │
├──────────────────────────────┤
│ Authentication               │
│ Users                        │
│ Tickets                      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       BUSINESS SERVICES      │
├──────────────────────────────┤
│ Classification               │
│ Priority                     │
│ Recommendation               │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          SQLAlchemy          │
│       ORM / Persistence      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│           SQLite             │
│        hospitaltech.db       │
└──────────────────────────────┘
```
