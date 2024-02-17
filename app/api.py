from flask import Flask
from get_last_games_stats import get_last_games_stats


app = Flask(__name__)

@app.route('/')
def index():
    table = get_last_games_stats()
    return table

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
