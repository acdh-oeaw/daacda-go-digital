def flatten_graphs(graphs):
    nodes = []
    edges = []
    for x in graphs:
        for n in x['nodes']:
            nodes.append(n)
        for n in x['edges']:
            edges.append(n)
    return {
        'nodes': nodes,
        'edges': edges
    }
