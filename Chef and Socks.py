# Problem
#Today, Chef woke up to find that he had no clean socks. Doing laundry is such a turn-off for Chef, that in such a situation, he always buys new socks instead of cleaning the old dirty ones. He arrived at the fashion store with money rupees in his pocket and started looking for socks. Everything looked good, but then Chef saw a new jacket which cost jacketCost rupees. The jacket was so nice that he could not stop himself from buying it.
# Interestingly, the shop only stocks one kind of socks, enabling them to take the unsual route of selling single socks, instead of the more common way of selling in pairs. Each of the socks costs sockCost rupees.
# Chef bought as many socks as he could with his remaining money. It's guaranteed that the shop has more socks than Chef can buy. But now, he is interested in the question: will there be a day when he will have only 1 clean sock, if he uses a pair of socks each day starting tommorow? If such an unlucky day exists, output "Unlucky Chef", otherwise output "Lucky Chef". Remember that Chef never cleans or reuses any socks used once.

# Input
# The first line of input contains three integers — jacketCost, sockCost, money — denoting the cost of a jacket, cost of a single sock, and the initial amount of money Chef has, respectively.
# Output
# In a single line, output "Unlucky Chef" if such a day exists. Otherwise, output "Lucky Chef".

# cook your dish here
JC , SC , M = list(map(int, input().split()))
left_money = M - JC
left_money=left_money//SC
if (left_money%2==0):
    print("Lucky Chef")
else:
    print("Unlucky Chef")