def GetContribution(Analysis : list, Amount : int):
     totalMember = len(Analysis)
     totalContribution = totalMember * Amount
     for i in Analysis:
          print(f"Contribution will now be gotten for Week : {i["Week"]}")
          print("-----------------------------------------------------------------------")
          for j,k in i["Contributions"].items():
               currentName = k[0]
               print(f"Dear {j}, please enter your contribution Amount between 0 and {Amount}")
               invalidAmount = False
               while invalidAmount == False:
                    contributionamount = input(f"{j}, Enter your amount : ")
                    try:
                        contributionamount = float(contributionamount)
                    except Exception as E:
                        print("error occured")
                        pass
                    
                    if isinstance(contributionamount, float) and Amount>=contributionamount>=0:
                       print(f"{j},the value you entered is : {contributionamount}")
                       invalidAmount = True
                       i["Contributions"][j] = str(contributionamount)
                       i["Outstanding"][j] = str(Amount - contributionamount)
                       print("outstanding amount is " + str(i["Outstanding"][j]))
                    else:
                       print("Please enter a valid amount")
          print("-----------------------------------------------------------------------")
          print(f"week : {i["Week"]} contribution is completed")
          outstandingValue =0.00
          for j,k in i["Outstanding"].items():
              outstandingAmount = float(k)
              outstandingValue = outstandingValue +outstandingAmount
          print("-----------------------------------------------------------------------")
          if outstandingValue>0.00:
                  print(f"Amount wont be paid for week : {i["Week"]} as there are outstanding payments")
                  print("see breakdown below")
                  print("-----------------------------------------------------------------------")
                  print(i)
          else:
                  print(f"week : {i["Week"]} payment of GHS {str(totalContribution)} has been made to {currentName}")
                  i["Paid"] = "Yes"
                  print("see breakdown below")
                  print("-----------------------------------------------------------------------")
                  print(i)
          
                      
               

