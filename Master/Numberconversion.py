def digitToKanji(digit):
    kanjiList = ("","一","二","三","四","五","六","七","八","九","十")
    return kanjiList[int(digit)]


tensUnitList = ("","十","百","千")
myriadsUnitList = ("","万","億","兆","京")
def numConv(output,numAsList,myriadsIteration):
    myriadGroup = ""
    if myriadsIteration-1 == len(numAsList)//4+1:
        print("output"+output)
        
        return output.replace("#","")
    
    if len(numAsList) >= myriadsIteration*4:
        loopAmt = 4
    else:
        loopAmt = len(numAsList) - ((myriadsIteration-1) * 4)
    print("LOOP"+str(loopAmt))
    print(numAsList)
    for tensIteration in range(0,loopAmt):
        #print("tens"+str(tensIteration))
        #print("myriads"+str(myriadsIteration))
        print(tensIteration+(4 * (myriadsIteration-1)))
        digit = digitToKanji(numAsList[tensIteration+(4 * (myriadsIteration-1))])
        print(digit)
        if digit != "":
            tens = tensUnitList[tensIteration % 4]
        else:
            tens = ""
        if myriadsIteration != 1 and digit == "一":
            digit = "#"
        elif digit == "一" and (tens == "十" or tens == "百" or tens =="千"):
            digit = "#"
            
        myriadGroup = str(digit+tens+myriadGroup)
        #output = str(digit+tens+output)
        print("myriadGroup"+myriadGroup)


        
    myriadsIteration += 1
    print("myriadIteration"+str(myriadsIteration))
    if myriadGroup != "":
        output = myriadGroup+myriadsUnitList[myriadsIteration-2]+output
    print("output"+output)
    #output = str(output+myriadsUnitList[myriadsIteration-2])
    return numConv(output,numAsList,myriadsIteration)

            
def conv(num):
    if num == 0:
        return "〇"
    numAsList = []
    while num != 0:
        digit = num % 10
        num = num // 10
        numAsList.append(digit)

    print("FINAL: "+numConv("",numAsList,1))
    print("NUM: " +str(numAsList))



#########################################
#########################################
#########################################
#########################################
#########################################
#########################################
    
def digitToKanjiOld(digit):
    kanjiList = ("","一","二","三","四","五","六","七","八","九","十")
    return kanjiList[int(digit)]

placeList = ("","十","百","千")
newUnitList = ("","万","億","兆","京")
def numConvOld(output,numAsList,iteration):

    if iteration == len(numAsList)+1:

        return output
    else:

        digit = digitToKanji(numAsList[iteration-1])


        if digit != "":
            tens = placeList[(iteration % 4)-1]
        else:
            tens = ""

        if iteration % 4 == 1 and digit != "":
            myriad = newUnitList[int((iteration-1)/4)]
        else:
            myriad = ""
        if iteration != 1:
            digit = ""

        output = str(digit+tens+myriad+output)

        iteration += 1

        return numConv(output,numAsList,iteration)

def convOld(num):
    if num == 0:
        return "〇"
    numAsList = []
    while num != 0:
        digit = num % 10
        num = num // 10
        numAsList.append(digit)
    print(numConv("",numAsList,1))
    
    


def numberToJpOld(num):
    if num == 0:
        return "〇"
    numAsList = []
    while num != 0:
        digit = num % 10
        print(digit)
        num = num // 10
        numAsList.append(digit)
    print(numAsList)
    
    placeList = ("","十","百","千")
    newUnitList = ("","万","億","兆","京")

    
    placeIndex = -1
    newUnitIndex = -1
    while len(numAsList) != 0:
        placeIndex += 1
        if placeIndex == 4:
            placeIndex = -1
            newUnit += 1
            
        if int(numAsList[0]) != 0:
            digit = digitToKanji(int(numAsList[0]))
            numAsList = numAsList[1:]

            return str(newUnitList[newUnitIndex]+placeList[placeIndex]+digit)
             
            
conv(1000000000000000)
