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


ENCOUNTER_MONSTER = """
<!-- Curly braces let us inject values into the string -->
You are in {}. You found a monster!<br>

<!-- Image taken from site that generates random Corgi pictures-->
<img src="http://placecorgi.com/260/180" /><br>
    
What is its name?

<!-- Form allows you to have more text entry -->    
<form action="/save/name/">
    <input type="text" name="player"><br>
    <input type="submit" value="Submit"><br>
</form>
"""

@simple_route('/race')
def character(world:dict):
    return render_template("race.html")

@simple_route('/save/race/')
def race(world:dict, race:str):
    return race
@simple_route('/head')
def head(world:dict, head:str):
    return render_template("head.html")
@simple_route('/legs')
def legs(world:dict, legs:str):
    return render_template("legs.html")

@simple_route('/goto/<where>/')
def open_door(world: dict, where: str, GAME_HEADER=None) -> str:
    """
    Update the player location and encounter a monster, prompting the player
    to give them a name.

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player
    """
    world['location'] = where
    return GAME_HEADER+ENCOUNTER_MONSTER.format(where)


@simple_route("/save/character/")
def save_character(world: dict, monsters_name: str, monsters_race: str,  monsters_head: str) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param monsters_name:
    :return:
    """
    world['name'] = monsters_name
    world['race'] = monsters_race
    world['head'] = monsters_head

    return GAME_HEADER+"""You are in {where}, and you are nearby {monster_name}
    <br><br>
    <a href='/'>Return to the start</a>
    """.format(where=world['location'], monster_name=world['name'])
