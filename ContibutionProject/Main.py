import GetContributionAmount
import GetAllMembers
import sortWeeks
import getContributions

print("weekly contribution project starts now...")
print("As contribution is about to start, enter the weekly contirbution amount")
print("-----------------------------------------------------------------------")
amount = GetContributionAmount.GetAmount()
memberList = GetAllMembers.getMembers()
Analysis = sortWeeks.SortWeeks(memberList)
print(Analysis)
getContributions.GetContribution(Analysis, amount)
#ContributionBreakDown = getContributions(Analysis, amount)
#print(Analysis)
