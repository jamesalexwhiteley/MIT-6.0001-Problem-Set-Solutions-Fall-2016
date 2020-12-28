# months needed to save for down payment 

salary = input("Enter your annual salary: ")
prop_saved = input("Enter the portion of your salary to be saved ")
total_cost = input("Enter cost of dream home: ")
sa_raise = input("Enter semi annual raise: ")

# salary = 80000
# prop_saved = 0.1
# total_cost = 800000
# sa_raise = 0.03

salary = float(salary)
prop_saved = float(prop_saved)
total_cost = float(total_cost)
sa_raise = float(sa_raise)

current_savings = 0
portion_down_payment = 0.25*(total_cost)
####annual return on saving = r
r = 0.04
# ####amount saved per month 
# amount_saved = (salary/12)*prop_saved
i = 0
sa_rc = 0

while current_savings < portion_down_payment:
	amount_saved = (salary/12)*prop_saved
	current_savings += (current_savings*(r/12)) + amount_saved 
	i = i + 1 
	sa_rc = sa_rc + 1
	if sa_rc == 6: 	
		salary = salary + salary*sa_raise 
		sa_rc = 0

print('Time for down payment =', str(i), 'months')
