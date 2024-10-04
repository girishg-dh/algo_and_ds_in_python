from typing import List
# Write any import statements here

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
    tunnels = sorted(zip(A,B))
    tunnel_time_per_round = sum(end - start for start, end in tunnels)
    if tunnel_time_per_round == 0:
        return -1
    total_time = 0
    if tunnel_time_per_round <= K:
        total_time += (K // tunnel_time_per_round) * C
        K = K % tunnel_time_per_round
    for start, end in tunnels:
        next_tunnel_time = end - start
        if next_tunnel_time < K:
            K -= next_tunnel_time
        else:
            total_time += start + K
            K = 0
            return total_time
    return -1 

print(getSecondsElapsed(10, 2, [1, 6], [3, 7], 7))
print(getSecondsElapsed(50, 3, [39, 19, 28], [49, 27, 35], 15))


