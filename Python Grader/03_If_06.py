x=float(input())

if x<=100:
    print("18")
elif x<=250 and x>100:
    print("22")
elif x<=500 and x>250:
    print("28")
elif x<=1000 and x>500:
    print("38")
elif x<=2000 and x>1000:
    print("58")
elif x>2000:
    print("Reject")