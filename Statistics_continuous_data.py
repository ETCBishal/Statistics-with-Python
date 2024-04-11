from functools import reduce

classInterval = ["0-50", "50-100", "100-150", "150-200", "200-250"]
frequency = [1, 5, 6, 3, 80]


# i^th position calculator
def locator(i):
    pos_i = pos(i, c_f((frequency))[-1])
    c_cf = list(filter(lambda x: x >= pos_i, c_f(frequency)))
    helper = classInterval[c_f(frequency).index(c_cf[0])].split("-")
    l = int(helper[0])
    f = frequency[c_f(frequency).index(c_cf[0])]
    p_cf = c_f(frequency)[(frequency.index(f) - 1)]
    i = int(helper[1]) - l

    return pos_i, l, f, p_cf, i


pos = lambda i, n: i * (n / 4)


def middle_value(x):
    m = []
    helper = []

    init = 0
    nxt = 1

    for item in x:
        classs = item.split("-")
        for i in classs:
            helper.append(int(i))

    for i in range(len(helper)):
        if nxt < len(helper):
            avg = lambda a, b: (a + b) / 2
            average = avg(helper[init], helper[nxt])
            init += 2
            nxt += 2
            m.append(average)

    return m


# c.f
def c_f(freq):
    cnt = 0
    _cf = []
    _cf.append(freq[0])

    for i in range(1, len(freq)):
        if cnt < len(freq):
            _cf.append(_cf[cnt] + freq[i])
            cnt += 1

    return _cf


# fm
def _fm(f, m):
    _fm = []
    for i in range(len(f)):
        fm = f[i] * m[i]
        _fm.append(fm)

    return _fm


# mean

operation = int(
    input(
        "\nPlease select an operation\n1.Mean\n2.Upper quartile(Q3)\n3.Lower quartile(Q1)\n4.Median/Q2\n5.Mode\n>> "
    )
)

if operation == 1:

    def mean(f):
        m = middle_value(x=classInterval)
        fm = _fm(f=f, m=m)
        n = c_f(frequency)[-1]
        summessionFM = reduce(lambda x, y: x + y, fm)
        return summessionFM / n

    print(f"x: {classInterval}")

    print(f"f: {frequency}")

    mv = middle_value(classInterval)
    print(f"m: {mv}")

    fm = _fm(frequency, mv)
    print(f"fm: {fm}")

    mean = mean(f=frequency)
    print(f"Mean: {mean}")

elif operation == 2:
    # Q3
    def Upper_quartile():
        pos_i, l, f, p_cf, i = locator(3)
        print(
            f"\nClass-Interval(x): {classInterval}\nFrequency     (f): {frequency}\nPosition of (Q3): {pos_i}\nl: {l}  f: {f}  c.f: {p_cf}  i: {i}\n"
        )
        return l + ((pos_i - p_cf) / f) * i

    Q3 = Upper_quartile()
    print(f"Upper Quartile (Q3):  {Q3}")

elif operation == 3:
    # Q1

    def Lower_quartile():
        pos_i, l, f, p_cf, i = locator(1)
        print(
            f"\nClass-Interval(x): {classInterval}\nFrequency     (f): {frequency}\nPosition of (Q1): {pos_i}\nl: {l}  f: {f}  c.f: {p_cf}  i: {i}\n"
        )
        return l + ((pos_i - p_cf) / f) * i

    Q1 = Lower_quartile()
    print(f"Lower Quartile (Q1):  {Q1}")


elif operation == 4:
    # median or Q2
    def median():
        pos_i, l, f, p_cf, i = locator(2)
        print(
            f"\nClass-Interval(x): {classInterval}\nFrequency     (f): {frequency}\nPosition of median or  (Q2): {pos_i}\nl: {l}  f: {f}  c.f: {p_cf}  i: {i}\n"
        )
        return l + ((pos_i - p_cf) / f) * i

    md = median()
    print(f"Median(Md) or 2nd Quartile (Q2):  {md}")

elif operation == 5:
    # mode
    def mode(f):
        f1 = max(f)
        f1_index = f.index(f1)
        helper = classInterval[f1_index].split("-")
        l = int(helper[0])
        f0 = f[f1_index - 1]
        f2 = 0
        i = int(helper[1]) - l

        try:
            f2 = f2 + f[f1_index + 1]

        except:
            f2 = f2 + 0

        print(
            f"\nClass-Interval(x): {classInterval}\nFrequency     (f): {frequency}\nl:{l}  f1:{f1}  f0:{f0}  f2:{f2}  i:{i}"
        )
        return l + ((f1 - f0) / (2 * f1 - f0 - f2)) * i

    mo = mode(frequency)
    print(f"\nMode:{mo}")

