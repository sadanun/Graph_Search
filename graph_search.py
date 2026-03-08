
def read_file(file_name):

    # Check if file exists 
    try:
        with open(file_name, 'r') as f:
            pass
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")   
        return 
    # Check file .csv 
    if not file_name.endswith('.csv'):     
        print(f"Error: File '{file_name}' is not a CSV file.")   
        return 
    
    graph = {}

    for line in open(file_name, 'r'):
        parts = line.strip().split(',')

        # Check if line has at least 3 parts (node1, node2, cost)
        if  len(parts) < 3: 
            print(f"Error: Invalid line format: {parts}")  
            return
        
        parts = line.strip().split(',')
        node1, node2, cost = parts[0], parts[1], parts[2].strip()

        # Check if cost is a valid number
        try:
            cost = int(cost)
        except ValueError:
            print(f"Error: '{cost}' is not a valid number.")     
            return

        # Add nodes and cost to the graph 
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = cost
        graph[node2][node1] = cost

    return graph
    
def find_path(graph, start, goal):

    # Convert start and goal to uppercase 
    start = start.upper()
    goal = goal.upper()

    # Check if start and goal nodes exist in the graph
    if start not in graph or goal not in graph:
        return None, None
    
    elif start == goal:
        return [start], 0
    
    queue = [(0, [start])]  
    
    shortest_path = None
    min_total_cost = float('inf')

    while(len(queue) >  0 ):
        queue.sort()
        curent_cost , current_path = queue.pop(0)
        current_node = current_path[-1]

        if current_node == goal:
            if curent_cost < min_total_cost:
                min_total_cost = curent_cost
                shortest_path = current_path
            continue
        
        # ex Data : graph = {
        #     'A': {'B': 5, 'C': 10},  
        #     'B': {'A': 5, 'C': 3},
        #     'C': {'A': 10, 'B': 3},
        # }
        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in current_path: 
                new_cost = curent_cost + weight
                queue.append((new_cost, current_path + [neighbor]))
         
    return shortest_path, min_total_cost
    

def run_app():
    file_name = input("Enter file name: ").strip()
    ## Check if file exists before trying to read it

    
    data = read_file(file_name)
    if data is None:
        print("File not found.")
        return
    
    start = input("What is start node?: ").strip()
    
    goal = input("What is goal node?: ").strip()

    value , cost = find_path(data, start, goal)

    if value is not None:
        print(f"Path from {start} to {goal} is {'->'.join(value)}, and have cost {cost}.")
    else:
        print(f"No path found from {start} to {goal}.")   



if __name__ == "__main__":
    run_app()
