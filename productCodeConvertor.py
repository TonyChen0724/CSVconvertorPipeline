def product_code_convertor(product_code_template, product_attributes):
    product_attributes.strip("\"")
    product_attributes.strip("\n")

    if product_code_template == '':
        return "ERROR:No ProductCode"

    if product_attributes == '' or product_attributes == '\n' or product_attributes == '"':
        return product_code_template


    product_attributes_list = product_attributes.split('|')
    try:
        product_attributes_list = product_attributes_list[:-1]
    except:
        pass

    template_part_list = product_code_template.split('-')
    prefix = template_part_list[0]

    for i in range(len(product_attributes_list)):
        product_attribute_item = product_attributes_list[i]
        attribute_type = product_attribute_item.split(":")[0].strip()
        append_value = ""
        if attribute_type == 'Options-AN Sizes':
            append_value = an_size_convertor(product_attribute_item)
        elif attribute_type == 'Options-Angles':
            append_value = angles_convertor(product_attribute_item)
        elif attribute_type == 'Options-Colours':
            append_value = colours_convertor(product_attribute_item)
        elif attribute_type == 'Options-Sizes':
            append_value = size_convertor(product_attribute_item)
        elif attribute_type == 'Options-NPT':
            append_value = npt_convertor(product_attribute_item + " ")
        elif attribute_type == 'Oil Cooler Options':
            append_value = oil_cooler_option_convertor(product_attribute_item)
        elif attribute_type == 'Dimension':
            append_value = dimension_convertor(product_attribute_item)
        elif attribute_type == 'Banjo sizes':
            append_value = banjoSize_convertor(product_attribute_item)
        elif attribute_type == 'Hose Dimensions':
            append_value = hose_dimension_convertor(product_attribute_item)
        elif attribute_type == 'Options-Metric':
            append_value = options_metric_convertor(product_attribute_item)
        elif attribute_type == 'Left / Right':
            append_value = leftRight_convertor(product_attribute_item)
        elif attribute_type == 'Gloves sizes':
            append_value = glove_size_convertor(product_attribute_item)
        elif attribute_type == 'Glove colours':
            append_value = colours_convertor(product_attribute_item)
        elif attribute_type == 'NPT to Barb':
            append_value = npt_to_barb_convertor(product_attribute_item)
        elif attribute_type == 'Alloy Spanner':
            append_value = alloy_spanner_convertor(product_attribute_item)

        if "*" in product_code_template:
            template_components = product_code_template.split('*')
            while '' in template_components:
                template_components.remove('')
            prefix = template_components[0] + append_value + template_components[1]

        else:
            prefix = prefix + append_value

    print(prefix)
    return prefix

# alloy spanner
def alloy_spanner_convertor(input):
    res = ""
    input_list = input.split(':')
    spanners = input_list[1].split('-')
    for spanner in spanners:
        res += spanner
    return res.upper()



# NPT to Barb
def npt_to_barb_convertor(input):
    input_list = input.split('(')
    number = input_list[1][:-3]
    if len(number) == 1:
        number = "0" + number
    return number




# Gloves sizes

def glove_size_convertor(input):
    input_list = input.split(':')
    res = input_list[1]
    return res



# hose dimension
def hose_dimension_convertor(input):
    input_list = input.split('(')
    value = input_list[1][:-4]
    return value


# Left / Right
def leftRight_convertor(input):
    input_list = input.split(':')
    value = input_list[1][1:]
    value = value.strip()

    if value == 'Left':
        res = 'L'
    else:
        res = 'R'

    return res


# options_metric
def options_metric_convertor(input):
    input_list = input.split(':')
    values = input_list[1].split('x')
    value1 = values[0].strip()
    value2 = str(float(values[1][:-1]) * 100).replace('0', '')

    value = (value1 + value2)[:-1]
    return value


# banjo sizes
def banjoSize_convertor(input):
    input_list = input.split(' ')
    value = input_list[2].strip()
    value = value.replace('M', '')
    appendVal = value
    return appendVal


# Dimension
def dimension_convertor(input):
    input_list = input.split(' ')
    value = input_list[2].strip()
    value = value.strip('(')
    value = value.strip(')')
    value = value.replace('m', '')

    value_pair = value.split('-')
    appendVal = value_pair[0] + value_pair[1]
    return appendVal

    # if len(number) == 1:
    #     number = "0" + number

    # return number

dimension_convertor("Dimension: 2'~2-1/2' (51mm-64mm) | ")


# Oil Cooler Options
def oil_cooler_option_convertor(input):
    input_list = input.split(':')
    value = input_list[1].strip()
    number = value.split(" ")[0]

    if len(number) == 1:
        number = "0" + number

    return number


# size
def size_convertor(input):


    input_list = input.split(':')
    value = input_list[1].strip()

    valuesplict_space = value.split(' ')

    # 10 Row
    if len(valuesplict_space) == 2:
        return valuesplict_space[0]

    number = value[:-2]

    if len(number) == 1:
        number = "0" + number

    return number

# npt : basic npt convertor, still need improvement
def npt_convertor(input):
    input_list = input.split(':')
    value = input_list[1].strip()[:-1]

    output = ""
    if value == '1/8':
        output = "02"
    elif value == '1/4':
        output = "03"
    elif value == '3/8':
        output = "04"
    elif value == '1/2':
        output = "05"
    elif value == '3/4':
        output = "06"
    elif value == '1':
        output = "16D"

    return output


# AN size
def an_size_convertor(input):
    input_list = input.split(':')
    value = input_list[1].strip()
    number = value[:-2]

    if len(number) == 1:
        number = "0" + number

    return number


# angle
def angles_convertor(input):
    input_list = input.split(':')
    value = input_list[1].strip()
    if "Straight" in value:
        number = value.split()[1]
    else:
        number = value.split()[0]

    if len(number) == 3:
        number = number[:-1]
    if len(number) == 1:
        number = "0" + number


    return number

# color
def colours_convertor(input):
    input_list = input.split(':')
    value = input_list[1].strip()

    output = ""
    if value == 'Black':
        output = "BK"
    elif value == 'Red/Blue':
        output = "RB"
    elif value == 'Silver':
        output = 'SL'
    elif value == 'Blue':
        output = 'BL'


    return output


# test
#  an_size_convertor("Options-AN Sizes: 12AN")
# # angles_convertor("Options-Angles: 120 Degree")
# #colours_convertor("Options-Colours: Red/Blue")

# product_code_convertor("KWFF0209-XX-YY-ZZ", "Options-AN Sizes: 06AN | Options-Angles: 120 Degree | Options-Colours: Black | ")
# product_code_convertor("KWFX725-XX", "Options-Sizes: 10AN | ")
# product_code_convertor("KWFAN816-XX-YY-ZZ", "Options-AN Sizes: 10AN | Options-NPT: 3/8' | Options-Colours: Black | ")


# while (True):
#     template = input("Please input the product code template: ")
#
#     attribute = input("Please input the product attribute: ")
#
#     product_code_convertor(template, attribute)




