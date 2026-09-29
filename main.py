"""Точка входа в программу анимации дождя."""

from src.app import App


def main() -> None:
    """Запускает приложение."""
    app = App()
    app.run()


if __name__ == "__main__":
    main()