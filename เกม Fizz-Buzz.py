count = 0
correct = 0
incorrect = 0
score =0
max = int(input("Maximum Number :"))
number = 0
while count < max:
  count +=1
  number += 1
  ans = input(f'{number} : ')
  if ans == "0":
    print ("The game stopped")
    break;
  elif number %3 ==0 and ans =="f":
    correct +=1
    score +=1
  elif number %5 ==0 and ans =="b":
    correct +=1
    score +=1
  elif number %3 ==0 and number %5 == 0 and ans == "fb":
    correct +=1
    score +=1
  elif number %3 !=0 and number %5 !=0 and ans !="f" and ans !="b" and
ans !="fb" and number == int(ans):
    correct +=1
    score +=1
  else :
    incorrect +=1
    score -=2
  if incorrect == 3 :
    print ("You have answerd wrong 3 times.")
    break;
print (f'correct :{correct} times')
print (f'incorrect :{incorrect} times')
print (f'Score : ',score)
