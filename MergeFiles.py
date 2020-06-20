####################################################################################################
#   This program will merge any number user-specified files into a single file
#   User chooses files, user specifies result file name
#   Program opens each input file, writes it to the output file, and saves the output file in this directory
####################################################################################################

# Variables
files = ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt", "6.txt", "7.txt"]       # List of user-inputted file names
fileBreak = "\n"        # String to be used to separate different input files
outputFile = input("Enter output file name: ") + ".txt"     # Desired output file name
i = 0       # Loop counter for looping through all input files

# Let user pick files to be merged


# Loop through user specified files, adding each one to the output file
with open(outputFile, "w") as output:
    # Loop through all input files
    while i < len(files):
        # Open a single input file
        with open(files[i], "r") as inputFile:
            # Add contents of input file to output file
            for line in inputFile:
                output.write(line)
            # If there will be more content added, move to the next line
            if i + 1 < len(files):
                output.write(fileBreak)
        i += 1

# Print results
with open(outputFile, "r") as result:
    print(result.read())