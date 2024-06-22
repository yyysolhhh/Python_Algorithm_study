def solution(N):
    bin_N = bin(N)
    gap = list(str(bin_N).rstrip("0").split("1"))[1:]
    gap_len = map(len, gap)
    return max(gap_len)
