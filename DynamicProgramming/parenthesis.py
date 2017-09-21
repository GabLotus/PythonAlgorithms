def generatePossibilities(n, possibilities):
    generateParenthesisChain(n, 0, "", possibilities)


def generateParenthesisChain(n_left, n_right, chain, possibilities):
    if n_left == 0 and n_right == 0:
        possibilities.append(chain)
    if n_left > 0:
        generateParenthesisChain(n_left - 1, n_right + 1, chain + "(", possibilities)
    if n_right > 0:
        generateParenthesisChain(n_left, n_right - 1, chain + ")", possibilities)
    

possibilities = []
generatePossibilities(4, possibilities)
print(possibilities)
