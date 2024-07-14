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

    # Method take one line form csv file add results of thad line to sumId list 
    def addingToGameArray(gimeLine=[]):

        # Join all senstens
        wholeList = "".join(gimeLine)
        # print(wholeList)

        #Remove punctuation from string
        sentesnNoPunctatiomMarks = wholeList.translate(str.maketrans('', '', string.punctuation))
        
        #split sentens 
        slpliSenstens = sentesnNoPunctatiomMarks.split(' ')
        # print(slpliSenstens)
        
        #Get lis lenght 
        lenghOfListSplitSentens = len(slpliSenstens)
        # print(lenghOfListSplitSentens)

        red = 0
        green = 0
        blue = 0

        i = 2 
        while i < lenghOfListSplitSentens:
            #if id i is even 
            if i % 2 == 0:
                cubeNumber = int(slpliSenstens[i])
                # print(cubesNumber)
                if "red" == slpliSenstens[i + 1] and red < cubeNumber:
                    red =  cubeNumber
                elif "green" == slpliSenstens[i + 1] and green < cubeNumber:
                    green =  cubeNumber
                elif "blue" == slpliSenstens[i + 1] and blue < cubeNumber:
                    blue =  cubeNumber
            i = i + 1

        # add result to sumId List
        sumId.append(int(red * green * blue))
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
    
    #Add digits from sumId[1]
    Sum = sum(sumId)
    print(Sum)



if __name__ == "__main__":
    main()