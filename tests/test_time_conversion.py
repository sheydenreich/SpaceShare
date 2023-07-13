from SpaceShare.optimize_rideshares import get_time_of_year
from datetime import datetime
import pytest

def test_get_time_of_year():
    # generate a datetime object to test on 
    time = datetime.datetime(2023, 7, 13, 15, 28, 00)

    #calculate the number of seconds of the year to the given date using the function
    func_time = get_time_of_year(time)

    # hard coded check value 
    check_time = 4671.466666666666

    # assert correctness to within a minute
    assert check_time == pytest.approx(func_time, abs = 1.0*60/3600)