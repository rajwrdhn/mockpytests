from examples.main import func_slowdown, num_return

#mocking a class
def test_mocking_class_method(mocker):
    expected = 'xyz'

    def mock_load(self):
        return 'xyz'

    mocker.patch(
        'examples.main.DataSet.data_loader',
        mock_load
    )
    actual = func_slowdown()
    assert expected == actual

#mocking another class
def test_return_val_class_method(mocker):
    expected = 10

    def mock_num(self):
        return 10

    mocker.patch(
        'examples.main.DataSet.return_val',
        mock_num
    )
    actual = num_return()
    assert expected == actual