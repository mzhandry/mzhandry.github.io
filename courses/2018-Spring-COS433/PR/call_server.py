import time
from multiprocessing import Pool
import RIAserver
import random



 #calling RIAserver, with timing:

q = 83992003185014143150590272358854849633419445729589423043532391689031602005248382047760568924832901185307919815346457169269465413610582939734737779885386661839188660526365262302313750475275234760028913005930893542673653714283601367

c0 = random.randrange(0,q)
c1 = random.randrange(0,q)
start = time.time()
ret = RIAserver.execute(c0,c1)
end = time.time()
print(end-start)
print(ret)


def f(c): 
	return RIAserver.execute(c0,c)



#calling RIAserver in parallel:

numparallel = 512 #number of parallel calls
pool = Pool(numparallel)

arr = pool.map(f,[c0]*numparallel)

print(arr)