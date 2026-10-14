def test_session_is_ready(test_session):
    # Эта же фикстура test_session берётся из conftest.py
    assert test_session == "ready"


def test_second_session_is_ready(test_session):
    assert test_session == "ready"
