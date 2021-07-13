
print("1. =============Displaying the Keys Alphabetically=============")
key_value={}
key_value[2] = '64'
key_value[1] = '69'
key_value[4] = '23'
key_value[5] = '65'
key_value[6] = '34'
key_value[3] = '76'

print(key_value)

print(sorted(key_value))

''''###########################################################################################################'''
print("2. ==================Sorting the Keys and Values in Alphabetical Order using the Key.====================")
''''###########################################################################################################'''
key_value={}
key_value[2] = '64'
key_value[1] = '69'
key_value[4] = '23'
key_value[5] = '65'
key_value[6] = '34'
key_value[3] = '76'

for i in sorted(key_value):
    print((i, key_value[i]))

''''###########################################################################################################'''
print("3. Sorting the Keys and Values in alphabetical using the value")
''''###########################################################################################################'''
key_value={}
key_value[2] = '64'
key_value[1] = '69'
key_value[4] = '23'
key_value[5] = '65'
key_value[6] = '34'
key_value[3] = '76'

print(key_value)
#1 Way
print(sorted(key_value.items(),key=lambda kv:kv[1]))
#2nd Way
print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))

''''###########################################################################################################'''
print("4. Handling missing keys in Python dictionaries")
''''###########################################################################################################'''

d = { 'a' : 1 , 'b' : 2 }

print(d['a'])

try:
    print(d['c'])
except KeyError:
    print("key is not availble")


''''###########################################################################################################'''
print("5. ========Handling missing keys in Python dictionaries using get=======")
''''###########################################################################################################'''

d1 = { 'a' : 1 , 'b' : 2 }

print(d1.get('c',"key not found"))

dict = {}

''''###########################################################################################################'''
print("6. ========How to create a dictionary where a key is formed using inputs?=======")
''''###########################################################################################################'''

x,y,z=10,20,30

dict[x,y,z]=0

print(dict)
''''###########################################################################################################'''
print("7. ========Let’s get access to the keys.=======")
''''###########################################################################################################'''

#Method 1
places_dict = {("19.07'53.2", "72.54'51.0"):"Mumbai",("28.33'34.1", "77.06'16.6"):"Delhi"}
places_dict_keys=[]
places=[]
values1=[]
for ele in places_dict:
    places.append(ele)
    values1.append(places_dict[ele])

print(places)
print(values1)

#Method:2
places_dict_keys=map(lambda dict_ele:list(dict_ele),places_dict)

l1=(list(places_dict_keys))
print(l1)
for ele in l1:
    print(ele)

''''###########################################################################################################'''
print("8. write a Python program to find the sum of all Items in the dictionary.")
''''###########################################################################################################'''
#method 1
Input={'a': 100, 'b':200, 'c':300}

value_l=Input.values()

print(sum(value_l))

Input={'x': 25, 'y':18, 'z':45}
print(Input['x'])

#Method 2:
sum1=0
for ele in Input:
    sum1=sum1+Input[ele]

print(sum1)
''''###########################################################################################################'''
print("9. write a Python program to find Size of dict")
''''###########################################################################################################'''

print(Input.__sizeof__())

''''###########################################################################################################'''
print("10. Sort by age")
''''###########################################################################################################'''

from operator import itemgetter,attrgetter

lis = [{ "name" : "Arora", "age" : 20}, { "name" : "Manjeet", "age" : 20 },{ "name" : "Nikhil" , "age" : 19 }]

#Sort by age
print(sorted(lis,key=lambda kv:(kv['age'])))

#Sort by age and name
print(sorted(lis,key=lambda kv:(kv['age'],['name'])))

#Sort by age using itemgetter

print(sorted(lis,key=itemgetter('age')))

#print(sorted(lis,key=attrgetter('name')))

print(sorted(lis,key=itemgetter('age','name')))
''''###########################################################################################################'''
print("11. Merge two dict")
''''###########################################################################################################'''
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'a': 4}

