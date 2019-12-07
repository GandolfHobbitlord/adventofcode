from collections import defaultdict
import os

#next time use import networkx
def get_num_of_connections(d, key):
    connections = 0
    for c in d.copy()[key]:
        connections +=1
        connections += get_num_of_connections(d, c)

    return connections

def find_san(d, key, jumps = 0, traveled = set()):
    if str("SAN") in d[key]:
        return jumps - 1 #UGLY but yeah, last jump was uncessecary
    min_conns_to_san = 9999999
    for c in d[key]:
        if c in traveled:
            continue
        else:
            traveled.add(c)
            conns_to_san = find_san(d,c,jumps+1, traveled)
            if conns_to_san < min_conns_to_san:
                min_conns_to_san =  conns_to_san
    return min_conns_to_san

    
with open(os.path.join("day6","input_day6.txt")) as f:
    data = [c.split(')') for c in (f.read().split('\n'))]
    dag = defaultdict(set) # DAG
    uag = defaultdict(set) # Undirected
    for k, v in data:
        dag[k].add(v)
        uag[k].add(v)
        uag[v].add(k)

    tot = 0
    for key, _ in dag.items():
        tot += get_num_of_connections(dag,key)
    print("Total connections {}".format(tot))
    print("Minimum distance to santa {}".format(find_san(uag,"YOU",0,set({"YOU"}))))
