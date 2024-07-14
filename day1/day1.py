
import csv
import os
# import sys
# import random


def main():
    
    # Storage text in a tabee below
    indeksy = []
    textTable = []
    calibrationValues = []
    sumCalibaration = 0

    word_digit_pairs = [
        ('one', '1'),
        ('zero', '0'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9')
    ]


    def findSentens(row):
        #find word in senstens, and add to indeksy arry
        for word, digit in word_digit_pairs:

            indeksWord = row.find(word)

            while indeksWord != -1:
                indeksy.append((indeksWord, digit))
                indeksWord = row.find(word, indeksWord + 1)
                
                   
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
 
        for j, element in enumerate(row):
            findSentens(element)
            for k, letter in enumerate(element):
                # print(letter)
                if letter.isdigit():
                    # 'k' to miejsce litery w ciągu znaków 
                    digitIndeks = element.find(letter)
                    while digitIndeks != -1:
                        indeksy.append((digitIndeks, letter))
                        digitIndeks = element.find(letter, digitIndeks + 1)
                         
                    # print(f"Znaleziono liczbę '{letter}', licza '{k}' na indeksie:", indeksy) 

        #lenght of table with all numbers
        indeksy.sort()
        lenghtTable = len(indeksy)
 
        # if there is more than 1 digit in the line, add first and last digit 
        if lenghtTable > 1:
            calibrationValues.append(str(indeksy[0][1]) + str(indeksy[-1][1]))
        # in other cases, duble the number
        else:
            calibrationValues.append(str(indeksy[0][1]) + str(indeksy[0][1]))
        indeksy.clear()
    # # print(calibrationValues)

    # Add number to number from table calibrationValues    
    for number in calibrationValues:
        sumCalibaration += int(number)        
    
    print(sumCalibaration)
            

if __name__ == "__main__":
    main()