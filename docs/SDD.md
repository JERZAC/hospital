# SDD - HospitalTech

## 1. Información general

**Nombre del proyecto:** HospitalTech

**Tipo:** Sistema web de soporte técnico hospitalario.

**Tecnologías principales:**

- Python
- FastAPI
- SQLAlchemy
- SQLite
- HTML
- CSS
- JavaScript
- JWT
- Pytest

---

# 2. Definición del problema

En un entorno hospitalario pueden presentarse diferentes incidentes
relacionados con infraestructura tecnológica, equipos informáticos,
redes, software y cuentas de usuario.

Cuando estos problemas no se registran y clasifican correctamente,
el personal de soporte puede tener dificultades para determinar la
prioridad del incidente y la acción que debe realizarse.

HospitalTech busca solucionar esta situación mediante un sistema web
que permita registrar, clasificar y gestionar tickets de soporte
técnico.

---

# 3. Objetivo general

Desarrollar un sistema web de soporte técnico que permita registrar
incidentes tecnológicos, clasificarlos automáticamente, determinar
su prioridad y generar recomendaciones para facilitar la atención
por parte del personal de soporte.

---

# 4. Usuarios

El sistema contempla principalmente:

### Usuario

Puede:

- Registrarse.
- Iniciar sesión.
- Crear tickets.
- Consultar sus tickets.

### Personal de soporte

Puede utilizar la información de los tickets para identificar:

- Categoría.
- Prioridad.
- Problema reportado.
- Recomendación de atención.

---

# 5. Requisitos funcionales

## RF-01 - Registro y autenticación

El sistema debe permitir registrar usuarios e iniciar sesión.

### Criterios de aceptación

1. El usuario puede registrarse.
2. El correo debe ser único.
3. La contraseña debe almacenarse mediante hashing.
4. El usuario puede iniciar sesión.
5. El sistema genera un JWT.
6. Los endpoints protegidos requieren autenticación.

---

## RF-02 - Gestión de tickets

El sistema debe permitir crear y consultar tickets.

### Criterios de aceptación

1. Un usuario autenticado puede crear un ticket.
2. El ticket contiene título y descripción.
3. El ticket se guarda en la base de datos.
4. El ticket queda asociado al usuario.
5. El usuario puede consultar sus tickets.

---

## RF-03 - Clasificación automática

El sistema debe analizar el contenido del ticket para determinar
automáticamente su categoría.

Categorías:

- network
- hardware
- software
- accounts
- general

### Criterios de aceptación

Un problema relacionado con Internet o conectividad debe clasificarse
como `network`.

Un problema relacionado con componentes físicos debe clasificarse
como `hardware`.

Un problema relacionado con programas o sistemas operativos debe
clasificarse como `software`.

Un problema relacionado con cuentas o acceso debe clasificarse como
`accounts`.

Los problemas que no coincidan deben clasificarse como `general`.

---

## RF-04 - Prioridad

El sistema debe determinar la prioridad del ticket.

Prioridades:

- low
- medium
- high
- critical

### Criterios de aceptación

Los incidentes críticos deben recibir prioridad `critical`.

Los incidentes importantes deben recibir prioridad `high`.

Los incidentes normales deben recibir prioridad `medium`.

Los incidentes de bajo impacto deben recibir prioridad `low`.

---

# 6. Requisitos no funcionales

### RNF-01 Seguridad

El sistema debe proteger las operaciones mediante autenticación JWT.

### RNF-02 Mantenibilidad

El código debe estar organizado en componentes separados.

### RNF-03 Persistencia

La información de los usuarios y tickets debe almacenarse en una
base de datos.

### RNF-04 Pruebas

Las funcionalidades principales deben contar con pruebas unitarias
y de integración.

### RNF-05 Usabilidad

La interfaz debe permitir al usuario registrar y consultar tickets
de manera sencilla.

---

# 7. Criterios generales de aceptación

El proyecto se considera funcional cuando:

- El usuario puede registrarse.
- El usuario puede iniciar sesión.
- El sistema genera un JWT.
- Los endpoints protegidos requieren autenticación.
- El usuario puede crear tickets.
- Los tickets se almacenan correctamente.
- Los tickets son clasificados.
- Se determina su prioridad.
- Se genera una recomendación.
- Los tickets pueden ser consultados.
- Las pruebas automatizadas se ejecutan correctamente.
