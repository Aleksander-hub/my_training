
def  get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if str_number or 1:
        return first

result = (get_multiplied_digits(40203))
print(result)
