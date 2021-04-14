""" A simple scheduling program to assist UMD students. """


class Schedule:
    """ A student's schedule.

    Attributes:
        classes (list of Class objects): the classes in the student's schedule.

    """

    def __init__(self, file):
        """ Creates a new instance of the Schedule class.

        Args:
            file (string): A string containing the path to a CSV file.

        """

    def print_schedule(self):
        """ Prints the current state of the user's Schedule.

        Side Effect:
            print: This method prints to the console.

        """


class Class:
    """ A Class.

    Attributes:
        code (string): A string containing the class code.
        name (string): A string containing the class name.
        credits (int): the number of credits associated with the class.
        professor (string): A string containing the professor's name.
        days (list of Days): A list containing Day objects associated with the class.

    """

    def __init__(self, file):
        """ Creates a new instance of a Class.

        Args:
            file (string): a string containing the filepath of a CSV file.

        """


class Day:
    """ A Day.

    Attributes:
        name (string): a string containing the name of the day.
        start (int): the time that the class starts.
        end (int): the time that the class ends.

    """

    def __init__(self, file):
        """ Creates a new instance of the Day class.

       Args:
           file: a string containing the path to a CSV file.

       """


def add_class(class_wanted):
    """ Adds a class to the student's schedule.

    Args:
        class_wanted (Class): the class that the user wants to add.

    Side Effects:
        this function edits the attributes of the student's schedule.

    """


def remove_class(class_unwanted):
    """ Removes a class from the student's schedule.

    Args:
        class_unwanted (Class): the class that the user wants to remove.

    Side Effects:
        this function edits the attributes of the student's schedule.

    """


def credit_count(current_schedule):
    """ Counts the total number of credits in the student's current schedule.

    Args:
        current_schedule (Schedule): the student's schedule.

    Returns:
        credits (int): the total number of credits in the student's schedule.

    """


def main(major_link, student_schedule):
    """ Create two Schedules based on a URL and a CSV file.

    Args:
        major_link (string): a link to the major's Schedule of Classes.
        student_schedule (string): the filepath of the user's schedule.

    Returns:
        see credit_count().

    Side Effects:
        See add_class() and remove_class().

    """


if __name__ == "__main__":

