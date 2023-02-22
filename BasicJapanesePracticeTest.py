from random import *


a = (u"あ",u"い",u"う",u"え",u"お")
k = (u"か",u"き",u"く",u"け",u"こ")
s = (u"さ",u"し",u"す",u"せ",u"そ")
t = (u"た",u"ち",u"つ",u"て",u"と")

aE = ("a","i","u","e","o")
kE = ("ka","ki","ku","ke","ko")
sE = ("sa","shi","su","se","so")
tE = ("ta","chi","tsu","te","to")

letterMatrix = (a,k,s,t)
englishMatrix = (aE,kE,sE,tE)

def test():


    while 0 == 0:
        column = randint(0,3)
        row = randint(0,4)
        answer = input(letterMatrix[column][row])
        if englishMatrix[column][row] == answer:
            print("Correct\n")
        else:
            print (englishMatrix[column][row])
            print("Wrong\n")
        

test()
