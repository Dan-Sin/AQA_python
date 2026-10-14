import pytest


@pytest.fixture(scope="module")
def database_connection():
    # Показываем в терминале момент запуска фикстуры
    print("\nПодключаемся к тестовой БД")

    # Создаем условный результат подготовки
    connection_status = "connected"

    # Передаем результат тестам
    return connection_status


@pytest.fixture(autouse=True)
def clear_test_cache():
    # Эта строка нужна, чтобы увидеть автоматический запуск фикстуры
    print("\nОчищаем тестовый кэш")


def test_create_user(database_connection, test_session):
    # Проверяем, что фикстура передала ожидаемое значение
    assert database_connection == "connected"


def test_delete_user(database_connection):
    assert database_connection == "connected"


def test_seesion_is_ready(test_session):
    assert test_session == "ready"
