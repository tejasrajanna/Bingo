import random as r
# 2 gives number and 1 gives blank space
cols=9;rows=3
l = [[0 for i in range(cols)]for j in range(rows)]  # to make initial array with all 0's
for i in range(0,3):              # to assign random 2's and 1's such that every row has five 2's and four 1's
    for j in range(0,9):
        if l[i].count(1)>=4:
            # print("count 1",l[i].count(1))
            l[i][j] = 2
        elif l[i].count(2)>=5:
            #print("count 2", l[i].count(2))
            l[i][j]=1
        else:
            #print("Random")
            l[i][j]=r.randrange(1,3)
"""print(l[0])
print(l[1])
print(l[2])"""
excol=[]  #colunms with more than one 2
necol=[]  #column with three 1's
def chec():  #to check if any column has three 1's and if any column has more than one 2
    excol.clear()
    necol.clear()
    for i in range(0,9):
        cou=0
        for j in range(0,3):
            if l[j][i]==1:
                cou=cou+1
        if cou==3:
            necol.append(i)
        if cou==1 or cou==0:
            excol.append(i)
    #jprint(necol)
    #print(excol)
chec()
if(len(necol))>0:  #to exchange 2's and 1's in same row so each column has atleast one 2
    for i in range(0,3):
        if(len(necol))==0: #to make sure chec doesn't keep getting called for every iteration of i
            break
        for j in range(0,9):
            temp=0
            if j in necol:
                for k in excol:
                    if(l[i][k]==2):
                        #print(i, j, excol,k)
                        temp=l[i][j]
                        l[i][j]=l[i][k]
                        l[i][k]=temp
                        break
        chec()    #to make sure that in a column which has two 2's, both 2's don't get changed into 1's
"""print(l[0])
print(l[1])
print(l[2])"""
for i in range(0, 3):  #finally making tambola card
    for j in range(0, 9):
        if l[i][j]==1 and j==0:
            l[i][j]=''
        elif l[i][j]==1:
            l[i][j]=' '
        else:
            if j==0:
                l[i][j]=r.randrange(1,10)
            elif j==1:
                l[i][j]=r.randrange(10,20)
            elif j==2:
                l[i][j]=r.randrange(20,30)
            elif j==3:
                l[i][j]=r.randrange(30,40)
            elif j==4:
                l[i][j]=r.randrange(40,50)
            elif j==5:
                l[i][j]=r.randrange(50,60)
            elif j==6:
                l[i][j]=r.randrange(60,70)
            elif j==7:
                l[i][j]=r.randrange(70,80)
            elif j==8:
                l[i][j]=r.randrange(80,90)
print(l[0])
print(l[1])
print(l[2])
