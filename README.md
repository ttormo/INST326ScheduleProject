# INST326ScheduleProject

## Files

 - INST326ScheduleProject.py is the file that includes the code for the main portion of this project. It is what should be run to actually use this program.

 - WebScraper.py is a support file for INST326ScheduleProject.py. It scrapes the HTML of a valid URL to find information on different classes.

 - scheduleTests.py contains unit tests for methods and functions within INST326ScheduleProject.py and WebScraper.py.

 - example_schedule.csv is the file that is used to test run this program. It contains information on an example schedule, formatted exactly as it should be for any given user.


## Running from the Command Line

 - To run this program from the command line, use the command "python" (or python3, if you are on a UNIX-based system), followed by INST326ScheduleProject.py, followed by the URL for a specific major page on Testudo's Schedule of Classes (for example, "https://app.testudo.umd.edu/soc/202108/INST"). Follow this with the filepath to your schedule (this MUST be a CSV file, formatted exactly as example_schedule.csv is).

 - Example: python INST326ScheduleProject.py "https://app.testudo.umd.edu/soc/202108/INST" "example_schedule.csv"

## Interpreting Output

 - Most of the output displayed in this program is faily self-explanatory. When the program is first run, it will output a list of all classes that have at least one open seat, and were found in the provided testudo page. This will be followed by some blank space, and then a representation of the user's provided schedule.

 - After this initial output, the program will ask several questions, all of which lead to output that is explained within the questions themselves.


