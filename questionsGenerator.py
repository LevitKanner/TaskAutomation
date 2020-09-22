import shelve, os , math
from pathlib import Path
import random

capitals = {
'Alabama': 'Montgomery', 'Alaska': 'Juneau',
'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento',
'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'
}

for quizSet in range(2):
    quiz = open(f"QuizSet {quizSet}.txt", "w")
    markScheme = open(f"Quiz{quizSet}Ans.txt", "w")

    quiz.write("Name:\nClass:\nDate:\n\n\n")
    quiz.write((" " * 15) + f"Quiz Form {quizSet + 1}\n\n")

    markScheme.write((" " * 15) + f"QuizSet{quizSet + 1} Marking Scheme\n\n")

    states = list(capitals.keys())
    random.shuffle(states)
    questions = random.sample(states, 50)

    for question in range(50):
        letters = "ABCD"
        capital = list(capitals.values())

        currentState = states[question]
        quiz.write(f"Q{question + 1}: What is the capital of {currentState }?\n")

        rightAns = capitals[currentState]
        del capital[capital.index(rightAns)]

        options = random.sample(capital, 3)
        options.append(rightAns)
        random.shuffle(options)

        for option in range(4):
            quiz.write(f"  {letters[option]}. {options[option]}\n")
        quiz.write("\n")
        markScheme.write(f"Q{question + 1}. {letters[options.index(rightAns)]}\n")

    quiz.close()
    markScheme.close()
