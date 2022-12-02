input = open("./day2_input")

scores_1 = {
    "AX": 1+3,
    "BX": 1+0,
    "CX": 1+6,
    "AY": 2+6,
    "BY": 2+3,
    "CY": 2+0,
    "AZ": 3+0,
    "BZ": 3+6,
    "CZ": 3+3,
}

games = [line.strip().replace(' ', '').replace('\n', '') for line in input]

result = sum([scores_1[game] for game in games])
print(result)
# 15523

scores_2 = {
    "AX": 3+0,
    "BX": 1+0,
    "CX": 2+0,
    "AY": 1+3,
    "BY": 2+3,
    "CY": 3+3,
    "AZ": 2+6,
    "BZ": 3+6,
    "CZ": 1+6,
}

result = sum([scores_2[game] for game in games])
print(result)
# 15702
