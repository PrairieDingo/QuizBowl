#Quiz game for Gerald

import random

state_capitols = {}
world_capitols = {}

def import_info():
    state_file = open('states_and_capitols.txt', 'r')
    state_lines = state_file.readlines()
    for line in state_lines:
        entry = line.split(', ')
        state_capitols[entry[0]] = entry[1].strip()
    state_file.close()

    world_file = open('world_capitals.txt', 'r')
    world_lines = world_file.readlines()
    for line in world_lines:
        entry = line.split(',')
        world_capitols[entry[0]] = entry[1].strip()
    world_file.close()

def ask_state_capitol_question():
    state = random.choice(list(state_capitols.keys()))
    print("What is the state capitol of " + state + "?")
    answer = input().lower().strip()
    if answer == state_capitols[state].lower():
        print('That is correct!')
    else:
        print("I'm sorry! The answer is " + state_capitols[state])

def ask_world_capitol_question():
    nation = random.choice(list(world_capitols.keys()))
    print("What is the capitol of " + nation + "?")
    answer = input().lower().strip()
    if answer == world_capitols[nation].lower():
        print('That is correct!')
    else:
        print("I'm sorry! The answer is " + world_capitols[nation])

import_info()

while True:
    asks = [ask_state_capitol_question, ask_world_capitol_question]
    fn = random.choice(asks)
    fn()

    print('Try again? (y for yes)')
    if not input().lower().startswith('y'):
        break
