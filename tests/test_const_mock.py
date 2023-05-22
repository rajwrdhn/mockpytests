import examples.func
from examples.func import concat

def test_const_mock(mocker):
    mocker.patch.object(examples.func, 'STRING_A', 'HELLO ')
    expected = "HELLO RAJ!"
    actual = concat()

    assert expected == actual


def test_mock_twice(mocker):
    mocker.patch.object(examples.func, 'STRING_A', 'HI ')
    expected = "HI RAJ!"
    actual = concat()

    assert expected == actual