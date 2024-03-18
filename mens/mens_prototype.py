class Team:

    def __init__(self, team_name, region, seed):
        self.team_name = team_name
        self.region = region
        self.seed = seed

    def __repr__(self) -> str:
        return repr(f"{self.team_name}, {str(self.seed)} seed, {self.region} region")

    def getSeed(self):
        return self.seed
    
    def getRegion(self):
        return self.region
    
    #Fill in to create bracket from df or other object
    def createBracket(self):
        pass

def setMatchups(teams):
        num_teams = [2, 4, 8, 16]
        if len(teams) not in num_teams:
            raise ValueError('Not the correct number of teams.\
                             Need 2, 4, 8, or 16 teams')
        else:
            teams.sort(key=lambda x: x.seed)