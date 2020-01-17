import pandas as pd
import time
import datetime
start_time =time.time()
df = pd.read_pickle(r'C:\Users\Akshay\Desktop\Programming Interview Questions\px.xz')
print("hello")

x = df.bbgid.unique()
ans=[[]]

print(len(x))

x = df.bbgid.unique()
##12652212
j=0
i=1
min = df.dt[1]
while j<len(x):
    max_value=datetime.timedelta(days=1)
    while i < int(12652212):
        
        if x[j] == df.bbgid[i]:
            one = df.dt[i]
            two = df.dt[i+1]
            diff = (abs(one -two))
##            print(one, two, diff)
            if diff > max_value and x[j] == df.bbgid[i+1]:
                max_value=diff
                row=[]
                row.append(one)
                row.append(two)
                row.append(diff)
                row.append(x[j])
##                print("-----------", one, two, diff, "------------")
            

            i=i+1
            

            continue
        else:
##            print(min)
            i=i+1
##            print(x[j])
##            print(df.bbgid[i])         
            break
        
    
    if i == 12652211:
        break
    ans.append(row[:])

    
    j=j+1
    print("------- %s seconds -----" % (time.time() -start_time), j)   
    
print("------- %s seconds -----" % (time.time() -start_time))            
        
res= pd.DataFrame(ans,columns =['Start_date', 'End_date', 'length', 'bbgid'])
b= res.sort_values('length', ascending=False)








    
    
        
    
        
        
        
        





    
        
            
        
            
            
            
            
            
            
            
    
        
        


 
##y.reindex(pd.date_range(y.iloc[0], y.iloc[-1]).isnull().all(1)
##
    
