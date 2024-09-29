from number_generator import *
from word_generator import *


def username_generator(command='c(user)'):
    """
    Generating all possible states of a username

    l : the letters that must be in ID
    w : the number of letters in a word
    n : the number of digits of numbers
    c : constant (usually a person's name)
    
    - : without underline before
    + : with underline before
    = : - and +
    
    example command : c(user)-,w(3)+,n(1)=,l(s-s-a-d-7)
    """
    
    lst = command.split(',')

    results = ['']
    for i in lst:
        if i[0]=='c':
            pre = []
            for j in results:
                if i[-1] == '=':
                    pre.append(j+i[2:-2])
                    pre.append(j+'_'+i[2:-2])
                elif i[-1] == "+":
                    pre.append(j+'_'+i[2:-2])
                elif i[-1] == "-":
                    pre.append(j+i[2:-2])

        elif i[0]=='w':
            pre = []
            for j in word_generator(int(i[2:-2])):
                for k in results:
                    if i[-1] == '=':
                        pre.append(k+str(j))
                        pre.append(k+'_'+str(j))
                    elif i[-1] == "+":
                        pre.append(k+'_'+str(j))
                    elif i[-1] == "-":
                        pre.append(k+str(j))

        elif i[0]=='n':
            pre = []
            for j in number_generator(int(i[2:-2])):
                for k in results:
                    if i[-1] == '=':
                        pre.append(k+j)
                        pre.append(k+'_'+j)
                    elif i[-1] == "+":
                        pre.append(k+'_'+j)
                    elif i[-1] == "-":
                        pre.append(k+j)
        
        results = pre

        
    pre2 = []
    for i in lst:
        if i[0] == "l":
            
            limits = i[2:-1].split('-')
            for i in pre:
                limits_copy = limits.copy()
                i_copy = i
                
                for k in range(len(limits)):
                    j = limits[k]
                    if j in i_copy:
                        i_copy = i_copy.replace(j, '', 1)
                        # return
                        limits_copy.remove(j)
                if len(limits_copy)==0:
                    pre2.append(i)
                            
            results = pre2

    return results

