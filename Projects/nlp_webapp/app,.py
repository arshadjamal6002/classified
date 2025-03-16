from flask import Flask, jsonify, request
import ipl

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Worldzzd"

@app.route('/api/teams')
def teams():
    teams = ipl.teamsapi()
    # return should always be a json in case of an api
    # convert the dict to a json using inbuilt funciton
    return jsonify(teams)

@app.route('/api/team1vsteam2')
def team1vsteam2():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.team1vsteam2(team1, team2)
    return jsonify(response)

app.run(debug = True)