dict1.update(dict2)
print(dict1)

print({**dict1,**dict2})

''''###########################################################################################################'''
print("12. Grade Calculations")
''''###########################################################################################################'''
'''
1. score >= 90 : "A"
2. score >= 80 : "B"
3. score >= 70 : "C"
4. score >= 60 : "D"
'''
#l1=[{'name':'neha','age':20},{'name':'rohit','age':30}]
#print(l1[0]['name'])

jack = { "name":"Jack","assignment" : [80, 50, 40, 20],"test" : [75, 75],"lab" : [78.20, 77.20]}
james = { "name":"James","assignment" : [82, 56, 44, 30],"test" : [80, 80],"lab" : [67.90, 78.72]}
dylan = { "name" : "Dylan Rhodes","assignment" : [77, 82, 23, 39],"test" : [78, 77],"lab" : [80, 80]}
jess = {"name": "Jessica Stone","assignment": [67, 55, 77, 21],"test": [40, 50], "lab": [69, 44.56]}
tom = {"name": "Tom Hanks","assignment": [29, 89, 60, 56],"test": [65, 56],"lab": [50, 40.6]}


l1=[james,dylan,jess,tom]

def get_avg(mask_list):
    total_sum=sum(mask_list)
    return total_sum/len(mask_list)


for i in l1:
    print(i['name'])
    Total_Avg_num=get_avg(i['assignment'])
    Total_Avg_test_num=get_avg(i['test'])
    Total_Avg_lab_num=get_avg(i['lab'])
    print("Total_Avg_num : ",Total_Avg_num,"Total_Avg_test_num : ", Total_Avg_test_num ,"Total_Avg_lab_num : ",Total_Avg_lab_num)

''''###########################################################################################################'''
print("13 . Insertion at the beginning in OrderedDict")
''''###########################################################################################################'''
#Method 1
original_dict = {'a':1, 'b':2}
original_dict['c']=3
print(original_dict)

#Method2:
original_dict = {'a':1, 'b':2}
dic_to_added={'c':3}

original_dict.update(dic_to_added)
print(original_dict)
original_dict

''''###########################################################################################################'''
print("13 . Insertion at the beginning in OrderedDict")
''''###########################################################################################################'''
from collections import OrderedDict
od = OrderedDict()
od['a']=1
od['b']=2
od['c']=3

od['h']=4
print(od)

od.move_to_end('c',False)
print(od)

''''###########################################################################################################'''
print("14 . Check order of character in string using OrderedDict( )")
''''###########################################################################################################'''

input1 = 'engineers rock'
input2 = 'er'

print(input1.find(input2))


print(input1.count(input2))

''''###########################################################################################################'''
print("15.Find common elements in three sorted arrays by dictionary intersection")
''''###########################################################################################################'''
from collections import Counter
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

commonEle=[80,20]

print(set(ar1))
print(set(ar1)&set(ar2)&set(ar3))

print(set(ar1).intersection(set(ar2)))

ar1 = Counter(ar1)
ar2 = Counter(ar2)
ar3 = Counter(ar3)


''''###########################################################################################################'''
print("16.Dictionary and counter in Python to find winner of election")
''''###########################################################################################################'''

vote = ["john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"]

vote_dict=(Counter(vote))
print(vote_dict)
vote_dict.keys()
vote_dict.values()
toFind=max(vote_dict.values())
l1=[]
for k,v in vote_dict.items():
    if v==toFind:
        l1.append(k)


print(l1)
print(min(l1))

''''###########################################################################################################'''
print("17.Key with maximum unique values")
''''###########################################################################################################'''
from collections import Counter
test_dict = {'Gfg' : [5, 7, 9, 4, 0], 'is' : [6, 7, 4, 3, 3], 'Best' : [9, 9, 6, 5, 5]}

new_dict={}

