from route_helper import simple_route
from flask import render_template, session, request


@simple_route('/')
def hello(world: dict) -> str:
    return render_template('index.html', world=world)


@simple_route('/race')
def race(world: dict, *args) -> str:
    return render_template('race.html', world=world)


@simple_route('/head')
def character_head(world: dict)->str:
    return render_template('head.html', world=world)


@simple_route('/legs')
def legs(world: dict, legs: str):
    return render_template("legs.html")


@simple_route("/save/race")
def save_character(world: dict, character_race: str) -> str:
    """
    Update the name of the monster.

    :param character_race:
    :param world: The current world
    :return:
    """


    return render_template('head.html', world=world)
