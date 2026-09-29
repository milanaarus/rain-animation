"""Элементы управления: слайдеры плотности и ветра."""

import tkinter as tk
from tkinter import ttk

from src.models.rain_model import RainModel


class Controls:
    """Панель управления под Canvas."""

    def __init__(self, root: tk.Tk, model: RainModel) -> None:
        """Создаёт слайдеры.

        Args:
            root: главное окно.
            model: модель дождя.
        """
        self.model = model
        frame = tk.Frame(root, bg="#dcdcdc")
        frame.pack(fill="x")

        # Слайдер плотности дождя
        tk.Label(frame, text="Плотность дождя:", bg="#dcdcdc", fg="black").pack(
            side="left", padx=5
        )
        self.intensity_scale = ttk.Scale(
            frame, from_=0, to=30, orient="horizontal", command=self._on_intensity
        )
        self.intensity_scale.set(5)
        self.intensity_scale.pack(side="left", fill="x", expand=True, padx=5)

        # Слайдер ветра
        tk.Label(frame, text="Ветер:", bg="#dcdcdc", fg="black").pack(
            side="left", padx=5
        )
        self.wind_scale = ttk.Scale(
            frame, from_=-5, to=5, orient="horizontal", command=self._on_wind
        )
        self.wind_scale.set(0)
        self.wind_scale.pack(side="left", fill="x", expand=True, padx=5)

    def _on_intensity(self, value: str) -> None:
        """Обработчик изменения плотности дождя."""
        self.model.set_intensity(float(value))

    def _on_wind(self, value: str) -> None:
        """Обработчик изменения ветра."""
        self.model.set_wind(float(value))