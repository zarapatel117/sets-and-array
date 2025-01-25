import array as arr
array_num=arr.array('i',[1,3,5,3,7,9,3])
print("num of occurences of the num 3 is the said array:",str(array_num.count(3)))
array_num.reverse()
print("reverse the order of the items:")
print(str(array_num))