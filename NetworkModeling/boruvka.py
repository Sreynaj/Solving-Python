# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/minimum-spanning-trees-boruvkas-algorithm/#borvkasalgorithm
# class Graph:

def __init__(self, num_of_nodes):
    self.m_v = num_of_nodes
    self.m_edges = []
    self.m_component = {}
        
        
        
def add_edge(self, u, v, weight):
        self.m_edges.append([u, v, weight])
    
    
    
    
def find_component(self, u):
    if self.m_component[u] == u:
        return u
    return self.find_component(self.m_component[u])

def set_component(self, u):
    if self.m_component[u] == u:
        return
    else:
        for k in self.m_component.keys():
            self.m_component[k] = self.find_component(k)
            
            
            
def union(self, component_size, u, v):
    if component_size[u] <= component_size[v]:
        self.m_component[u] = v
        component_size[v] += component_size[u]
        self.set_component(u)

    elif component_size[u] >= component_size[v]:
        self.m_component[v] = self.find_component(u)
        component_size[u] += component_size[v]
        self.set_component(v)

    print(self.m_component)
        
        
        
def boruvka(self):
    component_size = []
    mst_weight = 0

    minimum_weight_edge = [-1] * self.m_v

    for node in range(self.m_v):
        self.m_component.update({node: node})
        component_size.append(1)

    num_of_components = self.m_v

    print("---------Forming MST------------")
    while num_of_components > 1:
        for i in range(len(self.m_edges)):

            u = self.m_edges[i][0]
            v = self.m_edges[i][1]
            w = self.m_edges[i][2]

            u_component = self.m_component[u]
            v_component = self.m_component[v]

            if u_component != v_component:
                if minimum_weight_edge[u_component] == -1 or \
                        minimum_weight_edge[u_component][2] > w:
                    minimum_weight_edge[u_component] = [u, v, w]
                if minimum_weight_edge[v_component] == -1 or \
                        minimum_weight_edge[v_component][2] > w:
                    minimum_weight_edge[v_component] = [u, v, w]

        for node in range(self.m_v):
            if minimum_weight_edge[node] != -1:
                u = minimum_weight_edge[node][0]
                v = minimum_weight_edge[node][1]
                w = minimum_weight_edge[node][2]

                u_component = self.m_component[u]
                v_component = self.m_component[v]

                if u_component != v_component:
                    mst_weight += w
                    self.union(component_size, u_component, v_component)
                    print("Added edge [" + str(u) + " - "
                            + str(v) + "]\n"
                            + "Added weight: " + str(w) + "\n")
                    num_of_components -= 1

        minimum_weight_edge = [-1] * self.m_v
    print("----------------------------------")
    print("The total weight of the minimal spanning tree is: " + str(mst_weight))
        
        
        
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3)

g.boruvka()        
