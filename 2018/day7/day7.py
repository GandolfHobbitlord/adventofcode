from collections import defaultdict 

nodes = defaultdict(list)
num_edges = defaultdict(int) #number of INCOMING edges (makes sence for problem)
f = open(r"day7\input.txt")
for line in f.readlines():
    word = line.split(" ")
    nodes[word[1]].append(word[7])
    num_edges[word[7]] += 1
    num_edges[word[1]] #add to list at least
print(nodes)

for k in nodes:
    nodes[k].sort()

def complete_work(S, work_node):
    for out in nodes[work_node]:
        num_edges[out] -= 1
        if num_edges[out] == 0:
            S.append(out)
    return S

def do_work(S):
    num_of_workers = 5
    working = {}
    time = 0
    L = []
    while len(L) != len(num_edges):
        if S and len(working) < num_of_workers: 
            S.sort()
            work_node = S.pop(0)
            working[work_node] =  60+1 + ord(work_node) - ord('A')
            print("Starting work on ", work_node, "time is ", working[work_node])
        else:
            working_copy = dict(working)
            for node in working_copy:
                if working[node] == 0:
                    working.pop(node)
                    S=complete_work(S,node)
                    L.append(node)
            if not S or len(working) == num_of_workers:
                time +=1
                print("T:", time)
                for k in working:
                    working[k] -= 1
    print(time-1) #ticks one time too many
    return L

Q = []
roots = [k for k,v in num_edges.items() if not v]
roots.sort()
for r in roots:
    Q.append(r)
sorted_list = do_work(Q)
print(sorted_list)
