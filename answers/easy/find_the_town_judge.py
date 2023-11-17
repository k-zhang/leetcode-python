def find_the_town_judge(n, trust):
    if n == 1:
        return 1

    trust_map = {}
    judge = -1
    for pair in trust:
        trust_map[pair[0]] = -1
        if judge == pair[0]:
            judge = -1

        key = pair[1]
        r = trust_map.get(key)

        if r is None:
            trust_map[key] = trust_count = 1
        elif r != -1:
            trust_map[key] = trust_count = r + 1
        else:
            trust_map[key] = trust_count = r

        if trust_count == n - 1:
            judge = pair[1]

    return judge
