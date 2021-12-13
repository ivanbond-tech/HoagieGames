#!/usr/bin/python3

'''
    A simulation script to run Hunger Games style battle using
    data from wrpdc Pittsburgh Database. For class CMPINF0010
    Final project.
    
    Ivan Bondarenko
    BSCS + Mathematics
    University of Pittsburgh
    Class of 2023
    
    Support:
    ivb8@pitt.edu
    ivanbonddev@gmail.com
'''

import os, sys, getopt
import time
import random
import pandas as pd
from Map import Map
from Tributes import Tribute
from Players import Players

# Colors
RED = '\033[0;31m'
GREEN = '\033[0;32m'
BLUE = '\033[0;36m'
YELLOW = '\033[33m'
GRAY = '\033[0;37m'
NC = '\033[0m' # No Color

def main(argv):
    
    # Options
    VERBOSE = True
    NO_DISPLAY = False
    COLORS = False
    DELAY = 0.05
    TRIALS = 5
    SIZE = 40
    
    # Random number generator
    r = random.Random()
    
    # Command line arguments
    args_list = sys.argv[1:]
    options = "hcvt:"
    long_options = ["help", "color", "verbose", "trials="]
    error_message = "Invalid option. Try run_sim.py -h for help"
    
    try:
        args, vals = getopt.getopt(args_list, options, long_options)
        
        for curr_arg, curr_val in args:
            if curr_arg in ("-h", "--help"):
                print("\nPython simulation script for battle royale/hunger games style event.")
                print("example usage: python3 run_sim.py -v -c -t 20\n")
                print("options \t\t description\n")
                print("-h \t\t prints this help message")
                print("-c \t\t activates ANSI escape codes for terminal output. Default=on")
                print("-v \t\t activates verbose mode, lets you see sim in real-time. Default=off")
                print("-t [trials] \t set number of trials to perform. Default=5")
                print("\n")
                sys.exit()
            elif curr_arg in ("-c", "--color"):
                COLORS = True
            elif curr_arg in ("-v", "--verbose"):
                VERBOSE = True
                NO_DISPLAY = False
            elif curr_arg in ("-t", "--trials"):
                TRIALS = curr_val
                print(f"Trials set to {TRIALS}")
                
    except getopt.GetoptError:
        print(error_message)
        sys.exit(2)
            
    # Getting data from crime-data.csv
    data = pd.read_csv("./data/crime-data.csv")
    
    # cleaning data
    filters = [
        'Outside State',
        'Outside County', 
        'Outside City', 
        'Mt. Oliver Boro', 
        'Mt. Oliver Neighborhood', 
        'Golden Triangle/Civic Arena'
        'Troy Hill-Herrs Island',
        'Central North Side'
    ]
    pattern = '|'.join(filters)

    query_mask = data['INCIDENTNEIGHBORHOOD'].str.contains(pattern, na=False, case=False)==0
    data = data[query_mask].dropna()
    
    # Storing neighborhood names in list
    neighborhoods = []
    for i in data.INCIDENTNEIGHBORHOOD.unique():
        # Don't add the following non-neighborhoods
        if i != "Troy Hill-Herrs Island" and i!= "Central North Side" and i != "Golden Triangle/Civic Arena":
            neighborhoods.append(i)

    # look through data to find certain codes for offenses
    codes = [
        '2715', # Weapons of Mass Destruction
        '2706', # Terroristic threats
        '4953', # Mob related activity
        '8106', # Shots fired
        '2702', # Aggravated assualt
        '2501', # Criminal homicide
        '2707', # Propulsion of missiles
    ]

    pat = '|'.join(codes)
    query_mask = data['OFFENSES'].str.contains(pat, na=False, case=False)
    data = data[query_mask]
    
    # Generating map
    m = Map(SIZE)
    m.generate_map()
    
    # Initialize Players class to keep track of players
    p = Players()

    # Generating tributes for each neighborhood
    # and placing them into arena
    for n in neighborhoods:
        # Male tributes
        player = Tribute("M", n)
        player.set_neighborhood_id(neighborhoods)
        p.add_player(player)
        
        found = False
        if not found:
            for x in range(SIZE):
                if found:
                    break
                else:
                    for y in range(SIZE):
                        res = m.get_pos(x, y)
                        if res == 999:
                            m.set_pos(x, y, player.identifier)
                            player.set_pos(x, y)
                            p.add_player_pos(x, y)
                            found = True
                            break
        # Female tributes           
        player = Tribute("F", n)
        player.set_neighborhood_id(neighborhoods)
        p.add_player(player)
        
        found = False
        if not found:
            for x in range(SIZE):
                if found:
                    break
                else:
                    for y in range(SIZE):
                        res = m.get_pos(x, y)
                        if res == 999:
                            m.set_pos(x, y, player.identifier)
                            player.set_pos(x, y)
                            p.add_player_pos(x, y)
                            found = True
                            break
                    
    m.update_map()
    #p.print_players()
    
    # if verbose option set
    if VERBOSE: 
        print("\nStarting map:\n")
        m.print_map()
        print("\n")
        time.sleep(5)
        os.system("clear")
        print(f"{RED}Let the games begin!{NC}")
        time.sleep(3)
        
        trials = 200
        for n in range(trials):
            for pos in p.players_pos:
                x = pos[0]
                y = pos[1]
                player = p.get_player_by_pos(x, y)
                
                m.move(player)
                m.print_map()
                time.sleep(DELAY)
                os.system("clear")
            
            
        winner = r.randint(0, 91)
        os.system("./fireworks/main")
        os.system("clear")
        print(f"And the victor is tribute {GREEN}#{winner}{NC}! Congratulations District {BLUE}{neighborhoods[winner]}{NC}, \nyou are the winners of the {YELLOW}2021 Hoagie Games{NC}")


if __name__ == "__main__":
    main(sys.argv[1:])