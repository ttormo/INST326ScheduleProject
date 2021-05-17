import pytest
import INST326ScheduleProject
from WebScraper import classInfo


@pytest.fixture
def test_schedule():
    """Creates a schedule based off of the example_schedule.csv file for use
        with testing."""
    return INST326ScheduleProject.Schedule("example_schedule.csv")


@pytest.fixture
def output_schedule():
    """Creates a schedule based off of the schedule_for_tests.csv file for use
            with testing."""
    return INST326ScheduleProject.Schedule("schedule_for_tests.csv")


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
    """Does print_schedule() print the provided schedule in the correct
        format?"""

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


def test_add_class_1(capsys, output_schedule, test_schedule):
    """Does add_class() print the correct statement when an invalid course
        is requested?"""

    output_schedule.add_class(test_schedule, "not real", "not a class")
    outerr = capsys.readouterr()
    out = outerr.out
    print(out)
    assert out == "\n\nThe course code or section number you entered is not " \
                  "valid.\n"


def test_add_class_2(capsys, output_schedule, test_schedule):
    """Does add_class() print the correct statement when a valid course
        is requested?"""

    output_schedule.add_class(test_schedule, "INST208L", "0101")
    outerr = capsys.readouterr()
    out = outerr.out
    print(out)
    assert out == "\n\nCourse successfully added.\n"


def test_remove_class_1(capsys, output_schedule):
    """Does remove_class() print the correct statement if an invalid course is
        requested?"""

    output_schedule.remove_class("not real", "not a class")
    outerr = capsys.readouterr()
    out = outerr.out
    print(out)
    assert out == "\n\nThe course code or section number you entered is not " \
                  "valid.\n"


def test_remove_class_2(capsys, output_schedule):
    """Does remove_class() print the correct statement if a valid course is
        requested?"""

    output_schedule.remove_class("INST208L", "0101")
    outerr = capsys.readouterr()
    out = outerr.out
    print(out)
    assert out == "\n\nCourse successfully removed.\n"


def test_credit_count(capsys, output_schedule):
    """Does credit_count print the correct amount of credits in the student's
        schedule?"""

    INST326ScheduleProject.credit_count(output_schedule)
    outerr = capsys.readouterr()
    out = outerr.out
    print(out)
    assert out == "Your schedule currently contains 10 credits\n"
    
def test_classInfo():
    """ does classInfo() return the correct class information?"""
    assert classInfo(['CPSF100'], "https://app.testudo.umd.edu/soc/202108/CPSF") == {"CPSF100":[["CPSF100","College Park Scholars: Life Sciences First-Year Colloquium l","0101","1","W","3:30pm","5:00pm"]]}





