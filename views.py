from route_helper import simple_route
from flask import render_template, session, request


@simple_route('/')
def hello(world: dict) -> str:
    return render_template('index.html', world=world)

@simple_route('/character')
def character_race(world: dict, where:str):
    world['location'] = where

    if not world['character']:
        world['character'].append()
    return render_template('race.html', world=world)


@simple_route('/head')
def character_head(world: dict, where:str):
    return render_template('head.html', world=world)


@simple_route('/legs')
def legs(world: dict, legs: str):
    return render_template("legs.html")

@simple_route("/save/")
def save_character(world: dict, *args) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param character_name:
    :return:
    """
    world['name'] = character_name
    world['race'] = character_race
    world['head'] = character_head

    world['character']['Race'] = request.values.get('character_race')
    world['character']['Head'] = request.values.get('character_head')

    return render_template('character_change.html', world=world)