#AUTHOR: Jordan Barnes
#EMAIL: jordanbarnesneuro@gmail.com
   
import math
import csv

#This function calculates the distance from 0,0 to x, y coord to check if this is a NC3 shot
def calculateDist(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

#this function checks if the shot was made in bounds
def checkIfBounds(x, y):
    if x < 0.0 and y < 0.0:
        return False
    elif x > 0.0 and y < 0.0:
        return False
    else:
        return True
    
#this function calculates the zone in which the shot was attempted
def calculateZone(x, y):
    
    #checks if FG attempt was oob
    if checkIfBounds(x, y) == False:
        return 'OOB'
    elif x > 22 and y < 7.8 or x < -22 and y < 7.8:
        return 'C3'
    elif x > 22 and y > 7.8 or x < -22 and y > 7.8:
        return 'NC3'
    elif y > 7.8 and calculateDist(0, 0, x, y) > 23.75 or y > 7.8 and calculateDist(0, 0, x, y) < -23.75:
        return 'NC3'
    else:
        return 'PT2'
#this is our main function, returns our percentages and reads the CSV file
def readData():
    
    #lists declarations to be filled with CSV data
    team = []
    xVal = []
    yVal = []
    shotsMade = []
    #Team A's data fields
    AtotalAttemptNC3 = 0
    AtotalAttemptC3 = 0
    AtotalAttemptPT2 = 0
    
    AtotalMadeNC3 = 0
    AtotalMadeC3 = 0
    AtotalMadePT2 = 0
    
    #Team B's data fields
    BtotalAttemptNC3 = 0
    BtotalAttemptC3 = 0
    BtotalAttemptPT2 = 0
    
    BtotalMadeNC3 = 0
    BtotalMadeC3 = 0
    BtotalMadePT2 = 0
    
    #OOB count for each team
    aOOB = 0
    bOOB = 0
    
    #here we read the data from the CSV file deliminating by ,
    with open('shots_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            #here we append the data from the CSV into our lists above
            team.append(row[0])
            xVal.append(float(row[1]))
            yVal.append(float(row[2]))
            shotsMade.append(int(row[3]))
    

    

#here we are looping through each row of data labeled under a team and provide it to our calculations and checks
    for i in range(1, len(team)):
         if team[i] == 'Team A':
             #below are our if statements that calculate whether the given shot was made or attempted
             #and it checks what zone it was attempted/made in.
             
             #this section is for the A team
            if calculateZone(xVal[i], yVal[i]) == 'OOB':
                 aOOB += 1
            elif calculateZone(xVal[i], yVal[i]) == 'NC3':
                 AtotalAttemptNC3 += 1
                 if shotsMade[i] == 1:
                     AtotalMadeNC3 += 1
            elif calculateZone(xVal[i], yVal[i]) == 'C3':
                AtotalAttemptC3 += 1
                if shotsMade[i] == 1:
                    AtotalMadeC3 += 1
            elif calculateZone(xVal[i], yVal[i]) == 'PT2':
                AtotalAttemptPT2 += 1
                if shotsMade[i] == 1:
                    AtotalMadePT2 += 1
                 
        #this section is for the B team
         else:

            if calculateZone(xVal[i], yVal[i]) == 'OOB':
                 bOOB += 1
            elif calculateZone(xVal[i], yVal[i]) == 'NC3':
                 BtotalAttemptNC3 += 1
                 if shotsMade[i] == 1:
                     BtotalMadeNC3 += 1
            elif calculateZone(xVal[i], yVal[i]) == 'C3':
                BtotalAttemptC3 += 1
                if shotsMade[i] == 1:
                    BtotalMadeC3 += 1
            elif calculateZone(xVal[i], yVal[i]) == 'PT2':
                BtotalAttemptPT2 += 1
                if shotsMade[i] == 1:
                    BtotalMadePT2 += 1



    #below we calculate all the data with standard average formulas
    #see print statements for sectional data declarations
    print('========================================')
    print('A team average FG attempt for each zone:')
    print('========================================')
    
    aTotalShotsAttempted = AtotalAttemptC3 + AtotalAttemptNC3 + AtotalAttemptPT2
    aPT2PercAttempt = AtotalAttemptPT2 / aTotalShotsAttempted
    print("Percentage 2PT Attempts: " + str(round(aPT2PercAttempt, 3)))
    
    aNC3PercAttempt = AtotalAttemptNC3 / aTotalShotsAttempted
    print("Percentage NC3 Attempts: " + str(round(aNC3PercAttempt, 3)))
    
    aC3PercAttempt = AtotalAttemptC3 / aTotalShotsAttempted
    print("Percentage C3 Attempts: " + str(round(aC3PercAttempt, 3)))
    print("")
    
    print('========================================')
    print('B team average FG attempt for each zone:')
    print('========================================')
    
    bTotalShotsAttempted = BtotalAttemptC3 + BtotalAttemptNC3 + BtotalAttemptPT2
    bPT2PercAttempt = BtotalAttemptPT2 / bTotalShotsAttempted
    print("Percentage 2PT Attempts: " + str(round(bPT2PercAttempt, 3)))
    
    bNC3PercAttempt = BtotalAttemptNC3 / bTotalShotsAttempted
    print("Percentage NC3 Attempts: " + str(round(bNC3PercAttempt, 3)))
    
    bC3PercAttempt = BtotalAttemptC3 / bTotalShotsAttempted
    print("Percentage C3 Attempts: " + str(round(bC3PercAttempt, 3)))
    
    print("")
    
    
    print('========================================')
    print('A team average eFG for each zone:')
    print('========================================')
    
    aPT2PercMade = AtotalMadePT2 / AtotalAttemptPT2
    print("Percentage 2PT made: " + str(round(aPT2PercMade, 3)))
    
    aNC3PercMade = AtotalMadeNC3 / AtotalAttemptNC3
    print("Percentage NC3 made: " + str(round(aNC3PercMade, 3)))
    
    aC3PercMade = AtotalMadeC3 / AtotalAttemptC3
    print("Percentage C3 made: " + str(round(aC3PercMade, 3)))
    print("")
    
    print('========================================')
    print('B team average eFG for each zone:')
    print('========================================')
    
    bPT2PercMade = BtotalMadePT2 / BtotalAttemptPT2
    print("Percentage 2PT made: " + str(round(bPT2PercMade, 3)))
    
    bNC3PercMade = BtotalMadeNC3 / BtotalAttemptNC3
    print("Percentage NC3 made: " + str(round(bNC3PercMade, 3)))
    
    bC3PercMade = BtotalMadeC3 / BtotalAttemptC3
    print("Percentage C3 made: " + str(round(bC3PercMade, 3)))
    
    
    
    
    
#calling the function to provide the data.
readData()
        
                
            
            
        



