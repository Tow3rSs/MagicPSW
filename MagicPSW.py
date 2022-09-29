print("""
---------------------------------------------------------
    __  __             _      ____  ______        __
   |  \/  | __ _  __ _(_) ___|  _ \/ ___\ \      / / ®
   | |\/| |/ _` |/ _` | |/ __| |_) \___  \ \ /\ / / 
   | |  | | (_| | (_| | | (__|  __/ ___) |\ V  V /  
   |_|  |_|\__,_|\__, |_|\___|_|   |____/  \_/\_/   
                 |___/  

              On The Fly Wordlist Generator

 Press Enter to start.                        By Tow3rSs. 
----------------------------------------------------------
""")

userwords = []
userinput = input()
if userinput != " ":

    print("[+] Type in any info or leave it blank and press enter, then type '???' to start \n")

    day = input("Victim Birth Day (DD) -> ")
    month = input("Victim Birth Month (MM) -> " )
    year = input("Victim Birth Year (YYYY) -> ")
    
    yeared = str(year)[-2:]

    while True:
        word = input("Any Word -> ")
        if word == "???":
            print(" ")

            restrain = input("[+] Minimum password lenght [8] -> ")
            if restrain == "":
                restrain = 8

            strict = input("[+] Words must contain at least one upper, number and char? [y/N] -> ")
            if strict == "":
                strict = "N"
            
            print(" ")
            print("[*] Starting generation with {} words. Computing words number... \n ".format(len(userwords)))
            break

        else:
            userwords.append(word)


uppercased = []

def uppercaser(userwords):
    print("[*] Uppercasing...")
    for word in userwords:
        uppercasedt = word.upper()
        uppercased.append(uppercasedt)


lowercased = []

def lowercaser(userwords):
    print("[*] Lowercasing...")
    for word in userwords:
        lowercasedt = word.lower()
        lowercased.append(lowercasedt)


titled = []

def titler(userwords):
    print("[*] Titiling...")
    for word in userwords:
        titledt = word.title()
        titled.append(titledt)

multiplexed = []

def multiplexor(uppercased, lowercased, titled):
    print("[*] Multiplexing...")
    len1 = len(uppercased)
    import itertools

    compositeuppercased = (
        uppercased + list("".join(e) for e in itertools.permutations(uppercased, 2))
        + list(".".join(e) for e in itertools.permutations(uppercased, 2))
        + list("_".join(e) for e in itertools.permutations(uppercased, 2))
        + list("-".join(e) for e in itertools.permutations(uppercased, 2))
    )
    compositelowercased = (
        lowercased + list("".join(e) for e in itertools.permutations(lowercased, 2))
        + list(".".join(e) for e in itertools.permutations(lowercased, 2)) 
        + list("_".join(e) for e in itertools.permutations(lowercased, 2))
        + list("-".join(e) for e in itertools.permutations(lowercased, 2))
    )
    compositetitled = (
        titled + list("".join(e) for e in itertools.permutations(titled, 2))
        + list(".".join(e) for e in itertools.permutations(titled, 2)) 
        + list("_".join(e) for e in itertools.permutations(titled, 2))
        + list("-".join(e) for e in itertools.permutations(titled, 2))
    )

    compositeuppercasedlowercased = []
    compositeuppercasedlowercased.extend(uppercased)
    compositeuppercasedlowercased.extend(lowercased)

    for i in range(0, len1):
        for s in range(1, len1):

            eln1 = uppercased[i]
            eln2 = lowercased[(i - s)]
            both = eln1 + eln2
            bothchar = eln1 + "." + eln2
            bothchar2 = eln1 + "_" + eln2
            bothchar3 = eln1 + "-" + eln2
            both2 = eln2 + eln1
            bothcharev = eln2 + "." + eln1
            bothcharev2 = eln2 + "_" + eln1
            bothcharev3 = eln2 + "-" + eln1
            toappend = [both, bothchar, bothchar2, bothchar3, both2, bothcharev, bothcharev2, bothcharev3]
            compositeuppercasedlowercased.extend(toappend)       
   

    compositeuppercasedtitled = []
    compositeuppercasedtitled.extend(titled)

    for i in range(0, len1):
        for s in range(1, len1):

            eln1 = uppercased[i]
            eln2 = titled[(i - s)]
            both = eln1 + eln2
            bothchar = eln1 + "." + eln2
            bothchar2 = eln1 + "_" + eln2
            bothchar3 = eln1 + "-" + eln2
            both2 = eln2 + eln1
            bothcharev = eln2 + "." + eln1
            bothcharev2 = eln2 + "_" + eln1
            bothcharev3 = eln2 + "-" + eln1
            toappend = [both, bothchar, bothchar2, bothchar3, both2, bothcharev, bothcharev2, bothcharev3]
            compositeuppercasedtitled.extend(toappend)

    compositelowercasedtitled = []

    for i in range(0, len1):
        for s in range(1, len1):

            eln1 = uppercased[i]
            eln2 = titled[(i - s)]
            both = eln1 + eln2
            bothchar = eln1 + "." + eln2
            bothchar2 = eln1 + "_" + eln2
            bothchar3 = eln1 + "-" + eln2
            both2 = eln2 + eln1
            bothcharev = eln2 + "." + eln1
            bothcharev2 = eln2 + "_" + eln1
            bothcharev3 = eln2 + "-" + eln1
            toappend = [both, bothchar, bothchar2, bothchar3, both2, bothcharev, bothcharev2, bothcharev3]
            compositelowercasedtitled.extend(toappend)

    final = set(
        compositeuppercased
        + compositelowercased
        + compositetitled
        + compositeuppercasedlowercased
        + compositeuppercasedtitled
        + compositelowercasedtitled
    )
    
    return final


