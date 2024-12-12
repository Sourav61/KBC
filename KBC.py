questions = [
    ["Which of the following countries is the world's largest producer of saffron?","Spain","Iran","India","Greece",2], 
    ["Which god is also known as 'Gauri Nandan'?", "Agni","Indra","Hanuman","Ganesha", 4],
    ["What does not grow on tree according to a popular Hindi saying?", "Money", "Flower", "Leaves","Fruits", 1],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
name = input("Please enter your name: ")

print(f"Everbody please welcome {name} on Kaun Banega Crorepati Show 🎉🎉")

money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"{name} Please be ready, Here comes the question No. {i+1} for Rs. {levels[i]}")
    print(question[0])
    
    print(f"The options are: a {question[1]}                 b {question[2]}")
    print(f"                 c {question[3]}                 d {question[4]}")

    answer = int(input("Please let us know your answer(1-4): "))

    if answer == question[-1]:
        print(f"Congratulations 🎉🍾🥂, you have won Rs. {levels[i]} and you have moved to the next level")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print(f"Sorry😥😔, you have lost the game. The correct answer was option {question[-1]} {question[question[-1]]}.")
        break

print(f"We were happy to have you on our show, Your take home money is {money}.")