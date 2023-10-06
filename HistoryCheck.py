from pybaseball import schedule_and_record

def PullTeam(teamAbb, year):
    team_record = schedule_and_record(year, teamAbb)
    team_record.head()