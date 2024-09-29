def number_generator(n, combain=False):
    result = []
    all = []

    for number in range(0,int(n*"9")+1):
        fixed_number = str(number)
        while len(fixed_number) != n:
            fixed_number = '0'+fixed_number
        result.append(fixed_number)
    
    if combain == True:
        if n > 1:
            all+=(number_generator(n-1, True))
    all+=result
    
    return all