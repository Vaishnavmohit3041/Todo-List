# list for todo 
list=[]

#loop for continuous
while True:
    # operations that what user is todo with the list
    operation=input("\n'A' for Add\n'R' for Remove\n'Q' for Quit\n")

# if user want to add
    if operation=="A":
        todo=input('\nWrite what to add: ')
        list.append(todo)
        print('\n'.join(list))
    
    # if user want to remove
    elif operation=='R':
        print('\n'.join(list)) 
        remove=input('\nWhat to remove: ')
        if remove in list:
            list.remove(remove)
            print('\n'.join(list))
        else:
             print('\nIt is not in list')
             
     # if user want to quit
    elif operation=='Q':
         print('\nThanks')    
         print('\n'.join(list))         
         break
    else:
        print('\nPlease try again.')