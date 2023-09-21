import pandas as pd
import numpy as np
import sys

# Input.csv 파일을 읽어오기
network_data = pd.read_csv('Input.csv', index_col=0)

# 도시 수
num_cities = len(network_data)

# 모든 도시를 비트마스크로 표현
all_cities = (1 << num_cities) - 1

# 동적 프로그래밍을 위한 Memoization 테이블 초기화
dp = [[None] * all_cities for _ in range(num_cities)]


def tsp(current_city, visited_cities, start_city):
    # 모든 도시를 방문한 경우
    if visited_cities == all_cities:
        return network_data.iloc[current_city, start_city], [current_city, start_city]

    # Memoization
    if dp[current_city][visited_cities] is not None:
        return dp[current_city][visited_cities]

    min_distance = sys.maxsize
    min_path = None

    for next_city in range(num_cities):
        if (visited_cities >> next_city) & 1 == 0:
            distance, path = tsp(next_city, visited_cities | (1 << next_city), start_city)
            distance += network_data.iloc[current_city, next_city]

            if distance < min_distance:
                min_distance = distance
                min_path = [current_city] + path

    # Memoization 업데이트
    dp[current_city][visited_cities] = (min_distance, min_path)
    return dp[current_city][visited_cities]


# 시작 도시를 0번 도시로 설정하여 TSP 알고리즘 실행
shortest_distance, shortest_path = tsp(0, 1, 0)

print("최단 거리:", shortest_distance)
print("최단 경로:", shortest_path)
