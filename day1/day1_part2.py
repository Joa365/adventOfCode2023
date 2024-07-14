
import csv
import sys
import random


def main():
    
    # Storage text in a tabee below
    textTable = []
    calibrationValues = []
    sumCalibaration = 0
    word_digit_pairs = [
        ('zero', '0'),
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9')
    ]

    def searchThroughWordNumberTable(row):
        
        for word, digit in word_digit_pairs:
            lenghtWord = len(word)
            # print(lenghtWord)
            counter = 0
            for i, letterNumber in enumerate(word):
                for sentense in row:
                    for j, letterSentense in enumerate(sentense):
                        if letterSentense.isalpha() and letterNumber == letterSentense:
                            counter += 1
                        else:
                            counter = 0
            if counter == lenghtWord:
                print(counter)


    try:
        # Read data into memory from file
        with open('input.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                #print(row)
                textTable.append(row)
                #print(teams)
    except FileNotFoundError:
        print("File not found. Make sure the file 'input.csv' exists.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")    


    #Add numbers to new table from rows
    for i, row in enumerate(textTable):
        tableNumbers = []
        # searchThroughWordNumberTable(row)
        for j, element in enumerate(row):
            for k, letter in enumerate(element):
                # print(letter)
                if letter.isdigit():
                    # 'k' to miejsce litery w ciągu znaków 
                    tableNumbers.append(letter)
        #lenght of table with all numbers
        lenghtTable = len(tableNumbers)
        # print(tableNumbers)
        # if there is more than 1 digit in the line, add first and last digit 
        if lenghtTable > 1:
            calibrationValues.append(str(tableNumbers[0]) + str(tableNumbers[lenghtTable-1]))
        # in other cases, duble the number
        else:
            calibrationValues.append(str(tableNumbers[0]) + str(tableNumbers[0]))
    # print(calibrationValues)

    # Add number to number from table calibrationValues    
    for number in calibrationValues:
        sumCalibaration += int(number)        
    
    print(sumCalibaration)


            

if __name__ == "__main__":
    main()