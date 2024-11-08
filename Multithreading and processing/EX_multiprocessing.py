from multiprocessing import Process
import time



def numbersqure():
    for i in range(10):
        time.sleep(1)
        print(f"Square of {i} is: {i*i}")


def cube():
    for i in range(10):
        time.sleep(1.5)
        print(f"Cube of {i} is: {i*i*i}")


if __name__=="__main__":

    p1=Process(target=numbersqure)

    p2=Process(target=cube)

    start=time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end=time.time()

    total=end-start
    print(f"Total time taken with multiprocessing: {total}")