#Selection Sort
#O(n^2) - time

import random

def selection_sort(list,n):
    j = 0
    i = 0
    #Last element have to be on good position
    while j < n:
        i = j+1
        pmin = j
        while i <= n-1:
            #Condition of sorting
            if int(list[pmin]) > int(list[i]):
                k = list[pmin]
                list[pmin] = list[i]
                list[i] = k
            i+=1
        j+=1
    return list

def generator_of_random_numbers(amount):
    list_for_numbers = []
    for i in range(amount):
        rand = random.randint(1,100) #generatin numbers in range from 1 to 100
        list_for_numbers.append(rand)
    print("The list of random numbers: {}".format(list_for_numbers))
    return list_for_numbers

amount_user = int(input("How many random numbers do you want to habe? "))
lista = generator_of_random_numbers(amount_user)
print("")
print(selection_sort(lista,len(lista)))
