#  HospitalTech AI

Sistema web de soporte técnico hospitalario que permite registrar, clasificar y gestionar incidentes tecnológicos mediante una API REST desarrollada con **FastAPI**, autenticación mediante **JWT**, persistencia con **SQLAlchemy/SQLite** y una interfaz web desarrollada con **HTML, CSS y JavaScript**.

---

##  Descripción del proyecto

En un entorno hospitalario, los equipos informáticos, sistemas, redes, impresoras y cuentas de usuario son componentes importantes para el funcionamiento de las diferentes áreas.

Cuando ocurre un incidente tecnológico, es necesario registrarlo, identificar su tipo, determinar su prioridad y proporcionar una orientación inicial para su atención.

**HospitalTech AI** centraliza este proceso mediante un sistema web que permite:

* Registrar usuarios.
* Iniciar sesión de forma segura.
* Autenticar usuarios mediante JWT.
* Crear tickets de soporte.
* Clasificar automáticamente los incidentes.
* Calcular la prioridad del ticket.
* Generar recomendaciones de atención.
* Consultar los tickets registrados.
* Aplicar control de acceso según el rol del usuario.

---

##  Objetivo del proyecto

Desarrollar una aplicación web para la gestión de incidentes de soporte técnico hospitalario que permita registrar problemas tecnológicos, clasificarlos automáticamente, determinar su prioridad y proporcionar recomendaciones para facilitar su atención.

---

##  Funcionalidades principales

###  Autenticación

El sistema implementa:

* Registro de usuarios.
* Inicio de sesión.
* Hashing de contraseñas.
* Generación de tokens JWT.
* Validación de tokens.
* Consulta del usuario autenticado.
* Protección de endpoints privados.

###  Gestión de tickets

Los usuarios autenticados pueden:

* Crear tickets.
* Consultar sus tickets.
* Consultar un ticket específico.
* Asociar automáticamente cada ticket con su propietario.

Los usuarios con rol `tecnico` pueden consultar todos los tickets registrados.

###  Clasificación automática

El sistema analiza el título y descripción del ticket y determina automáticamente una categoría.

Categorías disponibles:

| Categoría  | Ejemplos                                                 |
| ---------- | -------------------------------------------------------- |
| `red`      | Internet, WiFi, router, switch, conexión                 |
| `hardware` | Computadora, monitor, teclado, mouse, impresora          |
| `software` | Windows, programas, aplicaciones, errores                |
| `cuentas`  | Contraseña, usuario, cuenta, acceso                      |
| `general`  | Problemas que no coinciden con las categorías anteriores |

Ejemplo:

```text
Título:
Sin internet

Descripción:
La computadora perdió la conexión WiFi
```

Resultado:

```text
Categoría: red
```

###  Cálculo de prioridad

La prioridad se obtiene a partir de:

* Impacto.
* Urgencia.

Cada valor puede estar entre `1` y `3`.

| Impacto + Urgencia | Prioridad |
| -----------------: | --------- |
|                  6 | crítica   |
|              4 - 5 | alta      |
|                  3 | media     |
|                  2 | baja      |

Ejemplo:

```text
Impacto: 3
Urgencia: 3

Resultado: crítica
```

###  Recomendaciones

El sistema genera una recomendación inicial según la categoría detectada.

Ejemplos:

```text
red
→ Verificar cableado, WiFi, IP, gateway y switch.

hardware
→ Revisar alimentación, conexiones y periféricos.

software
→ Revisar error, permisos, servicios y registros.

cuentas
→ Verificar usuario, cuenta y permisos.
```

---

##  Arquitectura

El proyecto utiliza una arquitectura cliente-servidor:

```text
┌─────────────────────────────────────┐
│              FRONTEND               │
│                                     │
│       HTML / CSS / JavaScript       │
│                                     │
│  Login / Registro / Dashboard       │
└──────────────────┬──────────────────┘
                   │
                   │ HTTP / JSON
                   ▼
┌─────────────────────────────────────┐
│              FASTAPI                │
│                                     │
│             REST API                │
│                                     │
│  Auth       Users       Tickets      │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│        SERVICIOS DE NEGOCIO         │
│                                     │
│  Clasificación                      │
│  Cálculo de prioridad               │
│  Recomendaciones                    │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│             SQLAlchemy              │
│                 ORM                 │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│               SQLite                │
│          hospitaltech.db            │
└─────────────────────────────────────┘
```

---

##  Estructura del proyecto

