#Binary search musi mieć w inpucie liste posortowaną
import math


def binary_search(list_of_arguments,target):
    ogr_1 = 0
    ogr_2 = len(list_of_arguments)
    index = int(round((ogr_2+ogr_1)/2))
    step = 1;
    for x in range(len(list_of_arguments)):
        print("Przejsc: {}, aktualny index: {}, na ktorym jest wartosc: {}".format(step,index-1,list_of_arguments[index-1]))
        if int(list_of_arguments[index-1]) == target:
            return index - 1
        elif int(list_of_arguments[index-1]) > target:
            ogr_2 = index;
            index = int(round((ogr_2+ogr_1)/2))
        elif int(list_of_arguments[index-1])< target:
            ogr_1 = index
            index = int(round((ogr_2+ogr_1)/2))
        step += 1
    return None

def verify(wartosc):
    if wartosc is not None:
        print("Szukana liczba znajduje sie na pozycji: {}".format(wartosc))
    else:
        print("Szukana liczba nie znajduje sie w zborze")
        
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
wynik = binary_search(lista,40)
verify(wynik)

    