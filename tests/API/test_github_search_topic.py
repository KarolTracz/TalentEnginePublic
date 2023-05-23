def test_items_in_topic_is_not_empty(request_get_fixture):
    assert len(request_get_fixture["items"]) != 0


def test_first_topic_for_python_is_python(request_get_fixture):
    assert request_get_fixture["items"][0]["name"] == "python"


def test_per_page_below_is_30_by_default(request_get_fixture):
    assert len(request_get_fixture["items"]) == 30
