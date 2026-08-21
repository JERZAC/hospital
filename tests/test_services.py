from app.services import (
    calculate_priority,
    classify_ticket,
    recommend_solution
)


def test_classify_network_ticket():

    result = classify_ticket(
        "Sin internet",
        "La computadora perdió conexión WiFi"
    )

    assert result == "red"


def test_classify_hardware_ticket():

    result = classify_ticket(
        "Impresora dañada",
        "La impresora no imprime"
    )

    assert result == "hardware"


def test_classify_software_ticket():

    result = classify_ticket(
        "Error Windows",
        "El sistema muestra un error"
    )

    assert result == "software"


def test_priority_critical():

    result = calculate_priority(
        3,
        3
    )

    assert result == "crítica"


def test_priority_high():

    result = calculate_priority(
        3,
        1
    )

    assert result == "alta"


def test_priority_low():

    result = calculate_priority(
        1,
        1
    )

    assert result == "baja"


def test_recommendation():

    result = recommend_solution(
        "red"
    )

    assert "Verificar" in result