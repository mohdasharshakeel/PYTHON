numbers = [1,2,3,4,5]
numbers.append(6) # add 6 at the end of the list
numbers.insert(2,15) # add 15 at the index of 2
numbers.extend([9,10,11]) # add multiple element at last  [1, 2, 15, 3, 4, 5, 6, 9, 10, 11]
numbers.remove(5) # remove first occurence of 5
popped_item = numbers.pop(3) # isme se three nikal ke popped item me store kr dega 
index = numbers.index(6) # index of 6 is 4
count_5 = numbers.count(5)  # 0
numbers.sort() # sort in accending order
numbers.reverse() # decending order
new_num = numbers.copy() # create a copy of list
new_num.clear() # remove all the element form the list
print(numbers)
