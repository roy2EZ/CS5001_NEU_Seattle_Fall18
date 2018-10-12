LINK_STATIONS = ["University of Washington", "Capitol Hill", "Westlake", 
                "University Street", "Pioneer Square", 
                "International District/Chinatown", "Stadium", "SODO", 
                "Beacon Hill", "Mount Baker", "Columbia City", "Othello", 
                "Rainier Beach", "Tukwila International Boulevard", 
                "SeaTac/Airport", "Angle Lake"]

#### PURPOSE
# Returns True if a given string is a valid Seattle Link station name, 
# False otherwise.
#### SIGNATURE
# is_valid_station :: String => Boolean
#### TEMPLATE
# def is_valid_station(given given…):
#   return returns…
#### EXAMPLES
# is_valid_station(“Tacoma”) => False
# is_valid_station(“SeaTac/Airport”) => True
def is_valid_station(station):
    return station in LINK_STATIONS   

#### PURPOSE
# Given start and end stations, returns “Northbound” if the end station is 
# north of the start station, or “Southbound” if the end station is south of 
# the start station. If either station is invalid, or start and end stations 
# are the same, return “No destincation found”.
#### SIGNATURE
# get_direction :: (String, String) => String
#### TEMPLATE
# def get_direction(given given…):
#   return returns…
#### EXAMPLES
# NOTE: These examples assume the first parameter is the start station
# get_direction(“Stadium”, “Capitol Hill”) => “Northbound”
# get_direction(“Othello”, “SeaTac/Airport”) => “Southbound”
# get_direction(“Othello”, “Othello”) => “No destination found”
def get_direction(station1,station2):
    if LINK_STATIONS.index(station1)<LINK_STATIONS.index(station2):
        return "Southbound"
    elif LINK_STATIONS.index(station1)>LINK_STATIONS.index(station2):
        return "Northbound"
    else:
        return "No destination found"

#### PURPOSE
# Returns the number of stops from start to end. If either station is invalid 
# or both stations are the same, return 0.
#### SIGNATURE
# get_num_stops :: (String, String) => Integer
#### TEMPLATE
# def get_num_stops(given…):
#   return returns…
#### EXAMPLES
# NOTE: These examples assume the first parameter is the start station
# get_num_stops(“Stadium”, “Capitol Hill”) => 5
# get_num_stops(“Othello”, “SeaTac/Airport”) => 3
# get_num_stops(“Othello”, “Othello”) => 0
def get_num_stops(station1,station2):
    return abs(LINK_STATIONS.index(station1)-LINK_STATIONS.index(station2))

#### ADDITIONAL (OPTIONAL) HELPER FUNCTIONS

#### TESTS (REQUIRED FUNCTIONS)
def test_is_valid_station():
    assert(is_valid_station("Angle Lake") == True)
    assert(is_valid_station("Bellingham") == False)
    assert(is_valid_station("SeaTac/Airport") == True)

def test_get_direction():
    assert(get_direction("University of Washington", "Angle Lake") == "Southbound")
    assert(get_direction("Angle Lake", "University of Washington") == "Northbound")
    assert(get_direction("University Street", "University Street") == "No destination found")

def test_get_num_stops():
    assert(get_num_stops("University of Washington", "Angle Lake") == 15)
    assert(get_num_stops("Angle Lake", "University of Washington") == 15)
    assert(get_num_stops("University Street", "University Street") == 0)

#### TESTS (OPTIONAL HELPER FUNCTIONS)

#### MAIN FUNCTION DEFINITION
def main():
    station1 = input("Please enter your start station: ")
    station2 = input("Please enter your end station: ")
    if is_valid_station(station1) and is_valid_station(station2):
        print("Your direction is: %s" % get_direction(station1,station2))
        print("There are %s stops to arrive your destination." % get_num_stops(station1,station2))
    else:   
        print("Sorry, please double check the station name(s) you entered.")
        main()
 
main()

    
        
    
        
    


        