from collections import deque

class HTMLGraphSearchBFS:
    def __init__(self, graph, content_dict):
        self.graph = graph
        self.content_dict = content_dict

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        content_list = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                content_list.append(self.content_dict.get(node, ""))
                visited.add(node)
                queue.extend(child for child in self.graph.get(node, []) if child not in visited)
        return content_list
