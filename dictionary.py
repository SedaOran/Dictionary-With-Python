from decimal import Decimal
import sys

dictionory_file = "Dictionary.txt"
sample_file = "binarian_transmission.txt"
output_file = "binarian_message.txt"
computation_file = "computations.txt"
peace_message= "peace_message.txt"
output_file1 = "message.txt"
punctuation_list = {'.',',',';','!','?',':'}

temperateure = 0;
speed = 0;
distance = 0;

binarian_to_english_dictionary = {}
english_to_binarian_dictionary = {}


def read_dictionary(file):
    with open(sys.argv[1]) as f:
        for line in f:
            lineArr = line.strip().split(" ")
            binarian_to_english_dictionary[lineArr[0]] = lineArr[1]
            english_to_binarian_dictionary[lineArr[1]] = lineArr[0]


def binarian_to_english(text):
    translatedWord = ""
    if text in binarian_to_english_dictionary:
        translatedWord = binarian_to_english_dictionary[text]
    else:
        translatedWord = text
    return translatedWord


def english_to_binarian(text):
    translatedWord = ""
    if text in english_to_binarian_dictionary:
        translatedWord = english_to_binarian_dictionary[text]
    else:
        translatedWord = text
    return translatedWord


def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return int(bin(decimal)[2:])


def ly_to_km(distance):
    return distance*(9.4607e+12)


read_dictionary(dictionory_file)

with open(sys.argv[2]) as sample:
    with open(output_file, "w") as output:
        for line in sample:
            if line[0] == "#":
                continue
            elif line[0] == "+":
                lineArr = line.strip().split(" ")
                if "Hata" in lineArr:
                        for i in lineArr:
                            try:
                                i=int(i)
                                i=str(i)
                                temperateure = binary_to_decimal(i)
                            except:
                                continue
                elif "bav'Do" in lineArr:
                    for i in lineArr:
                            try:
                                i=int(i)
                                i=str(i)
                                speed = binary_to_decimal(i)
                            except:
                                continue
                elif "chuqD" in lineArr:
                    for i in lineArr:
                            try:
                                i=int(i)
                                i=str(i)
                                distance_ly = binary_to_decimal(i)
                                distance=ly_to_km(distance_ly)
                            except:
                                continue
            else:
                translatedLine = ""
                lineArr = line.strip().split(" ")
                for word in lineArr:
                    translatedWord = binarian_to_english(word)
                    translatedLine = translatedLine + str(translatedWord)

                    if (word != lineArr[len(lineArr) - 1]):
                        translatedLine = translatedLine + " "
                print(translatedLine)
                output.write(translatedLine + '\n')
    output.close()
with open(sys.argv[3]) as message:
    with open(output_file1, "w") as output1:
        for line in message:
            line = line.lower()
            lineArr1 = line.strip().split(" ")
            translatedLine1 = ""
            for word in lineArr1:
                translatedWord = ""
                try:
                   decimal_number = int(word)
                   binary_number = decimal_to_binary(decimal_number)
                   translatedWord = str(binary_number)
                except ValueError:
                    if word[len(word)-1] in punctuation_list:
                        word = word[:-1]
                    translatedWord = english_to_binarian(word)

                translatedLine1 = translatedLine1 + str(translatedWord)

                if (word != lineArr1[len(lineArr1) -1]):
                    translatedLine1 = translatedLine1 + " "
            print(translatedLine1)
            output1.write(translatedLine1 + '\n')
    output1.close()



with open(computation_file, "w") as computation:
    computation.write("Data about Binarian planet:" + '\n')
    computation.write("Distance from the Earth:" + str(distance) + " km" + '\n')
    computation.write("Planet temperature:" + str(temperateure) + " degrees Celsius" + '\n')
    computation.write("Orbital speed:" + str(speed)+ " km/s" + '\n')
print("Data about Binarian planet:")
print("Distance from the Earth:" + str(distance) + " km")
print("Planet temperature:" + str(temperateure) + " degrees Celsius")
print("Orbital speed:" + str(speed)+ " km/s")
