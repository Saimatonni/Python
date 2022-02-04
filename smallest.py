smalest_so_far=None
print('before',smalest_so_far)
for the_number in [45,67,23,43,34] :
    if smalest_so_far is None:
        smalest_so_far=the_number
    elif the_number<smalest_so_far :
        smalest_so_far=the_number
    print(smalest_so_far,the_number)
print('after',smalest_so_far)
