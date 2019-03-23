'''CSC108 Assignment 2 Starter code'''

from typing import List, TextIO
import math

# A type to represent cleaned (see clean_data()) for multiple stations
SystemData = List[List[object]]
# A type to represent cleaned data for one station
StationData = List[object]
# A type to represent a list of stations
StationList = List[int]


####### CONSTANTS ##################################

# A set of constants representing a list index for particular
# station information.
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6
IS_RENTING = 7
IS_RETURNING = 8


####### BEGIN HELPER FUNCTIONS ####################

def is_number(value: str) -> bool:
    '''Return True iff value represents a decimal number.

    >>> is_number('csc108')
    False
    >>> is_number('  108 ')
    True
    >>> is_number('+3.14159')
    True
    '''

    return value.strip().lstrip('+-').replace('.', '', 1).isnumeric()


def direction_bearing(variable: int) -> str:
    ''' Convert a bearing into degrees to a compass direction

    >>> direction_bearing(0)
    'NORTH'
    >>> direction_bearing(180)
    'SOUTH'
    >>> direction_bearing(252.9)
    'WEST'
    '''

    if variable >= 22.5 and variable < 67.5:
        return 'NORTHEAST'
    if variable >= 67.5 and variable < 112.5:
        return 'EAST'
    if variable >= 112.5 and variable < 157.5:
        return 'SOUTHEAST'
    if variable >= 157.5 and variable < 202.5:
        return 'SOUTH'
    if variable >= 202.5 and variable < 247.5:
        return 'SOUTHWEST'
    if variable >= 247.5 and variable < 292.5:
        return 'WEST'
    if variable >= 292.5 and variable < 337.5:
        return 'NORTHWEST'
    else:
        return 'NORTH'


def attain_variance(stations: SystemData) -> float:
    ''' Returns a float containing the variance for all
    the stations in stations.

    >>> attain_variance(SAMPLE_STATIONS)
    176.05
    >>> attain_variance(HANDOUT_STATIONS)
    272.50
    >>> attain_variance(bike_stations)
    886.49

    '''

    avg = get_total(BIKES_AVAILABLE, stations) / \
          get_total(CAPACITY, stations) * 100

    variance = 0
    for i in range(len(stations)):
        if stations[i][IS_RENTING] or stations[i][IS_RETURNING]:
            variance += ((stations[i][BIKES_AVAILABLE]/ \
                          stations[i][CAPACITY]*100 - avg) ** 2)
    variance = variance / (len(stations))
    
    return round(variance, 2)


# It isn't necessary to call this function to implement your bikes.py
# functions, but you can use it to create larger lists for testing.
# See the main block below for an example of how to do that.
def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    '''Return the contents of the open CSV file csv_file as a list of lists,
    where each inner list contains the values from one line of csv_file.

    Docstring examples not provided since results depend on a data file.
    '''

    # Read and discard the header
    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data


### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####
# You will wish to add additional examples, but when you do, either
# create new constants or update the results that use these examples.

SAMPLE_STATIONS = [
    [7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False],
    ]

HANDOUT_STATIONS = [
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, True,
     True],
    [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,
     15, 5, 10, True, True]]

STATION_LST = [
    [7009, 'King St E / Jarvis St', 43.650325, -79.372287, 11, 0, 11, True, True], 
    [7004, 'University Ave / Elm St', 43.656518, -79.389099, 11, 0, 11, True, True]]

GET_DIRECTION_LST = [
    [7009, 'King St E / Jarvis St', 43.650325, -79.372287, 11, 0, 11, True, True], 
    [7009, 'King St E / Jarvis St', 43.650325, -79.372287, 11, 0, 11, True, True]]

DIRECTION_LST = [
    [7005, 'University Ave / King St W', 43.648093, -79.384749, 19, 0, 18, True, True]
    , [7006, 'Bay St / College St', 43.66009, -79.3857, 11, 0, 11, True, True]]

RETURN_BIKE_LST = [
    [7012, 'Elizabeth St / Edward St', 43.65615, -79.3852, 15, 15,
     0, True, True]]


####### FUNCTIONS TO WRITE ########################

