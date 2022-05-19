# list
a = [1, "ddd", True]
print(a)
print(a[0], a[1:], a[1:3], a[:3], a[-1], a[:-1])
print(max([1,2,3]))
for x in a:
    print(x)

a1 = list(filter(lambda x:x>5, range(10)))
a2 = list(map(lambda x:x*2, a1))
print(a1, a2)

from functools import reduce
print(reduce(lambda x,y:x+y, range(10),0))
print(list(range(1,10,2)))

a = [1,2,3]
del a[1]
t = (1,) + (2,3)
print(t)

d = {1:2, 'ape':'red'}
d[7]=8
print(a[1],d[7])

s1 = {2,5,"ghhh"}
s2 = {5,6}
print(s1, s2, s1|s2, s1&s2)


import pandas as pd
d = pd.DataFrame([[1,2,3,"momo"], [4,5,6,"koko"]])
d.columns = ['w','h','d','name']
print(d)
print(d[['name','w']])
print("----------------")
print(d.iloc[:,:]) # rows range, col range
print(d[d.w ==1]) # selecting

import numpy as np
m=np.array([[1,2,3],[4,5,6]])
print(m);print(m.transpose())

np.array([1,2, 3])

from sorting import Sort

print(Sort.bubble([1,5,3,2,6,1]))
print(Sort.insert([1,5,3,2,6,1]))
print(Sort.merge([1,5,3,2,6,1]))
print(Sort.selection([1,5,3,2,6,1]))