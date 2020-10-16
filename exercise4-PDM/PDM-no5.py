def overlap (list1, list2):
    for i in list1:
        for j in list2:
            if list1.count(j) >= 1:
                return True
            elif list2.count(i) >= 1:
                return True
            else:
                return False

if __name__ == '__main__':
    listno1 = list(eval(input("input list 1 = ")))
    listno2 = list(eval(input("input list 2 = ")))
    print("the list overlaps = ", overlap(listno1,listno2))