# todo: add full name
import os
from productCodeConvertor import *


def setColumn(included_cols, array):
    firstName = array[included_cols[0]]
    lastName = array[included_cols[1]]
    emailAddress = array[included_cols[2]]
    phoneNumber = array[included_cols[3]]

    return firstName, lastName, emailAddress, phoneNumber

def writeToCSV(csvFile, line):
    csvFile.write(line)
    csvFile.write('\n')

def shippingTotalConvertor(input):
    input = input.strip("\"")
    output = str(round(float(input) - float(input) * 3 / 23, 2))
    return output



def productCodeProcess():
    pass

def startConvertingCSV(csv_file):
    # command arguments
    # parser = argparse.ArgumentParser(description='csv to postgres',\
    #  fromfile_prefix_chars="@")
    # parser.add_argument('file', help='csv file to import', action='store')
    # args = parser.parse_args()
    # # csv_file = args.file
    #
    # print("debug")

    new_csv_file = os.path.dirname(csv_file) + "/TradevineOrder.csv"

    # new_csv_file = "C:\\Users\\OEM\\Desktop\\nzkwRebuild\\newOrder2.csv" # need to be arguments

    included_cols = [2, 3, 5, 8]
    i = 0

    # open csv file
    with open(csv_file, 'r') as csvfile:
        next(csvfile)
        # 43 columns : product code -37
        headerLineTradevine = "Order Reference,Order Grand Total,Customer First Name,Customer Last Name,Customer Email,Billing Address Line 1,Billing Address Line 2,Billing Address Line 3,Billing Address Town,Billing Address Post Code,Billing Address Region,Billing Address Country,Shipping Address Same As Billing,Shipping Address Line 1,Shipping Address Line 2,Shipping Address Line 3,Shipping Address Town,Shipping Address Post Code,Shipping Address Region,Shipping Address Country,Shipping Method,Requested Shipping Date,Order Shipping Amount,Order Shipping Description,Order Shipping Tax Percent,Order Shipping Tax Amount,Payment Method,Is Payment Received,Payment Reference,Is Manually Approved,Payment Terms,Public Notes,Private Notes,Is Tax Applicable,Order Discount Amount,Prices Tax Inclusive,Label List,Product Code,Quantity,Unit Price,Tax Code,Tax Percent,Tax Line Amount,Line Note"
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
            quantity_price_array = [] # order discount problem

            zencartArray = line.split(',')
            for i in range(len(zencartArray)):
                zencartArray[i] = zencartArray[i].strip("\"")
            arrayTradevine = 43 * [""]

    #------------------------------------------------------------------------
            # mapping zencart to tradevine
            arrayTradevine[0] = "nzkw-" + zencartArray[0]
            print(zencartArray[15])
            # try:
            #     arrayTradevine[1] = shippingTotalConvertor(zencartArray[15])
            # except:
            #     print("error line is " + zencartArray[15])

            # arrayTradevine[1] = shippingTotalConvertor(zencartArray[15]) toggle based on settings of website
            arrayTradevine[1] = zencartArray[15]
            arrayTradevine[3] = zencartArray[4]
            arrayTradevine[4] = zencartArray[1]
            arrayTradevine[2] = zencartArray[2] + " " + zencartArray[3]
            arrayTradevine[5] = zencartArray[5] + zencartArray[8]
            arrayTradevine[8] = zencartArray[6]
            arrayTradevine[9] = zencartArray[9]
            arrayTradevine[11] = zencartArray[10]
            arrayTradevine[12] = "Yes"


            region_town = zencartArray[7]
            arrayTradevine[8] = region_town
            arrayTradevine[10] = region_town


            # ----------------------------------------------------------------------------------------------------------
            # determine tax code based on country
            if arrayTradevine[11] == "New Zealand":
                arrayTradevine[40] = "GST"
                arrayTradevine[41] = "15"
                arrayTradevine[22] = shippingTotalConvertor(zencartArray[13])

            else:
                arrayTradevine[40] = "NONE"
                arrayTradevine[22] = zencartArray[13]
                # ----------------------------------------------------------------------------------------------------------

            paymentMethod = zencartArray[20]
            paymentMethod = paymentMethod.replace('"', '')

            print("delivery method is " + paymentMethod)  # delivery method

            if paymentMethod == "PayPal" or paymentMethod == "dps":
                arrayTradevine[27] = "Yes"
            else:
                arrayTradevine[27] = "No"

            if paymentMethod == 'PayPal' or paymentMethod == 'dps':
                arrayTradevine[26] = "PayPal"
            else:
                arrayTradevine[26] = "EFTPOS"

            quantity = zencartArray[21]
            arrayTradevine[38] = quantity
            arrayTradevine[39] = zencartArray[22]

            quantity_price_array.append(arrayTradevine[38])
            quantity_price_array.append(arrayTradevine[39])

            product_code_template = zencartArray[24]
            product_attribute = zencartArray[25]
            product_code = product_code_convertor(product_code_template, product_attribute)
            arrayTradevine[37] = product_code
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
                writeToCSV(csvFile, newTradevineLine + ",")
            #---------------------------------------------------------

            for i in range(line2Generate):
                arrayTradevine = 43 * [""]

                # ------------------------------------------------------------------------
                # mapping zencart to tradevine
                arrayTradevine[0] = "nzkw-" + zencartArray[0]
                arrayTradevine[3] = zencartArray[4]
                arrayTradevine[1] = zencartArray[15]
                arrayTradevine[4] = zencartArray[1]
                arrayTradevine[2] = zencartArray[2] + " " + zencartArray[3]
                arrayTradevine[5] = zencartArray[5] + zencartArray[8]
                arrayTradevine[8] = zencartArray[6]
                arrayTradevine[9] = zencartArray[9]
                arrayTradevine[11] = zencartArray[10] # country
                arrayTradevine[12] = "Yes"

                region_town = zencartArray[7]
                arrayTradevine[8] = region_town
                arrayTradevine[10] = region_town

                paymentMethod = zencartArray[20]
                paymentMethod = paymentMethod.replace('"', '')

                print("delivery method is " + paymentMethod) # delivery method

                if (paymentMethod == "PayPal" or paymentMethod == "dps"):
                    arrayTradevine[27] = "Yes"
                else:
                    arrayTradevine[27] = "No"

                if paymentMethod == 'PayPal':
                    arrayTradevine[26] = "PayPal"
                elif paymentMethod == 'dps':
                    arrayTradevine[26] = 'Credit Card'
                else:
                    arrayTradevine[26] = "EFTPOS"


    #----------------------------------------------------------------------------------------------------------
                # determine tax code based on country
                if arrayTradevine[11] == "New Zealand":
                    arrayTradevine[40] = "GST"
                    arrayTradevine[41] = "15"
                    arrayTradevine[22] = shippingTotalConvertor(zencartArray[13])
                else:
                    arrayTradevine[40] = "NONE"
                    arrayTradevine[22] = zencartArray[13]
    #----------------------------------------------------------------------------------------------------------
                quantity = zencartArray[26 + 5 * i]

                arrayTradevine[38] = zencartArray[26 + 5 * i]
                arrayTradevine[39] = zencartArray[27 + 5 * i]

                quantity_price_array.append(arrayTradevine[38])
                quantity_price_array.append(arrayTradevine[39])

                product_code_template = zencartArray[29 + 5 * i] # later use
                try:

                    product_attribute = zencartArray[30 + 5 * i]
                except:
                    product_attribute = ''
                product_attribute = product_attribute.strip("\n")


                product_code = product_code_convertor(product_code_template, product_attribute)
                arrayTradevine[37] = product_code


                #arrayTradevine[37] = "KWTB003BK"

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
                    writeToCSV(csvFile, newTradevineLine + ",")
                # ---------------------------------------------------------

            # for order discount -------------------------------------------------------------------------------------------------------------------------------------------------------
            print("--------------------------------------------------")
            print(quantity_price_array)
            print("--------------------------------------------------")
            shipping_amount = arrayTradevine[22]

            #sumvalue = sum([float(quantity_price_array[i]) * float(quantity_price_array[i+1]) for i in range(len(quantity_price_array) - 1) if i % 2 == 1])

            sumvalue = 0
            for i in range(0, len(quantity_price_array), +2):
                sumvalue += float(quantity_price_array[i]) * float(quantity_price_array[i+1])
            order_cal_total = (sumvalue + float(shipping_amount)) * 1.15

            order_discount = order_cal_total - float(arrayTradevine[1])
            order_discount = round(order_discount, 2)

            print("order discount is :")
            print(order_discount)
            # for order discount --------------------------------------------------------------------------------------------------------------------------------------------------------









