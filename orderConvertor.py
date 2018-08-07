import sys, argparse, csv

def setColumn(included_cols, array):
    firstName = array[included_cols[0]]
    lastName = array[included_cols[1]]
    emailAddress = array[included_cols[2]]
    phoneNumber = array[included_cols[3]]

    return firstName, lastName, emailAddress, phoneNumber

def writeToCSV(csvFile, line):
    csvFile.write(line)
    csvFile.write('\n')


def productCodeProcess():
    pass

# command arguments
parser = argparse.ArgumentParser(description='csv to postgres',\
 fromfile_prefix_chars="@")
parser.add_argument('file', help='csv file to import', action='store')
args = parser.parse_args()
csv_file = args.file

print("debug")
new_csv_file = "C:\\Users\\OEM\\Desktop\\nzkwRebuild\\databaseTransfer\\newCustomer.csv" # need to be arguments

included_cols = [2, 3, 5, 8]
i = 0

# open csv file
with open(csv_file, 'r') as csvfile:


    # get number of columns
    for line in csvfile.readlines():
        array = line.split(',')
        firstName, lastName, emailAddress, phoneNumber = setColumn(included_cols, array)

        newCSVline = emailAddress + "," + firstName + "," + lastName + ",,,,,,,,,,,,,,,,"
        i += 1

        if (i == 1999):
            break

        with open(new_csv_file, "a") as csvFile:
            writeToCSV(csvFile, newCSVline)










