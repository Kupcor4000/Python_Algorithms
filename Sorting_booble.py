#booble sort
def sorting(a_list):
        i = True
        while i:
            z = True
            for j in range(len(a_list)-1):
                if int(a_list[j]) > int(a_list[j+1]):
                        k = a_list[j]
                        a_list[j] = a_list[j+1]
                        a_list[j+1] = k
                        z = False
            if z:
                i = False
        return a_list
                   
        
#spushowanie
lista = input("Please enter some numbers: ")
lista = lista.split(" ")
print("Sorted list: {}".format(sorting(lista)))


