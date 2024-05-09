

question_list = []

    
def menu():
    print('1.add a question\n2.delete a question\n3.edit aquestion\n4.get a question\n5.start quiz')
    n = input('choose:(q for quit)')
    match n:
        case '1':
            addQuestion()
        case '2':
            deleteQuestion()
        case '3':
            pass
        case '4':
            getByName()
        case '5':
            pass
        case _:
            print('wrong choice!')


def addQuestion():
    answer_list = []
    question_dict = {}
    question_dict['q'] = input('enter questios:')
    for q in range(1,5):
        answer_dict = {}
        answer_dict['answer'] = input(f'enter answer number {q}:')
        answer_dict['validation'] = input(f'enter validation:')
        answer_list.append(answer_dict)
    question_dict['answer'] = answer_list 
    question_list.append(question_dict)
    print(question_list)
    menu()
        
def getByName():
    flag = 0
    ques = input('enter the question to delete:')
    for q in question_list:
        if q['q'] == ques:
            print(q)
            flag = 1
            menu()
    if flag ==0 :
        print('question not found!')
    print(question_list)
    menu()
       
def deleteQuestion():
    flag = 0
    ques = input('enter the question to delete:')
    for q in question_list:
        if q['q'] == ques:
            question_list.remove(q)
            print('question deleted!')
            flag = 1
            menu()
    if flag ==0 :
        print('question not found!')
    print(question_list)
    menu()
     
menu()
    