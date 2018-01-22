# This is a simple frequency analysis program to determine the number
# of occurences of each letter in a file. This program assumes that the
# user will only type files storing text with capital letters, spaces, and
# newline characters.

# Create a dictionary to store the alphabet with a count of each letter
alphabet = {
    "A" : 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0, "G" : 0, "H" : 0,
    "I" : 0, "J" : 0, "K" : 0, "L" : 0, "M" : 0, "N" : 0, "O" : 0, "P" : 0,
    "Q" : 0, "R" : 0, "S" : 0, "T" : 0, "U" : 0, "V" : 0, "W" : 0, "X" : 0,
    "Y" : 0, "Z" : 0,
}

# Create an empty array to store filenames
files = [];

answer = "";
count = 0;
# Prompt the user for files to analyze until they type done
while (answer != 'done'):
    answer = input("Name of Text File " + str(count + 1) +
                    "(or type 'done' when finished): ")
    if(answer != 'done'):
        files.append(answer)
        count += 1

# Open and read each file, count the number of letters in the file
for y in range(0, count):
    with open(files[y], 'r') as f1:
        read_data = f1.read()
        for letter in read_data:
            if(letter != " " and letter != "\n"):
                alphabet[letter] += 1
    f1.close()

# Write the frequency of each letter into the specified output file
with open(input("Output File Name (.txt file): "), 'w') as f2:
    for letter in alphabet:
        f2.write(letter + ': ' + str(alphabet[letter]) + '\n')
f2.close()
