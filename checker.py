"""Checker for CSC108 Assignment 2"""

import sys

sys.path.insert(0, './pyta')

print("================= Start: checking coding style =================")

import python_ta
python_ta.check_all('bikes.py', config='pyta/a2_pyta.txt')

print("================= End: checking coding style =================\n")

print("================= Start: checking parameter and return types =================")

import builtins
import bikes  # imported here so code that doesn't import correctly gets style checked

# Check for use of functions print and input.

our_print = print
our_input = input


def disable_print(*_args, **_kwargs):
    """ Notices if print is called """
    raise Exception("You must not call built-in function print!")


def disable_input(*_args, **_kwargs):
    """ Notices if input is called """
    raise Exception("You must not call built-in function input!")

builtins.print = disable_print
builtins.input = disable_input

# sample data for testing
sample_stations = [[7087,
                    'Danforth/Aldridge',
                    43.684371,
                    -79.316756,
                    23,
                    9,
                    14,
                    True,
                    True],
                   [7088,
                    'Danforth',
                    43.683378,
                    -79.322961,
                    15,
                    13,
                    2,
                    True,
                    False]]

# Type checks and simple checks for bikes module

# Type and simple check bikes.get_station_info
sample = [inner[:] for inner in sample_stations]
result = bikes.get_station_info(7087, sample)
assert isinstance(result, list), \
    '''bikes.get_station_info should return a list'''
assert len(result) == 3, \
    '''bikes.get_station_info should return a list of length 3'''
assert isinstance(result[0], str), \
    '''the first value in the list returned by bikes.get_station_info should be a str'''
assert isinstance(result[1], int), \
    '''the second value in the list returned by bikes.get_station_info should be an int'''
assert isinstance(result[2], int), \
    '''the third value in the list returned by bikes.get_station_info should be an int'''

# Type and simple check bikes.get_total
sample = [inner[:] for inner in sample_stations]
result = bikes.get_total(0, sample)
assert isinstance(result, int), \
    '''bikes.get_total should return an int'''
    
#Type and simple check for bikes.get_station_with_max_bikes
sample = [inner[:] for inner in sample_stations]
result = bikes.get_station_with_max_bikes(sample)
assert isinstance(result, int), \
    '''bikes.get_station_with_max_bikes should return an int'''
    
#Type and simple check for bikes.get_stations_with_n_docks
sample = [inner[:] for inner in sample_stations]
result = bikes.get_stations_with_n_docks(0, sample)
for inner in result:
    assert isinstance(inner, int), \
        '''bikes.get_stations_with_n_docks should return a list of ints'''
    
#Type and simple check bikes.get_direction
sample = [inner[:] for inner in sample_stations]
result = bikes.get_direction(7087, 7088, sample)
assert result.upper() in ['NORTH', 'WEST', 'EAST', 'SOUTH', \
                  'NORTHWEST', 'NORTHEAST', 'SOUTHWEST', 'SOUTHEAST'], \
       '''bikes.get_direction should return a direction string (check your spelling)'''

#Type and simple check bikes.clean_data
sample = [['1.5', 'bicycles', 'make'], ['a', 'tricycle', '', 'True']]
result = bikes.clean_data(sample)
assert isinstance(result, type(None)), \
    '''bikes.clean_data should return None'''

#Type and simple check bikes.rent_bike
sample = [inner[:] for inner in sample_stations]
result = bikes.rent_bike(7087, sample)
assert isinstance(result, bool), \
    '''bikes.rent_bike should return a bool'''

#Type and simple check bikes.return_bike
sample = [inner[:] for inner in sample_stations]
result = bikes.return_bike(7087, sample)
assert isinstance(result, bool), \
    '''bikes.return_bike should return a bool'''

#Type and simple check bikes.balance_all_bikes
sample = [inner[:] for inner in sample_stations]
result = bikes.balance_all_bikes(sample)
assert isinstance(result, type(None)), \
    '''bikes.balance_all_bikes should return None'''

builtins.print = our_print
builtins.input = our_input 

print("================= End: checking parameter and return types =================\n")

print("The parameter and return type checker passed.")
print("This means we will be able to test your code.")
print("It does NOT mean your code is necessarily correct.")
print("You should run your own thorough tests to convince yourself your code is correct.")
print()
print("Review the messages above to see the results of the style checking.")
