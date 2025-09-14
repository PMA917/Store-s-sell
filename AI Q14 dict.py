result={}
goal_result={}
import sys
print("Welcome if you wanna see the result type <<result>>.If you wanna exit the program type <<exit>>. You need to write  days")
for _ in range(7):
    day=input("please enter date:").lower()
    if day == "result":
        break
    if day == "exit":
        sys.exit()
    sell=float(input("please enter your sell:"))
    result[day]=sell
average=sum(result.values())/len(result)
Total=sum(result.values())#all money you have made.
goal_result={k:v  for k,v in result.items() if v > average}    
print("average of your sell:",round(average,2))
print("Total sale:",Total)

