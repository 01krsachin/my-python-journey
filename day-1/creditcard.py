balance = int(input("enter your balance :"))
rate = float(input("inter the bank interest rate :"))

balance_new = balance + (balance * rate/100)

print(balance_new)
