#Quiz game for Gerald

import random

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
    global num_correct
    state = random.choice(list(state_capitols.keys()))
    print("What is the state capitol of " + state + "?")
    answer = input().lower().strip()
    if answer == state_capitols[state].lower():
        print('That is correct!')
        num_correct += 1
    else:
        print("I'm sorry! The answer is " + state_capitols[state])
        while answer != state_capitols[state].lower():
            print('What is the state capitol of ' + state + '?')
            answer = input().lower().strip()
    state_capitols.pop(state)

def ask_world_capitol_question():
    global num_correct
    nation = random.choice(list(world_capitols.keys()))
    print("What is the capitol of " + nation + "?")
    answer = input().lower().strip()
    if answer == world_capitols[nation].lower():
        print('That is correct!')
        num_correct += 1
    else:
        print("I'm sorry! The answer is " + world_capitols[nation])
        while answer != world_capitols[nation].lower():
            print('What is the capitol of ' + nation + '?')
            answer = input().lower().strip()
    world_capitols.pop(nation)

def run_quiz(q_number, categories):
    for x in range(q_number):
        asks = categories
        fn = random.choice(asks)
        fn()

def get_question_number():
    print('How many questions would you like to answer?')
    q_number = 0
    while(q_number == 0 or q_number > 50):
        try:
            q_number = int(input())
            if q_number==0 or q_number > 50:
                print('Enter an integer greater than zero and less than 50.')
        except:
            print('Make sure to enter an integer greater than zero.')
    return q_number

#Start the program
while True:
    state_capitols = {}
    world_capitols = {}
    num_correct = 0

    import_info()
    q_number = get_question_number()
    categories = [ask_state_capitol_question, ask_world_capitol_question]
    run_quiz(q_number, categories)

    print('You answered ' + str(num_correct) + ' of ' + str(q_number) + ' questions correctly on the first try!\n')
    print('Try again? (y for yes)')
    if not input().lower().startswith('y'):
        break
