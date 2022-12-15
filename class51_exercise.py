def cube_finder(m):
    cube = {}
    for i  in range(1,m+1):
        cube[i]=i**3
    return cube
print(cube_finder(15))