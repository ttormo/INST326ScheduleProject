import pytest
import INST326ScheduleProject


@pytest.fixture
def test_schedule():
    return INST326ScheduleProject.Schedule("example_schedule.csv")


def test_schedule_init_1():
    """Does the __init__() method of the Schedule class raise a Value Error
        when expected?
    """

    with pytest.raises(ValueError):
        new_schedule = INST326ScheduleProject.Schedule("example_schedule.txt")


def test_schedule_init_2():
    """Does the __init__() method of the Schedule class raise a Value Error
        when expected?
    """

    with pytest.raises(ValueError):
        new_schedule = INST326ScheduleProject.Schedule("https://google.com")


def test_print_schedule(capsys, test_schedule):
    test_schedule.print_schedule()
    outerr = capsys.readouterr()
    out = outerr.out
    print(out)
    assert out == "INST208L, Linux Command Line Tools, 0101, 3, " \
                  "[[Class Time and Details on ELMS]]\n" \
                  "INST326, Object-Oriented Programming for Information " \
                  "Science, 0102, 3, [[MWF: 9:00am - 9:50am]]\n" \
                  "ASTR101, General Astronomy, 0103, 4, " \
                  "[[TuTh: 11:00am - 12:15pm], [W: 11:00am - 1:00pm], " \
                  "[W: 10:00am - 10:50am]]\n"


def test_add_class():
    return


def test_remove_class():
    return


def test_add_to_file():
    return


def test_credit_count():
    return





