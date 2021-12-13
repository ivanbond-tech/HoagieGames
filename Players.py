from Tributes import Tribute

class Players:
    
    def __init__(self):
        self.players_list = []
        self.players_pos = []
        self.dead_players = []
        self.winner = None
        
    def set_winner(self, player):
        self.winner = player
        
    def get_winner(self):
        return self.winner
    
    def add_player(self, player):
        self.players_list.append(player)
    
    def set_dead_player(self, player):
        self.dead_players.append(player)
        
    def add_player_pos(self, x, y):
        pos = (x, y)
        self.players_pos.append(pos)
        
    def get_player_pos(self, player):
        for i in range(len(self.players_list)):
            if player == self.players_list[i]:
                return self.players_pos[i]
            
    def get_player_by_pos(self, x, y):
        pos = (x, y)
        for i in range(len(self.players_pos)):
            if pos == self.players_pos[i]:
                return self.players_list[i]
    
    def print_players(self):
        count = 0
        for i in self.players_list:
            print(i.id)
            count+=1
        print(f"Total players: {count}")