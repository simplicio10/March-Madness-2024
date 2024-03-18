class Team:

    def __init__(self, team_name, region, seed):
        self.team_name = team_name
        self.region = region
        self.seed = seed

    def get_seed(self):
        return self.seed