def create_phone_number(number):
    if type(number) == int and len(str(number)) == 10:
        string = str(number)

        phone_number = "(" + string[:3] + ") " + string[3:6] + "-" + string[6:]
        return phone_number