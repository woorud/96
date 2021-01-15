def _14888():
    global n, max_value, min_value
    def cal(num, idx, plus, minus, mul, div):
        global n, max_value, min_value
        if idx == n:
            max_value = max(num, max_value)
            min_value = min(num, min_value)
            return
        else:
            if plus >= 1:
                cal(num+num_list[idx], idx+1, plus-1, minus, mul, div)
            if minus >= 1:
                cal(num-num_list[idx], idx+1, plus, minus-1, mul, div)
            if mul >= 1:
                cal(num*num_list[idx], idx+1, plus, minus, mul-1, div)
            if div >= 1:
                cal(int(num/num_list[idx]), idx+1, plus, minus, mul, div-1)

    n = int(input())
    num_list = list(map(int, input().split()))
    plus, minus, mul, div = map(int, input().split())
    max_value = -100000000
    min_value = 100000000
    cal(num_list[0], 1, plus, minus, mul, div)
    print(max_value)
    print(min_value)

_14888()