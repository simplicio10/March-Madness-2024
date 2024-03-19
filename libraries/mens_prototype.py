from libraries import win_probabilities as wp
import numpy as np

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

def set_matchups(teams):
        
        num_teams = [2, 4, 8, 16]

        if len(teams) not in num_teams:
            raise ValueError('Not the correct number of teams.\
                             Need 2, 4, 8, or 16 teams')
        else:
            teams.sort(key=lambda x: x.seed)
            top_half = [teams[i] for i in range((len(teams) // 2))]
            bottom_half = [teams[i] for i in range((len(teams) // 2), len(teams))]
            games = {}
            count = 1
            while top_half:
                games['game_' + str(count)] = (
                    top_half[0], 
                    bottom_half[-1])
                top_half.pop(0)
                bottom_half.pop()
                count += 1

        return games

#Write test for function
def play_region(matchups):
    
    winners = []

    for matchup in matchups.values():

        if matchup[0].getSeed() < matchup[1].getSeed():     
            high_seed = matchup[0].getSeed()
            low_seed = matchup[1].getSeed()
            diff = low_seed - high_seed
            winner = np.random.choice(
                        [matchup[0], matchup[1]], 
                        p=[wp.win_probs[diff], (1-wp.win_probs[diff])])
            winners.append(winner)

        elif matchup[0].getSeed() > matchup[1].getSeed():
            high_seed = matchup[1].getSeed()
            low_seed = matchup[0].getSeed()
            diff = low_seed - high_seed
            winner = np.random.choice(
                        [matchup[0], matchup[1]], 
                        p=[(1-wp.win_probs[diff]), wp.win_probs[diff]])
            winners.append(winner)

        else:
            winner = np.random.choice(
                        [matchup[0], matchup[1]], 
                        p=[wp.win_probs[0], wp.win_probs[0]])
            winners.append(winner)
            
    return winners
