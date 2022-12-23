print("ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴘᴇɴ-ʙɪᴅᴅɪɴɢ ᴘʀᴏᴄᴇᴅᴜʀᴇ")
names = input(" write the name of providers (seprate each provider name with a ',')").split(",")
costs = input(" write the cost of offers (seprate each offer name with a ',')").split(",")

rates = []
accepted_names = []
accepted_costs = []

if len(names) != len(costs):
    print(" sorry, the count of names and offers must be equal, you have to write for each provider an offer")
else:
    rate1= float(input(f"wrtie the rate of {names[0]}'s bid with cost {costs[0]}: "))
    if rate1 > 5:
        accepted_names.append(names[0])
        accepted_costs.append(float(costs[0]))
        rates.append(rate1)
    rate2 = float(input(f"wrtie the rate of {names[1]}'s bid with cost {costs[1]}: "))
    if rate2 > 5:
        accepted_names.append(names[1])
        accepted_costs.append(float(costs[1]))
        rates.append(rate2)
    rate3 = float(input(f"wrtie the rate of {names[2]}'s bid with cost {costs[2]}: "))
    if rate3 > 5:
        accepted_names.append(names[2])
        accepted_costs.append(float(costs[2]))
        rates.append(rate3)

    winner_cost = min(accepted_costs)
    accepted_offer = accepted_costs.index(winner_cost)

    print("*=*=**==*=**=*=*=*==*=**=*=*=*=*=*=*=*=")
    print(f"number of offerd bids is {len(costs)}")
    if len(accepted_names) == 0:
        print('there is no accepted offers')
    else:
        print(f"number of accepted bids is {len(accepted_names)}")
        print(f" the winner offer is {accepted_names[accepted_offer]} with cost {accepted_costs[accepted_offer]}")

