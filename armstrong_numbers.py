def is_armstrong_number(number):
    tempnumber = number
    sum = 0
    digits = 0
    while (tempnumber!=0):
        tempnumber = tempnumber//10
        digits += 1
    temp1number = number
    while(temp1number!=0):
        rem = temp1number%10
        temp1number = temp1number//10
        sum = sum + (rem**digits)
    if sum == number:
        return True
    return False

print(is_armstrong_number(153))