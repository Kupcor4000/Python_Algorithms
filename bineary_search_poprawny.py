#lista musi byc posortowana!

def binary_search(list, target):
    first = 0
    last = len(list) - 1
    step = 0
    
    while first <= last:
        midpoint = (first + last) //2 #zaokraglanie w dol
        step = step+1
        print("Przejscie: {}, midpoint: {} , aktualna wartosc na midpoincie: {}, first: {}, last: {}".format(step,midpoint,list[midpoint],first,last))
        if int(list[midpoint]) == target:
            return midpoint
        elif int(list[midpoint]) < target:
            first = midpoint + 1 #wszystkie wartosci przed midpointem zostaja odrzucone
        #warunek kiedy target < list[midpoint]
        else:
            last = midpoint - 1 #wszystkie wartosci po midpoincie zostaja odrzucone
    return None
            
            
def verify(wartosc):
    if wartosc is not None:
        print("Szukana liczba znajduje sie na pozycji: {}".format(wartosc))
    else:
        print("Szukana liczba nie znajduje sie w zbiorze")

#booble sort
#TODO dodać funkcje która sortuje liste podaną przez uzytkownika
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
                   
        
        
lista = input("Please enter some number seperate by coma: ")
lista = lista.split(" ")
print("Posortowana lista: {}".format(sorting(lista)))
ta = int(input("Ktora z podanych wyzej liczb chcesz znaleźć? "))
wynik = binary_search(sorting(lista),ta)
verify(wynik)
