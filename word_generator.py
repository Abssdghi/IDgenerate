def word_generator(n, combain=False):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ['']
    all = []
    
    for _ in range(n):
        new_result = []
        for prefix in result:
            for letter in letters:
                new_result.append(prefix + letter)
        result = new_result
    
    if combain == True:
        if n > 1:
            all+=(word_generator(n-1, True))
    all+=result
    
    return all