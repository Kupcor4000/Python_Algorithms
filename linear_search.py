def linear_search(list_of_arguments,target):
    step = 1
    for i in range(len(list_of_arguments)):
        if int(list_of_arguments[i]) == target:
            print("We find target number {} in {} atemps!".format(target,step))
            break;
        step += 1
        if step == len(list_of_arguments)+1:
            print("Nie ma takiej liczby w zbiorze!")
            break;
        
        
user_list = input("Please enter some number: ")
a_list = user_list.split();
print(a_list)
linear_search(a_list,5)