###########################################################
print("Create Nested Dictionary using given List")
###########################################################
test_dict = {"Gfg": 4, "best": 9}
test_list = [8, 2]
#{8: {‘Gfg’: 4}, 2: {‘best’: 9}}


print(dict(zip(test_list, test_dict)))
print(dict(zip(test_list, test_dict.items())))
res=dict()
for ele, val in zip(test_list, test_dict.items()):
    res[ele]=dict({val})
print(res)

#One Line Solution
res={ele:dict({val}) for ele, val in zip(test_list, test_dict.items())}

print(res)

###########################################################
print("Swapping Hierarchy in Nested Dictionaries")
###########################################################

test_dict = {"Gfg": { "a" : [1, 3, 7, 8], "b" : [4, 9], "c" : [0, 7]}}
#{‘c’: {‘Gfg’: [0, 7]}, ‘b’: {‘Gfg’: [4, 9]}, ‘a’: {‘Gfg’: [1, 3, 7, 8]}}
print(test_dict.items())
res=dict()
for key,value in test_dict.items():
    print(key,value)
    for key1,value1 in value.items():
        temp=dict()
        temp[key]=value1
        res[key1]=temp

print(res)

###########################################################
print(" Inversion in nested dictionary")
###########################################################
#test_dict ={'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {}}}}

#test_dict = {'a' : {"b" : {}},'d' : {"e" : {}},'f' : {"g" : {}}}
#{‘b’: {‘a’: {}}, ‘e’: {‘d’: {}}, ‘g’: {‘f’: {}}
#{'c': {'b': {'a': {}}}, 'e': {'d': {}}, 'h': {'g': {'f': {}}}}
test_dict = {'a' : {'b' : { 'c' : {}}}}

final_res=dict()
outside_res=dict()
inside_res1=dict()
for key1,value1 in test_dict.items():
    print(key1,value1)
    for key2,value2 in value1.items():
        print(key2,value2)
        if len(value2) == 0:
             inside_res1[key1]=value2
             final_res[key2]=inside_res1
             inside_res1=dict()
            #print()
        else:
            for key3,value3 in value2.items():
                print(key3,value3)
                inside_res1[key1]=value3
                outside_res[key2]=inside_res1
                final_res[key3]=outside_res
                outside_res = dict()
                inside_res1 = dict()

print(final_res)

###########################################################
print("Reverse Dictionary Keys Order")
###########################################################

test_dict ={'is': 2, 'best': 5, 'gfg': 4}
#OrderedDict([(‘gfg’, 4), (‘best’, 5), (‘is’, 2)])
l1=(list(test_dict.items()))
print(dict(l1[::-1]))

###########################################################
print("Extract Key’s Value, if Key Present in List and Dictionary")
###########################################################

test_list = ['Gfg', 'is', 'Good', 'for', 'Geeks']
test_dict = {'Gfg' : 5, 'Best' : 6}

for ele in range(0,len(test_list)-1):
    if test_list[ele] in test_list and test_list[ele] in test_dict:
        print(test_dict[test_list[ele]])

#One line code
res=[test_dict[test_list[ele]]  for ele in range(0,len(test_list)-1) if test_list[ele] in test_list and test_list[ele] in test_dict]

print(res)
###########################################################
print("Remove keys with Values Greater than K ( Including mixed values )")
###########################################################
test_dict = {"Gfg" : 3, "is" : 7, "best" : 10, "for" : 6, "geeks" : 'CS'}
to_check=7
test_dict2=test_dict.copy()
for k,v in test_dict.items():
    if isinstance(v,int)==True:
        if v>=to_check:
            test_dict2.pop(k)

#print(dict(test_dict2))
print((test_dict2))

###########################################################
print("Remove keys with substring values")
###########################################################
test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
#Filtered Dictionary : {1: ‘Gfg is best for geeks’}
sub_list = ['love', 'good']
sample_dict=dict()
'''
for k,v in test_dict.items():
    for ele in sub_list:
        if v.find(ele)>=0:
            sample_dict[k]=v
'''
sample_dict={k:v for k,v in test_dict.items() for ele in sub_list if v.find(ele)>=0}
res=set(test_dict)-set(sample_dict)
print(list(res))

