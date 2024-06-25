# file1 = {'This is page 1', 'This is page 2'}
file1 = {'this is page 1 only'}
allContent =  {'This is page 1', 'This is page 2', 'hello my name is dev'}
# goal is to make file 2 which is unique (as in it should not have contents of file 1)

if file1.intersection(allContent) == set():
    print("there is not intersection, they are mutually exclusive")
else:
    file2 = ((file1.union(allContent))-(file1.intersection(allContent)))

# print(file2)
