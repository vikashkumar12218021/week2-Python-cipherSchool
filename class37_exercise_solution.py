def common_finder(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output
l1 = [1,2,5,6]
l2 = [1,2,4,6,7,9]
print(common_finder(l1,l2))