def linear_search(list_of_arguments,target):
    step = 1
    for i in range(len(list_of_arguments)):
        if int(list_of_arguments[i]) == target:
            return i
        step += 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index {}".format(index))
    else:
        print("Target not found!")
        
user_list = input("Please enter some number: ")
a_list = user_list.split()

iterator = linear_search(a_list,5)
verify(iterator)