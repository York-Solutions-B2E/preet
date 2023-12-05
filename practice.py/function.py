num= (-1,-2,-3,0,1,2,3,4)

def positive_number(num):
    sum=0
    for i in num:
        if i> 0:
            sum=sum+i
    
    return sum
positive_number(num)
print("The Sum of positive numbers is",positive_number(num))


def answer(value):
   if value == True:
     return("yes")
   else:
      return("no")
myAnswer=answer(True) 


def minimum_number(num):
   min_value=min(num)
   return min_value
   print("The minimum Value is ",min_value)

minimum_number(num)   
 
def avg(num):
    sum=0
    for i in num:
         sum=sum+i
    avg=sum/len(num)
    return avg
    

print("The Average Sum of Numbers is",avg(num))

myrange=range(1,20,1)
for num in myrange:
    if num % 15 == 0 :
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 ==0 :
        print("Fizz")
    else :
        print(num)







   
   

        
    
