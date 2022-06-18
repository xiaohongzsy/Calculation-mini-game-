import time
import random
#导入时间库，导入随机库

correctCount=0#正确题目的数量=0初始化为零
count=0#已做题目数量=0初始化为零
NUMBER_OF_QUESTIONS=6#题目数量不超过100

startTime=time.time()#开始时间

while count<NUMBER_OF_QUESTIONS:#循环目的，当题目少于101题时，每做一题，计数表+1，直到101
    a1=random.randint(0,10)
    a2=random.randint(0,10)
    if a1<a2:
        a1,a2=a2,a1#为减数换位，以免出现负数
    answer=eval(input("Please enter you answer~"+str(a1)+"*"+str(a2)+"=?"))
    if a1*a2==answer:
        print("Well Done!")
        correctCount+=1
    else:
        print("Wrong☺✘☝")
    count+=1
endTime=time.time()
testTime=int(endTime-startTime)
print("The probability that you got it right today is  "+str(correctCount)+" topic！"+"We did 10 problems！"+"And use  "\
      +str(testTime)+" second.")