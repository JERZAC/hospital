# HospitalTech - Requirements

## 1. Descripción del problema

HospitalTech es un sistema de soporte técnico para un entorno hospitalario.

En un hospital pueden presentarse diferentes incidentes relacionados con equipos
informáticos, redes, software, cuentas de usuario y otros servicios tecnológicos.

Cuando estos incidentes son registrados manualmente y sin clasificación,
el personal de soporte puede tener dificultades para determinar:

- El tipo de incidente.
- La prioridad.
- La acción recomendada.
- El seguimiento del ticket.
- El estado de atención.

El sistema HospitalTech busca centralizar estos incidentes mediante una aplicación
web que permita registrar usuarios, autenticar usuarios, crear tickets de soporte
y clasificarlos automáticamente.

---

# 2. Objetivos

El sistema debe permitir:

1. Registrar y autenticar usuarios.
2. Registrar tickets de soporte.
3. Clasificar automáticamente los tickets.
4. Calcular la prioridad de los incidentes.
5. Generar recomendaciones de atención.
6. Consultar los tickets registrados.
7. Proteger las operaciones mediante autenticación JWT.

---

# 3. Requisitos funcionales

## REQ-01 - Registro y autenticación de usuarios

El sistema deberá permitir que un usuario cree una cuenta utilizando:

- Nombre.
- Correo electrónico.
- Contraseña.

El usuario deberá poder iniciar sesión mediante sus credenciales.

### Criterios de aceptación

- El usuario puede registrarse correctamente.
- El correo electrónico debe ser único.
- No se permite registrar dos usuarios con el mismo correo.
- La contraseña no debe almacenarse en texto plano.
- El usuario puede iniciar sesión.
- El sistema genera un token JWT.
- El token permite acceder a endpoints protegidos.
- Un usuario no autenticado recibe una respuesta HTTP 401.

---

# REQ-02 - Gestión de tickets

El sistema deberá permitir a un usuario autenticado crear tickets
de soporte técnico.

Cada ticket debe contener como mínimo:

- Título.
- Descripción.
- Categoría.
- Prioridad.
- Recomendación.
- Usuario propietario.
- Fecha de creación.

### Criterios de aceptación

- Un usuario autenticado puede crear un ticket.
- El ticket se almacena en la base de datos.
- El ticket queda asociado al usuario que lo creó.
- El sistema devuelve el ticket creado.
- El usuario puede consultar sus tickets.
- Un usuario no autenticado no puede crear tickets.
- El sistema conserva la información del ticket después de reiniciar la aplicación.

---

# REQ-03 - Clasificación automática

El sistema deberá analizar el título y la descripción del ticket para
determinar automáticamente su categoría.

Las categorías principales serán:

- network
- hardware
- software
- accounts
- general

### Criterios de aceptación

Cuando el contenido de un ticket contenga palabras relacionadas con una
categoría, el sistema deberá asignar dicha categoría.

Ejemplos:

- "No tengo conexión a Internet" → network.
- "La computadora no enciende" → hardware.
- "Windows presenta errores" → software.
- "No puedo ingresar a mi cuenta" → accounts.
- Un problema que no coincida con las anteriores → general.

---

# REQ-04 - Cálculo de prioridad

El sistema deberá determinar la prioridad del ticket según las características
del incidente.

Las prioridades serán:

- low
- medium
- high
- critical

### Criterios de aceptación

- Los incidentes críticos deben recibir prioridad critical.
- Los incidentes importantes deben recibir prioridad high.
- Los incidentes normales deben recibir prioridad medium.
- Los incidentes de bajo impacto deben recibir prioridad low.

---

# REQ-05 - Recomendaciones

El sistema deberá generar una recomendación de atención basada en la categoría
y prioridad del ticket.

### Criterios de aceptación

- Un ticket de red debe generar una recomendación relacionada con conectividad.
- Un ticket de hardware debe generar una recomendación relacionada con revisión
  del equipo.
- Un ticket de software debe generar una recomendación relacionada con
  diagnóstico o reinstalación.
- Un ticket de cuentas debe generar una recomendación relacionada con
  credenciales o acceso.

---

# REQ-06 - Seguridad

Los endpoints protegidos deberán requerir autenticación.

### Criterios de aceptación

- Las solicitudes sin token son rechazadas.
- Los tokens inválidos son rechazados.
- El usuario autenticado se identifica mediante el JWT.
- Los tickets pertenecen al usuario que los creó.

---

# 4. Requisitos no funcionales

## RNF-01 - Seguridad

Las contraseñas deben almacenarse utilizando hashing.

## RNF-02 - Rendimiento

Las operaciones principales deben responder en tiempos adecuados para
una aplicación web de soporte.

## RNF-03 - Mantenibilidad

El backend debe mantener una separación entre:

- API.
- Modelos.
- Base de datos.
- Autenticación.
- Servicios.

## RNF-04 - Pruebas

Las funcionalidades principales deben contar con pruebas unitarias y de integración.

## RNF-05 - Documentación

El proyecto debe incluir:

- README.
- SDD.
- Architecture.
- Requirements.
- Design.
- Tasks.
- Documentación de pruebas.