```text
hospital/
│
├── app/
│   ├── auth.py              # Autenticación, JWT y contraseñas
│   ├── database.py          # Configuración de SQLAlchemy
│   ├── main.py              # Aplicación FastAPI y endpoints
│   ├── models.py            # Modelos User y Ticket
│   ├── schemas.py           # Schemas Pydantic
│   └── services.py          # Clasificación, prioridad y recomendaciones
│
├── frontend/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   ├── auth.js          # Login y registro
│   │   └── dashboard.js     # Dashboard y tickets
│   │
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── docs/
│   ├── architecture.md      # Arquitectura del sistema
│   ├── DEMO.md              # Guía de demostración
│   ├── git-workflow.md      # Flujo de trabajo Git
│   ├── problem-definition.md
│   ├── SDD.md               # Software Design Document
│   └── testing.md           # Documentación de pruebas
│
├── kiro/
│   └── specs/
│       └── hospitaltech/
│           ├── requiriments.md
│           ├── design.md
│           └── tasks.md
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_integration.py
│   ├── test_services.py
│   └── test_tickets.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── hospitaltech.db
├── GIT_WORKFLOW.md
├── README.md
└── LEAME.md
```

---

##  Tecnologías utilizadas

| Tecnología       | Uso                               |
| ---------------- | --------------------------------- |
| Python 3         | Lenguaje principal                |
| FastAPI          | Framework para la API REST        |
| Uvicorn          | Servidor ASGI                     |
| SQLAlchemy       | ORM y persistencia                |
| SQLite           | Base de datos                     |
| Pydantic         | Validación de datos               |
| python-jose      | Generación y validación de JWT    |
| Passlib + bcrypt | Hashing de contraseñas            |
| HTML             | Interfaz                          |
| CSS              | Estilos                           |
| JavaScript       | Comunicación con la API           |
| Pytest           | Pruebas automatizadas             |
| HTTPX            | Cliente utilizado por las pruebas |

---

##  Modelo de seguridad

La autenticación utiliza JWT.

El flujo principal es:

```text
Usuario
   │
   ▼
Registro
   │
   ▼
Contraseña → Hash bcrypt
   │
   ▼
Base de datos
```

Para iniciar sesión:

```text
Usuario + contraseña
        │
        ▼
   /auth/login
        │
        ▼
Validación de credenciales
        │
        ▼
     JWT Token
        │
        ▼
Frontend almacena token
        │
        ▼
Authorization: Bearer <token>
```

Los endpoints protegidos validan el token antes de permitir el acceso.

---

## Roles

Actualmente el sistema contempla los siguientes roles:

### `usuario`

Puede:

* Crear tickets.
* Consultar sus propios tickets.
* Consultar su información de usuario.

### `tecnico`

Puede:

* Crear tickets.
* Consultar tickets.
* Consultar tickets de otros usuarios.

El backend también contempla el rol `admin` para las comprobaciones de acceso a tickets.

> La versión actual no incluye todavía un panel administrativo ni endpoints específicos para administrar roles.

---

#  Instalación

## 1. Clonar el repositorio

```bash
git clone <URL-DE-TU-REPOSITORIO>
cd hospital
```

---

## 2. Crear entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Configurar variables de entorno

Crear un archivo `.env` tomando como referencia:

```text
.env.example
```

Ejemplo:

```env
DATABASE_URL=sqlite:///./hospitaltech.db
SECRET_KEY=cambiar-esta-clave-en-produccion
```

> No subir el archivo `.env` al repositorio.

---

# Ejecución

Desde la raíz del proyecto ejecutar:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

La documentación interactiva de FastAPI estará disponible en:

```text
http://127.0.0.1:8000/docs
```

También se puede acceder a la interfaz web mediante:

```text
http://127.0.0.1:8000/web
```

---

#  Endpoints principales

## Autenticación

| Método | Endpoint         | Descripción            | Autenticación |
| ------ | ---------------- | ---------------------- | ------------- |
| POST   | `/auth/register` | Registrar usuario      | No            |
| POST   | `/auth/login`    | Iniciar sesión         | No            |
| GET    | `/auth/me`       | Obtener usuario actual | Sí            |

## Tickets

| Método | Endpoint               | Descripción    | Autenticación |
| ------ | ---------------------- | -------------- | ------------- |
| POST   | `/tickets`             | Crear ticket   | Sí            |
| GET    | `/tickets`             | Listar tickets | Sí            |
| GET    | `/tickets/{ticket_id}` | Obtener ticket | Sí            |

---

#  Ejemplo de uso

## 1. Registrar usuario

```http
POST /auth/register
Content-Type: application/json
```

```json
{
  "full_name": "Usuario Hospital",
  "email": "usuario@hospital.local",
  "password": "Password123",
  "role": "usuario"
}
```

