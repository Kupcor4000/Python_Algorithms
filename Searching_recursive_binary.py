#Warunke I - lista musi być posortowana
#Funkcja będzie zwracała True jeśli element istnieje lub False jeśli nie
#Space Complexity O(log n)

def recursive_binary_search(list,target):
    #jeśli lista jest pusta to zwrocimy falsz
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                #wolamy funkcje ponownie dajac jej nowa liste zmiennych, ktora juz ucielismy
                return recursive_binary_search(list[midpoint+1:],target)
            else:
                return recursive_binary_search(list[:midpoint],target)
                               
                
def veryfi(result):
    print("Target found: ",result)
    
    
    
    
numbers = [1,2,3]
result = recursive_binary_search(numbers,4)
veryfi(result)