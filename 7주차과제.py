numbers=list()
count=0
while True:
    s=input('양정수를 입력하세요: ')
    if count==0 and int(s)<0:
        print('입력된 양정수가 없습니다.')
        break
    count+=1
    if '-'in s:
        break
    if s in '0123456789':
        numbers.append(int(s))
    else:
        print('다시 입력하시오')
        
def my_max():
    while True:
        if len(numbers)==0:
            pass
        else:
            i=0
            a=numbers[0]
            while i<len(numbers):
                if a<numbers[i]:
                    a=numbers[i]
                i+=1
            return a
print('최대값은',my_max())

def my_min():
    while True:
        if len(numbers)==0:
            pass
        else:
            i=0
            a=numbers[0]
            while i<len(numbers):
                if a>numbers[i]:
                    a=numbers[i]
                i+=1
            return a
print('최소값은',my_min())

def my_sum():
    while True:
        if len(numbers)==0:
            pass
        else:
            i=0
            sum=0
            while i<len(numbers):
                sum+=numbers[i]
                i+=1
            return sum
print('합은',my_sum())

def my_avg():
    while True:
        if len(numbers)==0:
            pass
        else:
            i=0
            sum=0
            while i<len(numbers):
                sum+=numbers[i]
                i+=1
            result=sum/len(numbers)
            return result
print('평균은',my_avg())