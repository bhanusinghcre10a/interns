
#i assume that value at each day is integer as given so average always converted to int
def solution(D):
  let=[]
  ans={}
  for i in D.items():
    let.append([int(j) for j in i[0].split('-')]+[i[1]])
  let.sort()
  def finddays(d1,d2):
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    days1=d1[0]*365+d1[2]
    for i in range(0,d1[1]-1):
      days1+=months[i]
    if(d1[1]<=2):
      y=d1[0]-1
    else:
      y=d1[0]
    days1+=(int(y/4+y/400-y/100))
    
    days2=d2[0]*365+d2[2]
    for i in range(0,d2[1]-1):
      days2+=months[i]
    if(d2[1]<=2):
      y=d2[0]-1
    else:
      y=d2[0]
    days2+=(int(y/4+y/400-y/100))
    return days2-days1
  months1=[31,28,31,30,31,30,31,31,30,31,30,31]
  months2=[31,29,31,30,31,30,31,31,30,31,30,31]
  for i in range(1,len(let)):
    x=finddays(let[i-1],let[i])
    if(x==1):
      ans[str(let[i-1][0])+'-'+str(let[i-1][1])+'-'+str(let[i-1][2])]=let[i-1][3]
      ans[str(let[i][0])+'-'+str(let[i][1])+'-'+str(let[i][2])]=let[i][3]
    else:
      med=((let[i][-1]-let[i-1][-1])/x)
      prev=let[i-1]
      while(x>0):
        ans[str(prev[0])+'-'+str(prev[1])+'-'+str(prev[2])]=int(prev[3])
        prev[2]+=1
        if((prev[0]%4==0 and prev[0]%100!=0) or prev[0]%400==0):
          if(prev[2]>months2[prev[1]-1]):
            prev[2]=1
            prev[1]+=1
            if(prev[1]>12):
              prev[2]=1
              prev[1]=1
              prev[0]+=1
        else:
          if(prev[2]>months1[prev[1]-1]):
            prev[2]=1
            prev[1]+=1
            if(prev[1]>12):
              prev[2]=1
              prev[1]=1
              prev[0]+=1
        prev[3]+=med
        x-=1
      ans[str(let[i][0])+'-'+str(let[i][1])+'-'+str(let[i][2])]=let[i][3]
  return ans
