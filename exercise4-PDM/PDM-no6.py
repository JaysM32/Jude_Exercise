def histrogram(list):
    for i in list:
        print ( i*"*")


if __name__ == '__main__':
    list1 = list(eval(input("input list = ")))
    histrogram(list1)