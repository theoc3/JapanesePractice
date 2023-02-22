import random as rd
import numpy as np
import time as tm
import statistics as stats
import pandas as pandas
import datetime as datetime


def katakanaTest():
    kCharsFile = open("KatakanaCharacters.txt","r",encoding="utf-8")
    kChars = np.loadtxt(kCharsFile,dtype=object)
    kCharsFile.close()
    print(kChars)

    kTransFile = open("KatakanaTranslations.txt","r",encoding="utf-8")
    kTrans = np.loadtxt(kTransFile,dtype=object)
    kTransFile.close()
    print(kTrans)

    kScoresFile = open("KatakanaScores.txt","r")
    kScores = np.loadtxt(kScoresFile,dtype=str)
    kScoresFile.close()
    print(kScores)

    kCorrectTimingsFile = open("KatakanaCorrectTimings.txt","r")
    kCorrectTimings = np.loadtxt(kCorrectTimingsFile,dtype=object)
    kCorrectTimingsFile.close()
    print(kCorrectTimings)

    kWrongTimingsFile = open("KatakanaWrongTimings.txt","r")
    kWrongTimings = np.loadtxt(kWrongTimingsFile,dtype=object)
    kWrongTimingsFile.close()
    print(kWrongTimings)



    while 0 == 0:
        row = rd.randint(0,len(kChars)-1)
        column = rd.randint(0,4)

        if kChars[row,column] != "/":
            score = rd.randint(1,100)
            
            if 100 - int(kScores[row,column]) >= score:

                start = tm.time()
                answer = input("\n"+kChars[row,column])
                end = tm.time()
                
                if answer == (kTrans[row,column]):
                    print("CORRECT\n---------------------------------\n")

                    kScores[row,column] = str(int(kScores[row,column]) + 5)

                    kCorrectTimings[row,column] = (kCorrectTimings[row,column]+"-"+str(round(end-start,5)))


                    kCorrectTimingsFile = open("KatakanaCorrectTimings.txt","w")
                    for i in kCorrectTimings:
                        kCorrectTimingsFile.write(" ".join(list(i))+"\n")
                    kCorrectTimingsFile.close()
                        
                else:
                    print("WRONG\n"+kTrans[row,column]+"\n---------------------------------\n")
                    if int(kScores[row,column]) > 10:
                        kScores[row,column] = str(int(kScores[row,column]) - 10)
                    else:
                        kScores[row,column] = str(0)

                    kWrongTimings[row,column] = (kWrongTimings[row,column]+"-"+str(round(end-start,5)))


                    kWrongTimingsFile = open("KatakanaWrongTimings.txt","w")
                    for i in kWrongTimings:
                        kWrongTimingsFile.write(" ".join(list(i))+"\n")
                    kWrongTimingsFile.close()
                        
                                
                kScoresFile = open("KatakanaScores.txt","w")
                for i in kScores:
                    #print(" ".join(list(i)))
                    kScoresFile.write(" ".join(list(i))+"\n")
                kScoresFile.close()

def timeTest():
    start = tm.time()
    answer = input("test")
    end = tm.time()
    print("it took", (end-start), "seconds")

