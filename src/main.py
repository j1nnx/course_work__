from src.services import main_services
from src.views import main_views
from src.reports import main_reports


def main() -> None:
    """Отвечате за основную логику проекта с пользователем"""
    main_views()
    main_services()
    main_reports()


if __name__ == "__main__":
    main()
