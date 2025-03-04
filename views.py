from route_helper import simple_route
from flask import render_template, session, request


@simple_route('/')
def hello(world: dict) -> str:
    return render_template('index.html', world=world)


@simple_route('/race')
def race(world: dict, *args) -> str:
    return render_template('race.html', world=world)


@simple_route('/head')
def head(world: dict, *args) -> str:
    return render_template('head.html', world=world)


@simple_route('/legs')
def legs(world: dict, *args):
    return render_template('legs.html', world=world)


@simple_route('/weapon')
def weapons(world: dict, *args):
    return render_template('weapon.html', world=world)


@simple_route('/skills')
def skills(world: dict, *args):
    return render_template('skills.html', world=world)


@simple_route('/character/completion')
def character_completion(world: dict, *args):
    return render_template('character_completion.html', world=world)


@simple_route("/save/race")
def save_race(world: dict, character_race: str) -> str:
    world['character']['race'] = character_race
    return render_template('head.html', world=world)


@simple_route("/save/head")
def save_head(world: dict, character_head: str) -> str:
    world['character']['head'] = character_head
    return render_template('legs.html', world=world)


@simple_route("/save/legs")
def save_legs(world: dict, character_legs: str) -> str:
    world['character']['legs'] = character_legs
    return render_template('weapon.html', world=world)


@simple_route("/save/weapon")
def save_weapon(world: dict, character_weapon: str) -> str:
    world['character']['weapon'] = character_weapon
    return render_template('skills.html', world=world)


@simple_route("/save/skills")
def save_skills(world: dict, character_skills: str, *args) -> str:
        world['character']['skills'] = character_skills
        return render_template('character_completion.html', world=world)
