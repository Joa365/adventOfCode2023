import csv
import re

def main():

    engine_schemat = [] 
    new_schemat = []
    engine_Number = []
    count = 0

    def specialCharacters(letter):
        for c in letter:
            if c == '*':
                return True
        return False
        
    
    def addingEngineNumner(indexNumber, numnerLenght, digit, stringLine, lineNumber):
        #Ustawienie siatki wokół liczb 
        baze =[(-1, 0), (-1, -1), (0, -1), (+1, -1), (+1, 0), (-1, +1), (+1, +1), (0, +1)]
        offset_2 = [(-1, +2), (+1, +2), (0, +2)]
        offset_3 =[(-1, +3), (+1, +3), (0, +3)]
        combain_Lists =[]

        # print(digit)

        # print(type(int(digit)))
        # for lineNumber in range(len(new_schemat)):
        #     for indexNumber in range(len(new_schemat[i])):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ˙˙ ̇ ̣ ̣
   
        if numnerLenght ==  1:
            combain_Lists = baze
            # print(combain_Lists)
        elif numnerLenght == 2:
            combain_Lists = baze + offset_2
            # print(combain_Lists)
        elif numnerLenght == 3:
            combain_Lists = baze + offset_2 + offset_3
            # print(combain_Lists)
        else:
            print(numnerLenght)
                    
        for list in combain_Lists:
            try:
                if specialCharacters(new_schemat[lineNumber + list[0]][indexNumber + list[1]]):
                    engine_Number.append(int(digit))
                    break
            except:
                continue
                


    try:
        # Read data into memory from file
        with open('test11.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                #print(row)
                engine_schemat.append(row)
                #print(teams)
    except FileNotFoundError:
        print("File not found. Make sure the file '_______.csv' exists.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")    


    for item in engine_schemat:
        for element in item:
            new_schemat.append(list(element))
                
    
    # for element in new_schemat:
    #     print(element)



    digitCounter = 0

    for i in range(len(new_schemat)):
        # print(new_schemat[i])
        maxLenght = 0
        inexNumberFilstDigit = 0
        newDigit = ''
        for j in range(len(new_schemat[i])):
            # musimy srawdzić czy j jest liczbą
            # print(new_schemat[i][j])
            
            # Sprawdzam czy j jest *
            if specialCharacters(new_schemat[i][j]):
                print("*")

            if new_schemat[i][j].isdigit():
                digitCounter += 1
                newDigit += new_schemat[i][j]
                if maxLenght < digitCounter:
                    maxLenght = digitCounter
                if maxLenght == 1:
                    inexNumberFilstDigit = j
                    # print(j)
            else:
                if digitCounter != 0:
                    # print(digitCounter)
                    addingEngineNumner(inexNumberFilstDigit, maxLenght, newDigit, new_schemat[i], i)
                    # print(newDigit)
                    # print('line: ' + str(i))
                    digitCounter = 0
                    maxLenght = 0
                    inexNumberFilstDigit = 0
                    newDigit = ''
        if digitCounter != 0:
            addingEngineNumner(inexNumberFilstDigit, maxLenght, newDigit, new_schemat[i], i)

        # break
    # print(maxValue)

    print(engine_Number)
 
    Sum = sum(engine_Number)
    print(Sum)


if __name__ == "__main__":  
    main()