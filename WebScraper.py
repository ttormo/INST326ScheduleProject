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
    html = urllib.request.urlopen(url, context=ctx).read()
    rowList = str(html).split("\\n")
    return rowList


def classNames(rowList):
    names=[]
    for line in rowList:
        if '"course-id"'in line:
            name_start=line.find(">")+1
            name_end=line.find("</")
            class_name=line[name_start:name_end]
            names.append(class_name)
    return names


def getClassURL(url,class_name):
    newURL=str(url)+"/"+str(class_name)
    html = urllib.request.urlopen(newURL, context=ctx).read()
    cpage_lines = str(html).split("\\n")
    return cpage_lines


def classInfo(course_codes, user_input):
    """Pulls the official names, section numbers, days of the week,
    and start/end times for each course code, skipping over classes with
    no seats remaining. Two dictionaries are created: one pairing course
    code with course names, and one pairing course code with the rest of the
    above listed data. 
    
    classDict Outline -> course_code:[[course name, section number, day,
        start time, end-time],...]
    Note: Each course code has lists for each section number. Some section numbers
    may appear in two consecutive lists, indicating that the section meets twice
    in the same day.
    
    Args:
    course_codes (list): list of course codes
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
