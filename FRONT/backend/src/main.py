# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS

from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .entities.cycling_team import CyclingTeam, CyclingTeamSchema, engine, Base

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/cycling_teams')
def get_cycling_teams():
    # fetching from the database
    teams_objects = session.query(CyclingTeam).all()
    for team in teams_objects:
        print(team)

    # transforming into JSON-serializable objects
    schema = CyclingTeamSchema(many=True)
    teams = schema.dump(teams_objects)

    # serializing as JSON
    session.close()
    return jsonify(teams)


@app.route('/cycling_teams/new', methods=['POST'])
def add_cycling_team():
    print(">> Posts")
    # mount exam object
    print(">> Req", request.get_json)
    posted_team = CyclingTeamSchema(only=('name', 'cyclist_number', 'victories'))\
        .load(request.get_json())
    print(">> Posted", posted_team)
    print(">> Requets", request.get_json())
    team = CyclingTeam(**posted_team, created_by="HTTP post request")

    # persist exam
    session.add(team)
    session.commit()

    # return created exam
    new_team = CyclingTeamSchema().dump(team)
    session.close()
    return jsonify(new_team), 201

@app.route('/cycling_teams/<key>/edit', methods=['PUT'])
def edit_cycling_team(key):
    print(">> Put",key)
    print(">> Req", request)
    team = session.query(CyclingTeam).get(key)
    
    edit_team = CyclingTeamSchema(only=('name', 'cyclist_number', 'victories'))\
        .load(request.get_json())
    print(edit_team)
    team.name = edit_team['name']
    team.victories = edit_team['victories']
    team.cyclist_number = edit_team['cyclist_number']
    team.update_at = datetime.now().strftime('%s')+'123'
   
    session.commit()
    new_team = CyclingTeamSchema().dump(team)
    session.close()
    return jsonify(new_team), 201

@app.route('/cycling_teams/<key>/delete', methods=['DELETE'])
def delete_cycling_team(key):
    print(">> Put",key)
    print(">> Req", request)
    team = session.query(CyclingTeam).get(key)
    print(team.name)
    session.delete(team)
    session.commit()
    session.close()
    del_team = CyclingTeamSchema().dump(team)
    return jsonify(del_team), 201

