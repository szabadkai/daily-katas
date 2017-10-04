# given two sorted lists divise a function to merge the two functions
# try to do it in linear 'time'

def linear_merge(list1, list2):
    merged_list = []
    while list1 and list2:
        a = list1[-1]
        b = list2[-1]
        if a>b:
            merged_list.append(list1.pop(-1))
        elif a<b:
            merged_list.append(list2.pop(-1))
        else:
            merged_list.append(list1.pop(-1))
            merged_list.append(list2.pop(-1))
    merged_list.extend(list1+list2)
    merged_list.reverse()
    return merged_list

print (linear_merge([1,2,3],[2,5,7]))
