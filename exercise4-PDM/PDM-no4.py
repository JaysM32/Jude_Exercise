def check (search, list):
    if list.count(search) >= 1:
        return True
    else:
        return False


if __name__ == '__main__':
    searchval = eval(input("input search value: "))
    searchlist = list(eval(input("input list:")))
    print("-------------------------")
    print("the searched value is",check(searchval, searchlist))