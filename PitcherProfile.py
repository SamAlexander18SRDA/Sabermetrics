from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
import numpy as np

#Tool to give basic representation of a pitcher's arsenal, based on a given sample size, and first last name
#DATE FORMAT (YYYY-MM-DD) for both start and end
def PitcherProfile(firstName, lastName, dateStart, dateEnd):
    playerFound = playerid_lookup(lastName, firstName)

    #Implement fail-safe here incase player not located (null return val)
    print("Retrieved stats of " + playerFound['name_first'][0] + " " + playerFound['name_last'][0])

    #Now, pull pitch arsenal and average velocity
    pitcherNums = statcast_pitcher(dateStart, dateEnd, playerFound['key_mlbam'][0])
    pitchProfile = pitcherNums.groupby('pitch_type').release_speed.agg('mean')
    print(np.round(pitchProfile, 2))

PitcherProfile('kevin', 'gausman', '2023-04-01', '2023-10-06')

    