form_dict=dict()

form_dict={ele:test_dict[ele] for ele in list((res))}

print(form_dict)

###########################################################
print("Dictionary with maximum count of pairs")
###########################################################

test_list = [{"gfg": 2, "best" : 4},{"gfg": 2, "is" : 3, "best" : 4},{"gfg": 2}]
#test_list = [{“gfg”: 2, “best” : 4}, {“gfg”: 2}]
dict1={}
'''
for ele in test_list:
    for k,v in ele.items():
     dict1[k]=v
print(dict1)
'''
#Second way: One line
dict1={}

dict1={k:v for ele in test_list for k,v in ele.items()}

print(dict1)
###########################################################
print("Append Dictionary Keys and Values ( In order ) in dictionary")
###########################################################
test_dict = {"Gfg": 1, "is": 2, "Best": 3}
#[‘Gfg’, ‘is’, ‘Best’, 1, 2, 3]
l1=[]
for k in test_dict.keys():
    l1.append(k)

for v in test_dict.values():
    l1.append(v)

print(l1)

###########################################################
print("Extract Unique values dictionary values")
###########################################################
dict1={"gfg": [5, 6, 7, 8], "best": [6, 12, 10, 8], "is": [10, 11, 7, 5], "for": [1, 2, 5]}
#The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]
l1=[]

l1=[sorted(set((ele) for v in dict1.values() for ele in v))]

print(l1)
###########################################################
print("Keys associated with Values in Dictionary")
###########################################################
from collections import defaultdict
dict11={'is': [1, 4], 'gfg': [1, 2, 3], 'best': [4, 2]}
#{1: ['is', 'gfg'], 2: ['gfg', 'best'], 3: ['gfg'], 4: ['is', 'best']}
dict1=defaultdict(list)

#d2[key].extend(Value)

l1=[]

for k,v in dict11.items():
    for ele in v:
       # l1=[]
        #l1.append(k)
        dict1[ele].append(k)

print(dict1)
###########################################################
print("Filter dictionary values in heterogenous dictionary")
###########################################################
dict1={'Gfg': 4, 'for': 'geeks', 'is': 2, 'best': 3}
test_dict2={}
#{'Gfg': 4, 'for': 'geeks'}

test_dict2={k:v for k,v in dict1.items()  if isinstance(v,str) or v > 3}
print(test_dict2)

###########################################################
print("Anagrams together in Python using List and Dictionary")
###########################################################
def allAnagram(input):
    dict = {}
    for strVal in input:
        key = ''.join(sorted(strVal))
        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key] = []
            dict[key].append(strVal)

    output = ""
    for key, value in dict.items():
        output = output + ' '.join(value) + ' '

    return output


# Driver function
if __name__ == "__main__":
    input = ['cat', 'dog', 'tac', 'god', 'act']
    print(allAnagram(input))

###########################################################
print("Sort Dictionary key and values List")
###########################################################
test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
dict2=defaultdict(list)
dict1=sorted(test_dict.items(),key=lambda k:k[1])
print(dict1)

for k,v in test_dict.items():
    l3=sorted(v)

    dict2[k].append(l3)

print(sorted(dict2.items()))
dict3={}
for k,v in sorted(dict2.items()):
    dict3[k]=v

print(dict3)
###########################################################
print("Sort Dictionary by Values Summation")
###########################################################
test_dict = {"Gfg" : [6, 7, 4], "best" : [7, 6, 5]}
dict3={}
for k , v in test_dict.items():
    x=sum(v)
    dict3[k]=x

print(dict3)

dict3={k:sum(v) for k , v in test_dict.items()}

print(dict3)

###########################################################
print("Sort dictionaries list by Key’s Value list index")
###########################################################

test_list = [{"Gfg" : [6, 7, 8], "is" : 9, "best" : 10},{"Gfg" : [2, 0, 3], "is" : 11, "best" : 19},{"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}]

res = sorted(test_list, key = lambda ele: ele['Gfg'][0])
print(res)
