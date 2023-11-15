class oper:
    def fibo(value):
        if value==1: return 1
        elif value==2: return 1
        else: return   fibo(value-1) + fibo(value-2)

print(oper.fibo(1))
print(oper.fibo(2))
print(oper.fibo(3))