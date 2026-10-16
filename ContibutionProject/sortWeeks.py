def SortWeeks(MembersList: list):
    Analysis = []
    for i in MembersList:
        id = i["ID"]
        Name = i["Name"]
        contribution = i["Contribution"]
        Analysis.append({"Week":id,
                         "Paid": "No",
                         "receiver": Name,
                         "Contributions":{x["Name"]: str(x["Contribution"]) for x in MembersList},
                         "Outstanding":{x["Name"]: str(x["Contribution"]) for x in MembersList}})
    return Analysis

