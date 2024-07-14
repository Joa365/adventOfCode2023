import csv
import os
import string

def main():
    
    # print("Current working directory:", os.getcwd())

    stringTable =[]
    setGame = {}
    sumId = []

    bagset = [
        ("red", 12),
        ("blue",  14),
        ("green", 13)
    ]

    # Method take one line form csv file add adding game data to sumId list 
    def addingToGameArray(gimeLine=[]):

        # Join all senstens
        wholeList = "".join(gimeLine)
        print(wholeList)

        #Remove punctuation from string
        sentesnNoPunctatiomMarks = wholeList.translate(str.maketrans('', '', string.punctuation))
        
        #split sentens 
        slpliSenstens = sentesnNoPunctatiomMarks.split(' ')
        # print(slpliSenstens)
        
        #Get list lenght 
        lenghOfListSplitSentens = len(slpliSenstens)
        # print(lenghOfListSplitSentens)

        i = 2 
        countResult = 0  
        while i < lenghOfListSplitSentens:
            #id i is even 
            if i % 2 == 0:
                cubeNumber = int(slpliSenstens[i])
                # print(cubesNumber)
                for color, number in bagset:
                    if color == slpliSenstens[i + 1] and cubeNumber <= number:
                        # print (int(slpliSenstens[i]))
                        countResult = countResult + 1  
                        break  
            i = i + 1

        #if countResulr is equla lenght of sensten splited, add ro sumId List
        if countResult == ((lenghOfListSplitSentens-2)/2):
            sumId.append(int(slpliSenstens[1]))
            # print(slpliSenstens[1])

                

    try:
        # Read data into memory from file
        with open('game_input.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                stringTable.append(row)
    except FileNotFoundError:
        print("File not found. Make sure the file 'game_input.csv' exists.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")    


    #From csv file  
    for item in stringTable:
        addingToGameArray(item)


    # for number in  sumId:
    #     print(number)

    Sum = sum(sumId)
    print(Sum)

if __name__ == "__main__":
    main()