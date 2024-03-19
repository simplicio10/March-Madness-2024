from libraries import prototype_functions as func
from libraries import team_object as tm

houston = tm.Team('Houston', 'South', 1)
marquette = tm.Team('Marquette', 'South', 2)
kentucky = tm.Team('Kentucky', 'South', 3)
duke = tm.Team('Duke', 'South', 4)
wisconsin = tm.Team('Wisconsin', 'South', 5)
tex_tech = tm.Team('Texas Tech', 'South', 6)
florida = tm.Team('Florida', 'South', 7)
nebraska = tm.Team('Nebraska', 'South', 8)
tex_am = tm.Team('Texas A&M', 'South', 9)
colorado = tm.Team('Colorado', 'South', 10)
nc_state = tm.Team('North Carolina State', 'South', 11)
mcneese_st = tm.Team('McNeese State', 'South', 12)
samford = tm.Team('Samford', 'South', 13)
akron = tm.Team('Akron', 'South', 14)
western_ky = tm.Team('Western Kentucky', 'South', 15)
longwood = tm.Team('Longwood', 'South', 16)

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

#print(func.set_matchups(test_bracket))

print(func.play_region(test_bracket))
