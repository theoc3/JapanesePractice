import random as rd
import numpy as np
import time as tm
import statistics as stats
import pandas as pandas
import datetime as datetime

def main():
    active = True
    while active == True:
        #COMMANDLINE#
        userSelection = str(input("What would you like to practice?\n1 - Syllabary\n2 - Vocab\n>>> "))
        if userSelection == "1":
            practice(syllabary())
            active = False
        elif userSelection == "2":
            practice(vocab())
            active = False
        elif userSelection == "add":
            addVocab()
            active = False
        else:
            #COMMANDLINE#
            print("\nseriously\n")

def addVocab():
    active = True
    while active == True:
        #ejDataList = np.empty((1,7),dtype=object)
        #jeDataList = np.empty((1,7),dtype=object)
        #typingDataList = np.empty((1,7),dtype=object)
        chapter = str(input("Chapter/Category:\n>>> "))
        if chapter == "esc":
            active = False
            main()
        english = str(input("English:\n>>> "))
        if english == "esc":
            active = False
            main()
        japanese = str(input("Japanese:\n>>> "))
        if japanese == "esc":
            active = False
            main()
        #EJ#
        ejVocabFile = open("EnJpVocabData.txt","r",encoding="utf-8")
        ejVocab = np.loadtxt(ejVocabFile,dtype=object,delimiter=",")
        ejVocabFile.close()

        ejAddedVocab = np.array([[len(ejVocab),"EJVCh"+chapter,english,japanese,0,"/","/"]])
        ejVocab = np.vstack((ejVocab,ejAddedVocab))

        ejVocabFile = open("EnJpVocabData.txt","w",encoding="utf-8")
        for i in ejVocab:
            ejVocabFile.write(",".join(list(i))+"\n")
        ejVocabFile.close()

        #JE#
        jeVocabFile = open("JpEnVocabData.txt","r",encoding="utf-8")
        jeVocab = np.loadtxt(jeVocabFile,dtype=object,delimiter=",")
        jeVocabFile.close()

        jeAddedVocab = np.array([[len(jeVocab),"JEVCh"+chapter,japanese,english,0,"/","/"]])
        jeVocab = np.vstack((jeVocab,jeAddedVocab))

        jeVocabFile = open("JpEnVocabData.txt","w",encoding="utf-8")
        for i in jeVocab:
            jeVocabFile.write(",".join(list(i))+"\n")
        jeVocabFile.close()
        
        #TY#
        typingVocabFile = open("TypingVocabData.txt","r",encoding="utf-8")
        typingVocab = np.loadtxt(typingVocabFile,dtype=object,delimiter=",")
        typingVocabFile.close()

        typingAddedVocab = np.array([[len(typingVocab),"TYVCh"+chapter,japanese,japanese,0,"/","/"]])
        typingVocab = np.vstack((typingVocab,typingAddedVocab))

        typingVocabFile = open("TypingVocabData.txt","w",encoding="utf-8")
        for i in typingVocab:
            typingVocabFile.write(",".join(list(i))+"\n")
        typingVocabFile.close()

        
        
def syllabary():
    ##COLUMNADJUST##
    dataList = np.empty((1,7),dtype=object)
    print(dataList)
    charLoop = True
    while charLoop == True:
        #COMMANDLINE#
        userSelection = str(input("Type all numbers of your desired selection.\nSyllabary:\n1 - Hiragana\n2 - Katakana\n>>> "))
        if "1" in userSelection:
            hCharsFile = open("HiraganaData.txt","r",encoding="utf-8")
            hChars = np.loadtxt(hCharsFile,dtype=object,delimiter=",")
            hCharsFile.close()
            print(hChars)
            
            dataList = np.vstack((dataList,hChars))
            charLoop = False
            return dataList[1:]
        if "2" in userSelection:
            kCharsFile = open("KatakanaData.txt","r",encoding="utf-8")
            kChars = np.loadtxt(kCharsFile,dtype=object,delimiter=",")
            kCharsFile.close()
            print(kChars)

            dataList = np.vstack((dataList,kChars))
            charLoop = False
            return dataList[1:]
        if "esc" == userSelection:
            charLoop = False
            main()
            


def vocab():
    dataList = np.empty((1,7),dtype=object)
    print(dataList)
    modeLoop = True
    while modeLoop == True:
        #COMMANDLINE#
        userSelection = str(input("Type all numbers of desired selection.\nVocab Modes:\n1 - Eng. > Jap.\n2 - Jap. > Eng.\n3 - Typing\n>>> "))
        if "1" in userSelection:
            ejVocabFile = open("EnJpVocabData.txt","r",encoding="utf-8")
            ejVocab = np.loadtxt(ejVocabFile,dtype=object,delimiter=",")
            ejVocabFile.close()
            
            dataList = np.vstack((dataList,ejVocab))
            modeLoop = False
            groupLoop = True
        if "2" in userSelection:
            jeVocabFile = open("JpEnVocabData.txt","r",encoding="utf-8")
            jeVocab = np.loadtxt(jeVocabFile,dtype=object,delimiter=",")
            jeVocabFile.close()
            
            dataList = np.vstack((dataList,jeVocab))
            modeLoop = False
            groupLoop = True
        if "3" in userSelection:
            typingVocabFile = open("typingVocabData.txt","r",encoding="utf-8")
            typingVocab = np.loadtxt(typingVocabFile,dtype=object,delimiter=",")
            typingVocabFile.close()
            
            dataList = np.vstack((dataList,typingVocab))
            modeLoop = False
            groupLoop = True
        if userSelection == "esc":
            modeLoop = False
            groupLoop = False
            main()
    while groupLoop == True:
        dataList = dataList[1:]
        #COMMANDLINE#
        vocabDataList = np.empty((1,7),dtype=object)
        userSelection = str(input("Type all designiated indexes w/ spaces of desired lists.\nChapters:\n6,7,8...\n\nMisc Groups:\nALL\n>>> "))
        userSelection = userSelection.split()
        if userSelection[0] == "esc":
            groupLoop = False
            main()
        elif userSelection[0] != "ALL":
            for chapter in userSelection:
                for row in dataList:
                    print(str("VCh"+chapter))
                    print(row[1][2:])
                    if str("VCh"+chapter) == row[1][2:]:
                        vocabDataList = np.vstack((vocabDataList,row))
            return vocabDataList[1:]
        elif userSelection[0] == "ALL":
            return dataList

