"""
[Gold 4] 백준 15683번 감시

사무실은 N X M 크기의 직사각형
총 K 개의 CCTV. 5종류임
1번: 단방향
2번: 양방향 (두 방향은 반대)
3번: 양방향 (두 방향은 직각)
4번: 삼방향
5번: 사방향

지도에서 0: 빈칸
    1~5: CCTV
    6: 벽

CCTV는 CCTV 통과 가능, 벽은 통과 못함

입력: 
    첫째 줄: N M - 세로 크기, 가로 크기 (1 <= N, M <= 8)
    ~N개 줄: 사무실 칸 정보 mat (CCTV 최대 개수는 8개 넘지 않음)

출력:
    첫째 줄에 사각 지대의 최소 크기 출력
"""

"""
1. cctv 위치가 담긴 queue deepcopy

"""

import sys
from collections import deque
from copy import deepcopy

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def get_observe_dir(type):
    match type:
        case 1:
            return [[0], [1], [2], [3]]
        case 2:
            return [[0, 2], [1, 3]]
        case 3:
            return [[0, 1], [1, 2], [2, 3], [3, 0]]
        case 4:
            return [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
        case 5:
            return [[0, 1, 2, 3]]


def observe(r, c, directions, mat_copy):
    for dir in directions:
        nr, nc = r, c
        while True:
            nr += dirs[dir][0]
            nc += dirs[dir][1]
            if 0 <= nr < N and 0 <= nc < M and mat_copy[nr][nc] != 6:
                if mat_copy[nr][nc] == 0:
                    mat_copy[nr][nc] = -1
            else:
                break


def dfs(depth, mat):
    if depth == len(cctvs):
        return sum(row.count(0) for row in mat)

    r, c, type = cctvs[depth]
    ret = float("inf")

    for direction in get_observe_dir(type):
        mat_copy = [row[:] for row in mat]
        observe(r, c, direction, mat_copy)

        ret = min(ret, dfs(depth + 1, mat_copy))

    return ret


if __name__ == "__main__":
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    cctvs = []
    for i in range(N):
        for j in range(M):
            if 1 <= mat[i][j] <= 5:
                cctvs.append((i, j, mat[i][j]))

    #
    ans = dfs(0, mat)
    print(ans)
