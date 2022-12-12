# def reverse_list(l):
#     l.reverse()
#     return l
# def reverse_list(l):
#     return l[::-1]
def reversed_list(l):
    r_list = []
    for i in range(len(l)):
       popped_items = l.pop()
       r_list.append(popped_items)
    return r_list


numbers = [1,2,3,4,5,6,7,8,9]
print(reversed_list(numbers))