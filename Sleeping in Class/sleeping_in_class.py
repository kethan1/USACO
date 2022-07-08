T = int(input())
test_cases = [
    [int(input()), list(map(int, input().split()))] for _ in range(T)
]


for test_case in test_cases:
    N, a = test_case
    sum_a = sum(a)
    for r in range(N, 0, -1):
        if sum_a % r == 0:
            range_sum = sum_a / r
            current_range_sum = 0
            for times_slept in a:
                current_range_sum += times_slept
                if current_range_sum > range_sum:
                    break
                if current_range_sum == range_sum:
                    current_range_sum = 0
            else:
                print(N - r)
                break
