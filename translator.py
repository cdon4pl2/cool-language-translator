#variables



ltr1 = input("Wpisz słowo do przetłumaczenia(max 10 ltrs):")
ltr2 = input("Wpisz słowo do przetłumaczenia(max 10 ltrs):")
ltr3 = input("Wpisz słowo do przetłumaczenia(max 10 ltrs):")
ltr4 = input("Wpisz słowo do przetłumaczenia(max 10 ltrs):")
ltr5 = input("Wpisz słowo do przetłumaczenia(max 10 ltrs):")
ltr6 = input("Wpisz słowo do przetłumaczenia(max 10 ltrs):")
ltr7 = input("Wpisz słowo do przetłumaczenia(max 10 ltrs):")
ltr8 = input("Wpisz słowo do przetłumaczenia(max 10 ltrs):")
ltr9 = input("Wpisz słowo do przetłumaczenia(max 10 ltrs):")
ltr10 = input("Wpisz słowo do przetłumaczenia(max 10 ltrs):")

def translator(letter):
    alphabet = ["None", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(1, 27):
        if letter == alphabet[i]:
            number = str(i)
            print(number + "x😎🤡")
        
translator(ltr1)
translator(ltr2)
translator(ltr3)
translator(ltr4)
translator(ltr5)
translator(ltr6)
translator(ltr7)
translator(ltr8)
translator(ltr9)
translator(ltr10)





#example:

#INPUT: zwykłe słowo np.:       ok
#OUTPUT: tłumaczenie np.: 15x😎🤡11x😎🤡
