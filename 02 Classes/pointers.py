num1 = 11
#num2 is not set forever, instead you are initializing
#num2 with a value of num1
#changing num1 doesnt change num2
#This is because you are not using a pointer to 
#num1
num2 = num1

print("Before value is updated")
print("num1 =", num1)
print("num2 =", num2)

num1 = 22

print("\nAfter value is updated")
print("num1 =", num1)
print("num2 =", num2)

#with Pointers
#When we say dict2 = dict1 with a pointer
#it means that dict2 points to the same place in memory
#as dict1
dict1 = {'value':11}
dict2 = dict1

print("Before value is updated")
print("dict1 =",dict1)
print("dict2 =",dict2)

#Notice that dict2 is also pointing to dict1
#Hence the value changes accordingly
dict1['value'] = 22
print("Before value is updated")
print("dict1 =",dict1)
print("dict2 =",dict2)

dict3 = {'value':57}
dict2 = dict3
dict1 = dict3
#Now all the pointers point to dict3

#What happens to previous dict1?
#Only way to get to this is through a pointer. 
#Once you have moved all pointers away from this, you
#have no way to access it
#Hence Python will run Garbage Collection to remove 
#these