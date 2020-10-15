def makeintolisttuple(input1):
    list1 = list(input1.split(","))
    tuple1 = tuple(input1.split(","))
    print(list1)
    print(tuple1)

if __name__ == '__main__':
    input2 = input("insert a sequence of comma-separated numbers: ")
    print("-----------------------------------------------")
    makeintolisttuple(input2)
