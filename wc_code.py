import pandas as pd
from statistics import mean
from matplotlib import pyplot as plt
import collections as cl
df=pd.read_excel('dob_data.xlsx')
dob=list(df['DOB'])
name=list(df['NAME'])
number=list(df['CONTACT NUMBER'])
Rating=list(map(int,df['RATE OUR SERVICE']))
n=int(input("TO CHECK BIRTDAYS ENTER 1 |||| TO CHECK CUSTOMER DETAILS ENTER 2 |||| To check rating distribution ENTER 3 |||| To check birthday-month distribution ENTER 4||||Enter 5 to verify customer with name  "))
if(n==1):
    today=input("Enter date(dd/mm)  ")
    if(len(today)!=5):
        print("Enter corrent date in form of dd/mm  (example: 28/02)")
    else:
        bdays=[]
        for i in range(len(number)):
            if(dob[i][0:5]==today):
                bdays.append(name[i]+' '+str(number[i]))        
        if(len(bdays)==0):
            print("NO BIRTHDAYS ON ENTERED DATE")
        else:
            print("THESE CUSTOMERS HAVE BIRTHDAY ON ENTERED DATE ",*set(bdays),sep="\n") 
elif(n==2):
    avg=[]
    x=int(input("Enter the mobile number of customer  "))
    for j in range(len(number)):
        if(number[j]==x):
            print(df.loc[[j]])
            avg.append(Rating[j]) 
    if(len(avg)!=0):
        print("This customer has visited",len(avg),"times")            
        print("average rating given by this customer is",mean(avg))
    elif(len(avg)==0):
        print("This customer has not visited yet")
                      
elif(n==3):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.axis('equal')
    points = ['1 point', '2 point', '3 point', '4 point', '5 point']
    arr=cl.Counter(Rating)
    distribution=[]
    beta=[1,2,3,4,5]
    for o in range(len(beta)):
        distribution.append(arr[beta[o]])
    ax.pie(distribution, labels = points,autopct='%1.2f%%')
    plt.show()
elif(n==4):
    m_freq=[]
    for z in range(len(number)):
        m_freq.append(dob[z][3:5])
    mfreq=sorted(m_freq)
    fig = plt.figure(figsize = (10, 5))  
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    arr=cl.Counter(mfreq)
    dist=[]
    alpha=['01','02','03','04','05','06','07','08','09','10','11','12']
    for p in range(len(alpha)):
        dist.append(int(arr[alpha[p]]))
    plt.bar(months, dist, color ='grey', width = 0.4)   
    plt.xlabel("Months")
    plt.ylabel("DIstribution Of bithday") 
    plt.title("BIRTHDAY DISTRIBUTION TABLE") 
    for k in range(len(alpha)):
        plt.text(x =months[k] , y = dist[k], s = dist[k],size=15)
    plt.subplots_adjust(bottom= 0.2, top = 1.0)
    plt.show()
elif(n==5):
    f_name=[]
    fname=[]
    x=input("Enter first name of customer(eg: Rajan)  ")
    print("customers having the first name as",x,"are")
    for v in range(len(number)):
        if([name[v].split()][0][0]==x):
            f_name.append(name[v])
    for g in f_name:
        if g not in fname:
            fname.append(g)
    print(fname)
    avg=[]
    x_1=input("Now enter the exact name of customer  ")
    for c in range(len(number)):
        if(name[c]==x_1):
            print(df.loc[[c]])
            avg.append(Rating[c]) 
    
    print("This customer has visited",len(avg),"times")            
    print("average rating given by this customer is",mean(avg))
else:
    print("Enter correct number")    
        