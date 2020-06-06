fname=input('Enter your file name')
fhand=open(fname)
dic={}
newdic={}
for line in fhand:
  if not line.startswith('From:'):
    continue
  else:
    words=line.split()
  for word in words:
      dic[word]=dic.get(word,0)+1  # key er value assign kora hochche for loop er madhdhome
#print(dic)       dictionary print er jonno                  # eikhane dictionary ta print kora hocche
#Once we have printed the dictionary, it's time for use to print the largest number.
#largest value print korar jonno for loop die key value pair er vitor die jawa lagbe
#item method use kore duita iteration variable use kora jay
max1=-1
theword=None
for k,v in dic.items():
    if v>max1:
        max1=v
        theword=k
max2=0
for k1,v1 in dic.items():
    if v1>max2 and v1<max1:
        max2=v1
        theword2=k1
print(theword2,max2)
