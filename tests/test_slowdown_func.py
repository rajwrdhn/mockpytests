import pytest
from examples.main import func_slow

#@pytest.mark.skip
#test function call
def test_slow_function_super_slow():
    expected = 9
    actual = func_slow()
    assert expected == actual

#mocking a function call
def test_slow_function_mocked_api_call(mocker):
    mocker.patch(
        'examples.main.apiCall',
        return_value=5
    )

    expected = 5
    actual = func_slow()
    assert expected == actual