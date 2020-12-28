# best saving rate for your salary to pay for the down payment of the house in 36 months

start_salary = float(input("salary: "))
sara = 0.07 
sara_c = 0
### annual return on investments = r
r = 0.04
cost = 1000000
por_downpay = 0.25
downpay = por_downpay*cost
savings = 0

high = 1 
low = 0
prop_saved = (high+low)/2
count = 0

for i in range (0,36):
	prop_saved = high 
	salary = start_salary
	savings += (savings*(r/12)) + prop_saved*(salary/12)
if savings < (downpay - 100):
	print("n/a")
else:
	while abs(savings - downpay) > 100:
		count += 1
		savings = 0
		salary = start_salary
		sara_c = 0
		for i in range (0,36):
			savings += (savings*(r/12)) + prop_saved*(salary/12)
			sara_c += 1
			if sara_c == 6:
				salary += salary*sara
				sara_c = 0
		if savings > downpay:
			high = prop_saved
		else:
			low = prop_saved
		prop_saved = (high+low)/2

	print(prop_saved)
	print(count)