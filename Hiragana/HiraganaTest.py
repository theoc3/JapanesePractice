import random as rd
import numpy as np
import time as tm
import statistics as stats


def hiraganaTest():
    hCharsFile = open("HiraganaCharacters.txt","r",encoding="utf-8")
    hChars = np.loadtxt(hCharsFile,dtype=object)
    hCharsFile.close()
    print(hChars)

    hTransFile = open("HiraganaTranslations.txt","r",encoding="utf-8")
    hTrans = np.loadtxt(hTransFile,dtype=object)
    hTransFile.close()
    print(hTrans)

    hScoresFile = open("HiraganaScores.txt","r")
    hScores = np.loadtxt(hScoresFile,dtype=str)
    hScoresFile.close()
    print(hScores)

    hCorrectTimingsFile = open("HiraganaCorrectTimings.txt","r")
    hCorrectTimings = np.loadtxt(hCorrectTimingsFile,dtype=object)
    hCorrectTimingsFile.close()
    print(hCorrectTimings)

    hWrongTimingsFile = open("HiraganaWrongTimings.txt","r")
    hWrongTimings = np.loadtxt(hWrongTimingsFile,dtype=object)
    hWrongTimingsFile.close()
    print(hWrongTimings)



    while 0 == 0:
        row = rd.randint(0,len(hChars)-1)
        column = rd.randint(0,4)

        if hChars[row,column] != "/":
            score = rd.randint(1,100)
            
            if 100 - int(hScores[row,column]) >= score:

                start = tm.time()
                answer = input("\n"+hChars[row,column])
                end = tm.time()
                
                if answer == (hTrans[row,column]):
                    print("CORRECT\n---------------------------------\n")

                    hScores[row,column] = str(int(hScores[row,column]) + 5)

                    hCorrectTimings[row,column] = (hCorrectTimings[row,column]+"-"+str(round(end-start,5)))


                    hCorrectTimingsFile = open("HiraganaCorrectTimings.txt","w")
                    for i in hCorrectTimings:
                        hCorrectTimingsFile.write(" ".join(list(i))+"\n")
                    hCorrectTimingsFile.close()
                        
                else:
                    print("WRONG\n"+hTrans[row,column]+"\n---------------------------------\n")
                    if int(hScores[row,column]) > 10:
                        hScores[row,column] = str(int(hScores[row,column]) - 10)
                    else:
                        hScores[row,column] = str(0)

                    hWrongTimings[row,column] = (hWrongTimings[row,column]+"-"+str(round(end-start,5)))


                    hWrongTimingsFile = open("HiraganaWrongTimings.txt","w")
                    for i in hWrongTimings:
                        hWrongTimingsFile.write(" ".join(list(i))+"\n")
                    hWrongTimingsFile.close()
                        
                                
                hScoresFile = open("HiraganaScores.txt","w")
                for i in hScores:
                    #print(" ".join(list(i)))
                    hScoresFile.write(" ".join(list(i))+"\n")
                hScoresFile.close()

def timeTest():
    start = tm.time()
    answer = input("test")
    end = tm.time()
    print("it took", (end-start), "seconds")

def characterInfo(x):
    hCharsFile = open("HiraganaCharacters.txt","r",encoding="utf-8")
    hChars = np.loadtxt(hCharsFile,dtype=object)
    hCharsFile.close()
    hTransFile = open("HiraganaTranslations.txt","r",encoding="utf-8")
    hTrans = np.loadtxt(hTransFile,dtype=object)
    hTransFile.close()
    hScoresFile = open("HiraganaScores.txt","r")
    hScores = np.loadtxt(hScoresFile,dtype=str)
    hScoresFile.close()
    hCorrectTimingsFile = open("HiraganaCorrectTimings.txt","r")
    hCorrectTimings = np.loadtxt(hCorrectTimingsFile,dtype=str)
    hCorrectTimingsFile.close()
    hWrongTimingsFile = open("HiraganaWrongTimings.txt","r")
    hWrongTimings = np.loadtxt(hWrongTimingsFile,dtype=str)
    hWrongTimingsFile.close()


    indexLocation = np.where(hTrans == x)
    correctTimingList = str(hCorrectTimings[indexLocation][0]).split("-")
    wrongTimingList = str(hWrongTimings[indexLocation][0]).split("-")
    
    correctTimingList.remove("/")
    wrongTimingList.remove("/")
    correctFloatList = [float(i) for i in correctTimingList]
    correctTimingList = correctFloatList
    wrongFloatList = [float(i) for i in wrongTimingList]
    wrongTimingList = wrongFloatList

    correctMean = None
    wrongMean = None
    if len(correctTimingList) > 0:
        correctMean = stats.mean(correctTimingList)
        correctMedian = stats.median(correctTimingList)
    if len(wrongTimingList) > 0:
        wrongMean = stats.mean(wrongTimingList)
        wrongMedian = stats.median(wrongTimingList)
        
    print(str(hChars[indexLocation][0])+" : "+str(hTrans[indexLocation][0])+"\nCurrentScore: "+str(hScores[indexLocation][0])+"\n")
    if correctMean == None:
        print("0 Correct Answers")
    else:
        print(str(len(correctTimingList))+" Correct Answers")
        print(str(correctMean)+"s Correct Answer Mean Response Time")
        print(str(correctMedian)+"s Correct Answer Median Response Time")
    if wrongMean == None:
        print("0 Wrong Answers")
    else:
        print(str(len(wrongTimingList))+" Wrong Answers")
        print(str(wrongMean)+"s Wrong Answer Mean Response Time")
        print(str(wrongMedian)+"s Wrong Answer Median Response Time")





    

