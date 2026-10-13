names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
def winner(names, scores):
    return names[scores.index(max(scores))]


def average(scores: list):
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def ranking(names, scores):
    result = []
    for i in range(len(names)):
        result.append((names[i], scores[i]))
    result.sort(key=lambda x: x[1], reverse=True)
    return [name for name, _ in result]


def above_average(names, scores):
    namebest = []
    ave = average(scores)
    for i in range(len(scores)):
        if scores[i] > ave:
            namebest.append(names[i])
    return namebest

if __name__== '__main__':
    names = ['Аня','Боря','Вика']
    scores = [7.0,9.0,9.0]
    print(winner(names,scores),f'{average(scores):.2f}',ranking(names,scores), above_average(names,scores))
