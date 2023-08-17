def calc(num1, num2, num3):
    if num2 == 0:
        ans = num1+num3
    elif num2 == 1:
        ans = num1-num3
    elif num2 == 2:
        ans = num1*num3
    elif num2 == 3:
        ans = num1/num3
    else:
        ans = num1 % num3
    return ans


testcase = int(input("number of test_case"))
while testcase != 0:
    testcase -= 1
    num1 = int(input("first number---->"))
    ope_num = int(input("operation number from(0,1,2,3,4)--->(+,-,*,/,%)"))
    num3 = int(input("second number---->"))
    if ope_num > 4:
        print("operation not found")
        continue
    elif ope_num == 3 and num3 == 0:
        print("You can't divide by zero")
    elif ope_num >= 0 or ope_num <= 4:
        print(calc(num1, ope_num, num3))

print("thx :)")
