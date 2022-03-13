import datetime as dt
a = dt.datetime.now()
def strl_to_intl(L):
    for i in range(len(L)):
        L[i]=int(L[i])
    return L
L = str(a).split(" ")[0].split("-")
L = strl_to_intl(L)
b = a+dt.timedelta(7)
L2 = str(b).split(" ")[0].split("-")
L2 = strl_to_intl(L2)

with open("tb.dat","rb") as f:
    a = "".join(str(f.read(),"utf-8").split("\x00")).split("\n")
    a1 = strl_to_intl(a[0].split("-"))
    a2 = strl_to_intl(a[1].split("-"))
    a1 = dt.datetime(*a1)
    a2 = dt.datetime(*a2)
    if(a1<=dt.datetime.now()<=a2):
        return__ = 0
    else:
        return__ = 1
def return_():
    global return__
    return return__