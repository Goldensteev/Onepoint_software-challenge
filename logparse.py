#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from dateutil.parser import *

def gettime(line):
    """
    this function gets the time in the given string
    Args:
        line(str): the line wished to extract the time from
    Returns:
        time(datetime.datetime): returns the datetime.datetime object
    """
    time_ = parse(line, fuzzy=True, ignoretz=True)
    time_ = time_.replace(year=2021, microsecond=0)
    return time_

def logparse(file_):
    """
    this function goes through a file looking for 3 distinct messages (ON, OFF & ERR)
    Args:
        file_(str): path to the logfile
    """
    report = ""
    errorlogs = ""
    file_ = os.path.join(file_)
    with open(file_) as logfile:
        for line in logfile.readlines():
            if re.findall(r'Device State', line):
                if re.findall(r'ON', line):
                    starttime_ = gettime(line)
                elif re.findall(r'ERR', line):
                    time_ = gettime(line)
                    errorlogs += "Error logged on " + time_.strftime("%Y/%m/%d %I:%M:%S") + '\n'
                elif re.findall(r'OFF', line):
                    endtime_ = gettime(line)
        difference = endtime_ - starttime_
        report += "Device ran for: " + str(difference) + '\n' + errorlogs
    return report

print(logparse("C:\\Users\\fletc\\codespace\\Onepoint_software-challenge\\logfile.log"))