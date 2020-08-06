def binary_search(list, target):
    first = 0
    last = len(list) - 1
    step = 0
    
    while first <= last:
        midpoint = (first + last) //2 #zaokraglanie w dol
        step = step+1
        print("Przejscie: {}, midpoint: {} , aktualna wartosc na midpoincie: {}, first: {}, last: {}".format(step,midpoint,list[midpoint],first,last))
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
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

        
lista = [0,1,2,3,4,5,6,7,8]
wynik = binary_search(lista,9)
verify(wynik)
