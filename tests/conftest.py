import pytest


@pytest.fixture(scope="session")
def test_session():
    # Подготовка выполняется один раз в начале pytest-сессии
    print("\nПодготавливаем общую тестовую сессию")

    session_status = "ready"

    # Передаём значение тестам и ставим фикстуру на паузу
    yield session_status

    # Этот код выполнится один раз после завершения всех тестов
    print("\nОчищаем общую тестовую сессию")