def clean_data(data: List[List[str]]) -> None:
    '''Modify the list data by converting each string in data to:
        . an int iff if it represents a whole number
        . a float iff it represents a number that is not a whole number
        . True or False iff the string is 'True' or 'False', respectively
        . None iff the string is 'null' or the empty string
    and leaving the string as it is otherwise.

    >>> d = [['abc', '123', '45.6', 'True', 'False']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, True, False]]
    >>> d = [['ab2'], ['-123'], ['False', '3.2']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], [False, 3.2]]
    >>> d =[['43.9'], 'CSC108', ['CSC148', '4.0']]
    >>> clean_data(d)
    >>> d
    [[43.9], 'CSC108', ['CSC148', 4.0]]
    '''
    
    for sublist in data:
        for a in range(len(sublist)):
            if is_number(sublist[a]):
                if float(sublist[a]) % 2 == 0 or (float(sublist[a]) + 1) % 2\
                   == 0:
                    sublist[a] = float(sublist[a])
                    sublist[a] = int(sublist[a])
                else:
                    sublist[a] = float(sublist[a])
            elif sublist[a].lower() == 'true':
                sublist[a] = True
            elif sublist[a].lower() == 'false':
                sublist[a] = False
            elif sublist[a] == 'null' or sublist[a] == '':
                sublist[a] = None

                
def get_station_info(station_id: int, stations: SystemData) -> StationData:
    '''Return a list containing the following information from stations
    about the station with id number station_id:
        . station name
        . number of bikes available
        . number of docks available
    (in this order)

    Precondition: station_id will appear in stations.

    >>> get_station_info(7087, SAMPLE_STATIONS)
    ['Danforth/Aldridge', 9, 14]
    >>> get_station_info(7088, SAMPLE_STATIONS)
    ['Danforth/Coxwell', 13, 2]
    >>> get_station_info(7012, RETURN_BIKE_LST)
    ['Elizabeth St / Edward St', 15, 0]
    '''
    
    station_info = []

    for b in stations:
        if station_id == b[ID]:
            station_info.append(b[NAME])
            station_info.append(b[BIKES_AVAILABLE])
            station_info.append(b[DOCKS_AVAILABLE])

    return station_info


def get_total(index: int, stations: SystemData) -> int:
    '''Return the sum of the column in stations given by index.

    Precondition: the items in stations at the position
                  that index refers to are ints.

    >>> get_total(BIKES_AVAILABLE, SAMPLE_STATIONS)
    22
    >>> get_total(DOCKS_AVAILABLE, SAMPLE_STATIONS)
    16
    >>> get_total(BIKES_AVAILABLE, HANDOUT_STATIONS)
    25
    >>> get_total(DOCKS_AVAILABLE, HANDOUT_STATIONS)
    21
    '''
    
    total = 0
    for c in range(len(stations)):
        total += stations[c][index]
    return total 


def get_station_with_max_bikes(stations: SystemData) -> int:
    '''Return the station ID of the station that has the most bikes available.
    If there is a tie for the most available, return the station ID that appears
    first in stations.

    Precondition: len(stations) > 0

    >>> get_station_with_max_bikes(SAMPLE_STATIONS)
    7088
    >>> get_station_with_max_bikes(bike_station)
    7033
    >>> get_station_with_max_bikes(STATION_LST)
    7009
    '''
    
    id_max_bikes = stations[0][0]
    max_bikes = stations[0][5]
    for d in (range(len(stations))):
        if (stations[d][5] > max_bikes):
            max_bikes = stations[d][5]
            id_max_bikes = stations[d][0]

    return id_max_bikes


def get_stations_with_n_docks(n: int, stations: SystemData) -> StationList:
    '''Return a list containing the station IDs for the stations in stations
    that have at least n docks available, in the same order as they appear
    in stations.

    Precondition: n >= 0

    >>> get_stations_with_n_docks(2, SAMPLE_STATIONS)
    [7087, 7088]
    >>> get_stations_with_n_docks(5, SAMPLE_STATIONS)
    [7087]
    >>> get_stations_with_n_docks(99, STATION_LST)
    []
    >>> get_stations_with_n_docks(0, HANDOUT_STATIONS)
    [7000, 7001]
    '''
    
    station_id_list = []
    for e in range(len(stations)):
        if stations[e][6] >= n:
            station_id_list.append(stations[e][0])
    return station_id_list 


