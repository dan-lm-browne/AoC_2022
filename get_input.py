from aocd import get_data


def get_input_string(day=None, year=None):
    input_string = get_data(day=day, year=year)
    return input_string


def get_raw_input_string(day=None, year=None):
    input_string = get_data(day=day, year=year)
    return input_string.encode("unicode_escape")


def get_input_list(day=None, year=None):
    i_string = get_input_string(day, year)
    input_list = i_string.split()
    return input_list