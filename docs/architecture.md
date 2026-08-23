# Arquitectura del sistema - HospitalTech

## 1. Arquitectura general

HospitalTech utiliza una arquitectura cliente-servidor.

El frontend se comunica con el backend mediante una API REST
desarrollada con FastAPI.

El backend procesa las solicitudes, ejecuta la lógica de negocio
y utiliza SQLAlchemy para acceder a la base de datos.

---

## 2. Componentes

### Frontend

Tecnologías:

- HTML
- CSS
- JavaScript

Responsabilidades:

- Mostrar la interfaz.
- Registrar usuarios.
- Iniciar sesión.
- Crear tickets.
- Consultar tickets.
- Consumir la API.

---

### Backend

Tecnología:

- FastAPI

Archivo principal:

```text
app/main.py
```
