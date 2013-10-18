"""
Reservation finder

Along with this file, you'll find two files named units.csv and reservations.csv with fields in the following format

location_id, unit_size
location_id, reservation_start_date, reservation_end_date

You will write a simple application that manages a reservation system. It will have two commands, 'available' and 'reserve' with the following behaviors:

available <date> <number of occupants> <length of stay>
This will print all available units that match the criteria. Any unit with capacity equal or greater to the number of occupants will be printed out.

Example:
SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available

reserve <unit number> <start date> <length of stay>
This creates a record in your reservations that indicates the unit has been reserved. It will print a message indicating its success.

A reservation that ends on any given day may be rebooked for the same evening, ie:
    
    If a reservation ends on 10/10/2013, a different reservation may be made starting on 10/10/2013 as well.

Example:
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights

Reserving a unit must make the unit available for later reservations. Here's a sample session:

SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights
SeaBnb> available 10/10/2013 2 4
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Unit 10 is unavailable during those dates
SeaBnb> quit

Notes:
Start first by writing the functions to read in the csv file. These have been stubbed for you. Then write the availability function, then reservation. Test your program at each step (it may be beneficial to write tests in a separate file.) Use the 'reservations' variable as your database. Store all the reservations in there, including the ones from the new ones you will create.

The datetime and timedelta classes will be immensely helpful here, as will the strptime function.
"""

import sys
from datetime import datetime, timedelta
import csv

def parse_date(date):

    parsed_date = datetime.strptime(
        date, "%m/%d/%Y")

    return parsed_date

def parse_one_record(reservation_list):#line
    """Take a line from reservations.csv and return a dictionary representing that record. (hint: use the datetime type when parsing the start and end date columns)"""

    reserve_dict = {}

    reservation = reservation_list.split(", ")

    reserve_id = reservation[0]
    start_date = parse_date(reservation[1])
    end_date = parse_date(reservation[2])

    reserve_dict["unit_id"] = reserve_id
    reserve_dict["start_date"] = start_date
    reserve_dict["end_date"] = end_date

    return reserve_dict

def read_units():
    """Read in the file units.csv and returns a list of all known units."""
    units = []
    f = open("units.csv")
    units_text = f.read().split("\n")
    for line in units_text:
        unit = line.split(', ')
        units.append(tuple(unit))
    return units

def read_existing_reservations():
    """Reads in the file reservations.csv and returns a list of reservations."""
    reservations = []
    f = open("reservations.csv")
    reserve_text = f.read().split("\n")
    for line in reserve_text:
        reservations.append(parse_one_record(line))
    f.close()
    return reservations

def available(units, reservations, start_date, occupants, stay_length):
    unit_id = 0
    available = []
    occupants = int(occupants)
    s_date = parse_date(start_date)
    length_of_stay = timedelta(days = int(stay_length))
    e_date = s_date + length_of_stay
    # units is a list of tuples
    # reservations is a list of dicts
    for unit in units:
        unit_id = unit[0]
        occupancy = int(unit[1])
        if occupants <= occupancy:
            #it's big enough
            available.append(unit_id)

    for reservation in reservations:
        if s_date < reservation["end_date"] and e_date > reservation["start_date"]:
            while reservation["unit_id"] in available:
                available.remove(reservation["unit_id"])

    # for reservation in reservations:
    # #    if c >= b or d <= a:
    #     if (s_date >= reservation["start_date"] or 
    #         e_date <= reservation["end_date"]):

    # # a -------- b
    # #     c --------- d
    # #            c -------- d

    # check occupants against unit[1]
    # stay length uses time delta to get end date
    for unit in available:
        print "Unit %r is available"%unit

    return available

def reserve(units, reservations, unit_id, start_date, stay_length):

    new_reservation = {}

    s_date = parse_date(start_date)
    e_date = s_date + timedelta(days = int(stay_length))

    new_reservation["unit_id"] = unit_id
    new_reservation["start_date"] = s_date
    new_reservation["end_date"] = e_date

    reservations.append(new_reservation)

    print "Successfully reserved unit %r for %r days" %(unit_id, stay_length)

def main():
    units = read_units()
    reservations = read_existing_reservations()  

    while True:
        command = raw_input("SeaBnb> ")
        cmd = command.split()
        if cmd[0] == "available":
            # look up python variable arguments for explanation of the *
            available(units, reservations, *cmd[1:])
        elif cmd[0] == "reserve":
            reserve(units, reservations, *cmd[1:])
        elif cmd[0] == "quit":
            sys.exit(0)
        else:
            print "Unknown command"


if __name__ == "__main__":
    main()