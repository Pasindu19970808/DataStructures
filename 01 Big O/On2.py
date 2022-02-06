def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#print_items(10)

#The above is O(n2)

def print_items_2(n):
    l = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                l += 1
                print(i,j,k)
    print(l)
print_items_2(10)
#The above is O(n^3) but we drop the constant and call it
#O(n^2)

#DROP NON DOMINANTS
def print_items_3(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)

print_items_3(10)
#In total we have 110 operations here making O(n^2 + n)

