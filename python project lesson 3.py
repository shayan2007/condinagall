import time
import random



alpabits = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "^", "&", "*", "(", ")", "-", "_", "+", "=", "`", "~", "/", "?", "|", "]", "[", "{", "]", ";", ":", ",", "<", ".", "<"]
a = input("1 for encrpt 2 for decrpt\n")
if a == "1":
    thing = input("WHAT DO YOU WANT TO ENCRYPT HUH\n").lower()
    n = int(input("KEYYYY: "))
    new_thing = []
    for i in range(len(thing)):
        for e in range(len(alpabits)):
            if alpabits[e] == thing[i]:
                temp = e+n
                if temp >= 27:
                    temp = temp - 27
                new_thing.append(temp)
    newer_thing = ""
    for i in range(len(new_thing)):
        newer_thing = newer_thing + alpabits[new_thing[i]]
    print(newer_thing)
elif a == "2":
    thing = input("WHAT DO YOU WANT TO decrypt HUH\n").lower()
    n = int(input("KEYYYY: "))
    new_thing = []
    for i in range(len(thing)):
        for e in range(len(alpabits)):
            if alpabits[e] == thing[i]:
                temp = e-n
                if temp < 0:
                    temp = temp + 27
                new_thing.append(temp)
    newer_thing = ""
    for i in range(len(new_thing)):
        newer_thing = newer_thing + alpabits[new_thing[i]]
    print(newer_thing)
elif a == "3":
    THING = input("WHAT DO YOU WANT TO SAY YOU BROKEN EYED THING\n").lower()
    list_of_replacements_1 = ["p", "b", "o", "w", "u", "h", "z", "i", "8"]
    list_of_replacements_2 = ["q", "d", "0", "m", "n", "y", "d", "!", "&"]
    REPLACE = ""
    for i in range(len(THING)):
        if THING[i] in list_of_replacements_1 or THING[i] in list_of_replacements_2:
            if THING[i] in list_of_replacements_1:
                for e in range(len(list_of_replacements_1)):
                    if THING[i] == list_of_replacements_1[e]:
                        REPLACE = REPLACE + list_of_replacements_2[e]
            if THING[i] in list_of_replacements_2:
                for e in range(len(list_of_replacements_2)):
                    if THING[i] == list_of_replacements_2[e]:
                        REPLACE = REPLACE + list_of_replacements_1[e]
        else:
            REPLACE = REPLACE + THING[i]
    print(REPLACE)    
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