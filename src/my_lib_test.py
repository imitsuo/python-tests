import os
import mock
from tempfile import TemporaryDirectory
from my_lib import is_xablau, get_number_of_xablau


def test_is_xablau__abc__expected_false():
    # FIXTURES
    my_str = 'abc'

    # EXERCISE
    result = is_xablau(my_str)

    # ASSERTS
    assert not result


# Quais as possibilidades de input ?
# complexidade ciclomatica

def test_get_number_of_xablau():
    # FIXTURES
    path = '/tmp/file-not-exists'

    _mock_open = mock.mock_open(read_data='xablau\nxablau')
    with mock.patch('builtins.open', _mock_open):

        # EXERCISE
        result = get_number_of_xablau(path)

        # ASSERTS
        assert result == 2
        _mock_open.assert_called_once_with(path, 'r')


@mock.patch('my_lib.is_xablau')
def test_get_number_of_xablau_with_mock(mock_is_xablau: mock.Mock):
    # FIXTURES
    path = '/tmp/file-not-exists'

    mock_is_xablau.return_value = False

    _mock_open = mock.mock_open(read_data='xablau\nxablau')
    with mock.patch('builtins.open', _mock_open):

        # EXERCISE
        result = get_number_of_xablau(path)

        # ASSERTS
        assert result == 0

        _mock_open.assert_called_once_with(path, 'r')

        assert mock_is_xablau.call_count == 2

        mock_is_xablau.assert_has_calls(
            [mock.call('xablau'), mock.call('xablau')])


def test_get_number_of_xablau_from_file():
    # FIXTURES
    with TemporaryDirectory() as d:
        _file_path = os.path.join(d, 'file-x')
        with open(_file_path, 'w') as file:
            file.write('xablau')

        # EXERCISE
        result = get_number_of_xablau(_file_path)

        # ASSERTS
        assert result == 1
