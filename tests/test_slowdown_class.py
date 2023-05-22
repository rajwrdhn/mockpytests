from examples.main import func_slowdown


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