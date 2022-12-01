def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    result = []
    counter = 3
    while counter > 0:
        top_score = personal_best(scores)
        result.append(top_score)
        scores.remove(top_score)
        counter -= 1
    
    return result

def highest_to_lowest(scores):
    return sorted(scores, reverse=True)

def top_three_tie(scores):
    list = [*set(scores)]
    return personal_top_three(list)

def top_three_less_than_three(scores):
    result = []
    counter = 3
    while counter > 0 and len(scores) > 0:
        top_score = personal_best(scores)
        result.append(top_score)
        scores.remove(top_score)
        counter -= 1
    
    return result