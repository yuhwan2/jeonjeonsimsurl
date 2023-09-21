import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def network():
    file_path = 'Input.csv'
    df = pd.read_csv(file_path, index_col=0)

    G = nx.Graph()

    nodes = list(df.columns)
    G.add_nodes_from(nodes)

    for i, row in df.iterrows():
        for j, weight in row.items():
            if not pd.isna(weight) and weight > 0:
                G.add_edge(i, j, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis('off')
    plt.show()

def dijkstra():
    Network = pd.read_csv(filepath_or_buffer='Input.csv', index_col=[0])
    Start = input('출발점 입력 : ')
    End = input('도착점 입력 : ')
    Range = list(Network.columns)

    LN = 10000
    Saver = {node: LN for node in Range}
    Saver[Start] = 0
    Track = Saver.copy()
    StartSet = [Start]

    while True:
        for n in Range:
            Distance = Network.loc[Start, n]

            if Distance == 0:
                continue

            elif ~np.isnan(Distance):
                if Saver[n] <= Saver[Start] + Distance:
                    continue

                elif Saver[n] > Saver[Start] + Distance:
                    Saver[n] = Saver[Start] + Distance
                    Track[n] = Start
                else:
                    print('error')

        Range.remove(Start)
        Temp = Saver.copy()

        list(map(lambda x: Temp.pop(x), StartSet))
        B = list(Temp.values())
        if not B:
            break
        Start = Range[B.index(min(B))]
        StartSet.append(Start)

    path = []
    while True:
        path.append(End)
        End = Track[End]

        if End == 0:
            break

    path.reverse()

    for i in path:
        print(i + '-', end = '')
    print('도착')


if __name__ == '__main__':

    dijkstra()
    network()


