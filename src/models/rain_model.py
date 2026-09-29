"""Модель данных анимации дождя: капли и их поведение."""

import random
from dataclasses import dataclass


@dataclass
class Drop:
    """Одна капля дождя.

    Attributes:
        x: координата X.
        y: координата Y.
        length: длина капли.
        speed: скорость падения (пикселей за кадр).
        thickness: толщина линии.
        color: цвет капли.
    """

    x: float
    y: float
    length: float
    speed: float
    thickness: int = 1
    color: str = "#8a2be2"


class RainModel:
    """Модель дождя: хранит капли и обновляет их положение.

    Капли имеют три слоя глубины (depth):
        0 — дальний: маленькие, медленные, бледные;
        1 — средний: средние параметры;
        2 — ближний: крупные, быстрые, насыщенные.
    """

    def __init__(self, width: int, height: int) -> None:
        """Создаёт модель.

        Args:
            width: ширина области рисования.
            height: высота области рисования.
        """
        self.width = width
        self.height = height
        self.drops: list[Drop] = []
        self.intensity = 5  # сколько капель создаётся за кадр
        self.wind = 0.0  # горизонтальный сдвиг (ветер)
        self._spawn_initial()

    def _spawn_initial(self) -> None:
        """Создаёт начальный набор капель по всей высоте."""
        for _ in range(200):
            self.drops.append(self._create_drop(random.uniform(0, self.height)))

    def _create_drop(self, y: float | None = None) -> Drop:
        """Создаёт новую каплю с учётом трёхмерности.

        Args:
            y: начальная координата Y (по умолчанию — сверху).

        Returns:
            Новый объект Drop.
        """
        if y is None:
            y = random.uniform(-50, 0)

        # Определяем слой (глубину) капли
        depth = random.choice([0, 1, 2])

        if depth == 0:  # дальний слой
            length = random.uniform(5, 10)
            speed = random.uniform(2, 5)
            thickness = 1
            color = "#b19cd9"
        elif depth == 1:  # средний слой
            length = random.uniform(10, 18)
            speed = random.uniform(5, 9)
            thickness = 1
            color = "#8a2be2"
        else:  # ближний слой
            length = random.uniform(18, 28)
            speed = random.uniform(9, 15)
            thickness = 2
            color = "#4b0082"

        return Drop(
            x=random.uniform(0, self.width),
            y=y,
            length=length,
            speed=speed,
            thickness=thickness,
            color=color,
        )

    def update(self) -> None:
        """Обновляет положение всех капель и создаёт новые."""
        for drop in self.drops:
            drop.y += drop.speed
            drop.x += self.wind

        # Удаляем капли, ушедшие за нижнюю границу
        self.drops = [d for d in self.drops if d.y < self.height + 20]

        # Создаём новые капли в соответствии с плотностью
        for _ in range(self.intensity):
            self.drops.append(self._create_drop())

    def set_intensity(self, value: float) -> None:
        """Устанавливает плотность дождя.

        Args:
            value: новое значение плотности (0–30).
        """
        self.intensity = int(value)

    def set_wind(self, value: float) -> None:
        """Устанавливает силу ветра.

        Args:
            value: новое значение ветра (-5–5).
        """
        self.wind = float(value)