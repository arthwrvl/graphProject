#João Arthur e Humberto Barbosa
import networkx as nx
import itertools
import matplotlib.pyplot as plt

def get_path(graph, start):
    # gerar todas as permutações partindo do vertice inicial
    nodes = list(graph.nodes())
    nodes.remove(start)
    permutations = list(itertools.permutations(nodes))

    # inicializando as variaveis
    min_cost = float('inf')
    best_path = None

    # passar por todas as permutações e encontrar o custo total
    for permutation in permutations:
        current_cost = graph[start][permutation[0]]['weight']
        for i in range(len(permutation)-1):
            current_cost += graph[permutation[i]][permutation[i+1]]['weight']
        current_cost += graph[permutation[-1]][start]['weight']

        # Atualizar o custo, caso uma menor seja encontrada
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = (start,) + permutation + (start,)

    return best_path, min_cost


# criando o grafo
graph = nx.Graph()
graph.add_edge('DEPOSITO', 'DOCERIA', weight=4)
graph.add_edge('DEPOSITO', 'FARMACIA', weight=3)
graph.add_edge('DEPOSITO', 'DENTISTA', weight=6)
graph.add_edge('DOCERIA', 'FARMACIA', weight=5)
graph.add_edge('DOCERIA', 'DENTISTA', weight=3)
graph.add_edge('FARMACIA', 'DENTISTA', weight=4)

start_node = 'DEPOSITO'

best_path, min_distance = get_path(graph, start_node)

# Desenhar o grafo na tela com o caminho a ser seguido
pos = nx.spring_layout(graph)
fig = plt.figure(facecolor='#2d3436')
nx.draw_networkx(graph, pos, with_labels=True, node_color='#6c5ce7', node_size=500)
nx.draw_networkx_labels(graph, pos, font_color='#dfe6e9')
path_text = ' -> '.join(best_path)
plt.text(0.5, -0.05, f'Caminho a ser seguido: {path_text}', transform=plt.gca().transAxes, ha='center', color='#dfe6e9')
plt.text(0.5, -0.1, f'Custo: {min_distance}', transform=plt.gca().transAxes, ha='center', color='#dfe6e9')
plt.title('entrega de rapadura', color='#dfe6e9')

plt.axis('off')
plt.show()
