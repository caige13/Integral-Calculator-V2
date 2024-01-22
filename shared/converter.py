import shared.custom_exceptions as ce


def convert_start_end(start, end):
    if start.isnumeric() and end.isnumeric():
        return int(start), int(end)
    else:
        raise ce.MatchBreak
