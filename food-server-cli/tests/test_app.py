from app.storage import load_data


def test_load_data_returns_list():
    data = load_data()
    assert isinstance(data, list)