for k,v in test_dict.items():
        temp_len=len(Counter(v))
        new_dict[k]=temp_len

print(new_dict)
new_value=max(new_dict.values())


for k,v in new_dict.items():
    if new_value==v:
        found_key=k
        break

print("key is : ",found_key)

print(new_dict.get(found_key))
print(new_dict[found_key])
''''###########################################################################################################'''
print("17.Key with maximum unique values using set method")
''''###########################################################################################################'''
from collections import Counter
test_dict = {'Gfg' : [5, 7, 9, 4, 0], 'is' : [6, 7, 4, 3, 3], 'Best' : [9, 9, 6, 5, 5]}

new_dict={}

for k,v in test_dict.items():
        temp_len=len(set(v))
        new_dict[k]=temp_len

print(new_dict)
new_value=max(new_dict.values())


for k,v in new_dict.items():
    if new_value==v:
        found_key=k
        break

print("key is : ",found_key)

print(new_dict.get(found_key))
print(new_dict[found_key])

''''###########################################################################################################'''
print("18.Find all duplicate characters in string")
''''###########################################################################################################'''
from collections import Counter

Input1="geeksforgeeeks"

Dict1=Counter(Input1)
found_key=[]
item_dict=Dict1.items()
for k,v in Dict1.items():
    if v>1:
        found_key.append(k)

print(' '.join(found_key))


''''###########################################################################################################'''
print("19. K’th Non-repeating Character in Python using List Comprehension and OrderedDict")
''''###########################################################################################################'''
from collections import Counter

str = "geeksforgeeks"
found_key =[]
dict1=Counter(str)

for key,value in dict1.items():
    if value==1:
        found_key.append(key)


print(found_key)

found_key=[key for key,value in dict1.items() if value==1]
print(list(found_key))


''''###########################################################################################################'''
print("20. Replace String by Kth Dictionary value")
''''###########################################################################################################'''

#Method 1:
test_list = ["Gfg", "is", "Best"]
subs_dict = {"Gfg" : [5, 6, 7], "is" : [7, 4, 2]}
dummy_list=[]
#[5,7,"best"]
i=0
value1=list(subs_dict.values())
keys1=list(subs_dict.keys())
print(len(test_list))
#for k,v in subs_dict.items():
for ele in range(len(test_list)):
    try:
        if keys1[i]==test_list[ele]:
            dummy_list.append(value1[i][2])
        else:
            dummy_list.append(test_list[ele])
    except IndexError:
        dummy_list.append(test_list[ele])

    i=i+1

print(dummy_list)

''''###########################################################################################################'''
print("21. Ways to remove a key from dictionary")
''''###########################################################################################################'''
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
new_dict={}
#del test_dict['Mani']
'''
print(test_dict)
test_dict.pop('Mani')
print(test_dict)
new_dict=test_dict.pop('Mani',"No key found")
print(new_dict)

for k,v in test_dict.items():
    if k!= "Mani":
        new_dict[k]=v
print(new_dict)
'''
#Method 2: Use of dict
new_dict={k:v for k,v in test_dict.items() if k!="Mani"}
print(new_dict)

#filter(lambda k,v:k,v if k!="Mani" else '',test_dict.items())


''''###########################################################################################################'''
print("22. Replace words from Dictionary")
''''###########################################################################################################'''
test_str = "geekforgeeks best for geeks"
repl_dict = {"geeks" : "all CS aspirants","best":"Neha"}

dict_keys=repl_dict.keys()
newStr=[]

for ele in test_str.split(" "):
    #if ele in dict_keys:
        newStr.append(repl_dict.get(ele,ele))
    #else:
    #    newStr.append(ele)

print(' '.join(newStr))


print(repl_dict.get('rohit','rooohit'))