numbered = []

def numerator(userwords):
    print("[*] Appending Numbers...")
    for word in userwords:
        for i in ["{0:02}".format(i) for i in range(0, 101)]:
            neword = word + str(i)
            numbered.append(neword)

        for i in ["{0:01}".format(i) for i in range(0, 11)]: 
            neword = word + str(i)
            numbered.append(neword)

        if (year != ""):

            neword = word + year
            numbered.append(neword)    

        if (day != "" and month != ""):

            neword = word + day + month
            numbered.append(neword)

            neword = word + month + day
            numbered.append(neword)

        if (day != "" and month != "" and year != ""):

            neword = word + day + month + year
            numbered.append(neword)

            neword = word + day + month + yeared
            numbered.append(neword)

            neword = word + month + day + yeared
            numbered.append(neword)
        
        else:

            continue

chars = []
numchars = []
extrappended = []
 
def specialchar(userwords, nums):
    print("[*] Appending special chars...")
    
    for word in userwords:
        
        neword = word + "!"
        chars.append(neword)

        neword = word + "$"
        chars.append(neword)

        neword = word + "?"
        chars.append(neword)

    for word in userwords:

        neword = word + "."
        extrappended.append(neword)

        neword = word + "-"
        extrappended.append(neword)

        neword = word + "_"
        extrappended.append(neword)

    for word in nums:
        
        neword = word + "!"
        numchars.append(neword)

        neword = word + "$"
        numchars.append(neword)

        neword = word + "?"
        numchars.append(neword)


def extranumerator(userwords, extra):
    for word in userwords:

        for i in ["{0:02}".format(i) for i in range(0, 101)]:
            neword = word + str(i)
            numbered.append(neword)

        for i in ["{0:01}".format(i) for i in range(0, 11)]: 
            neword = word + str(i)
            numbered.append(neword)

        if (year != ""):
            
            neword = word + year
            numbered.append(neword)
        
        if (day != "" and month != ""):

            neword = word + day + month
            numbered.append(neword)

            neword = word + month + day
            numbered.append(neword)

        if (day != "" and month != "" and year != ""):

            neword = word + day + month + year
            numbered.append(neword)

            neword = word + day + month + yeared
            numbered.append(neword)

            neword = word + month + day + yeared
            numbered.append(neword)

        else: 
            continue
     

    for word in extra:

        for i in ["{0:02}".format(i) for i in range(0, 101)]: 
            neword = word + str(i)
            numbered.append(neword)

        for i in ["{0:01}".format(i) for i in range(0, 11)]: 
            neword = word + str(i)
            numbered.append(neword)

        if (year != ""):
            
            neword = word + year
            numbered.append(neword)

        if (day != "" and month != ""):

            neword = word + day + month
            numbered.append(neword)

            neword = word + month + day
            numbered.append(neword)

        if (day != "" and month != "" and year != ""): 

            neword = word + day + month + year
            numbered.append(neword)

            neword = word + day + month + yeared
            numbered.append(neword)

            neword = word + month + day + yeared
            numbered.append(neword)

        else: 
            continue

uppercaser(userwords)
lowercaser(userwords)
titler(userwords)

multiplexed = multiplexor(uppercased, lowercased, titled) 
numerator(multiplexed)
specialchar(multiplexed, numbered)
extranumerator(chars, extrappended)
toutput = set(chars + numchars + numbered + uppercased + lowercased + titled + list(multiplexed))

print("[*] Removing extra words... ")
reslist = []
for word in toutput:
    if len(word) >= int(restrain):
        reslist.append(word)
        
finaloutput = set(reslist)

strictlist = []
if (strict == "y"):
    for word in finaloutput:
        boo = False
        boo2 = False
        boo3 = False
        for letter in word:
            if letter.isupper():
                boo = True
            if letter.istitle():
                boo2 = True
            if (letter == "!" or letter == "?" or letter == "$"):
                boo3 = True

        if (boo and boo2 and boo3):
            strictlist.append(word)
   
defoutput = set(strictlist)

# File generation block
print(" ")
print("[+] Generating file...")
with open("wordlist.txt", "a+") as output:
    for elem in defoutput:
        output.write("{}\n".format(elem))

print(" ")
print("[!] Wordlist generated successfully. Providing {} guesses, Good luck.".format(len(defoutput)))
