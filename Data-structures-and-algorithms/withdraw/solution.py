def withdraw(amount: int) -> list:
  #Initialize
  number_of_bills = [0,0,0]
  
  #100 bill
  remainder = amount % 100
  if (remainder == 10 or remainder == 30) and (amount >= 100): 
    number_of_bills[0] = int(amount / 100)-1
  else: 
    number_of_bills[0] = int(amount / 100)
  amount -= number_of_bills[0] * 100
	
  #50 bill
  if(amount % 20 == 0):
    number_of_bills[1] =  0 
  elif(amount < 50): 
    number_of_bills[1] = 0 
  else: 
    number_of_bills[1] = 1
  amount -= number_of_bills[1] * 50
	
  #20 bill
  number_of_bills[2] = int(amount / 20)
  return(number_of_bills)
