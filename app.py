"""Pieni esimerkkisovellus CI-putken harjoitukseen."""


def add(a: float, b: float) -> float:
    """Palauta kahden luvun summa."""
    return a + b


def points_to_grade(points: int) -> str:
    """Muunna pisteet (0-10) arvosanaksi.

    0-4 hylätty, 5-7 hyväksytty, 8-9 hyvä, 10 erinomainen.
    """
    if not 0 <= points <= 10:
        raise ValueError("Pisteiden pitää olla välillä 0-10")
    if points < 5:
        return "hylätty"
    if points < 8:
        return "hyväksytty"
    if points < 10:
        return "hyvä"
    return "erinomainen"


def classify_temperature(celsius: float) -> str:
    """Luokittele lämpötila yksinkertaisesti."""
    if celsius < 0:
        return "freezing"
    if celsius < 20:
        return "cool"
    return "warm"


if __name__ == "__main__":
    print(points_to_grade(8))
    print(classify_temperature(21))
