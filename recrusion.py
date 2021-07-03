def recur(num):
    if num ==1:
        return num
    else:
        return  num*recur(num-1)



num = int(input('enter the number'))
output = recur(num)
print(output)