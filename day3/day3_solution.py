import csv

def main():
    engine_schemat = [] 
    new_schemat = []
    engine_numbers = []

    def is_special_character(letter):
        return not (letter.isalnum() or letter == '.')

    def extract_engine_number(line, start_index, length):
        engine_number = ''
        for j in range(start_index, start_index + length):
            if j < len(line) and line[j].isdigit():
                engine_number += line[j]
            else:
                break
        return engine_number

    try:
        # Read data into memory from file
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                engine_schemat.append(row)
    except FileNotFoundError:
        print("File not found. Make sure the file 'data.csv' exists.")
        return
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
        return

    for item in engine_schemat:
        for element in item:
            new_schemat.append(list(element))

    for i, line in enumerate(new_schemat):
        max_length = 0
        start_index = 0
        for j, char in enumerate(line):
            if char.isdigit():
                length = 1
                while j + length < len(line) and line[j + length].isdigit():
                    length += 1
                if length > max_length:
                    max_length = length
                    start_index = j
        if max_length > 0:
            engine_number = extract_engine_number(line, start_index, max_length)
            engine_numbers.append(int(engine_number))

    print("Engine Numbers:", engine_numbers)
    print("Sum of Engine Numbers:", sum(engine_numbers))

if __name__ == "__main__":
    main()
