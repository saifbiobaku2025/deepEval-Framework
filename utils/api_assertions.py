def assert_status_code(response, expected: int):
    assert response.status_code == expected, (
        f"Expected status {expected}, "
        f"got {response.status_code}"
    )