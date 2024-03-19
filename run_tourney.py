from libraries import mens_prototype as mp
#from libraries import win_probabilities as wp
import numpy as np

houston = mp.Team('Houston', 'South', 1)
marquette = mp.Team('Marquette', 'South', 2)
kentucky = mp.Team('Kentucky', 'South', 3)
duke = mp.Team('Duke', 'South', 4)
wisconsin = mp.Team('Wisconsin', 'South', 5)
tex_tech = mp.Team('Texas Tech', 'South', 6)
florida = mp.Team('Florida', 'South', 7)
nebraska = mp.Team('Nebraska', 'South', 8)

test_bracket = [
    houston,
    marquette,
    kentucky,
    duke,
    wisconsin,
    tex_tech,
    florida,
    nebraska
]

#print(mp.set_matchups(test_bracket))

print(mp.play_region(mp.set_matchups(test_bracket)))
