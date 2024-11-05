import time
import random
print("HELLO THIS IS THE BANK")
print("(where we rob you not the other way around)")

nameofvictims = []
tendigitnumbers = []
proofIDs = []
openingbalance = []
while True:
    print(" ")
    print("Menu:")
    print("1. open an account(that we will take money out from for our selfs)")
    print("2. veiw account balence(this will not increase the amount in there if you look at it 200 times)")
    print("3. make a transaction(we will be taking a 100% cut so make sure to put extra)")
    print("4. deposit money(for us to take out in random fees)")
    print("5. update account(we will cut money for this)")
    x = input("number: \n")
    if x == "1":
        nameofvictims.append(input("what is the name of the next victim: \n"))
        tendigitnumbers.append(random.randint(1000000000, 9999999999))
        proof = int(input("WHO ARE YOU: \n"))
        for i in range(len(proofIDs)-1):
            if proofIDs[i] == proof:
                print("YOU ALREADY HAVE AN ACCOUNT DIEEE")
                exit(random.randint(-1000000000000000000, 1000000000000000))
        proofIDs.append(proof)
        openingbalance.append(int(input("HOW MUCH MONEY DO YOU HAVE LEFT(in usd)\n")))
        print("loading.....")
        time.sleep(30)
        print(nameofvictims[len(nameofvictims)-1])
        print(tendigitnumbers[len(tendigitnumbers)-1])
        print(proofIDs[len(proofIDs)-1])
        print(openingbalance[len(openingbalance)-1])
        print("this is your information make sure to share it online")
    elif x == "2":
        proof = int(input("WHO ARE YOU\n"))
        for i in range(len(proofIDs)):
            if proofIDs[i] == proof:
                print("balance: " + str(openingbalance[i]))
    elif x == "3":
        print("SO YOU WANT MONEY HUHHHH")
        print("YOU GOTTA ANSWER SOME QUESTIONS FIRST")
        proof = int(input("WHO ARE YOU\n"))
        for i in range(len(proofIDs)):
            if proofIDs[i] == proof:
                money = int(input("HOW MUCN MONEY DO THY HAVE\n"))
                if money != 0:
                    print("we should fix that")
                if money == openingbalance[i]:
                    print("ok next question")
                    name = input("what is your name\n")
                    if name == nameofvictims[i]:
                        print("ok but it is still not enough")
                        print("WHAT IS THE TEN DISGIT NUMBER")
                        tendigit = int(input(""))
                        if tendigit == tendigitnumbers[i]:
                            print("good now that we know you are who you say you are")
                            print("1 for credit 2 for debit")
                            print("we do have a 200000000% intrest per second on the credit")
                            moneytype = int(input(""))
                            if moneytype == 1:
                                temp = int(input("how much money do you want on this 200000000% intrest per second loan?"))
                                if temp < 0:
                                    print("HOW DARE YOU TRY AND INCREASE YOUR MONEY NOW SUFFER")
                                    exit(random.randint(-1000000000000000000, 1000000000000000))
                                print("YOU FOOL YOU DUMBBUTT YOU ABSOLUTE MORON YOU PICKED THE ONE OPTION YOU SHOULDNT HAVE NOW SUFFER IN DEBT FOR YOU HAVE NO MONEY")
                                print(f"also no money is coming out of the atm because you need to already pay it back alont with {temp*19} usd")
                                print("also we will be taking out", openingbalance[i], "as paymeny for this excusite service")
                                openingbalance[i] = 0
                            elif moneytype == 2:
                                temp = int(input("how much money do you want to take out :D"))
                                if temp < 0:
                                    print("HOW DARE YOU TRY AND INCREASE YOUR MONEY NOW SUFFER")
                                    exit(random.randint(-1000000000000000000, 1000000000000000))
                                openingbalance[i] = openingbalance[i] - temp
                                print("HERE IS YOUR MEASLY", temp, "USD AS FOR THE PAYMENT FOR THIS SERVICE WE WILL BE TAKING", openingbalance[i])
                                openingbalance[i] = 0
    elif x == "4":
        print("SO YOU WANT PUT IN MONEY HUHHHH")
        print("YOU GOTTA ANSWER SOME QUESTIONS FIRST")
        proof = int(input("WHO ARE YOU\n"))
        for i in range(len(proofIDs)):
            if proofIDs[i] == proof:
                money = int(input("HOW MUCN MONEY DO THY HAVE\n"))
                if money != 0:
                    print("we should fix that")
                if money == openingbalance[i]:
                    print("ok next question")
                    name = input("what is your name\n")
                    if name == nameofvictims[i]:
                        print("ok but it is still not enough")
                        print("WHAT IS THE TEN DISGIT NUMBER")
                        tendigit = int(input(""))
                        if tendigit == tendigitnumbers[i]:
                            print("good now that we know you are who you say you are")
                            print("how much money do you want to put into this usless bank")
                            moneytotakefromthevictim = int(input(""))
                            print("thank you for puting in", moneytotakefromthevictim, "usd as payment for this great service we will take", moneytotakefromthevictim + openingbalance[i], "usd out of your account")
                            openingbalance[i] = 0
    elif x == "5":
        print("SO YOU WANT TO UPDATE THY ACCOUNT")
        print("YOU GOTTA ANSWER SOME QUESTIONS FIRST")
        proof = int(input("WHO ARE YOU\n"))
        for i in range(len(proofIDs)):
            if proofIDs[i] == proof:
                money = int(input("HOW MUCN MONEY DO THY HAVE\n"))
                if money != 0:
                    print("we should fix that")
                if money == openingbalance[i]:
                    print("ok next question")
                    name = input("what is your name\n")
                    if name == nameofvictims[i]:
                        print("ok but it is still not enough")
                        print("WHAT IS THE TEN DISGIT NUMBER")
                        tendigit = int(input(""))
                        if tendigit == tendigitnumbers[i]:
                            print("UNFORGIVABLE")
                            print("NO MONEY FOR YOU")
                            openingbalance[i] = 0
                            print("now do you want to change your name or remove account(1 or 2)")
                            poop = int(input(""))
                            if poop == 1:
                                nameofvictims[i] = input("what is your new name huh")
                            elif poop == 2:
                                print("BYE BYE HATED YOU TOO")
                                nameofvictims.pop(i)
                                tendigitnumbers.pop(i)
                                proofIDs.pop(i)
                                openingbalance.pop(i)
    else:
        print(" ")
        print("An Exploration into the Mystifying Difficulty of Inputting a Simple Number")
        print("In the grand catalog of human achievements—walking on the moon, decoding the human genome, harnessing the power of the internet—there exists one fundamental challenge that, to this day, eludes some: the inputting of a simple number. This perplexing conundrum, though seemingly trivial, has baffled individuals worldwide. It is, apparently, the Everest of minor tasks, an enigma that renders even the brightest minds utterly helpless.")
        print("")
        print("Part 1: The Great Numerical Enigma")
        print("Inputting a single number, like typing '1' into a field, might seem straightforward to the uninitiated. But consider the mental gymnastics required! One must recognize that there is a blank field, understand that this field requires information, determine that this information is numerical in nature, and finally, summon the Herculean strength needed to press the appropriate button on the keyboard or touchscreen. Clearly, this is not just a simple act but an intricate ballet of cognitive processes. It’s no wonder, then, that some stumble at the first step, their minds ensnared in the labyrinthine complexities of such a straightforward task.")
        print("")
        print("Part 2: The Psychological Toll")
        print("For some, the thought of inputting a number may induce a level of stress typically reserved for life-altering decisions. The reasons for this remain nebulous, but it could be that the act of typing a number into a field feels definitive and binding. After all, what if one selects the wrong number? What if one misinterprets the instructions? The anxiety of making a 'number-inputting error' can paralyze even the most capable individual, freezing them at the very gateway to numerical input.")
        print("")
        print("Part 3: Technological Barriers")
        print("Surely, some of the blame lies with the cold, unyielding machines that demand these numbers in the first place. Perhaps the screen is too bright, the keyboard unresponsive, or the phone screen too small. These excuses are as numerous as they are inventive. One might argue that we’ve had access to user-friendly interfaces for decades, that smartphones and computers alike offer a near-infinite amount of information on how to operate even the most complex machinery. But alas, the act of pressing a button remains unconquerable.")
        print("")
        print("Part 4: A Tragic Conclusion")
        print("In conclusion, the inability to input a number is not just a failure of the individual—it is a failure of society at large. How can we expect anyone to complete this Herculean task when we, as a culture, have not provided them with the necessary resources, emotional support, and hand-holding to face such a monumental challenge? Until we collectively embrace the gravity of this issue, there will always be those who falter, frozen before the screen, fingers hovering uncertainly, as the blank field stares back at them in silent reproach.")
        print("")
        print("In Summary")
        print("Thus, we find ourselves asking: Who among us is truly prepared to bear the weight of numerical input? Who is ready to ascend to that next level of human capability?")
