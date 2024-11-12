
class Quiz:

    def quiz(self,questions):
        points = 0
        for i in range(len(questions)):
            question = questions[i]
            print(f"{question[0]}. {question[1]} for 2 points.")
            print(f"1.{question[2]}       2.{question[3]}")
            print(f"3.{question[4]}       4.{question[5]}")
            ans = int(input("Enter your choice:"))
            if ans == question[-1]:
                print("Correct answer! You have earned 2 points")
                points += 2
                print("\n\n")
            else:
                print("Wrong answer!")
                print("\n\n")
        return points
    

    def edit(self,questions):
        for i in range (len(questions)):
            question = questions[i]
            print(f"{question[0]}.{question[1]}")
        edit_choice = int(input("Enter the question which you want to edit:"))
        new_question = input("Enter the new question:")
        questions[edit_choice-1][1] = new_question
        print("The question is successfully changed!")
    
    def edit_options(self,questions):
        for i in range (len(questions)):
            question = questions[i]
            print(f"{question[0]}.{question[1]}")
        question_choice = int(input("Enter the question number which you want to edit options:"))
        li = []
        for i in range(4):
            temp = input(f"Enter the {i+1} option:")
            li.append(temp)
        for i in range(4):
            questions[question_choice-1][i+2] = li[i]
        correct_ans = int(input("Enter the correct answer option:"))
        questions[question_choice-1][-1] = correct_ans
        print("Options have been successfully uploaded!")


    def add_questions(self,questions):
        question_number = len(questions)
        lis = []
        li = []
        question = input("Enter the question:")
        for i in range(4):
            temp = input(f"Enter the {i+1} option:")
            li.append(temp)
        correct_ans = int(input("Enter the option which is correct:"))
        lis.append(question_number+1)
        lis.append(question)
        lis.append(li[0])
        lis.append(li[1])
        lis.append(li[2])
        lis.append(li[3])
        lis.append(correct_ans)
        questions.append(lis)
        
    

if __name__ == "__main__":
    questions = [
    [1,'How many wonders in the world','2','5','7','3',3],
    [2,'How many avengers are there in the movie avengers','6','3','5','4',1],
    [3,'Capital of Telanagna','Mumbai','Bangalore','Chennai','Hyderabad',4],
    [4,'Hyderabad is famous for ','Biryani','Lassi','Laddu','Cakes',1],
    [5,'who is the marvel jesus','iron man','Deadpool','Captain America','Wolverine',2],
    [6,'who is literally me hero','Leonardo Decaprio','Ryan Reynolds','Ryan Gosling','Andrew Garfield',3]
    ]
    quiz = Quiz()
    print('Enter the choice:')
    print("1.play quiz \n2.Edit questions again \n3.edit options \n4.Add question  \n5.exit")
    choice = int(input())
    while (choice != 5):
        if choice == 1:
            points =quiz.quiz(questions)
            print(f"Your total score is {points}")
            print("1.play quiz again\n2.Edit questions\n3.edit options \n4.Add question \n5.exit")
            choice = int(input())
        elif choice == 2:
            quiz.edit(questions)
            print("1.play quiz \n2.Edit questions again \n3.edit options \n4.Add question  \n5.exit")
            choice = int(input())
        elif choice == 3:
            quiz.edit_options(questions)
            print("1.play quiz \n2.Edit questions\n3.edit options \n4.Add question \n5.exit")
            choice = int(input())
        elif choice == 4:
            quiz.add_questions(questions)
            print("1.play quiz \n2.Edit questions\n3.edit options \n4.Add question \n5.exit")
            choice = int(input())
