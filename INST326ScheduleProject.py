""" A simple scheduling program to assist UMD students. """


class Schedule:
    """ A schedule containing information on associated Courses.

        The student will input a file containing Course information,
        which will beused to create a new Schedule instance that
        represents the schedule that they have already built.
        Another Schedule instance will be created based off of
        information found in the URL that was input in main(),
        representing the list of courses for a given UMD major.

    Attributes:
        courses (list of Course objects): the classes in the student's schedule.

    """

    def __init__(self, file):
        """ Creates a new instance of the Schedule class.

        Args:
            file (string): The path to a CSV file containing the user's
                partially completed course schedule. This includes each
                course's code (ex. PSYC355), name, section number,
                available seats, credits, and meeting days.

        """

    def print_schedule(self):
        """ Prints the current state of the Schedule instance.

        Side Effect:
            print: This method prints to the console.

        """


class Course:
    """ Course information gathered from the CSV file input in main(), as well
            as from the URL provided in main().

    Attributes:
        code (string): A string containing the course code.
        name (string): A string containing the course name.
        section_number (int): the section number associated with that
            specific course.
        available_seats (int): the number of open slots for the course.
        credits (int): the number of credits associated with the course.
        days (list of Days): A list containing Day objects associated
            with the course.

    """

    def __init__(self, file):
        """ Creates a new instance of a Course.

        Args:
            file (string): The path to a CSV file containing the user's
                partially completed course schedule. This includes each
                course's code (ex. PSYC355), name, section number,
                available seats, credits, and meeting days.

        """


class Day:
    """ This class allows the day of the week, start time, and end time to be
    specified for the student's courses based on their provided file.

    Each instance of the Course class will have at least one associated Day class.

    Attributes:
        name (string): a string containing the name of the day.
        start (int): the time that the class starts.
        end (int): the time that the class ends.

    """

    def __init__(self, file):
        """ Creates a new instance of the Day class.

       Args:
           file (string): The path to a CSV file containing the user's
                partially completed course schedule. This includes each
                course's code (ex. PSYC355), name, section number,
                available seats, credits, and meeting days.

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
        current_schedule (Schedule): the student's current schedule.

    Returns:
        credits (int): the total number of credits in the student's schedule.

    """


def main(major_link, student_schedule):
    """ Create two Schedules based on a URL to a UMD course offerings page
        and a CSV file of the student's partially complete schedule.

        Compare the two schedules to determine which classes from the
        major_link schedule fit into student_schedule based on times.

    Args:
        major_link (string): a link to the major's Schedule of Classes.
        student_schedule (string): the filepath of the user's schedule. The
            schedule should contain information on the User's pre-chosen
            classes, including course code, name, section_number, available seats,
            credits, and meeting days.

    Returns:
        see credit_count().

    Side Effects:
        See add_class() and remove_class().

    """


if __name__ == "__main__":

