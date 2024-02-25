f = open("atgc_input.txt", "r")
datalines = f.readlines()
name=[]
mainlist=[]
sublist=[]
letters=[]
for i in datalines:
   sublist=[]
   if i[0]==">":
       letters=[]
       name=[]
       for j in i:
           if j==" ":
               break
           name.append(j)
       name="".join(name)
       sublist.append(name)
       sublist.append(letters)
       mainlist.append(sublist)
       continue
   letters.append(i)
   

for i in mainlist:
   acount=0
   ccount=0
   gcount=0
   tcount=0
   other=0
   i[1]="".join(i[1])
   i[1]=i[1].replace("\n","")
   length=len(i[1])
   i.append(length)
   for j in i[1]:
       if j[0]=='A':
           acount+=1
       elif j[0]=='C':
           ccount+=1
       elif j[0]=='G':
           gcount+=1
       elif j[0]=='T':
           tcount+=1
       else:
           other+=1
   i.append(acount)
   i.append(ccount)
   i.append(gcount)
   i.append(tcount)
   i.append(other)
##print(mainlist)


for i in mainlist:
   f=open("atgc_sorted.txt", "a")
   print(i[0],end=" ")
   f.write(i[0] + " ")
   print(i[2],end=" ")
   f.write(str(i[2]) + " ")
   print(i[3],end=" ")
   f.write(str(i[3]) + " ")
   print(i[4],end=" ")
   f.write(str(i[4]) + " ")
   print(i[5],end=" ")
   f.write(str(i[5]) + " ")
   print(i[6],end=" ")
   f.write(str(i[6]) + " ")
   print(i[7])
   f.write(str(i[7]) + "\n")