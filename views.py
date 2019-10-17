from route_helper import simple_route
from flask import render_template

@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return render_template("index.html")

@simple_route('/character/race')
def character(world:dict):
    return render_template("race.html")

@simple_route('/character/head')
def character(world:dict):
    return render_template("head.html")

@simple_route('/save/race/')
def race(world:dict, race:str):
    return race

@simple_route('/save/head')
def head(world:dict, head:str):
    return head


@simple_route("/save/character/")
def save_character(world: dict, monsters_name: str, monsters_race: str,  monsters_head: str) -> str:
    """
    Update the name of the monster.

    :param monsters_head:
    :param monsters_race:
    :param world: The current world
    :param monsters_name:
    :return:
    """
    world['name'] = monsters_name
    world['race'] = monsters_race
    world['head'] = monsters_head

    FINAL_CREATION="""
    
    """

