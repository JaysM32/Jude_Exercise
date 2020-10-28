def findvalue (dict,val):
    keylist = []
    for i in dict.keys():
        if  val == dict[i]  :
            keylist.append(i)

    return keylist

if __name__ == '__main__':
    database = {"test1":"pass1" , "test2":"pass2", "test3":"pass1"}
    val = input("searched value >> ")
    print( findvalue(database, val))