KEYWORDS = {

    "red": [
        "internet",
        "red",
        "wifi",
        "conexión",
        "conexion",
        "router",
        "switch"
    ],

    "hardware": [
        "computadora",
        "pc",
        "monitor",
        "teclado",
        "mouse",
        "impresora",
        "disco"
    ],

    "software": [
        "programa",
        "sistema",
        "aplicación",
        "aplicacion",
        "error",
        "windows"
    ],

    "cuentas": [
        "contraseña",
        "contrasena",
        "usuario",
        "cuenta",
        "acceso",
        "login"
    ]
}


def classify_ticket(
    title,
    description
):

    text = (
        f"{title} {description}"
    ).lower()

    scores = {}

    for category, words in KEYWORDS.items():

        scores[category] = sum(
            word in text
            for word in words
        )

    best_category = max(
        scores,
        key=scores.get
    )

    if scores[best_category] == 0:

        return "general"

    return best_category


def calculate_priority(
    impact,
    urgency
):

    score = impact + urgency

    if score >= 6:
        return "crítica"

    if score >= 4:
        return "alta"

    if score == 3:
        return "media"

    return "baja"


def recommend_solution(
    category
):

    recommendations = {

        "red":
        "Verificar cableado, WiFi, IP, gateway y switch.",

        "hardware":
        "Revisar alimentación, conexiones y periféricos.",

        "software":
        "Revisar error, permisos, servicios y registros.",

        "cuentas":
        "Verificar usuario, cuenta y permisos.",

        "general":
        "Realizar diagnóstico inicial."
    }

    return recommendations[
        category
    ]