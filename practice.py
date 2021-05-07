counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for x in counties_dict:
    print(f"{x} county has {counties_dict[x]} registered users")


# 2
print("# exercise 2")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

for x in voting_data:
    print(f"{x['county']} has {x['registered_voters']} registered users")