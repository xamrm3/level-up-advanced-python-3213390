from collections import namedtuple
import re

with open('challenge/specifications.txt', 'rt') as file:
    specifications = file.read()

specs = namedtuple('specs', 'range regex')
#specs range builtin module
#specs regex from re.compile

def get_linkedin_dict():
    '''Convert specifications into a dict where:
       keys: feature
       values: specs namedtuple'''
    specs_dict = {}
    for line in specifications.splitlines():
        if 'feature' in line:
            feature = line.split()[-1]
        elif 'requirements' in line:
            nums = re.findall(r'\d+', line)
            req_range = range(int(nums[0]), int(nums[1]) + 1)
        elif 'permitted characters' in line:
            sets = line.split(":")[1].strip().split()
            regex = re.compile(r'[' + ''.join(sets) + r']+')
        elif 'login characters' in line:
            sets = line.split(":")[1].strip().split()
            sets = "".join(sets)
            regex = re.compile(r'[' + sets + r']+@[' + sets + r']+.com|net|org')
        else:
            specs_dict[feature] = specs(req_range, regex)
    return specs_dict

def check_linkedin_feature(feature_text, url_or_login):
    '''Raise a ValueError if the url_or_login isn't login or custom_url
       If feature_text is valid, return True otherwise return False'''
    
    feature_specs = get_linkedin_dict().get(url_or_login)
    if not feature_specs:
        raise ValueError("url_or_login must be either 'login' or 'custom_url'")
    length = len(feature_text)  in feature_specs.range
    regex = re.fullmatch(feature_specs.regex, feature_text) is not None  
    return length & regex