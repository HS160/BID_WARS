def highest(dic):
    highest_bid = 0
    highest_bidder = ""
    for key in dic:
        if dic[key] > highest_bid:
            highest_bid = dic[key]
            highest_bidder = key
    return highest_bidder

def looping():
    for i in range(1,101):
        print("\n")
        
print("""
    **********************************************
     ____ ___ ____   __        ___    ____  ____  
    | __ )_ _|  _ \  \ \      / / \  |  _ \/ ___| 
    |  _ \| || | | |  \ \ /\ / / _ \ | |_) \___ \ 
    | |_) | || |_| |   \ V  V / ___ \|  _ < ___) |
    |____/___|____/     \_/\_/_/   \_\_| \_\____/ 
    
    **********************************************
      """)

should_continue = True
bid = {}

while should_continue:
    name = input("Enter Name:\n")
    bid_amount = int(input("Enter Bid amount in $\n"))
    
    bid[name] = bid_amount
    
    choose = input("Is there any other Bidder ('Yes' or 'No')").lower()
    
    if choose == 'no':
        break
    elif choose == 'yes':
        looping()

winner = highest(bid)

print(f"Winner of bid is {winner}!!\n")