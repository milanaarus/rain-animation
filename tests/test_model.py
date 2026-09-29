"""Тесты для модели дождя."""

import unittest

from src.models.rain_model import Drop, RainModel


class TestDrop(unittest.TestCase):
    """Тесты класса Drop."""

    def test_drop_creation(self) -> None:
        """Капля создаётся с корректными атрибутами."""
        drop = Drop(x=10, y=20, length=15, speed=5)
        self.assertEqual(drop.x, 10)
        self.assertEqual(drop.y, 20)
        self.assertEqual(drop.length, 15)
        self.assertEqual(drop.speed, 5)


class TestRainModel(unittest.TestCase):
    """Тесты класса RainModel."""

    def setUp(self) -> None:
        self.model = RainModel(width=800, height=600)

    def test_initial_drops(self) -> None:
        """Начальное количество капель больше нуля."""
        self.assertGreater(len(self.model.drops), 0)

    def test_update_moves_drops(self) -> None:
        """При обновлении капли движутся вниз."""
        y_before = self.model.drops[0].y
        self.model.update()
        self.assertGreaterEqual(self.model.drops[0].y, y_before)

    def test_set_intensity(self) -> None:
        """Плотность устанавливается корректно."""
        self.model.set_intensity(10)
        self.assertEqual(self.model.intensity, 10)

    def test_set_wind(self) -> None:
        """Ветер устанавливается корректно."""
        self.model.set_wind(2.5)
        self.assertEqual(self.model.wind, 2.5)

    def test_depth_layers(self) -> None:
        """Капли бывают разных слоёв (размеров)."""
        lengths = [self.model._create_drop().length for _ in range(50)]
        self.assertGreater(max(lengths) - min(lengths), 5)


if __name__ == "__main__":
    unittest.main()