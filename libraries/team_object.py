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
    
    #Will populate bracket with teams from dataframe
    def createBracket(self):
        pass