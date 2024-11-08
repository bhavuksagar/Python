from concurrent.futures import ProcessPoolExecutor
import time


def printnum(num):
    time.sleep(1)
    return f"Square is:{num*num}"

num=[1,2,3,4,5,6,7,8,2,3,4,5,6,4,3,5,3,5,6,335,3,43,5,4,5,3,4,3,]

start=time.time()
res=map(printnum,num)
end=time.time()
without=end=start

if __name__=="__main__":
    start=time.time()
    with ProcessPoolExecutor(max_workers=10) as executor:
        result=executor.map(printnum,num)

    end=time.time()
    withpool=end-start
    print(f"Total time taken without pool:{without}")
    print(f"Total time taken with pool:{withpool}")