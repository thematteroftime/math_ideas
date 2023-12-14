def Fibonacci(compared_n):
    output_arr = [1, 1]
    count = 2
    n = 20

    while n > count:
        Fib2 = output_arr[count - 1] + output_arr[count - 2]
        output_arr.append(Fib2)
        count += 1
        if compared_n <= output_arr[-1]:
            return output_arr
        if compared_n > output_arr[-1] and n == count:
            n += 5


def produce_p(compared_n, e):
    Fibo_arr = Fibonacci(compared_n)
    N = len(Fibo_arr) - 1
    count = 1
    p_arr = []

    while N != count:
        p_arr.append(cal_p(Fibo_arr, N, count))
        count += 1

    p_arr.pop()
    p_arr.append((1 + 2 * e) / 2)

    return p_arr


def cal_p(Fibo_arr, N, count):
    return 1 - Fibo_arr[N - count] / Fibo_arr[N - count + 1]



