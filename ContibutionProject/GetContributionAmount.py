def GetAmount():
   validAmount  = False
   contributionAmount = "invalid amount"
   amount = ""
   while validAmount == False:
      try:
        amount = input("Enter the conbribution Amount(in numbers only) : ")
        amount = float(amount)
        amount = f"{amount:.2f}"
        contributionAmount = float(amount)
        print(f"Amount entered is GHS {contributionAmount:.2f}")
      except Exception as E:
        print(f"Value entered is {amount}, which in invalid")
      if isinstance(contributionAmount, float) and contributionAmount<=0:
         print("please enter a valid amount greater than zero")
      elif isinstance(contributionAmount, float) and contributionAmount>0:
         validAmount = True
      else:
         print("please enter a valid amount greater than zero")
   print(f"The weekly contribution amount is {contributionAmount:.2f}")
   print("--------------------------------------------------------------")
   return contributionAmount