import csv
import re

def main():

    engine_schemat = [] 
    new_schemat = []
    engine_Number = []
    count = 0

    def specialCharacters(letter):

        for c in letter:
            if not (c.isalpha() or c.isdigit() or c == '.'):
                return True
        return False
    
    def addingEngineNumner(indexNumber, numnerLenght, digit, lineNumber):


        baze =[(-1, 0), (-1, -1), (0, -1), (+1, -1), (+1, 0), (-1, +1), (+1, +1), (0, +1)]
        offset_2 = [(-1, +2), (+1, +2), (0, +2)]
        offset_3 =[(-1, +3), (+1, +3), (0, +3)]
        combain_Lists =[]

        # print(digit)

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


    # 'Open file, append data to engine_shema List[]
    try:
        # Read data into memory from file
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                #print(row)
                engine_schemat.append(row)
                #print(teams)
    except FileNotFoundError:
        print("File not found. Make sure the file '_______.csv' exists.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")    

    # Addnig to ne list, each element form list as a char
    for item in engine_schemat:
        for element in item:
            new_schemat.append(list(element))
                

    digitCounter = 0
    # Ustalanie maxLenght, inexNumberFilstDigit i przekazanie danych do addingEngineNumner
    for i in range(len(new_schemat)):
        # print(new_schemat[i])
        #Zeruj dane przechodzać do nowej lini
        maxLenght = 0
        inexNumberFilstDigit = 0
        newDigit = ''
        for j in range(len(new_schemat[i])):
            #  srawdzić czy j jest liczbą, jeżeli jest dodaj 1 do digitCounter, i połącz cyfry
            # print(new_schemat[i][j])
            if new_schemat[i][j].isdigit():
                digitCounter += 1
                #łączenie cyfr ze sobą 
                newDigit += new_schemat[i][j]
                if maxLenght < digitCounter:
                    maxLenght = digitCounter
                if maxLenght == 1:
                    inexNumberFilstDigit = j
                    # print(j)
            else:
                if digitCounter != 0:
                    #Przekaż dane do funkcji 
                    addingEngineNumner(inexNumberFilstDigit, maxLenght, newDigit, i)
                    #Zeruj dane przechodzać do nowej lini
                    digitCounter = 0
                    maxLenght = 0
                    inexNumberFilstDigit = 0
                    newDigit = ''
        #Przechodząc do nowej lini, sprawdź czy addingEngineNumner jest różne od zera
        if digitCounter != 0:
            addingEngineNumner(inexNumberFilstDigit, maxLenght, newDigit, i)

    # print(engine_Number)
 
    Sum = sum(engine_Number)
    print(Sum)


if __name__ == "__main__":  
    main()