code = input('[Enter]: ')
flag = 10
sum = 0
for i in code[:-1]:
    sum += int(i)*flag
    flag -= 1

if sum%11 >= 2:
    true_one = (code[:-1]+str(11-(sum%11)))
else:
    true_one = (code[:-1]+str(sum%11))

if true_one == code:
    print('True')
else:
    print("False")
