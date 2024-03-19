from libraries import mens_prototype as mp
import numpy as np

houston = mp.Team('Houston', 'South', 1)
marquette = mp.Team('Marquette', 'South', 2)
kentucky = mp.Team('Kentucky', 'South', 3)
duke = mp.Team('Duke', 'South', 4)
wisconsin = mp.Team('Wisconsin', 'South', 5)
tex_tech = mp.Team('Texas Tech', 'South', 6)
florida = mp.Team('Florida', 'South', 7)
nebraska = mp.Team('Nebraska', 'South', 8)
tex_am = mp.Team('Texas A&M', 'South', 9)
colorado = mp.Team('Colorado', 'South', 10)
nc_state = mp.Team('North Carolina State', 'South', 11)
mcneese_st = mp.Team('McNeese State', 'South', 12)
samford = mp.Team('Samford', 'South', 13)
akron = mp.Team('Akron', 'South', 14)
western_ky = mp.Team('Western Kentucky', 'South', 15)
longwood = mp.Team('Longwood', 'South', 16)

test_bracket = [
    western_ky,
    houston,
    tex_am,
    colorado,
    samford,
    marquette,
    kentucky,
    nc_state,
    duke,
    mcneese_st,
    longwood,
    wisconsin,
    akron,
    tex_tech,
    florida,
    nebraska
]

#print(mp.set_matchups(test_bracket))

print(mp.play_region(test_bracket))
