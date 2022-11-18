# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.


#loop through list
#count method
#return value of the largest count

arr = [1,1,1,22,2,2,2,2,2,3,3,3,3]


def count_num(lst):
    
    dict = {
        
        
    }
    a_lst = []    
    for x in lst:
        number = lst[0]
        if lst.count(x)> lst.count(lst):
            dict[x]=lst.count(x)
    for key in dict:
        q = max(dict.values())
        if dict[key] == q:
            e = key
            a_lst.append(e)
    for i in a_lst:
        return max(a_lst)            
        


        
print(count_num(arr))

