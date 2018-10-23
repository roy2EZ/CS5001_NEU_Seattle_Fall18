#### Purpose
# Ask three questions to user to foresee what charactor 
# the user will be in Harry Potter movie
#### Signature
# harry_potter_character_teller :: (Char,Char,Char)=> Str
#### Template
# def harry_potter_character_teller(given...):
#    return returns...
#### Examples
#  harry_potter_character_teller(A, A, A) => Ginny
#  harry_potter_character_teller(C, A, B) => Hagrid
#  harry_potter_character_teller(B, B, A) => Hermione
import time

#Welcome title 
print("Welcome to Harry Potter Character test, please answer the following questions:")

#for calculate final score
your_sum=0

#list all questions and options
question1={"question":"Q1.When planning a trip, you...",\
    "answer":["A: Find the hot parties.",\
    "B: Sorts out all the logistics",\
    "C: Lets everyone else take charge"]}
question2={"question":"Q2.What are you most afraid of?",\
    "answer":["A: Not being accepted",\
    "B: Losing someone close to me",\
    "C: Looking stupid in front of others"]}
question3={"question":"Q3.What was your favorite toy as a kid?",\
    "answer":["A: She­Ra",\
    "B: He­Man",\
    "C: Video games"]}

#all answers and the options' value
scoring1={"A":9,"B":18,"C":27}
scoring2={"A":4,"B":7,"C":10}
scoring3={"A":1,"B":2,"C":3}

#all character results
person1="Ginny"
person2="Draco"
person3="Sirius"
person4="Dobby"
person5="Voldemort"
person6="Hermione"
person7="Luna"
person8="Hagrid"
person9="Ron"
person10="Tonks"
person11="Slughorn"


def harry_potter_character_teller(question,scoring):
    #print question and option
    print(question.get("question"))
    l=question["answer"]
    for allans in l:
        print(allans)
    #let user input answer of the question
    your_ans=input("> ") 
    #get user's answer and add the chosen option's score to the sum 
    score=scoring.get(your_ans.upper())
    if score==None:
        print("Your answer is not in the options, please input the answer again：")
        #If input from user is invalid, make user do it again
        harry_potter_character_teller(question,scoring)
        return
    global your_sum
    your_sum+=score

#let user answer all 3 questions 
harry_potter_character_teller(question1,scoring1)
harry_potter_character_teller(question2,scoring2)
harry_potter_character_teller(question3,scoring3)

print("You harry potter character is：\n")
#pair possible answer sum to characters
if your_sum == 14:
    print(person1)
elif your_sum == 15:
    print(person2)
elif your_sum == 16:
    print(person3)
elif your_sum>=17 & your_sum<=19:
    print(person4)
elif your_sum>=20 & your_sum<=22:
    print(person5)
elif your_sum>=23 & your_sum<=31:
    print(person6)
elif your_sum == 32:
    print(person7)
elif your_sum == 33:
    print(person8)
elif your_sum == 34:
    print(person9)
elif your_sum>=35 & your_sum<=37:
    print(person10)
elif your_sum>=38:
    print(person11)
else:
    print("Sorry, there is an error")
    
time.sleep(30) 