def combination(n, m):
    if n < m:
        return 0

    iteration = m

    member = 1
    denominator = 1
    result = 1

    if m != 0:
        for i in range(iteration):
            member *= n
            n -= 1
            denominator *= m
            m -= 1
        result = member / denominator

    return result


