def getMembers():
    membersList =[]
    print("please add members to the Contribution list")
    Names = input("Enter a name for member : ")
    Names = Names.strip().capitalize()
    print(f"The Name you entered is {Names}")
    id = 1
    membersList = [{"ID":id,"Name": Names, "Contribution":0.00}]
    
    addMore = False
    while addMore == False:
        print("will you like to add more member(s)?")
        print("Yes/No ?")
        myChoice = input("Enter your choice : ")
        myChoice = myChoice.strip().lower()
        if myChoice == "yes":
            Names = input("Enter a name for member : ")
            if Names =="":
              pass
            elif any(member["Name"] == Names for member in membersList):
               print(f"Error: {Names} is already a member of this Susu group!")
            else:
              Names = Names.strip().capitalize()
              id = id + 1
              membersList.append({"ID":id,"Name":Names,"Contribution":0.00})
        elif myChoice == "no":
            addMore = True
            print("ID  Name  Contribution")
            for i in membersList:
                print(str(i["ID"]) + " " + i["Name"] + " " + f"{i['Contribution']:.2f}")    
        else:
            print("invalid name enter, please try again")
    print("-----------------------------------------------------------------------")
    print(f"Total number of member(s) in the contribution team is {len(membersList)}")
    print(f"The contribution will run for {len(membersList)} week(s)")
    print("-----------------------------------------------------------------------")
    return membersList
