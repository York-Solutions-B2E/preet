def yes_or_no(value):
    if value:
        return "Yes"
    else:
        return "No"

# Example usage:
result = yes_or_no(True)
print(result)  # Output: Yes

result = yes_or_no(False)
print(result)  # Output: No
  
  #def avg(num):
   #total=sum(num)
   #average=total/len(num)
   #return average
#print("The Average Sum of Numbers is",avg(num))

num= (-1,-2,-3,0,1,2,3,4)
def average_number(num):
    sum=0
    for i in num:
         sum=sum+i
    avg=sum/len(num)
    return avg

print(average_number(num))