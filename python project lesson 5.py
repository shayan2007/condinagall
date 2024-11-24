PEOPLE = {"username1":"password1"}
signed_in = False
poop = True
while poop == True:
    if signed_in == False:
        print("sign up or login(1 or 2)")
        x = input("")
        if x == "1":
            username = input("what username do you want to set\n")
            try:
                PEOPLE[username]
                print("bad pick another username")
                exit(-1)
            except KeyError:
                pass
            print("ok what password do you want")
            password = input("")
            if password in PEOPLE:
                print("NO")
                exit(-1)
            PEOPLE.update({username:password})
            
            

