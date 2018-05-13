def split_all_even_numbers(numbers, way):
    x=len(numbers)-1
    tm=len(numbers)
    while(x!=-1):
        if numbers[x]%2==0:
            print(numbers[x])
            a=numbers[x]
            loc=x
            mid=a//2
            if way==2:
                del numbers[loc]
                count=0
                i=2
                while(a%i==0):
                    count+=1
                    i*=2
                i=i//2
                a=a//i
                for y in range(i):
                    numbers.insert(loc,a)
                x=len(numbers)
        x=x-1
                    
    return numbers
print(split_all_even_numbers([1, 1, 17, 11, 9, 11, 7, 2, 1, 3, 1, 2, 14, 2],2))
