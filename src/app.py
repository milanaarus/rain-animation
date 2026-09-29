"""Главное окно приложения и главный цикл анимации."""

import tkinter as tk

from src.models.rain_model import RainModel
from src.renderers.renderer import Renderer
from src.widgets.controls import Controls


class App:
    """Класс приложения: окно, Canvas, главный цикл."""

    WIDTH = 800
    HEIGHT = 600
    FPS_DELAY = 30  # мс между кадрами
    BG_COLOR = "#e6e6fa"  # светлый лавандовый фон

    def __init__(self) -> None:
        """Инициализирует окно, модель, рендерер и элементы управления."""
        self.root = tk.Tk()
        self.root.title("Анимация дождя")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root, width=self.WIDTH, height=self.HEIGHT, bg=self.BG_COLOR
        )
        self.canvas.pack()

        self.model = RainModel(width=self.WIDTH, height=self.HEIGHT)
        self.renderer = Renderer(self.canvas)
        self.controls = Controls(self.root, self.model)

        self._running = True

    def run(self) -> None:
        """Запускает главный цикл анимации."""
        self._animate()
        self.root.mainloop()

    def _animate(self) -> None:
        """Один кадр анимации: обновление модели и перерисовка."""
        if self._running:
            self.model.update()
            self.renderer.draw(self.model)
            self.root.after(self.FPS_DELAY, self._animate)