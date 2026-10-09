from utils.api_assertions import assert_status_code


def test_health(example_api):
    response = example_api.health()

    assert_status_code(response, 200)
