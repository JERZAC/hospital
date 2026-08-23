# Pruebas de software - HospitalTech

## 1. Objetivo

El objetivo de las pruebas es comprobar que las funcionalidades
principales de HospitalTech funcionan correctamente y que los
diferentes componentes del sistema pueden trabajar conjuntamente.

Para las pruebas automatizadas se utiliza:

- Python
- Pytest
- FastAPI TestClient
- SQLite para pruebas

---

# 2. Tipos de pruebas

Se implementaron dos tipos principales:

## 2.1 Pruebas unitarias

Las pruebas unitarias verifican funciones individuales de la lógica
del sistema sin depender de toda la aplicación.

Se prueban:

- Clasificación de tickets.
- Cálculo de prioridad.
- Generación de recomendaciones.

---

## 2.2 Pruebas de integración

Las pruebas de integración verifican el funcionamiento conjunto
de diferentes componentes.

Se comprueba el flujo:

```text
Registro
   ↓
Inicio de sesión
   ↓
Generación de JWT
   ↓
Autenticación
   ↓
Creación de ticket
   ↓
Clasificación
   ↓
Prioridad
   ↓
Persistencia
   ↓
Consulta
```
