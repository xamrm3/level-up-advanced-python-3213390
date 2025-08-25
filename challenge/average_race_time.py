# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('challenge/10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    results = re.split("\n", races)
    times = []
    for result in results:
        check = re.search("\\d+:\\d+?\\.?\\d+\\s+Jennifer Rhines", result)
        if check:
            times.append(check.group().split(" ")[0])
    return times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    
    delta = datetime.timedelta()
    for time in racetimes:
        if "." in time:
            delta += datetime.timedelta(minutes=int(time.split(":")[0]), seconds=int(time.split(":")[1].split(".")[0]), milliseconds=int(time.split(".")[1]))
        else:
            delta += datetime.timedelta(minutes=int(time.split(":")[0]), seconds=int(time.split(":")[1]))

    return str(delta/len(racetimes))[2:-5]