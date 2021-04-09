n = input("Enter number ")
def getSum(n):
    sumOdd = 0
    sumEven = 0
    num = str(n)
    for i in range(len(num)):
        if(i % 2 == 0):
            sumOdd = sumOdd+int(num[i])
        else:
            sumEven = sumEven+int(num[i])
    print("Sum odd = ", sumOdd )
    print("Sum even = ", sumEven )

if __name__ == "__main__":

            getSum(n)