""" A simple scheduling program to assist UMD students. """

import re
import sys
from WebScraper import getHTML, classNames, getClassURL, classInfo
from argparse import ArgumentParser


class Schedule:
    """ A schedule containing information on associated Courses.

        The student will input a file containing Course information,
        which will be used to create a new Schedule instance that
        represents the schedule that they have already built.
        Another Schedule instance will be created based off of
        information found in the URL that was input in main(),
        representing the list of courses for a given UMD major.

    Attributes:
        courses (list of Course objects): the classes in the student's
            schedule.

    """

    def __init__(self, user_input):
        """ Creates a new instance of the Schedule class.

        Args:
            user_input (string): The path to a CSV file containing the user's
                partially completed course schedule, OR a URL pointing to a
                testudo.umd.edu website containing information on a Major's
                courses.

        Raises:
            ValueError: The user input an unsupported file type or invalid URL.

        """

        self.courses = []
        if user_input.find(".csv") != -1:
            with open(user_input, "r", encoding="utf-8") as f:
                for line in f:
                    new_course = Course(line)
                    self.courses.append(new_course)
        elif user_input.find("https://app.testudo.umd.edu/soc/") != -1:
            html_list = getHTML(user_input)
            codes = classNames(html_list)
            courses = classInfo(codes)
            for key in courses:
                code_and_sec = []
                for i in courses[key]:
                    new_course = Course(i)
                    if new_course.code and new_course.section_number \
                            not in code_and_sec:
                        code_and_sec.append(new_course.code)
                        code_and_sec.append(new_course.section_number)
                        self.courses.append(new_course)
                    else:
                        self.courses[-1].days.append(new_course.days)
        else:
            raise ValueError("An invalid URL/Filetype was input.")

    def print_schedule(self):
        """ Prints the current state of the Schedule instance.

        Side Effect:
            print: This method prints to the console.

        """

        for course in self.courses:
            print(course)

    def add_class(self, major_schedule, course_code, course_section):
        """ Adds a class from major_schedule into the Schedule this is run
                on (self).

        Args:
            class_wanted (int): the index of the class from major_schedule that the user
                would like to add to their schedule.
            major_schedule (Schedule): the schedule to pull classes from.
            course_code(str): the code identifying the course being added to student schedule.
            course_section(int): the section number of the course being added to student schedule.

        Side Effects:
            This function edits the attributes of the student's schedule.

        """

        x = 0
        for course in major_schedule.courses:
            if course_code == course.code \
                    and course_section == course.section_number:
                self.courses.append(course)
                x = 1
        if x == 0:
            print("\n")
            print("The course code or section number you entered is not valid.")
        else:
            print("\n")
            print("Course successfully added.")

    def remove_class(self, course_code, course_section):
        """ Adds a class from the schedule this is run on (self).

        Args:
            class_unwanted (int): the index of the class that the user wishes
                to remove from their schedule.
            course_code(str): the code identifying the course being added to student schedule.
            course_section(int): the section number of the course being added to student schedule.

        Side Effects:
            Print: 

        """
                
        x = 0
        for course in self.courses:
            if course_code == course.code \
                    and course_section == course.section_number:
                self.courses.remove(course)
                x = 1
        if x == 0:
            print("\n")
            print("The course code or section number you entered is not valid")
        else:
            print("\n")
            print("Course successfully removed")

    def add_to_file(self, user_input):
        with open(user_input, "w", encoding="utf-8") as f:
            for course in self.courses:
                print(course, file=f)


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
            course_info (string): One line pulled from the CSV file or URL
                input in the Schedule class.

        """

        if isinstance(course_info, str):
            stripped = course_info.strip("\n")
            info = stripped.split(",")
            self.code = info[0]
            self.name = info[1]
            self.section_number = info[2]
            self.credits = info[3]
            self.days = []

            if info[4].find("Class") > -1:
                day_info = [info[4], "", ""]
                new_day = Day(day_info)
                self.days.append(new_day)

            else:
                regex = r"""(?xm)
                            (?P<day>(M|Tu|W|Th|F){1,4})
                            (?:\s)
                            (?P<start>\d{1,2}\:\d{2}[a-z]{2})
                            (?:\s\-\s)
                            (?P<end>\d{1,2}\:\d{2}[a-z]{2})"""

                for i in range(len(info)):
                    match = re.search(regex, info[i])
                    if match:
                        day_info = [match.group("day"), match.group("start"),
                                    match.group("end")]
                        new_day = Day(day_info)
                        self.days.append(new_day)

        elif isinstance(course_info, list):
            self.code = course_info[0]
            self.name = course_info[1]
            self.section_number = course_info[2]
            self.credits = course_info[3]
            self.days = []

            day_info = [course_info[4],course_info[5], course_info[6]]
            new_day = Day(day_info)
            self.days.append(new_day)

    def __repr__(self):
        """ Returns string as representation of course info containing course
            code, name, section number, number of credits and days of
            the week"""

        return f"{self.code}, {self.name}, {self.section_number}, " \
               f"{self.credits}, {self.days}"


class Day:
    """ This class allows the day of the week, start time, and end time to be
    specified for the student's courses based on their provided file.

    Each instance of the Course class will have at least one associated Day
        class.

    Attributes:
        name (string): a string containing the name of the day.
        start (int): the time that the class starts.
        end (int): the time that the class ends.

    """

    def __init__(self, day_info):
        """ Creates a new instance of the Day class.

        Args:
           day_info (list of Strings): A string containing information such
            as the name of the day, as well as course start and end times
            for that day.

        """
        self.name = day_info[0]
        self.start = day_info[1]
        self.end = day_info[2]

    def __repr__(self):
        """ Returns string representation of day info and prints the name
            of days of the week, start time and end time of specified
            course."""

        if self.name == "Class time/details on ELMS" or \
                self.name == "Class Time and Details on ELMS":
            return f"[{self.name}]"
        else:
            return f"[{self.name}: {self.start} - {self.end}]"


def credit_count(current_schedule):
    """ Counts the total number of credits in the specified schedule and
            prints it to stdout.

    Args:
        current_schedule (Schedule): the student's current schedule.

    Side effects:
        Print: A string stating the current number of credits of student's current schedule.

    """

    total = 0
    for course in current_schedule.courses:
        total += int(course.credits)
    print(f"Your schedule currently contains {total} credits")


def main(major_link, student_schedule):
    """ Create two Schedules based on a URL to a UMD course offerings page
            and a CSV file of the student's partially complete schedule.

        Print and manipulate the two Schedules. Courses can be added and
            removed from each schedule. The number of credits in a
            Schedule can also be counted.

    Args:
        major_link (string): a link to the major's Schedule of Classes.
        student_schedule (string): the filepath of the user's schedule. The
            schedule should contain information on the User's pre-chosen
            classes, including course code, name, section_number, available
            seats, credits, and meeting days.

    Returns:
        see credit_count().

    Side Effects:
        See add_class() and remove_class().

    """

    # Creating schedule of classes for the Major (URL)
    class_schedule = Schedule(major_link)
    # Printing the schedule of classes for the Major
    class_schedule.print_schedule()

    # Newline for readability
    print("\n")

    # Creating schedule of classes for the student (CSV file).
    stud_schedule = Schedule(student_schedule)
    # Printing the schedule of classes for the Student.
    stud_schedule.print_schedule()

    # Newline for readability
    print("\n")
    
    addC = "null"
    while addC != "stop":
        addC = input("Please enter the class code of the course you would like"
                     " to add/remove, or type stop to end this program: ")
        if addC == "stop":
            break
        addS = input(f"Please enter the desired section number for {addC}: ")
        userChoice=input("Would you like to add or remove the specified "
                         "course? (type add or remove): ")
        if userChoice == "add" or userChoice == "Add":
            stud_schedule.add_class(class_schedule, addC, addS)
        elif userChoice == "remove" or userChoice == "Remove":
            stud_schedule.remove_class(addC, addS)
        else:
            continue
        printQ=input("Would you like to view your schedule? (yes or no): ")
        if printQ == "yes" or printQ == "Yes":
            stud_schedule.print_schedule()
            credit_count(stud_schedule)
        elif printQ == "no" or printQ == "No":
            continue
        editQ = input("Would you like to add these changes to your schedule "
                      "file? (yes or no): ")
        if editQ == "yes" or printQ == "Yes":
            stud_schedule.add_to_file(student_schedule)
        elif editQ == "no" or printQ == "No":
            continue


def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("major_link", help="standard URL that points to"
                                           "a testudo schedule of classes"
                                           "page for a specific major")
    parser.add_argument("student_schedule", help="path to a CSV file"
                                                 "containing information on"
                                                 "a student's current"
                                                 "schedule")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.major_link, args.student_schedule)



