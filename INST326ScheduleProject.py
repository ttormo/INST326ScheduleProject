""" A simple scheduling program to assist UMD students. """

from WebScraper import getHTML,classNames, getClassURL, classInfo

class Schedule:
    """ A schedule containing information on associated Courses.

        The student will input a file containing Course information,
        which will be used to create a new Schedule instance that
        represents the schedule that they have already built.
        Another Schedule instance will be created based off of
        information found in the URL that was input in main(),
        representing the list of courses for a given UMD major.

    Attributes:
        courses (list of Course objects): the classes in the student's schedule.

    """

    def __init__(self, user_input):
        """ Creates a new instance of the Schedule class.

        Args:
            file (string): The path to a CSV file containing the user's
                partially completed course schedule. This includes each
                course's code (ex. PSYC355), name, section number,
                available seats, credits, and meeting days.

        """

        self.courses = []
        if user_input.find(".csv") > -1:
            with open(user_input, "r", encoding="utf-8") as f:
                for line in f:
                    new_course = Course(line)
                    self.courses.append(new_course)
        else:
            html_list = getHTML(user_input)
            codes = classNames(html_list)
            courses = classInfo(codes)
            for key in courses:
                for i in courses[key]:
                    new_course = Course(i)
                    self.courses.append(new_course)

    def print_schedule(self):
        """ Prints the current state of the Schedule instance.

        Side Effect:
            print: This method prints to the console.

        """
        for course in self.courses:
            print(course)


class Course:
    """ Course information gathered from the CSV file input in main(), as well
            as from the URL provided in main().

    Attributes:
        code (string): A string containing the course code.
        name (string): A string containing the course name.
        section_number (int): the section number associated with that
            specific course.
        credits (int): the number of credits associated with the course.
        days (list of Days): A list containing Day objects associated
            with the course.

    """

    def __init__(self, course_info):
        """ Creates a new instance of a Course.

        Args:
            course_info (string): One line pulled from the CSV file or URL input in the Schedule class.

        """

        # Build a regex that will match items from a single line of the CSV file (EXCEPT for the days)
        # Use the example_schedule.txt file to help build the regex
        # Set each attribute to a different matching group of the regex
        if isinstance(course_info, list):
            self.code = course_info[0]
            self.name = course_info[1]
            self.section_number = course_info[2]
            self.credits = course_info[3]
            self.days = []

            new_day = Day(course_info[4],course_info[5], course_info[6])
            self.days.append(new_day)

        else:
            print("you suck")

    def __repr__(self):
        return f"{self.code}, {self.name}, {self.section_number}, {self.credits}, {self.days}"


class Day:
    """ This class allows the day of the week, start time, and end time to be
    specified for the student's courses based on their provided file.

    Each instance of the Course class will have at least one associated Day class.

    Attributes:
        name (string): a string containing the name of the day.
        start (int): the time that the class starts.
        end (int): the time that the class ends.

    """

    def __init__(self, name, start, end):
        """ Creates a new instance of the Day class.

        Args:
           day_info (string): A string containing information such as the name of the day, as well as course start
                and end times for that day.

        """

        # Create a regex that finds the day name, start, and end times within the CSV file

        self.name = name
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{self.name}, {self.start}, {self.end}"


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


def main(major_link):
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
    class_schedule = Schedule(major_link)
    class_schedule.print_schedule()

main("https://app.testudo.umd.edu/soc/202108/INST")

