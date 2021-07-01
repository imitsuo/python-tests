"""xablau module."""


def is_xablau(value: str) -> bool:
    """Validate if value == 'xablau'."""
    return value == 'xablau'


def is_xablau2(value: str, value2: str) -> bool:
    """Validate if value == 'xablau' and value2 == 'xablau."""
    return value == 'xablau' and value2 == 'xablau'


def get_number_of_xablau(file_path: str):

    number_of_xablaus = 0
    with open(file_path, 'r') as _file:
        for _line in _file:
            _line = _line.strip()
            for _word in _line.split():
                if is_xablau(_word):
                    number_of_xablaus += 1

    return number_of_xablaus
