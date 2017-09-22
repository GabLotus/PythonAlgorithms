import sys

def changeGenerator(change, coin_stack, options):
    if change == 0:
        if coin_stack not in options:
            options.append(coin_stack)
    else:
        if change >= 25:
            coin_a = dict(coin_stack)
            coin_a["25"] += 1
            changeGenerator(change - 25, coin_a, options)
        if change >= 10:
            coin_b = dict(coin_stack)
            coin_b["10"] += 1
            changeGenerator(change - 10, coin_b, options)
        if change >= 5:
            coin_c = dict(coin_stack)
            coin_c["5"] += 1
            changeGenerator(change - 5, coin_c, options)
        if change >= 1:
            coin_d = dict(coin_stack)
            coin_d["1"] += 1
            changeGenerator(change - 1, coin_d, options)

if len(sys.argv) > 1:
    change = int(sys.argv[1])
else:
    change = 31
coin_stack = { "25": 0, "10": 0, "5": 0, "1": 0}
options = []
changeGenerator(10, coin_stack, options)
print(options)