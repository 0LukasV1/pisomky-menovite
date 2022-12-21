# input ak velke pismebko posun ho o 4 miesta
a = 95
def pismenko(text):
    for i in range(0, len(text)):
        x = ord(text[i])
        if a >= x:
            print(i,end=", ")
            print(x+4,end=", ")
            print(text[i],end=", ")
            print()
        else:
            print(i,end=", ")
            print(x,end=", ")
            print(text[i],end=", ")
            print()


pismenko(input('Zadaj vetu: ' ))
