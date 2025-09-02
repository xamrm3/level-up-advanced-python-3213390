from collections import namedtuple
import re

with open('challenge/olympics.txt', 'rt', encoding='utf-8') as file:    
    olympics = file.read()

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])

medals = [] #Complete this - medals is a list of medal namedtuples

for line in re.findall(r'.+;.+', olympics)[1:]:
    medals.append(medal(*line.split(";")))

def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    result = []
    for medal in medals:
        if all(getattr(medal, k) == v for k,v in kwargs.items()):
            result.append(medal)
    return result

