def sub_list(l):
    count = 0
    for i in l:
     if type(i) == list:
        count += 1
    return count
n = [1,2,3,[5,6,7,8,9],[4,5,6,5,4]]
print(sub_list(n))
