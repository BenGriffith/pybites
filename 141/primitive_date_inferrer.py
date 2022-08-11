from enum import Enum
from datetime import datetime
from collections import Counter
from sqlite3 import Date


class DateFormat(Enum):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, val=None):
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings 
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


def _maybe_DateFormats(date_str):
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(date_str, d_parse_fmt) # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def get_dates(dates):
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Allowed/supported date formats are defined in a DF enum class.
    """
    date_format_counter = Counter()

    for date in dates:
        for df in _maybe_DateFormats(date):
            date_format_counter.update([df])

    first_most_frequent = 0
    second_most_frequent = 0
    non_parsable_count = 0
    max_parsable_count = 0
    for key, value in date_format_counter.items():
        if key != DateFormat.NONPARSABLE:

            if value > max_parsable_count:
                max_parsable_count = value

            if value > first_most_frequent:
                most_frequent_format = key
                first_most_frequent = value
                continue
        else:
            non_parsable_count = value

        if value <= first_most_frequent and value > second_most_frequent:
            second_most_frequent = value

    if (non_parsable_count > max_parsable_count) or (first_most_frequent == second_most_frequent):
        raise InfDateFmtError()

    results = []
    df = DateFormat(most_frequent_format.value)
    for date in dates:
        try:
            date_format = datetime.strptime(date, df.get_d_parse_formats(df.value)).strftime("%Y-%m-%d")
            results.append(date_format)
        except:
            results.append("Invalid")

    return results