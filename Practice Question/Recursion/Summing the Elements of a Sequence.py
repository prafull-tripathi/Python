def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

if __name__ == '__main__':
    S=[4,3,6,8,2]
    print(linear_sum(S,5))
