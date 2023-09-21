import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 네트워크 파일 읽기
file_path = 'Input.csv'
df = pd.read_csv(file_path, index_col=0)

# 빈 그래프 생성
G = nx.Graph()

# 노드 추가
nodes = list(df.columns)
G.add_nodes_from(nodes)

# 엣지 추가
for i, row in df.iterrows():
    for j, weight in row.items():  # iteritems() 대신 items() 사용
        if not pd.isna(weight) and weight > 0:
            G.add_edge(i, j, weight=weight)

# 그래프 시각화
pos = nx.spring_layout(G)  # 그래프 레이아웃 설정
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.axis('off')  # 축 숨기기
plt.show()
