#design a calculator which will correctly solve all problems except the following
#45+3=555 , 56*45=6447, 28/98=46 , 34-87=233

print("Enter First Number")
num1 = int(input())
print("Which Opertaion Do You Want")
opt = input()
print("Enter Your Second Number")
num2 = int(input())
if opt == "+":
    if num1== 45 and num2== 3:
        print("Your Answer Is","555")
    else:
        print("Your Answer Is",num1+num2)
if opt == "-":
    if num1== 34 and num2== 87:
        print("Your Answer Is","233")
    else:
        print("Your Answer Is",num1-num2)
if opt == "*":
    if num1 == 56 and num2 == 45:
         print("Your Answer Is", "6447")
    else:
         print("Your Answer Is", num1*num2)
if opt == "/":
    if num1 == 28 and num2 == 98:
         print("Your Answer Is", "46")
    else:
         print("Your Answer Is", num1/num2)
