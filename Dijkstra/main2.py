import numpy as np
import pandas as pd

if __name__ == '__main__':
    Network = pd.read_csv(filepath_or_buffer='Input.csv', index_col=[0])
    Start = input("출발점을 입력하세요: ")
    End = input("도착점을 입력하세요: ")
    Range = list(Network.columns)

    LN = 10000
    Saver = {'A': LN, 'B': LN, 'C': LN, 'D': LN, 'E': LN, 'F': LN, 'G': LN, 'H': LN}
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

    # 최소 경로를 출력합니다
    path = []
    current_node = End
    while current_node != Start:
        path.append(current_node)
        current_node = Track[current_node]
    path.append(Start)
    path.reverse()

    print(f"최소 경로: {' -> '.join(path)}")
