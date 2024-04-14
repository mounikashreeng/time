t=input("Enter time")
hour=t[0:2]
minute=t[3:5]
second=t[6:8]
if int(hour)>12:
    print('not apllicable')
elif int(minute)>60:
    print("not applicable")
elif int(second)>60:
    print("not applicable")
elif "AM" in t:
    if int(hour)==12:
        hour='00'
        print(hour+':'+minute+':'+second)
    else:
        print(hour+":"+minute+':'+second)
elif "PM" in t:
    if int(hour)==12:
        print(hour+':'+minute+":"+second)
    else:
        h=int(hour)
        h=h+12
        h=str(h)
        print(h+":"+minute+":"+second)
