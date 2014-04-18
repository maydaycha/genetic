#!/usr/bin/python

N = 30951344
L = 201310
U = 3567891

def score(num):
    return num | N

def brute_force():
    p1 = L
    now_max = 0
    now_m = 0
    for i in range(p1, U):
        if now_max < score(i):
            now_max = score(i)
            now_m = i
        elif now_max == score(i):
            if now_m > i:
                now_m = i
        else:
            pass
        #print "now_max: %d, now_m : %d" %(now_max, now_m)
    return now_m

result = brute_force()
print result

