from flask import Flask
from flask_cors import CORS

from get_last_games_stats import get_last_games_stats


app = Flask(__name__)
CORS(app)

@app.route('/get_last_games')
def index():
    table = get_last_games_stats()
    return table

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
