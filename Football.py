import random
import time
import pprint


premier = ["Arsenal", "Aston Villa", "Brentford", "Brighton and Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Leeds United", "Leicester City", "Liverpool",
           "Manchester City", "Manchester United", "Newcastle United", "Norwich City", "Southampton", "Tottenham Hotspur", "Watford", "West Ham United", "Wolverhampton Wanderers"]

championship = ['Barnsley', 'Birmingham City', 'Blackburn Rovers', 'Blackpool', 'Bournmouth', 'Bristol City', 'Cardiff City', 'Coventry City', 'Derby County', 'Fulham', 'Huddersfield', 'Hull City', 'Luton Town',
                'Middlesbrough', 'Millwall', 'Nottingham Forest', 'Peterborough United', 'Preston North End', 'Queens Park Rangers', 'Reading', 'Sheffield United', 'Stoke City', 'Swansea City', 'West Bromwich Albion']

league_one = ['AFC Wimbledon', 'Accrington Stanley', 'Bolton', 'Burton', 'Cambridge United', 'Charlton', 'Cheltenham', 'Crewe Alexandra', 'Doncaster', 'Fleetwood', 'Gillingham', 'Ipswich Town',
              'Lincoln City', 'MK Dons', 'Morecambe', 'Oxford Utd', 'Plymouth Argyle', 'Portsmouth', 'Rotherham', 'Sheffield Wednesday', 'Shrewsbury', 'Sunderland', 'Wigan Athletic', 'Wycombe']

league_two = ['Barrow', 'Bradford City', 'Bristol Rovers', 'Carlisle', 'Colchester', 'Crawley Town', 'Exeter City', 'Forest Green', 'Harrogate Town', 'Hartlepool', 'Leyton Orient', 'Mansfield Town',
              'Newport County', 'Northampton Town', 'Oldham Athletic', 'Port Vale', 'Rochdale', 'Salford City', 'Scunthorpe', 'Stevenage', 'Sutton United', 'Swindon Town', 'Tranmere', 'Walsall']

# ***********************************************************************************************************************************

# print("")
# print("*"*100)
# print("")

# print(premier)
# print("")
# print("*"*100)
# print("")

# firstTeam = premier[random.randrange(0, len(premier))]
# secondTeam = premier[random.randrange(0, len(premier))]

# if (firstTeam == secondTeam):
#   firstTeam = premier[random.randrange(0, len(premier))]
#   secondTeam = premier[random.randrange(0, len(premier))]

# print(firstTeam)
# print("")
# print("*"*100)
# print(secondTeam)
# print("")

# home = []
# home.append(firstTeam)
# print(home)
# away = []
# away.append(secondTeam)
# fixtures = [home, away]
# print(fixtures)

# premierLeaugeFixtures = []
# premierLeaugeFixtures.append(fixtures)
# print(premierLeaugeFixtures)

# ***********************************************************************************************************************************

premierRound = premier
premierLeaugeFixtures = []

while (len(premierRound) > 0):
  firstTeam = premier[random.randrange(0, len(premier))]
  secondTeam = premier[random.randrange(0, len(premier))]
  goalsHome = random.randint(0,4)
  goalsAway = random.randint(0,4)
  if (firstTeam != secondTeam):
    # firstTeam = premier[random.randrange(0, len(premier))]
    # secondTeam = premier[random.randrange(0, len(premier))]
# ***********************************************************************************************************************************
    # print(firstTeam)
  # print("")
  # print("*"*100)
    # print(secondTeam)
  # print("")
# ***********************************************************************************************************************************
    home = []
    home.append(firstTeam)
    # print(home)
    away = []
    away.append(secondTeam)
    gameMatch = f"{firstTeam} {goalsHome} - {goalsAway} {secondTeam}" 
    fixtures = [home, away]
    # print(fixtures)
    # premierRound.remove(firstTeam)
    # premierRound.remove(secondTeam)
    premierLeaugeFixtures.append(gameMatch)
    print(premierRound)
    del premierRound[premier.index(firstTeam)]
    del premierRound[premier.index(secondTeam)]
# print(premierLeaugeFixtures)
for i in range(len(premierLeaugeFixtures)):
  print(premierLeaugeFixtures[i])
# extracting two teams done 



# Markos Code
# *************************************************************************************************************
# *************************************************************************************************************
# *************************************************************************************************************

# print(len(championship))
# print(championship[10].upper())
# print(championship[::2])
# championship.sort()
# print(championship)
# for index, club in enumerate(championship):
    
#     print(index + 1, club.upper())


# Map Function
# x = map(lambda club: club[0:], championship)
# for club in x:
#     print(club)

# Zip Function
# print(list(zip(league_one, league_two)))

# team1 = random.choice(championship)
# team2 = random.choice(championship)
# score1 = random.randint(0, 4)
# score2 = random.randint(0, 4)
# # print(f"{team1} {score1}-{score2} {team2}")


# fixtures = []

# for i in range(2):
#     fix = random.choice(championship)
#     while fix in fixtures:
#         fix = random.choice(championship)
#     fixtures.append(fix)
# print(fixtures)


# def home(team1):
#     return f"{team1} "


# def home_score(score1):
#     return f"{score1}"


# def away(team2):
#     return f"{team2}"


# def away_score(score2):
#     return f"{score2}"


# print(f"{home(team1)}vs {away(team2)}")
# print(f"{home(team1)}{home_score(score1)}-{away_score(score2)} {away(team2)}")

# listT = ["Arsenal", "Brentford"]
# print(f"{premier - listT}")