def practice(data):
    #data[ROW][COLUMN]
    practiceLoop = True
    while practiceLoop == True:
        itemIndex = rd.randint(0,len(data)-1)
        probability = rd.randint(1,100)
        
        if 100 - int(data[itemIndex][4]) >= probability:
            start = tm.time()
            #COMMANDLINE#

            answer = input(data[itemIndex][2]+"\n>>>")
            end = tm.time()
            if answer == "esc" or answer == "ESC":
                practiceLoop = False
                main()
            elif answer in data[itemIndex][3]:
                #COMMANDLINE#
                print("CORRECT\n===========================\n")
                print(data[itemIndex][3])
                print("\n===========================\n")
                data[itemIndex][4] = str(int(data[itemIndex][4])+5)
                data[itemIndex][5] = str(data[itemIndex][5]+"~"+str(round(end-start,5)))

            else:
                #COMMANDLINE#
                print("WRONG\n===========================\n")
                print(data[itemIndex][3])
                print("\n===========================\n")
                if int(data[itemIndex][4]) > 10:    
                    data[itemIndex][4] = str(int(data[itemIndex][4]) - 10)
                else:
                    data[itemIndex][4] = str(0)
                data[itemIndex][6] = str(data[itemIndex][6]+"~"+str(round(end-start,5)))

            if "H" == str(data[itemIndex][1]):
                hCharsFile = open("HiraganaData.txt","r",encoding="utf-8")
                hChars = np.loadtxt(hCharsFile,dtype=object,delimiter=",")
                hCharsFile.close()
                
                hChars[int(data[itemIndex][0])] = data[itemIndex]
                hCharsFile = open("HiraganaData.txt","w",encoding="utf-8")
                for i in hChars:
                    hCharsFile.write(",".join(list(i))+"\n")
                hCharsFile.close()

                
            if "K" == str(data[itemIndex][1]):
                #if len(data) > 72:
                    #itemIndexK = itemIndex - 71
                #else:
                    #itemIndexK = itemIndex
                kCharsFile = open("KatakanaData.txt","r",encoding="utf-8")
                kChars = np.loadtxt(kCharsFile,dtype=object,delimiter=",")
                kCharsFile.close()

                kChars[int(data[itemIndex][0])] = data[itemIndex]
                kCharsFile = open("KatakanaData.txt","w",encoding="utf-8")
                for i in kChars:
                    kCharsFile.write(",".join(list(i))+"\n")
                kCharsFile.close()

            if "EJ" in str(data[itemIndex][1]):
                ejVocabFile = open("EnJpVocabData.txt","r",encoding="utf-8")
                ejVocab = np.loadtxt(ejVocabFile,dtype=object,delimiter=",")
                ejVocabFile.close()

                ejVocab[int(data[itemIndex][0])] = data[itemIndex]
                ejVocabFile = open("EnJpVocabData.txt","w",encoding="utf-8")
                for i in ejVocab:
                      ejVocabFile.write(",".join(list(i))+"\n")
                ejVocabFile.close()
                
            if "JE" in str(data[itemIndex][1]):
                jeVocabFile = open("JpEnVocabData.txt","r",encoding="utf-8")
                jeVocab = np.loadtxt(jeVocabFile,dtype=object,delimiter=",")
                jeVocabFile.close()

                jeVocab[int(data[itemIndex][0])] = data[itemIndex]
                jeVocabFile = open("JpEnVocabData.txt","w",encoding="utf-8")
                for i in jeVocab:
                      jeVocabFile.write(",".join(list(i))+"\n")
                jeVocabFile.close()

            if "TY" in str(data[itemIndex][1]):
                typingVocabFile = open("TypingVocabData.txt","r",encoding="utf-8")
                typingVocab = np.loadtxt(typingVocabFile,dtype=object,delimiter=",")
                typingVocabFile.close()

                typingVocab[int(data[itemIndex][0])] = data[itemIndex]
                typingVocabFile = open("TypingVocabData.txt","w",encoding="utf-8")
                for i in typingVocab:
                      typingVocabFile.write(",".join(list(i))+"\n")
                typingVocabFile.close()






        


#main()
                
                
                

                

                

    
        

    






    

