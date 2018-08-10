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
new_csv_file = "C:\\Users\\OEM\\Desktop\\nzkwRebuild\\newOrder2.csv" # need to be arguments

included_cols = [2, 3, 5, 8]
i = 0

# open csv file
with open(csv_file, 'r') as csvfile:
    next(csvfile)
    # 43 columns : product code -37
    headerLineTradevine = "Order Reference,Order Grant Total,Customer First Name,Customer Last Name,Customer Email,Billing Address Line 1,Billing Address Line 2,Billing Address Line 3,Billing Address Town,Billing Address Post Code,Billing Address Region,Billing Address Country,Shipping Address Same As Billing,Shipping Address Line 1,Shipping Address Line 2,Shipping Address Line 3,Shipping Address Town,Shipping Address Post Code,Shipping Address Region,Shipping Address Country,Shipping Method,Requested Shipping Date,Order Shipping Amount,Order Shipping Description,Order Shipping Tax Percent,Order Shipping Tax Amount,Payment Method,Is Payment Received,Payment Reference,Is Manually Approved,Payment Terms,Public Notes,Private Notes,Is Tax Applicable,Order Discount Amount,Prices Tax Inclusive,Label List,Product Code,Quantity,Unit Price,Tax Code,Tax Percent,Tax Line Amount,Line Note"
    elements = headerLineTradevine.split(",")
    i = 0
    for element in elements:
        element += "[" + str(i) + "]"
        i += 1
        print(element)

    headerLineZencart = "Order ID,Customer Email,First Name,Last Name,Company,Delivery Street,Delivery Suburb,Delivery City,Delivery State,Delivery Post Code,Delivery Country,Ship Dest Type,Shipping Method,Shipping Total,Customers Telephone,Order Total,Order Date,Order Notes,Order Tax,Order Discount,Payment Method"
    print("-" * 40)

    elementsB = headerLineZencart.split(",")
    j = 0
    for element in elementsB:
        element += "[" + str(j) + "]"
        j += 1
        print(element)


    with open(new_csv_file, "a") as csvFile:
        writeToCSV(csvFile, headerLineTradevine)

    # get number of columns
    i = 0

    for line in csvfile.readlines():
        """array = line.split(',')
        firstName, lastName, emailAddress, phoneNumber = setColumn(included_cols, array)

        newCSVline = emailAddress + "," + firstName + "," + lastName + ",,,,,,,,,,,,,,,,"
        i += 1

        if (i == 1999):
            break

        with open(new_csv_file, "a") as csvFile:
            writeToCSV(csvFile, newCSVline)"""

        zencartArray = line.split(',')
        arrayTradevine = 43 * [""]

#------------------------------------------------------------------------
        # mapping zencart to tradevine
        arrayTradevine[0] = zencartArray[0]
        arrayTradevine[1] = zencartArray[15]
        arrayTradevine[2] = zencartArray[2]
        arrayTradevine[5] = zencartArray[5]
        arrayTradevine[8] = zencartArray[6]
        arrayTradevine[9] = zencartArray[9]
        arrayTradevine[11] = zencartArray[10]
        arrayTradevine[38] = zencartArray[21]
        arrayTradevine[39] = zencartArray[22]
        arrayTradevine[37] = zencartArray[24]
#-------------------------------------------------------------------------------------

        #------------------------------------------------------------------------------------------------
        # special process to get rid of trailing empty cells while leave the empty cells in between untouched
        for i in range(len(zencartArray)-1):
            if zencartArray[i] == '' and (zencartArray[i+1] == '' or zencartArray[i+1] == '\n'):
                zencartArray[i] = 'xxx'

        while 'xxx' in zencartArray:
            zencartArray.remove('xxx')

        if zencartArray[-1] == '':
            del zencartArray[-1]
        #------------------------------------------------------------------------------------------------

        product_number = int((len(zencartArray) - 20) / 5)
        line2Generate = product_number - 1

        print(arrayTradevine) # append to csv
        #---------------------------------------------------------
        # write line to csv file
        newTradevineLine = ""
        for i in range(len(arrayTradevine)):
            newTradevineLine += arrayTradevine[i]
            if i != len(arrayTradevine) - 1:
                newTradevineLine += ","

        with open(new_csv_file, "a") as csvFile:
            writeToCSV(csvFile, newTradevineLine)
        #---------------------------------------------------------

        for i in range(line2Generate):
            arrayTradevine = 43 * [""]

            # ------------------------------------------------------------------------
            # mapping zencart to tradevine
            arrayTradevine[0] = zencartArray[0]
            arrayTradevine[1] = zencartArray[15]
            arrayTradevine[2] = zencartArray[2]
            arrayTradevine[5] = zencartArray[5]
            arrayTradevine[8] = zencartArray[6]
            arrayTradevine[9] = zencartArray[9]
            arrayTradevine[11] = zencartArray[10]


            arrayTradevine[38] = zencartArray[26 + 5 * i]
            arrayTradevine[39] = zencartArray[27 + 5 * i]
            arrayTradevine[37] = zencartArray[29 + 5 * i]

            # -------------------------------------------------------------------------------------



            print(arrayTradevine) # append to csv
            # ---------------------------------------------------------
            # write line to csv file
            newTradevineLine = ""
            for i in range(len(arrayTradevine)):
                newTradevineLine += arrayTradevine[i]
                if i != len(arrayTradevine) - 1:
                    newTradevineLine += ","

            with open(new_csv_file, "a") as csvFile:
                writeToCSV(csvFile, newTradevineLine)
            # ---------------------------------------------------------




        pass










