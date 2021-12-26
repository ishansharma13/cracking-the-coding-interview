def fizzBuzz(n):
    
    for i in range(1,n+1):
        if i%3==0 and i%5 ==0:
            print("FizzBuzz",sep =" ")
        elif i%3==0:
            print("Fizz",sep =" ")
        elif i%5==0:
            print("Buzz",sep =" ")
        else:
            print(i,sep =" ")

if __name__ == '__main__':
    fizzBuzz(15)