res=[repl_dict.get(ele,ele) for ele in test_str.split(" ")]
print(res)
''''###########################################################################################################'''
print("23. Remove Dictionary Key Words")
''''###########################################################################################################'''
test_str = 'gfg is best for geeks'
test_dict = {'geeks': 1, 'best': 6}
new_dict=[]
#The string after replace : gfg is  for

l1=test_str.split(" ")

for ele in l1:
    if ele not in test_dict.keys():
        new_dict.append(ele)

print(" ".join(new_dict))


res=[ele if ele not in test_dict.keys() else '' for ele in l1]
print(" ".join(res))
''''###########################################################################################################'''
print("24. Remove all duplicates words from a given sentence")
''''###########################################################################################################'''

#remove duplicate word
input1 = "Geeks for Geeks"
input1="Python is great and Java is also great"

l1=input1.split(" ")
print(l1)
l2=[]
#way1
for ele in l1:
    if ele not in l2:
        l2.append(ele)
print(" ".join(l2))

#way2
l2=[]

l2=[ele if ele not in l2 else '' for ele in input1.split(" ")]
print(list(l2))

''''###########################################################################################################'''
print("25. Remove duplicate values across Dictionary Values")
''''###########################################################################################################'''
from collections import defaultdict
#test_dict = {'Manjeet' : [1, 4, 5, 6],'Akash' : [1, 8, 9],'Nikhil': [10, 22, 4],'Akshat': [5, 11, 22]}
#test_dict = {"Manjeet": [1], "Akash": [1, 8, 9]}
test_dict = {"Manjeet": [1, 1, 1], "Akash": [1, 1, 1]}

l2=[]
d2 = defaultdict(list)

value1=test_dict.values()

keys1=test_dict.keys()

print(value1)
print(keys1)
cnt=Counter()

for ele in value1:
    cnt.update(ele)

print(cnt)

for k,v in cnt.items():
    if v==1:
        l2.append(k)
print(l2)
key_list=[]
for ele in l2:
    key_reset=0
    key_list = []
    for val_dict in value1:
        key_to_add=(list(keys1)[key_reset])
        if ele in val_dict:
            key_list.append(ele)
            #d2[key_to_add]=key_list
            d2[key_to_add].extend(key_list)
        else:
            key_reset=key_reset+1
            d2[key_to_add].extend(key_list)
print(d2)

''''###########################################################################################################'''
print("26. find mirror characters in a string")
''''###########################################################################################################'''
import string
l2=[]
for i in string.ascii_lowercase:
    l2.append(i)

l3=l2[::-1]

print(l3)
print(l2)

input1="paradox"
#output1="paizwlc"
N=3
l4=[]
for i in range(len(input1)):
    if i>=(N-1):
        #print(input1[i])
        print(l2.index(input1[i]))
        print(l3[l2.index(input1[i])])
        l4.extend(l3[l2.index(input1[i])])
        print(l4)

print(input1[0:N]+''.join(l4))

''''###########################################################################################################'''
print("27. find mirror characters in a string")
''''###########################################################################################################'''

#way 1
Input =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
dict1=Counter(Input)
print(dict1)

#way 2
dict={}
count=1
for i in Input:
    if i in dict:
        dict[i]=dict[i]+count
    else:
        dict[i] = count

print(dict)

''''###########################################################################################################'''
print("28. Dictionary Values Mean")
''''###########################################################################################################'''
test_dict = {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4}
value=test_dict.values()
keys1=test_dict.keys()
print(keys1)
print(sum(value)/len(keys1))

''''###########################################################################################################'''
print("29. Python counter and dictionary intersection example (Make a string using deletion and rearrangement")
''''###########################################################################################################'''
#1 Way
s1 = "Hello"
s2 = "dnaKfhelddf"

bool=True

for i in s1:
    if not i in s2:
        bool=False
        print("No possible")
        break

if bool==True:
    print("Possible")

#2Way
dict1=Counter(s1)
dict2=Counter(s2)

print(dict1)
print(dict2)

result=dict1 & dict2

