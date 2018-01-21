# This program reads a provided message from a user provided file. It reads
# the cipher and rotates each character, providing the 25 possible variations
# of the message. This file assumes that only capital letters, spaces and
# newlines are used. It then saves this to a user provided output file.

# Create an empty string which will be used to store each iteration of our cipher
s = ""

# Get the Input and Output Files from the user
filetoread = input("Input File -Message to Encrypt/Decrypt-): ")
filetowrite = input("Output File: ")

# Open a file to save the results
with open(filetowrite, 'w') as f1:
    # Open the file to read from
    with open(filetoread, 'r') as f2:
        read_data = f2.read()
        # Iterate through the alphabet
        for x in range(0,25):
            f1.write('Rotation number:' + str(x + 1) + '\n')
            # For each of the characters in our text file
            for char in read_data:
                # Rotate the character, if it's Z, start over at A
                if(char != ' ' and char != '\n'):
                    y = ord(char)
                    if(y < 90):
                        y = y + 1
                    else:
                        y = 65
                    s += chr(y)
                # If the character is a space, print a space
                elif(char == ' '):
                    s += ' '
                # If the character is a newline, print a newline
                else:
                    s += '\n'
            f1.write(s + '\n\n')
            # Update the cipher text to the current letter set
            read_data = s
            s = ""
    f2.close()
f1.close()
