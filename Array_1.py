'''
#WAP : create an array of 5 integers and display the array items.
Access individual element through indexes
'''

import array as arr

a=arr.array('i',[1,2,3,4,5])

for i in range(0,3):
    print(a[i])

print("===========")
for i in a:
    print(i)

# Append a new item to the end of the array.

a=arr.array("i",[1,3,9,2])
a.append(11)
print(a)

#Reverse the order of the items in the array.
a1=arr.array("i",[1,3,9,2])
a1.reverse()

print(str(a1))

#==============================
#get the number of occurrences of a specified element in an array
Ori_arr = arr.array('i',[1, 3, 5, 3, 7, 9, 3,3])
z = Ori_arr.count(3)
print(z)

# 9 : append items from a specified list.

num_list = [1, 2, 6, -8]
array_num = arr.array('i', [])
print("Items in the list: " + str(num_list))
print("Append items from the list: " ,array_num)
array_num.fromlist(num_list)

print("=======insert a new item before the second element in an existing array.=====")
# 10 . insert a new item before the second element in an existing array.
num_list = [1, 2, 6, -8]
'============array int,pass the list =================='
covt_to_array = arr.array('i',num_list)
print(str(covt_to_array))
covt_to_array.insert(1,4)
print(str(covt_to_array))

print("==============remove a specified item using the index from an array======")
covt_to_array = arr.array('i',num_list)
covt_to_array.pop(1)
print(str(covt_to_array))
num_list=covt_to_array.tolist()
print(num_list)
print("13 .==============remove the first occurrence of a specified element from an array======")
