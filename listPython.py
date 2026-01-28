# a = [12,14,15,16]
# for i in range(len(a)):
#     print(a[i])
# for i in a:
#     print(i)R

#! Methods of list

# a.append(17) #? Last me jodo
# a.insert(1,13) #? Kisi bhi position per
# a.remove(15)#? remove kar dega 


# k = [-2,32,12,44,-12]
# for i in range(len(k)):
#     if k[i] >= 0:
#         print(k[i])
# for i in k:
#     if i < 0:
#         print(i)

#! Second largest value
l = [12,13,16,19,17]
largest = l[0]
secondLarest = l[0]

for i in range(len(l)):
    if l[i] > largest:
        secondLarest = largest 
        largest = l[i]
    elif l[i] > secondLarest:
        secondLarest = l[i]
 print(secondLarest, largest)



