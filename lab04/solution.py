names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
def winner(names: list[str], scores: list[float]) -> str:
    return names[scores.index(max(scores))]


def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def ranking(names, scores):
    result = []
    for i in range(len(names)):
        result.append((scores[i],names[i]))
    result.sort(reverse = True)
    return [name for _, name in result]


def above_average(names, scores):
    namebest = []
    ave = average(scores)
    for i in range(len(scores)):
        if scores[i] > ave:
            namebest.append(names[i])
    return namebest


print(winner(names,scores), average(scores), ranking(names,scores), above_average(names,scores))