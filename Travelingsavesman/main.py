import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import sys


def network():
    file_path = 'Input.csv'
    df = pd.read_csv(file_path, index_col=0)

    G = nx.Graph()

    nodes = list(df.columns)
    G.add_nodes_from(nodes)

    for i, row in df.iterrows():
        for j, weight in row.items():
            if not pd.isna(weight) and weight != sys.maxsize:
                G.add_edge(i, j, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.axis('off')
    plt.show()


def TSP(start_city_input):
    network_data = pd.read_csv('Input.csv', index_col=0)
    network_data.fillna(sys.maxsize, inplace=True)

    city_names = list(network_data.columns)
    city_mapping = {i: city_name for i, city_name in enumerate(city_names)}
    num_cities = len(city_names)
    all_cities = (1 << num_cities) - 1
    dp = [[None] * all_cities for _ in range(num_cities)]

    start_city_input = start_city_input.upper()

    if start_city_input not in city_mapping.values():
        print("입력한 도시가 존재하지 않습니다.")
        return

    start_city_index = city_names.index(start_city_input)

    def tsp(current_city, visited_cities, start_city):
        if visited_cities == all_cities:
            return network_data.iloc[current_city][start_city], [city_mapping[start_city]]

        if dp[current_city][visited_cities] is not None:
            return dp[current_city][visited_cities]

        min_distance = sys.maxsize
        min_path = None

        for next_city in range(num_cities):
            if not (visited_cities & (1 << next_city)):
                next_distance, next_path = tsp(next_city, visited_cities | (1 << next_city), start_city)
                distance = network_data.iloc[current_city][next_city] + next_distance

                if distance < min_distance:
                    min_distance = distance
                    min_path = [city_mapping[next_city]] + next_path

        dp[current_city][visited_cities] = (min_distance, min_path)
        return dp[current_city][visited_cities]

    shortest_distance, shortest_path = tsp(start_city_index, 1 << start_city_index, start_city_index)
    print("최단 거리:", shortest_distance)
    print("최단 경로:", start_city_input,"->", " -> ".join(shortest_path))


if __name__ == '__main__':
    start_city_input = input("시작 도시를 입력하세요 (알파벳): ")
    TSP(start_city_input)
    network()
