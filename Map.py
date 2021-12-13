import random
import os
import numpy as np 
from Tributes import Tribute

# Colors
RED = '\033[0;31m'
GREEN = '\033[0;32m'
BLUE = '\033[0;36m'
GRAY = '\033[0;37m'
NC = '\033[0m' # No Color

class Map:
    '''
    Matrix Map for Hoagie Games arena
    filled with traps and bonuses for tributes
    '''
    def __init__(self, size):
        self.area = None
        self.size = size
        self.traps = size-1
        self.bonuses = size-1
        
    def generate_empty_map(self):
        m = np.zeros((self.size, self.size))
        self.area = m
        
        
    def generate_map(self):
        m = np.zeros((self.size, self.size))
        
        r = random.Random()
        # randomly position traps
        for i in range(self.traps):
            x = r.randint(0, self.traps)
            y = r.randint(0, self.traps)
            m[x][y] = 9
        
        # randomly position bonuses
        for i in range(self.bonuses):
            x = r.randint(0, self.bonuses)
            y = r.randint(0, self.bonuses)
            m[x][y] = 1
        
        count = 0
        for i in range(180):
            x = r.randint(0, self.size-1)
            y = r.randint(0, self.size-1)
            m[x][y] = 999
            count+=1

        # write original map to file
        with open('./output/map.txt', 'w') as f:
            row = 0
            col = 0
            for i in range(len(m)):
                try:
                    for j in range(len(m)):
                        res = str(int(m[row][col]))
                        f.write(res + " ")
                        col+=1
                    f.write('\n')
                    col = 0
                    row+=1
                except:
                    pass
            f.close()
        
        self.area = m
        print(f'\nmap.txt written to {os.getcwd()}/output/map.txt')
        
    def print_map(self):
        m = self.area
        row = 0
        col = 0
        for i in range(len(m)):
            try:
                row_string = ""
                for j in range(len(m)):
                    res = int(m[row][col])
                    # free space
                    if res == 0:
                        row_string+=(str(res) + " ")
                    # space has a bonus
                    elif res == 1:
                        row_string+=(f"{GREEN}{str(res)}{NC} ")
                    # space has a trap
                    elif res == 9:
                        row_string+=(f"{RED}{str(res)}{NC} ")
                    # space is occupied by tribute
                    else:
                        row_string+=(f"{BLUE}{str(res)}{NC} ")
                    col+=1
                print(f"{row_string}")
                col = 0
                row+=1
            except:
                pass
            
    def update_map(self):
        m = self.area
        # write original map to file
        with open('./output/map.txt', 'w') as f:
            row = 0
            col = 0
            for i in range(len(m)):
                try:
                    for j in range(len(m)):
                        res = str(int(m[row][col]))
                        f.write(res + " ")
                        col+=1
                    f.write('\n')
                    col = 0
                    row+=1
                except:
                    pass
            f.close()
        
        self.area = m
        #print(f'map.txt written to {os.getcwd()}/output/map.txt')
            
    def get_pos(self, x, y):
        m = self.area
        return int(m[x][y])
    
    def set_pos(self, x, y, val):
        m = self.area
        m[x][y] = val
        
    
    def get_rand_pos(self):
        r = random.Random()
        x = r.randint(0, self.size-1)
        y = r.randint(0, self.size-1)
        return x,y
    
    def move(self, player):
        try:
            r = random.Random()
            current_pos = player.get_pos() # returns list [x, y]
            current_x = current_pos[0]
            current_y = current_pos[1]
            
            # 3x3 Matrix surrounding current pos
            # excluding current pos
            move_choices = [
                (current_x-1, current_y-1), # top left
                (current_x-1, current_y), # top middle
                (current_x-1, current_y+1), # top right
                (current_x, current_y-1), # left
                (current_x, current_y+1), # right
                (current_x+1, current_y-1), # bottom left
                (current_x+1, current_y), # bottom middle
                (current_x+1, current_y+1) # bottom right
            ]
            
            found_valid_move = False
            while not found_valid_move:
                rand_choice = r.choice(move_choices)
                move_x = rand_choice[0]
                if move_x < 0: # if row past start of map
                    move_x = 0
                elif move_x > self.size-1: # if row past end of map
                    move_x = self.size-1
                move_y = rand_choice[1] 
                if move_y < 0: # if col past start of map
                    move_y = 0
                elif move_y > self.size-1: # if col past end of map
                    move_y = self.size-1
                try:
                    check_valid_move = self.get_pos(move_x, move_y)
                    if check_valid_move is 0:
                        self.set_pos(move_x, move_y, player.identifier) # set player on map
                        player.set_pos(move_x, move_y) # set players pos
                        self.set_pos(current_x, current_y, 0) # reset players current pos
                        found_valid_move = True
                        break
                except:
                    continue
        except Exception:
            pass



            
            