Respuesta:

```json
{
  "id": 1,
  "full_name": "Usuario Hospital",
  "email": "usuario@hospital.local",
  "role": "usuario"
}
```

---

## 2. Iniciar sesión

```http
POST /auth/login
Content-Type: application/json
```

```json
{
  "email": "usuario@hospital.local",
  "password": "Password123"
}
```

Respuesta:

```json
{
  "access_token": "<JWT>",
  "token_type": "bearer"
}
```

---

## 3. Crear un ticket

Enviar el token:

```http
Authorization: Bearer <JWT>
```

Solicitud:

```http
POST /tickets
Content-Type: application/json
```

```json
{
  "title": "Sin internet",
  "description": "La computadora perdió conexión WiFi",
  "department": "Emergencias",
  "impact": 3,
  "urgency": 3
}
```

El sistema calcula automáticamente:

```text
Categoría: red
Prioridad: crítica
Estado: abierto
Recomendación: Verificar cableado, WiFi, IP, gateway y switch.
```

---

#  Pruebas

El proyecto utiliza **Pytest**.

Ejecutar todas las pruebas:

```bash
python -m pytest -v
```

Ejecutar únicamente las pruebas de servicios:

```bash
python -m pytest tests/test_services.py -v
```

Ejecutar las pruebas de autenticación:

```bash
python -m pytest tests/test_auth.py -v
```

Ejecutar las pruebas de tickets:

```bash
python -m pytest tests/test_tickets.py -v
```

Las pruebas utilizan una base de datos SQLite independiente en memoria mediante `StaticPool`.

---

#  Flujo funcional completo

El funcionamiento principal del sistema es:

```text
             ┌──────────────┐
             │    Usuario   │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │   Registro   │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │     Login    │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │     JWT      │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ Crear Ticket │
             └──────┬───────┘
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
     Categoría   Prioridad  Recomendación
          │         │         │
          └─────────┼─────────┘
                    ▼
             ┌──────────────┐
             │  SQLite DB   │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │  Dashboard   │
             └──────────────┘
```

---

#  Documentación

La documentación técnica del proyecto se encuentra en:

| Documento                                 | Descripción                     |
| ----------------------------------------- | ------------------------------- |
| `docs/problem-definition.md`              | Definición del problema         |
| `docs/SDD.md`                             | Documento de diseño del sistema |
| `docs/architecture.md`                    | Arquitectura                    |
| `docs/testing.md`                         | Estrategia de pruebas           |
| `docs/DEMO.md`                            | Guía de demostración            |
| `docs/git-workflow.md`                    | Flujo de trabajo Git            |
| `kiro/specs/hospitaltech/requiriments.md` | Requisitos                      |
| `kiro/specs/hospitaltech/design.md`       | Diseño                          |
| `kiro/specs/hospitaltech/tasks.md`        | Tareas del proyecto             |

---

#  Requisitos del sistema

Se requiere:

* Python 3.10 o superior.
* `pip`.
* Navegador web.
* Git.

No es necesario instalar PostgreSQL para ejecutar la versión actual, ya que utiliza SQLite.

---

#  Consideraciones

La base de datos utilizada actualmente es:

```text
hospitaltech.db
```

Para un entorno de producción se recomienda utilizar PostgreSQL u otro sistema de base de datos apropiado.

También se recomienda utilizar una `SECRET_KEY` segura y almacenada mediante variables de entorno.

---

#  Mejoras futuras

Entre las mejoras previstas se encuentran:

* Panel administrativo.
* Gestión completa de roles.
* Gestión de técnicos.
* Cambio de estado de tickets.
* Asignación de tickets a técnicos.
* Historial de cambios.
* Fechas de creación y actualización.
* Notificaciones.
* Dashboard estadístico.
* Filtros y búsqueda de tickets.
* PostgreSQL para producción.
* Docker.
* CI/CD.
* Mayor cobertura de pruebas.
* Clasificación inteligente más avanzada.

---

# 👨‍💻 Proyecto académico

**HospitalTech AI**

Sistema web de soporte técnico hospitalario desarrollado como proyecto académico para demostrar:

* Desarrollo de APIs REST.
* Arquitectura cliente-servidor.
* Autenticación JWT.
* Persistencia con SQLAlchemy.
* Validación con Pydantic.
* Lógica de negocio.
* Desarrollo frontend.
* Pruebas automatizadas.
* Documentación técnica.
* Control de versiones con Git y GitHub.

---

## 📄 Licencia

Proyecto académico CRISTHIAN ANDRES JERE AREVALO.
