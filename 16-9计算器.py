import time
print("计算16-9")
A = "16-9"
if A[1] < A[-1]:
    while True:
        print(A[1], "-", A[-1], "不够")
        time.sleep(1)
        print("借1")
        time.sleep(1)
        print("得到", A)
        time.sleep(1)
if A[1] > A[-1]:
    print(A[0],A[-1])