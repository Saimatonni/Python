largest_so_far=-1
print('before',largest_so_far)
for the_number in [45,67,23,43,34] :
    if the_number>largest_so_far :
        largest_so_far=the_number
    print(largest_so_far,the_number)
print('after',largest_so_far)
