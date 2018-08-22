def product_code_convertor(product_code_template, product_attributes):
    product_attributes_list = product_attributes.split('|')
    product_attributes_list.remove(' ')

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

        prefix = prefix + "-" + append_value

    print(prefix)

# size
def size_convertor(input):
    input_list = input.split(':')
    value = input_list[1].strip()
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
        output = "02D"
    elif value == '1/4':
        output = "04D"
    elif value == '3/8':
        output = "06D"
    elif value == '1/2':
        output = "08D"
    elif value == '3/4':
        output = "12D"
    elif value == '1':
        output = "16D"

    print(output)
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
    number = value.split()[0]

    if len(number) == 3:
        number = number[:-1]


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


    return output


# test
#  an_size_convertor("Options-AN Sizes: 12AN")
# # angles_convertor("Options-Angles: 120 Degree")
# #colours_convertor("Options-Colours: Red/Blue")

product_code_convertor("KWFF0209-XX-YY-ZZ", "Options-AN Sizes: 06AN | Options-Angles: 120 Degree | Options-Colours: Black | ")
product_code_convertor("KWFX725-XX", "Options-Sizes: 10AN | ")

npt_convertor("Options-NPT: 3/8' ")

