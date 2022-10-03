class Player:
    new_team1 = []
    
# Challenge 1: Update the Constructor
# I referenced a Stack Overflow post for help in building a constructor to accept data from a dictionary
    def __init__ (self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def get_team(cls, team_list):
        for i in team_list:
            new_member = Player(**i)
            Player.new_team1.append(new_member)

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, 
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

# Challenge 2: Create instances using individual player dictionaries  
player_kevin = Player(**kevin)
player_jason = Player(**jason)
player_kyrie = Player(**kyrie)

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, 
		"position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, 
		"position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, 
		"position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

# Challenge 3: Make a list of Player instances from a list of dictionaries
new_team = []
for i in players:
    member = Player(**i)
    new_team.append(member)

# Ninja Bonus
Player.get_team(players)

# Checking to make sure the class method works:
for i in range(0, len(Player.new_team1)):
	print(Player.new_team1[i].name)