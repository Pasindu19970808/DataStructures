#Given a sorted list, find the most efficient way to 
#find a number in the list

my_list = [11,3,23,7]

my_list.append(17)

#This just pops the 17 that was added in
x = my_list.pop()

#as there is no reordering, both opertions of append
#and pop are constant time operations (O(1))

#However here we try to pop the first index
my_list.pop(0)
#Now the entire list has to be reindexed

#Here we insert a value at a positon
my_list.insert(0,11)
#Now we have to reindex it again

#Hence when you remove or insert, you have to do n
#operations in order to reindex the entire list

#It is important to remember that adding or removing on
#the end of a list is a O(1) operation 
#But adding or removing at the start of the list
#is a O(n) operation

#What if we insert at the middle or any other position
my_list.insert(1,'Hi')
#The indexes after the position of insertion needs to be
#reindexed
#Although the number of reindexing operations is typically
#less than n operations, the worse case is always n. Hence
#complexity is O(n)

#How if we are trying to search for a value thats in the
#list?
#To do this we need to loop through the list and find
#the value. This would be a O(n) operation. 
#However if we want to find a value thats at a particular
#index, then we can directly go to that index and hence 
#it is a O(1) operation




