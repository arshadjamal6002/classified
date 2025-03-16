import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)

print(matches.head())

def teamsapi():
    teams = list(set(list(matches.Team1) + list(matches.Team2)))
    team_dict = {
        'teams' : teams
    }
    return team_dict

def team1vsteam2(team1, team2):
    filter1 = (matches.Team1 == team1) & (matches.Team2 == team2)
    filter2 = (matches.Team2 == team1) & (matches.Team1 == team2)
    temp = matches[filter1 | filter2]
    total = temp.shape[0]
    team1_win = temp.WinningTeam.value_counts()[team1]
    team2_win = temp.WinningTeam.value_counts()[team2]
    draws = temp.WinningTeam.isnull().sum()
    response = {
        'total_matches_played' : total,
        'team1_wins' : int(team1_win),
        'team2_wins' : int(team2_win),
        'matches_draw' : int(draws)
    }

    return response