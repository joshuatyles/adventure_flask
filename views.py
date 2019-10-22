from route_helper import simple_route
from flask import render_template, session, request


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return render_template('index.html', world=world)


@simple_route('/race')
def character(world: dict):
    return render_template("race.html")


@simple_route('/head')
def head(world: dict, head: str):
    return render_template("head.html")


@simple_route('/legs')
def legs(world: dict, legs: str):
    return render_template("legs.html")

@simple_route("/save/")
def save_character(world: dict, character_name: str, character_race: str, character_head: str) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param character_name:
    :return:
    """
    world['name'] = character_name
    world['race'] = character_race
    world['head'] = character_head

