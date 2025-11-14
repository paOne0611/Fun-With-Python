def isRotated(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) <= 2 or len(s2) <= 2:
        return s1 == s2
    clock = ""
    anticlock = ""
    length = len(s2)
    anticlock = s2[-2:] + s2[:-2]
    clock = s2[2:] + s2[:2]
    return s1 == clock or s1 == anticlock


def eff_isRotated3(s1,s2): 
    if len(s1) == len(s2):
        if len(s1) <= 2 or len(s2) <= 2:
            return s1 == s2
        return (s2[-2:] + s2[:-2]) or s1 == s2[2:] + s2[:2]

        
w1='gaming'
w2='mingga'
k=True

import time
start=time.time()
for i in range(100000):
    k=isRotated(w1, w2)
end=time.time()
print(end-start)

start=time.time()
for i in range(100000):
    k=eff_isRotated3(w1, w2)
end=time.time()
print(end-start)






