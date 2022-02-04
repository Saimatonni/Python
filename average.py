count=0
sum=0
print('before',count,sum)
for the_number in [45,67,23,43,34] :
    count=count+1
    sum=sum+the_number
    print(count,sum,the_number)
print('after',count,sum,sum/count)
