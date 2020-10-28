def login (database , username, password):
    if username in database:
        if password == database[username]:
            return True
        else:
            print("incorrrect password")
            return False
    else:
        return False


if __name__ == '__main__':
    database1 = {"test1":"pass1" , "test2":"pass2", "test3":"pass3"}
    testuser = input("username: ")
    testpass = input("password: ")
    logintest = login(database1, testuser, testpass)
    print("login = ", logintest)