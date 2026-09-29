"""Отрисовка капель дождя на Canvas."""

import tkinter as tk

from src.models.rain_model import RainModel


class Renderer:
    """Класс, отвечающий за отрисовку модели на Canvas."""

    def __init__(self, canvas: tk.Canvas) -> None:
        """Сохраняет ссылку на Canvas.

        Args:
            canvas: холст для рисования.
        """
        self.canvas = canvas

    def draw(self, model: RainModel) -> None:
        """Полностью перерисовывает сцену.

        Args:
            model: модель дождя.
        """
        self.canvas.delete("all")
        for drop in model.drops:
            self.canvas.create_line(
                drop.x,
                drop.y,
                drop.x + model.wind * 2,
                drop.y + drop.length,
                fill=drop.color,
                width=drop.thickness,
            )