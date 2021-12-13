class Tribute:
    
    def __init__(self, gender, neighborhood):
        self.alive = True
        self.allies = []
        self.gender = gender
        self.neighborhood = neighborhood
        self.identifier = None # int id
        self.id = None # string id
        self.pos_x = None
        self.pos_y = None
        self.pos = []
        #self.occupation = data['occupation']
        self.attributes = {
            "strength": 5,
            "perception": 5,
            "endurance": 5,
            "charisma": 5,
            "intelligence": 5,
            "agility": 5,
            "luck": 5,
        }
    
    def set_neighborhood_id(self, neighborhoods):
        hood_id = self.get_neighborhood_id(neighborhoods)
        self.identifier = hood_id
        self.set_str_id()
        
    def set_str_id(self):
        if self.gender == "M":
            self.id = str(self.identifier)+"M"
        elif self.gender == "F":
            self.id = str(self.identifier)+"F"
        
    def get_neighborhood_id(self, neighborhoods):
        count = 0
        for i in neighborhoods:
            if i == self.neighborhood:
                return count
            count+=1
            
    def get_pos(self):
        return self.pos
    
    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.pos = [self.pos_x, self.pos_y]
    
    def set_ally(self, Tribute):
        if len(self.allies) < 5:
            if self.attributes["charisma"] > 5 and Tribute.attributes["charisma"] > 5:
                self.allies.append(Tribute.identifier)
                
    def get_allies(self):
        return self.allies
    
    def print_allies(self, tabbed=False):
        for i in self.allies:
            if tabbed:
                print(f" - {i}")
            else:
                print(i)
            
    def print_attributes(self, tabbed=False):
        for i in self.attributes:
            if tabbed:
                print(f" - {i}: {self.get_attribute(i)}")
            else:
                print(f"{i}: {self.get_attribute(i)}")
            
    def set_attribute(self, attr, val):
        self.attributes[attr] = val
        
    def get_attribute(self, attr):
        return self.attributes[attr]
    
    def to_string(self):
        print(f"\nAlive: {self.alive}")
        print("Allies: ")
        self.print_allies(tabbed=True)
        print(f"Gender: {self.gender}")
        print(f"Neighborhood: {self.neighborhood}")
        print(f"Identifier: {self.identifier}")
        print(f"Pos: {self.pos}")
        print("Attributes: ")
        self.print_attributes(tabbed=True) 
        
    
    