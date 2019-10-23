from route_helper import simple_route
from flask import render_template, session, request


@simple_route('/')
def hello(world: dict) -> str:
    return render_template('index.html', world=world)


@simple_route('/race')
def race(world: dict, *args) -> str:
    return render_template('race.html', world=world)


@simple_route('/head')
def head(world: dict) -> str:
    return render_template('head.html', world=world)


@simple_route('/legs')
def legs(world: dict):
    return render_template('legs.html', world=world)

@simple_route('/weapon')
def weapons(world: dict):
    return render_template('weapon.html', world=world)

@simple_route("/save/race")
def save_race(world: dict, character_race: str) -> str:
    """
    Update the name of the monster.

    :param character_race:
    :param world: The current world
    :return:
    """

    return render_template('head.html', world=world)


@simple_route("/save/head")
def save_head(world: dict) -> str:
    """
    Update the name of the monster.

    :param character_head:
    :param world: The current world
    :return:
    """

    return render_template('legs.html', world=world)

@simple_route("/save/legs")
def save_legs(world: dict) -> str:
    """
    Update the name of the monster.

    :param character_legs:
    :param world: The current world
    :return:
    """

    return render_template('weapon.html', world=world)

@simple_route("/save/weapon")
def save_weapon(world: dict) -> str:
    """
    Update the name of the monster.

    :param character_weapon:
    :param world: The current world
    :return:
    """

    return render_template('skills.html', weapon=world)