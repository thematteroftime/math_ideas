import pandas as pd


def Euclid_method(m, n, choice, i=1, m_arr=None, n_arr=None):
    if m == 0:
        return n, pd.DataFrame(data=[m_arr, n_arr])
    if n == 0:
        return m, pd.DataFrame(data=[m_arr, n_arr])

    if m >= n:
        m = m % n
    else:
        n = n % m

    if choice == True:
        str = f"{i}"
        m_arr.append([f"{'m' + str}", m])
        n_arr.append([f"{'n' + str}", n])

    return Euclid_method(m, n, choice, i + 1, m_arr, n_arr)


def operate_Euclid(m, n, choice=False):
    if (m <= 0 and m * n >= 0) or m * n <= 0:
        return Warning

    return Euclid_method(m, n, choice, i=1, m_arr=[["m0", m]], n_arr=[["n0", n]])


result, arr = operate_Euclid(135, 315, choice=True)
print(result)
print(arr)
