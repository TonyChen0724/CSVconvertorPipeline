def product_code_convertor(product_code_template, product_attributes):
    product_attributes_list = product_attributes.split('|')
    product_attributes_list.remove(' ')

    print()


# AN size
def an_size_convertor(input):
    input_list = input.split(':')
    value = input_list[1].strip()
    number = value[:-2]

    if len(number) == 1:
        number = "0" + number

    print(number)

    return number


# angle
def angles_convertor(input):
    input_list = input.split(':')
    value = input_list[1].strip()
    number = value.split()[0]

    if len(number) == 3:
        number = number[:-1]

    print(number)

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





    print(output)

    return output


# test
product_code_convertor("KWFF0209-XX-YY-ZZ", "Options-AN Sizes: 06AN | Options-Angles: 120 Degree | Options-Colours: Black | ")
# an_size_convertor("Options-AN Sizes: 12AN")
# angles_convertor("Options-Angles: 120 Degree")
colours_convertor("Options-Colours: Red/Blue")