def characterInfo(x):
    kCharsFile = open("KatakanaCharacters.txt","r",encoding="utf-8")
    kChars = np.loadtxt(kCharsFile,dtype=object)
    kCharsFile.close()
    kTransFile = open("KatakanaTranslations.txt","r",encoding="utf-8")
    kTrans = np.loadtxt(kTransFile,dtype=object)
    kTransFile.close()
    kScoresFile = open("KatakanaScores.txt","r")
    kScores = np.loadtxt(kScoresFile,dtype=str)
    kScoresFile.close()
    kCorrectTimingsFile = open("KatakanaCorrectTimings.txt","r")
    kCorrectTimings = np.loadtxt(kCorrectTimingsFile,dtype=str)
    kCorrectTimingsFile.close()
    kWrongTimingsFile = open("KatakanaWrongTimings.txt","r")
    kWrongTimings = np.loadtxt(kWrongTimingsFile,dtype=str)
    kWrongTimingsFile.close()


    indexLocation = np.where(kTrans == x)
    correctTimingList = str(kCorrectTimings[indexLocation][0]).split("-")
    wrongTimingList = str(kWrongTimings[indexLocation][0]).split("-")
    
    correctTimingList.remove("/")
    wrongTimingList.remove("/")
    correctFloatList = [float(i) for i in correctTimingList]
    correctTimingList = correctFloatList
    wrongFloatList = [float(i) for i in wrongTimingList]
    wrongTimingList = wrongFloatList

    correctMean = None
    wrongMean = None
    if len(correctTimingList) > 0:
        correctMean = round(stats.mean(correctTimingList),2)
        correctMedian = round(stats.median(correctTimingList),2)
    if len(wrongTimingList) > 0:
        wrongMean = round(stats.mean(wrongTimingList),2)
        wrongMedian = round(stats.median(wrongTimingList),2)
        
    print(str(kChars[indexLocation][0])+" : "+str(kTrans[indexLocation][0])+"\nCurrentScore: "+str(kScores[indexLocation][0])+"\n")
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

def progress():
    kCharsFile = open("KatakanaCharacters.txt","r",encoding="utf-8")
    kChars = np.loadtxt(kCharsFile,dtype=object)
    kCharsFile.close()
    kTransFile = open("KatakanaTranslations.txt","r",encoding="utf-8")
    kTrans = np.loadtxt(kTransFile,dtype=object)
    kTransFile.close()
    kScoresFile = open("KatakanaScores.txt","r")
    kScores = np.loadtxt(kScoresFile,dtype=str)
    kScoresFile.close()
    kCorrectTimingsFile = open("KatakanaCorrectTimings.txt","r")
    kCorrectTimings = np.loadtxt(kCorrectTimingsFile,dtype=str)
    kCorrectTimingsFile.close()
    kWrongTimingsFile = open("KatakanaWrongTimings.txt","r")
    kWrongTimings = np.loadtxt(kWrongTimingsFile,dtype=str)
    kWrongTimingsFile.close()


    #print(kTable)
    kTable = []
    
    for x in kChars:
        for y in x:
            if y != "/":
                indexLocation = np.where(kChars == y)
                
                correctTimingList = str(kCorrectTimings[indexLocation][0]).split("-")
                wrongTimingList = str(kWrongTimings[indexLocation][0]).split("-")
                
                correctTimingList.remove("/")
                wrongTimingList.remove("/")
                correctFloatList = [float(i) for i in correctTimingList]
                correctTimingList = correctFloatList
                wrongFloatList = [float(i) for i in wrongTimingList]
                wrongTimingList = wrongFloatList

                correctMean = ""
                correctMedian = ""
                wrongMean = ""
                wrongMedian = ""
                if len(correctTimingList) > 0:
                    correctMean = stats.mean(correctTimingList)
                    correctMedian = stats.median(correctTimingList)
                if len(wrongTimingList) > 0:
                    wrongMean = stats.mean(wrongTimingList)
                    wrongMedian = stats.median(wrongTimingList)
                
                kTable.append([str(kChars[indexLocation][0]),str(kTrans[indexLocation][0]),str(kScores[indexLocation][0]),str(correctMean),str(correctMedian),str(wrongMean),str(wrongMedian)])
                #kTable = np.concatenate((kTable,kTableAdd), axis = 0)
    pandas.set_option("display.max_rows",72)
    #headers = ["Japanese","Pronunciation","Score","AvgCorrectTime","MedianCorrectTime","AvgerageWrongTime","MedianWrongTime"]
    now = datetime.datetime.now().strftime("%Y.%m.%d - %H.%M.%S.%f")
    fileName = "kData "+str(now)+".csv"
    pandas.DataFrame(kTable).to_csv(fileName, sep=',')
    print(pandas.DataFrame(kTable))
    #for i in kTable:
        #print(i)



    






    

