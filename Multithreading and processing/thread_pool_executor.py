from concurrent.futures import ThreadPoolExecutor
import time


def printnum(num):
    time.sleep(1)
    return f"Number is:{num}"

num=[1,2,3,4,5,6,7,8,2,3,4,5,6,4,3,5,3,5,6,335,3,43,5,4,5,3,4,3,]

start=time.time()
res=map(printnum,num)
for i in res:
    print(i)
end=time.time()
print(f"Total time taken without pool:{end-start}")

start=time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    result=executor.map(printnum,num)

for i in result:
    print(i)
end=time.time()
print(f"Total time taken with pool:{end-start}")