#!/usr/bin/env python3
"""
Zadanie: Strzelanie do celu przy stałych parametrach V0=50 m/s, H0=100 m i g=9.81 m/s^2.
- Cel losowany w zakresie [50, 340] m i wypisywany w konsoli.
- Użytkownik wprowadza kąt strzału (w stopniach). Próby powtarzane w pętli while aż do trafienia (±5 m).
- Po trafieniu: komunikat "Cel trafiony!" i liczba prób.
- Na końcu rysowana i zapisywana trajektoria udanego strzału jako trajektoria.png (matplotlib).

Wzór na zasięg (distance):
  distance = (v0*sin(alpha) + sqrt(v0^2*sin^2(alpha) + 2*g*h)) * v0*cos(alpha) / g
"""
from __future__ import annotations

import math
import random
from typing import Tuple, Any, Optional

try:
    import numpy as np
    import matplotlib.pyplot as plt
except Exception:
    # Pozwól uruchomić logikę bez wykresu, jeśli matplotlib/numpy nie są zainstalowane
    np = None  # type: ignore[assignment]
    plt = None  # type: ignore[assignment]

# Stałe
V0: float = 50.0
H0: float = 100.0
G: float = 9.81
TARGET_MIN: int = 50
TARGET_MAX: int = 340
HIT_THRESHOLD: float = 5.0


def projectile_distance(v0: float, angle_deg: float, h: float, g: float = G) -> float:
    """Zwraca poziomą odległość (distance) lotu dla podanego kąta w stopniach."""
    alpha = math.radians(angle_deg)
    vertical = v0 * math.sin(alpha)
    t = (vertical + math.sqrt(vertical ** 2 + 2 * g * h)) / g
    return v0 * math.cos(alpha) * t


def trajectory(v0: float, angle_deg: float, h: float, g: float = G, n: int = 300) -> Tuple[Any, Any]:
    """Zwraca punkty (x, y) trajektorii dla udanego kąta. Wymaga numpy."""
    if np is None:
        raise RuntimeError("Matplotlib/numpy nie są dostępne do rysowania.")
    alpha = math.radians(angle_deg)
    vx0 = v0 * math.cos(alpha)
    vy0 = v0 * math.sin(alpha)
    discr = vy0 ** 2 + 2 * g * h
    T = (vy0 + math.sqrt(discr)) / g
    t = np.linspace(0.0, T, n)
    x = vx0 * t
    y = h + vy0 * t - 0.5 * g * t ** 2
    return x, y


def plot_and_save(angle_deg: float, path: str = "trajektoria.png") -> None:
    """Rysuje i zapisuje trajektorię dla podanego kąta. Plik PNG zapisywany w bieżącym katalogu."""
    if plt is None or np is None:
        print("Brak bibliotek matplotlib/numpy – pomijam rysowanie wykresu.")
        return
    x, y = trajectory(V0, angle_deg, H0, G)
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color="blue")
    plt.grid(True, which="both", linestyle="--", alpha=0.6)
    plt.xlabel("Odległość [m]")
    plt.ylabel("Wysokość [m]")
    plt.title("Trajektoria pocisku Warwolf")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    print(f"Zapisano wykres trajektorii do pliku: {path}")
    try:
        plt.show()
    except Exception:
        # Np. w środowisku bez GUI
        pass
    finally:
        plt.close()


def main() -> None:
    target = random.randint(TARGET_MIN, TARGET_MAX)
    print(f"Wybrany cel znajduje się w odległości: {target} m")

    attempts = 0
    last_angle: Optional[float] = None

    while True:
        raw = input("Podaj kąt w stopniach (0-90): ").strip()
        try:
            angle_deg = float(raw.replace(",", "."))
        except ValueError:
            print("Nieprawidłowa wartość. Wpisz liczbę, np. 37.5")
            continue

        if not (0.0 < angle_deg < 90.0):
            print("Kąt musi być w zakresie (0, 90). Spróbuj ponownie.")
            continue

        attempts += 1
        last_angle = angle_deg

        distance = projectile_distance(V0, angle_deg, H0, G)
        delta = distance - target
        print(f"Odległość pocisku: {distance:.1f} m (cel: {target} m, różnica: {delta:+.1f} m)")

        if abs(delta) <= HIT_THRESHOLD:
            print("Cel trafiony!")
            print(f"Liczba prób: {attempts}")
            break
        else:
            if delta < 0:
                print("Za krótko – spróbuj zwiększyć kąt.")
            else:
                print("Za daleko – spróbuj zmniejszyć kąt.")

    # Po trafieniu – rysujemy trajektorię udanego strzału
    if last_angle is not None:
        plot_and_save(last_angle, "trajektoria.png")


if __name__ == "__main__":
    main()
