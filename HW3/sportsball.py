record = [ 'W', 'W', 'W', 'W', 'L', 'W',
'W', 'W', 'L', 'W', 'W', 'W',
'W', 'W', 'W', 'W', 'W', 'L',
'L', 'L', 'W', 'W', 'L', 'L',
'W', 'W', 'L', 'W', 'L', 'W', 'W',
'W', 'L', 'L', 'W', 'L', 'W',
'W', 'L', 'L', 'W', 'W', 'L', 'W',
'W', 'W', 'W', 'L', 'W', 'W',
'L', 'W', 'W', 'W', 'L', 'L', 'W',
'W', 'W', 'W', 'L', 'L', 'W', 'L',
'W', 'W', 'W', 'W', 'W', 'L', 'L',
'L', 'W', 'L', 'W', 'W', 'L',
'W', 'W', 'W', 'W', 'L', 'W',
'L', 'W', 'W', 'W', 'W', 'W',
'W', 'W', 'W', 'W', 'W', 'L', 'W',
'W', 'W', 'W', 'L' ]
score = [ 4, 1, 3, 2, 7, 4, 3, 10, 8, 14, 7, 6, 7, 10,
3, 10, 9, 8, 7, 0, 1, 3, 4, 5, 3, 6, 4, 10,
6, 5, 5, 5, 6, 6, 2, 6, 5, 3, 5, 5, 5, 3, 6,
5, 6, 6, 5, 4, 4, 3, 6, 8, 1, 8, 8, 6, 2, 3, 5, 9,
6, 7, 2, 0, 4, 2, 2, 6, 5, 2, 6, 0, 9, 2, 1,
9, 14, 2, 5, 9, 9, 4, 1, 11, 1, 4, 11, 3, 10,
15, 7, 5, 8, 4, 6, 7, 6, 5, 1, 0 ]

# Q1 What is the team’s win/loss record? 
# I.e., how many entries in the first list have a ‘W’, and how many have an ‘L’?
def record_count():
    for i in set(record):
        print("The amount of record %s is %d."%(i,record.count(i)))    

#Q2 What is the average score per game?
def score_average():
    sum=0
    for i in range(0,len(score)):
        sum += score[i]
    print("The average score is: " + str(sum/len(score)))

#Q3 How many games has the team played where they scored 0?
def score_0_count():
    print("The amount of score %s is %d."%(0,score.count(0)))

#Q4 How many games has the team played where they scored 10 or more?
def score_10_and_more_count():
    sum=0
    i=0
    for i in score:
        if i >= 10:
            sum += 1                
    print("There are %s games with score of 10 and more."%sum) 
        
#Q5 How many games did the team win with a score of exactly 1?
def win_with_score_1():
    sum = 0
    i = 0
    for i in range(len(record)):
        if record[i]=="W":
            if score[i] == 1:
                sum += 1
    print("There are %s win games with a score of exactly 1."%sum)

#Q6 How many games did the team lose with a score of at least 10?
def lose_with_score_10plus():
    sum = 0
    i = 0
    for i in range(len(record)):
        if record[i]=="L":
            if score[i]>=10:
                sum += 1
    print("There are %s lost games with a score of 10 and more."%sum)
           
#function test: run each functions to get results
record_count()
score_average()
score_0_count()
score_10_and_more_count()
win_with_score_1()
lose_with_score_10plus()