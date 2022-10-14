
S = 'Hello'
print(len(S))





S = "'Море', 'Чайки', 'Самолет', 'Санки', 'Города'"
print([e for e in eval('('+S+')') if len(e)<=5])

import heapq
nums = [10,8,-4]
print(heapq.nlargest(3, nums)) 
print(heapq.nsmallest(3, nums))