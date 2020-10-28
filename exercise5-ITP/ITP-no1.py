def removekeys(dict,list):
    for key1 in list:
        dict.pop(key1)


if __name__ == '__main__':
    testdict = {"name":"Timmy" , "age":"14" , "gender":"male"}
    print(testdict)
    input1 = input("input a list to remove the data >> ")
    removelist = list(input1.split(","))
    removekeys(testdict, removelist)
    print(testdict)