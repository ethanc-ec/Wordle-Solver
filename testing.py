def test(): # defining function
    ret_list = [] # list we're gonna be returning

    with open("filename.txt") as file: # opens the specified file and closes it after its done
        for i in file: # for each line in the file it will append that line to the ret_list
            ret_list.append(i) # appending line to ret_list
                
    return ret_list