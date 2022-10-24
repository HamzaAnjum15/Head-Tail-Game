# head or tail cricket game
# instructions
# when choosing head or tail use only first alphabet of head or tail 
# for example h or t
# when choosing bat or ball use only first first three alphabets of bat or ball
# for example type bat for batting and bal for balling don't use double l for balling
import random
h = "head"
t = "tail"
ask = (input(f"{h} or {t}? "))
def head_tail(ask):
    num = int(input("enter a number between 1 to 6 "))
    rand = random.randint(1, 6)
    print(f"the computer chose {rand}")
    head = "head comes"
    tail = "tail comes"
    if (num+rand) % 2 != 0:
        print(head)
        if ask == head[0]:
            bat = "Bat"
            ball = "Ball"
            print(f"you won the toss! {bat} or {ball}?")
        else:
            print("you lost the toss")
            ram=random.randint(0,1)            
            if ram==0:                
                 print("the computer chose balling")                 
                 score_run1 = 2
                 score_run=0
                 rand1=0
                 rand2=0
                 while rand1 != score_run1:        
                  rand1 = random.randint(1, 6)
                  score_run1 = int(input("enter score "))
                  print(f"the computer chose {rand1}")
                  score_run += score_run1
                  print(f"total score {score_run}")
                  if rand1==score_run1:
                    break
                 print("you are out")
                 a=score_run-score_run1
                 print(f"your score is {a} runs")   
                 print("now computer's batting")
                 score_run1 = 2
                 score_run=0
                 rand1=0
                 rand2=0
                 while rand2 != score_run1:        
                  rand2 = random.randint(1, 6)
                  score_run1 = int(input("enter score "))
                  print(f"the computer chose {rand2}")
                  rand1+=rand2
                  print(f"total score {rand1} runs")
                  if rand2==score_run1:
                      break
                 print("computer is out")
                 b=rand1-rand2
                 print(f"the score of computer is {b} runs")     
                 if a>b:
                    print("you win")
                 elif a==b:
                    print("the match is tie")
                 else:
                    print("computer wins")                                          
            else:
                print("the computer chose batting")                                
                score_run1 = 2
                score_run=0
                rand1=0
                rand2=0
                while rand2 != score_run1:        
                 rand2 = random.randint(1, 6)
                 score_run1 = int(input("enter score "))
                 print(f"the computer chose {rand2}")
                 rand1+=rand2
                 print(f"total score {rand1} runs")
                 if rand2==score_run1:
                     break
                print("computer is out")
                b=rand1-rand2
                print(f"the score of computer is {b} runs")     
                print("now your batting")
                score_run1 = 2
                score_run=0
                rand1=0
                rand2=0
                while rand1 != score_run1:        
                 rand1 = random.randint(1, 6)
                 score_run1 = int(input("enter score "))
                 print(f"the computer chose {rand1}")
                 score_run += score_run1
                 print(f"total score {score_run} runs")
                 if rand1==score_run1:
                   break
                print("you are out")
                a=score_run-score_run1
                print(f"your score is {a}") 
                if a>b:
                    print("you win")
                elif a==b:
                    print("the match is tie")
                else:
                    print("computer wins")                                                                  
    else:
        print(tail)
        if ask == tail[0]:
            bat = "Bat"
            ball = "Ball"
            print(f"you won the toss! {bat} or {ball}?")
        else:
            print("you lost the toss")
            ram=random.randint(0,1)
            if ram==0:
                 print("the computer chose balling")
                 score_run1 = 2
                 score_run=0
                 rand1=0
                 rand2=0
                 while rand1 != score_run1:        
                  rand1 = random.randint(1, 6)
                  score_run1 = int(input("enter score "))
                  print(f"the computer chose {rand1}")
                  score_run += score_run1
                  print(f"total score {score_run}")
                  if rand1==score_run1:
                    break
                 print("you are out")
                 a=score_run-score_run1
                 print(f"your score is {a}")  
                 print("now computer's batting")   
                 score_run1 = 2
                 score_run=0
                 rand1=0
                 rand2=0
                 while rand2 != score_run1:        
                  rand2 = random.randint(1, 6)
                  score_run1 = int(input("enter score "))
                  print(f"the computer chose {rand2}")
                  rand1+=rand2
                  print(f"total score {rand1}")
                  if rand2==score_run1:
                      break
                 print("computer is out")
                 b=rand1-rand2
                 print(f"the score of computer is {b}")  
                 if a>b:
                    print("you win")
                 elif a==b:
                    print("the match is tie")
                 else:
                    print("computer wins")            
            else:
                print("the computer chose batting")
                score_run1 = 2
                score_run=0
                rand1=0
                rand2=0
                while rand2 != score_run1:        
                 rand2 = random.randint(1, 6)
                 score_run1 = int(input("enter score "))
                 print(f"the computer chose {rand2}")
                 rand1+=rand2
                 print(f"total score {rand1}")
                 if rand2==score_run1:
                     break
                print("computer is out")
                b=rand1-rand2
                print(f"the score of computer is {b}")     
                print("now your batting")
                score_run1 = 2
                score_run=0
                rand1=0
                rand2=0
                while rand1 != score_run1:        
                 rand1 = random.randint(1, 6)
                 score_run1 = int(input("enter score "))
                 print(f"the computer chose {rand1}")
                 score_run += score_run1
                 print(f"total score {score_run}")
                 if rand1==score_run1:
                   break
                print("you are out")
                a=score_run-score_run1
                print(f"your score is {a} runs")  
                if a>b:
                    print("you win")
                elif a==b:
                    print("the match is tie")
                else:
                    print("computer wins")               
    bat_first = str("batting")
    ball_first = str("balling")
    decision = input()
    def bat(decision):
                if decision == bat_first[0:3]:
                 print("you chose batting")
                 score_run1 = 2
                 score_run=0
                 rand1=0
                 rand2=0
                while rand1 != score_run1:        
                  rand1 = random.randint(1, 6)
                  score_run1 = int(input("enter score "))
                  print(f"the computer chose {rand1}")
                  score_run += score_run1
                  print(f"total score {score_run} runs")
                  if rand1==score_run1:
                    break
                print("you are out")
                a=score_run-score_run1
                print(f"your score is {a} runs")
                print("now computer's batting")
                score_run1 = 2
                score_run=0
                rand1=0
                rand2=0
                while rand2 != score_run1:        
                 rand2 = random.randint(1, 6)
                 score_run1 = int(input("enter score "))
                 print(f"the computer chose {rand2}")
                 rand1+=rand2
                 print(f"total score {rand1} runs")
                 if rand2==score_run1:
                     break
                print("computer is out")
                b=rand1-rand2
                print(f"the score of computer is {b} runs") 
                print(f"your score is {a} runs")
                print(f"computer's score is {b} runs")
                if a>b:
                    print("you win")
                elif a==b:
                    print("the match is tie")
                else:
                    print("computer wins")
    def ball(decision):
                if decision == ball_first[0:3]:
                    print("you chose balling")
                score_run1 = 2
                score_run=0
                rand1=0
                rand2=0
                while rand2 != score_run1:        
                  rand2 = random.randint(1, 6)
                  score_run1 = int(input("enter score "))
                  print(f"the computer chose {rand2}")
                  rand1+=rand2
                  print(f"total score {rand1} runs")
                  if rand2==score_run1:
                    break
                print("computer is out")
                b=rand1-rand2
                print(f"the score of computer is {b} runs")
                print("now your batting")
                score_run1 = 2
                score_run=0
                rand1=0
                rand2=0
                while rand1 != score_run1:        
                 rand1 = random.randint(1, 6)
                 score_run1 = int(input("enter score "))
                 print(f"the computer chose {rand1}")
                 score_run += score_run1
                 print(f"total score {score_run}")
                 if rand1==score_run1:
                   break
                print("you are out")
                a=score_run-score_run1
                print(f"your score is {a} runs") 
                if a>b:
                    print("you win")
                elif a==b:
                    print("the match is tie")
                else:
                    print("computer wins")
    if decision == ball_first[0:3]:
      print(ball(decision))
    else:                                
      print(bat(decision))
print(head_tail(ask))




