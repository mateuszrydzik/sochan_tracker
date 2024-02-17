from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

def get_last_games_stats():
    play = players.find_players_by_last_name('sochan')
    sochan_id = play[0]['id']
    logs = playergamelog.PlayerGameLog(player_id = sochan_id).get_data_frames()
    logs = logs[0].head(5)
    logs = logs[['GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'PTS', 'FGM', 'FGA', 'REB', 'AST', 'STL', 'BLK', 'TOV']]
    table = logs.to_dict(orient='records')
    return table
