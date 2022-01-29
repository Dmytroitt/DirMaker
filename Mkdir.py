import os
names = str(input('Name for dirs: '))
nums = int(input('Number of Dirs you want: '))

for i in range(0, nums):
    os.mkdir(r'{}{:03d}'.format(names,i))
print('Done, Check your Dirs!')