print(result)
''''###########################################################################################################'''
print("Python dictionary, set and counter to check if frequencies can become same")
''''###########################################################################################################'''
input1="xxxxyyzz"

dict1=Counter(input1)
print(dict1)
#get the value 1
for k,v in dict1.items():
   # print(k,v)
    if v==1:
        print(k,"can be removed")
        break
    else:
        print("no")

same = list(set(dict1.values()))
print(same)

''''###########################################################################################################'''
print("Scraping And Finding Ordered Words In A Dictionary using Python")
''''###########################################################################################################'''
S1="abbott"
dict1={}
a_z=string.ascii_lowercase
print(list(S1))

for ele in (S1):
    dict1[ele]=a_z.index((ele))

print(dict1)
# now check if values are in increasing form

values1=list(dict1.values())
keys1=list(dict1.keys())

i=0
for ele in values1:
    if i<len(values1)-1:
        i=i+1
    next_ele=values1[i]
    if ele<=next_ele:
        bool=True
    else:
        bool=False
        break

if bool==True:
    print("Yes")
else:
    print("No")

''''###########################################################################################################'''
print("Possible Words using given characters in Python")
''''###########################################################################################################'''

Dict = ['goo', 'bat', 'me', 'eat', 'goala', 'boy', 'run']
arr = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
combinae_word=""
for ele in Dict:
    combinae_word=""
    for i in ele:
        if i in arr:
            combinae_word=combinae_word+i
        if combinae_word==ele:
            print(ele)

''''###########################################################################################################'''
print("Possible Words using given characters in Python - 2 thinking")
''''###########################################################################################################'''
Dict = ['goo', 'bat', 'me', 'eat', 'goala', 'boy', 'run']
arr = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
dict1={}

count_arr_value=(Counter(arr))
print(count_arr_value)

def countWord(word):
    for ele in Dict:
        for i in ele:
            dict1[i]=dict1.get(i,0)+1
    return dict1

flag=1
for word in Dict:
    flag=1
    dict1=countWord(word)
    for key in dict1:
        if key not in arr:
            flag=0
        else:
            if arr.count(key)!=dict1[key]:
                flag=0


    l3.append(word)

print(l3)
''''###########################################################################################################'''
print("Possible Words using given characters in Python - 2 thinking")
''''###########################################################################################################'''








''''###########################################################################################################'''
print("Maximum record value key in dictionary")
''''###########################################################################################################'''
test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
             'is' : {'Manjeet' : 8, 'Himani' : 9},
             'best' : {'Manjeet' : 10, 'Himani' : 15}}

key_to_get='Himani'

print(test_dict.keys())
value_l1=(list(test_dict.values()))

print(value_l1)

i=0
dict1={}
for k,v in test_dict.items():
    print(k,v)
    for sk,sv in v.items():
        if sk=='Himani':
            dict1[k]=sv

max_value=max(dict1.values())

for k,v in dict1.items():
    if v==max_value:
        print(k)


key = 'Himani'
res = None
res_max = 0
for sub in test_dict:
    if test_dict[sub]['Himani']>res_max:
        res_max = test_dict[sub][key]
        res = sub
''''###########################################################################################################'''
print("Extract values of Particular Key in Nested Values")
''''###########################################################################################################'''

test_dict = {'Gfg' : {"a" : 7, "b" : 9, "c" : 12},'is' : {"a" : 15, "b" : 19, "c" : 20},'best' :{"a" : 5, "b" : 10, "c" : 2}}

temp='b'
l3=[]
#print(test_dict['Gfg']["b"])

l3=[test_dict[key]['b'] for key in test_dict]
    #l3.append(test_dict[key]['b'])
print(sorted(l3))
l3=[]

for key,value in test_dict.items():
    if 'c' in value:
        l3.append(value['c'])


l3=[value['c'] for key,value in test_dict.items() if 'c' in value]
print(l3)

