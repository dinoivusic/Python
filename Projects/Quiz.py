import random

capitals = {'Netherlands': 'Amsterdam', 'Andorra': 'Andorra La Vella', 'Greece': 'Athens',
            'Serbia': 'Belgrade', 'Germany': 'Berlin', 'Switzerland': 'Bern', 'Slovakia': 'Bratislava',
            'Belgium': 'Brussels', 'Romania': 'Buchurest', 'Hungary': 'Budapest', 'Moldova': 'Chisinau',
            'Denmark': 'Copenhagen', 'Ireland': 'Dublin', 'Finland': 'Helsinki', 'Ukraine': 'Kiev',
            'Portugal': 'Lisbon', 'Slovenia': 'Ljubljana', 'UK': 'London', 'Spain': 'Madrid',
            'France': 'Paris', 'Croatia': 'Zagreb', 'Norway': 'Oslo'
            }
for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    quizQuestionFile = open('capitalsfile%s.txt' % (quizNum + 1), 'w')
    quizAnswerFile = open('capitalsAnswerFile%s.txt' % (quizNum + 1), 'w')

    # TODO: Write out the header for the quiz.
    quizQuestionFile.write('This is the European Capitals Quiz')
    quizQuestionFile.write('Please write your name here\nPlease specify the date\n')
    quizQuestionFile.write((' ' * 15) + 'EU capitals quiz (Form %s)' % (quizNum + 1))
    quizQuestionFile.write('\n')

    # TODO: Shuffle the order of the states.
    countries = list(capitals.keys())
    random.shuffle(countries)
    # TODO: Loop through all 22 states, making a question for each.
    for question in range(22):
        answer = capitals[countries[question]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(answer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        option = wrongAnswer + [answer]
        random.shuffle(option)
        # TODO: Write the question and answer options to the quiz file.
    quizQuestionFile.write(' %s. What is the capital of: %s \n' % (quizNum + 1, countries[question]))
    for i in range(4):
        quizQuestionFile.write('Answers are: \n %s %s\n' % ('1234'[i], option[i]))
    quizQuestionFile.write('\n')

    # TODO: Write the answer key to a file.
    quizAnswerFile.write('%s The answer is: %s' % (quizNum + 1, '1234'[option.index(answer)]))
quizQuestionFile.close()
