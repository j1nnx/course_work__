from src.services import main_services
from src.views import main_views


def main() -> None:
    """Отвечате за основную логику проекта с пользователем"""
    main_views()
    main_services()


if __name__ == "__main__":
    main()
