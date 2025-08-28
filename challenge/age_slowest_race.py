# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days

import re
import datetime

def get_data():
    with open('challenge/10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    
    def convert_date(date):
        date = date.split(" ")
        return datetime.date(int(date[2]), datetime.datetime.strptime(date[1], "%b").month, int(date[0]))
    
    race_time = line[3:re.search(r'\s', line[3:]).start() + 3]
    dates = re.findall(r'\d{2} .{3} \d{4}', line)
    age = (convert_date(dates[0]) - convert_date(dates[1])).days / 365.25
    age = str(int(age)) + "y" + str(round((age % 1) * 365.25)) + "d"
    return (age, race_time)
    
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    rhines_times = []
    
    # from average_race_time_solution.py
    for line in races.splitlines():
       if 'Jennifer Rhines' in line:
          rhines_times.append(get_event_time(line))
    
    race = max(rhines_times, key = lambda x: x[1])

    return race