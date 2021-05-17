import urllib.request, urllib.parse, urllib.error
import re
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#myURL = "https://app.testudo.umd.edu/soc/202108/INST"


#____FUNCTIONS_____

#takes URL, returns the list of the rows of code
def getHTML(url):
    """Takes given testudo schedule URL and splits it by line
    
    Args:
    url (string): a testudo link to a specific major's course list
    
    Returns:
    rowList is return, a list of each line from the split HTML
    """
    html = urllib.request.urlopen(url, context=ctx).read()
    rowList = str(html).split("\\n")
    return rowList


def classNames(rowList):
    """ Takes the lines of HTML from the given website and iterates through, pulling
    each course id as it goes and saving them to a list called names
    
    Args:
    rowList (list): A list of each line from the HTML
    
    Returns:
    names (list): list of course id's 
    """
    names=[]
    for line in rowList:
        if '"course-id"'in line:
            name_start=line.find(">")+1
            name_end=line.find("</")
            class_name=line[name_start:name_end]
            names.append(class_name)
    return names


def getClassURL(url,class_name):
     """ Takes the given url and class name and creates a new url for that specific
     class's info on testudo in order to pull specific class information
    
    Args:
    url (string): A given testudo url to all classes offered for a certain major
    class_name (string): the course id of a class from the names list
    
    Returns:
    cpage_lines (list): the lines of HTML from the newly created url
    """
    newURL=str(url)+"/"+str(class_name)
    html = urllib.request.urlopen(newURL, context=ctx).read()
    cpage_lines = str(html).split("\\n")
    return cpage_lines


def classInfo(course_codes, user_input):
    """Pulls the official names, section numbers, days of the week,
    and start/end times for each course code, skipping over classes with
    no seats remaining. A dictionary for all course info is created
    
    classDict Outline -> course_code:[[course_code, course name, section id, credits, day,
        start time, end-time],...]
    
    Args:
    course_codes (list): list of course codes
    user_input (string): the url to the full list of classes for a major
    
    returns: 
    classDict (dict): dictionary of course code as key and course info as value.
    the course info layout is given in an example above
    """
    classDict={}
    for name in course_codes:
        tList=[]
        cpage_lines=getClassURL(user_input,name)
        for line in cpage_lines:
            if "course-title" in line:
                tStart=line.find(">")+1
                tEnd=line.find("</span>")
                course_title=line[tStart:tEnd]

            if "course-min-credits" in line:
                credStart=line.find(">")+1
                credEnd=line.find("</span>")
                credits = line[credStart:credEnd]
            
            if 'name="sectionId" value' in line:
                id_start=line.find("value=")+7
                id_end=line.find("/>")-2
                class_id=line[id_start:id_end]
                
            if 'open-seats-count' in line: #890
                cstart=line.find(">")+1
                cend=line.find("</")
                seat_count=line[cstart:cend]

            if "section-days" in line:
                dstart=line.find(">")+1
                dend=line.find("</")
                day=line[dstart:dend]

            if "class-start-time" in line:
                time_start=line.find(">")+1
                time_end=line.find("</")
                time=line[time_start:time_end]
                
                leave_start=line.find('end-time">')+10
                leave_end=line.find("</",100)
                end_time=line[leave_start:leave_end]
                logistics=[name,course_title,class_id,credits,day,time,end_time]

                if int(seat_count) > 0:
                    tList.append(logistics)

            if "elms-class-message" in line: #964
                day="Class time/details on ELMS"
                time=""
                end_time=""
                logistics=[name,course_title,class_id,credits,day,time,end_time]
                if int(seat_count) > 0:
                    tList.append(logistics)
        classDict[name]=tList

    return classDict


#rowList=getHTML(myURL)
#course_codes=classNames(rowList)
#classInfo(course_codes)
