names = ["abc","wer","tyu","fgh","bnm",56,89,23]
numbers = [2,4,6,8,3,9]
print((len(names)))
print((names))

numbers.sort()   #sort the list
print((numbers))

numbers.reverse()   #reverse the list
print((numbers))

print((numbers[1:]))
print((numbers[1:4]))

numbers.append(7) #add at the end
print(numbers)

numbers.insert(1,55) #insert 55 at 1 index
print(numbers)

numbers.remove(6)   #remove element
print(numbers)

numbers.pop()     #remove last element
print(numbers)

numbers[1] = 98   #add 98 at index 1
print(numbers)