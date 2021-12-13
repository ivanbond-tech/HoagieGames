
from run_sim import *

def main():
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
    ]
    pattern = '|'.join(filters)

    query_mask = data['INCIDENTNEIGHBORHOOD'].str.contains(pattern, na=False, case=False)==0
    data = data[query_mask].dropna()
    
    # Storing neighborhood names in list
    neighborhoods = []
    for i in data.INCIDENTNEIGHBORHOOD.unique():
        neighborhoods.append(i)
    
    r = random.Random()
    player = Tribute("M", "South Oakland")
    player.set_neighborhood_id(neighborhoods)
    
    m = Map(40)
    m.generate_empty_map()
    
    x = r.randint(0, 39)
    y = r.randint(0, 39)
    m.set_pos(x, y, player.identifier)
    player.set_pos(x, y)
    
    print(f"{player.identifier} set at x: {x}, y: {y}")

    m.update_map()
    m.print_map()
    player.to_string()
    
    print("\nTESTING TUPLE METHODS\n")
    r = random.Random()
    current_x = 35
    current_y = 40
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
    move = r.choice(move_choices)
    print(f"x: {move[0]}")
    print(f"y: {move[1]}")
    
    print("\nTESTING PLAYER MOVEMENT\n")
    for i in range(200):
        m.move(player)
        m.print_map()
        time.sleep(0.2)
        os.system("clear")
    
    
    
if __name__ == "__main__":
    main()