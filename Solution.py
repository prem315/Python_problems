def loveLetterMystery ( str ):
    string = list(str)
    counter = 0
    l = int(len(string))
    for x in range(0,int(l/2)):
        while string[x] != string[l-x-1]:
            counter = counter + 1
            if string[x] > string[l-x-1]:
                string[x] = chr(ord(string[x]) - 1)
            else:
                string[l-x-1] = chr(ord(string[l-x-1]) - 1)
    print(counter)
    
N = int(input())

for x in range(0,N):
    loveLetterMystery(input())
