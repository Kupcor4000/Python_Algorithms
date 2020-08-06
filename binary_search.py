#Binary search musi mieć w inpucie liste posortowaną
import math


def binary_search(list_of_arguments,target):
    ##pierwszy wyraz w liscie
    ogr_1 = 0
    ##drugi wyraz w liscie
    ogr_2 = len(list_of_arguments)
    #mid point, round mozna zastapic //''// - zaokraglenie nastepuje do mniejszej liczby!
    index = int(round((ogr_2+ogr_1)/2))
    step = 1;
    # dzieki temu warunkowi program zakonczy sie jesli nie bedzie liczby w zbiorze, gdybysmy po prostu uzyli warunku while True to petla dzialalaby
    #w nieskonczonosc
    while ogr_1 < ogr_2:
        print("ogr_1: {} ogr_2: {}".format(ogr_1,ogr_2))
        print("Przejsc: {}, aktualny index: {}, na ktorym jest wartosc: {}".format(step,index-1,list_of_arguments[index-1]))
        #warunki wyjscia oraz zmienania wartosci ograniczen
        if int(list_of_arguments[index-1]) == target:
            return index - 1
        elif int(list_of_arguments[index-1]) > target:
            ogr_2 = index
            index = int(round((ogr_2+ogr_1)/2))
        elif int(list_of_arguments[index-1])< target:
            ogr_1 = index
            index = int(round((ogr_2+ogr_1)/2))
        elif index == len(list_of_arguments) or index == -1:
            return None
        step += 1
        

#funkcja pokazujaca ostateczny wynik
def verify(wartosc):
    if wartosc is not None:
        print("Szukana liczba znajduje sie na pozycji: {}".format(wartosc))
    else:
        print("Szukana liczba nie znajduje sie w zborze")
        
        
lista = [1,22,33,120,543,2332,22033]
wynik = binary_search(lista,2332)
verify(wynik)

    