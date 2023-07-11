import examples.func
from examples.func import concat

#Mocking a constant from examples.func
def test_const_mock(mocker):
    mocker.patch.object(examples.func, 'STRING_A', 'HELLO ')
    expected = "HELLO RAJ!"
    actual = concat()

    assert expected == actual


#Mocking a constant from examples.func
def test_mock_twice(mocker):
    mocker.patch.object(examples.func, 'STRING_A', 'HI ')
    expected = "HI RAJ!"
    actual = concat()

    assert expected == actual

def test_mock_double(mocker):
    mocker.patch.object(examples.func, 'NUM_CONST', 300)
    expected = 600
    actual = examples.func.double()

    assert expected == actual