def get_direction(start_id: int, end_id: int, stations: SystemData) -> str:
    '''Return a string that contains the direction to travel to get from
    station start_id to station end_id according to data in stations.

    Precondition: start_id and end_id will appear in stations.

    >>> get_direction(7087, 7088, SAMPLE_STATIONS)
    'WEST'
    >>> get_direction(7009, 7009, STATION_LST)
    ' '
    >>> get_direction(DIRECTION_LST)
    'NORTH' 
    '''

    
    for station in stations:
        if start_id == station[ID]:
            x1 = station[LONGITUDE]
            y1 = station[LATITUDE]
        if end_id == station[ID]:
            x2 = station[LONGITUDE]
            y2 = station[LATITUDE]
    longtitude_difference = math.radians(x2-x1)

    y1 = math.radians(y1)
    y2 = math.radians(y2)

    variable_y = math.sin(longtitude_difference) * math.cos(y2)
    variable_x = math.cos(y1) * math.sin(y2) - math.sin(y1) * math.cos(y2)*\
                 math.cos(longtitude_difference)

    variable = round(math.degrees(math.atan2(variable_y, variable_x)))

    if (variable < 0):
        variable = 360 - abs(variable)
    elif x1 == x2 and y1 == y2:
        return " "

    return direction_bearing(variable)


def rent_bike(station_id: int, stations: SystemData) -> bool:
    '''Update the specified available bike count and the docks available
    count in stations, if possible. Return True iff the rental from
    station_id was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available - 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available + 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    >>> rent_bike(7009, GET_DIRECTION_LST)
    False
    '''
    
    for station in stations:
        if station[0] == station_id:
            if station[7] and station[5] >= 1:
                station[5] = station[5] - 1
                station[6] = station[6] + 1
                return True
            else:
                return False 
                

def return_bike(station_id: int, stations: SystemData) -> bool:
    '''Update stations by incrementing the appropriate available bike
    count and decrementing the docks available count, if possible.
    Return True iff a bike is successfully returned to station_id.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available + 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available - 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    >>> return_bike(7009, RETURN_BIKE_LST)
    False
    '''
    
    for station in stations:
        if station[0] == station_id:
            if station[8] and station[6] >= 1:
                station[5] = station[5] + 1
                station[6] = station[6] - 1
                return True
            else:
                return False

def balance_all_bikes(stations: SystemData) -> None:
    '''Update stations by redistributing bikes so that, as closely as
    possible, all bike stations has the same percentage of bikes available.

    >>> balance_all_bikes(HANDOUT_STATIONS)
    >>> HANDOUT_STATIONS == [\
     [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 17, 14, True,
     True],\
     [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,\
     15, 8, 7, True, True]]
    True
    >>> balance_all_bikes(SAMPLE_STATIONS)
    >>> SAMPLE_STATIONS == [\
    [[7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False]]
    True
    >>> balance_all_bikes()
    
    
    '''
    # Notes:
    # Calculate the percentage of bikes available across all stati00ons
    # and balance the number of bikes available at each station so that
    # the percentage is similar across all stations.
    #
    # Remove bikes from a station if and only if the station is renting
    # and there is a bike available to rent, and return a bike if and
    # only if the station is allowing returns and there is a dock
    # availabletotal = 0

 
    mean = get_total(BIKES_AVAILABLE, stations) / \
              get_total(CAPACITY, stations) * 100
    variance = attain_variance(stations)

    z = 0
    while z < len(stations):
        for station in stations:
            for difference in stations:
                x = variance
                x = x * len(stations)
                x = x - (station[BIKES_AVAILABLE]/ \
                         station[CAPACITY] * 100 - mean) ** 2 - \
                         (difference[BIKES_AVAILABLE]/ difference[CAPACITY] \
                          * 100 - mean) ** 2
                x = x + ((station[BIKES_AVAILABLE] - 1) / \
                         station[CAPACITY] * 100 - mean) ** 2 + \
                         ((difference[BIKES_AVAILABLE] + 1) / \
                          difference[CAPACITY] * 100 - mean) ** 2
                x = x / len(stations)

                if x < variance \
                and station[IS_RENTING] and difference[IS_RETURNING] and \
                station[BIKES_AVAILABLE] > 0 and difference[DOCKS_AVAILABLE] > 0:
                    rent_bike(station[ID], stations)
                    return_bike(difference[ID], stations)
                    variance = x
                    z = -1
        z += 1

        
    # # To test your code with larger lists, you can uncomment the code below to
    # # read data from the provided CSV file.

if __name__ == '__main__':
            
    
    stations_file = open('stations.csv')
    bike_stations = csv_to_list(stations_file)
    clean_data(bike_stations)

    # # For example,
    # print('Testing get_station_with_max_bikes: ', \
    #     get_station_with_max_bikes(bike_stations) == 7033)
