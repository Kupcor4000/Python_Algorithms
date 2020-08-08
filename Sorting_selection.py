#Selection Sort
#O(n^2) - time

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


lista = [33,43,1123,443,54,23,43,123,43,23,545,223,54,11,2,3]
print(selection_sort(lista,len(lista)))
