def mutate_string(string, i, c):
    l=list(string)
    
    
    i=int(i)
    l[i]=c
    s_new=''.join(l)
    
    
    
    return s_new
mutate_string('abracadabra',5,'k')
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


