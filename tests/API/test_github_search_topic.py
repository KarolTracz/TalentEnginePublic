import pytest
from src.Applications.github_api_client import GitHubAPIClient


@pytest.fixture(scope='module')
def default_body():
    api = GitHubAPIClient().get_search_repo_body()
    yield api


def test_items_in_topic_is_not_empty(default_body):
    assert len(default_body["items"]) != 0


def test_num_of_pages_is_range_1_to_100(default_body):
    assert 1 <= len(default_body["items"]) <= 100


def test_incomplete_results_is_not_True(default_body):
    # All lines below does the same. Is that any prefer way how to compare variables, to tests be more readable?
    assert default_body["incomplete_results"] is not True
    assert default_body["incomplete_results"] is False
    assert default_body["incomplete_results"] != 1
    assert default_body["incomplete_results"] == 0
    assert default_body["incomplete_results"] == False
    assert default_body["incomplete_results"] != True


def test_first_topic_for_python_is_python():
    api = GitHubAPIClient()
    assert api.get_search_repo_body(q="python")["items"][0]["name"] == "python"


def test_per_page_query_over_100():
    api = GitHubAPIClient()
    assert len((api.get_search_repo_body(per_page=101))["items"]) <= 101


def test_per_page_query_below_0():
    api = GitHubAPIClient()
    assert len((api.get_search_repo_body(per_page=-1))["items"]) >= 1
