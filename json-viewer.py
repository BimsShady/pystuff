import json
import os
import msvcrt

tree_state = {}

def load_json_file(filename):  # Load JSON data from a file.
    with open(filename, 'r') as file:
        return json.load(file)

def traverse_json(json_obj, path=""):  # Flattens the JSON into a list of tuples (path, key, value_type).
    tree_list = []
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            new_path = f"{path}/{key}"
            tree_list.append((new_path, key, None))
            if tree_state.get(new_path, False):
                tree_list.extend(traverse_json(value, new_path))
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            new_path = f"{path}/{index}"
            tree_list.append((new_path, f"[{index}]", None))
            if tree_state.get(new_path, False):
                tree_list.extend(traverse_json(item, new_path))
    else:
        tree_list.append((path, json_obj, "leaf"))
    return tree_list

def draw_tree(tree_list, current_index):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, (path, key, value_type) in enumerate(tree_list):
        indent = "  " * (path.count("/") - 1)
        line = f"{indent}{'-' if tree_state.get(path, False) else '+'} {key}" if value_type is None else f"{indent}{key}"
        print(f"> {line}" if i == current_index else f"  {line}")

def get_key():
    key = msvcrt.getch()
    if key == b'\xe0':
        return msvcrt.getch()
    return key

def navigate_tree(tree_list, current_index, key):
    path, _, value_type = tree_list[current_index]
    if key == b'H' and current_index > 0: return current_index - 1  # Up
    if key == b'P' and current_index < len(tree_list) - 1: return current_index + 1  # Down
    if key == b'M':  # Right
        if value_type != "leaf":
            if not tree_state.get(path, False):
                tree_state[path] = True
                return current_index  # Expand
            next_index = current_index + 1
            return next_index if next_index < len(tree_list) and tree_list[next_index][0].startswith(path) else current_index  # Go to child
    if key == b'K':  # Left
        if value_type != "leaf" and tree_state.get(path, False):
            tree_state[path] = False  # Collapse
            return current_index
        parent_path = "/".join(path.split("/")[:-1])  # Move to parent
        return next(i for i in range(current_index - 1, -1, -1) if tree_list[i][0] == parent_path) if parent_path else current_index
    return current_index

def main():
    json_data = load_json_file('C:\\Users\\default\\Desktop\\data.json')
    tree_list = traverse_json(json_data)
    current_index = 0
    while True:
        draw_tree(tree_list, current_index)
        key = get_key()
        if key == b'q': break
        current_index = navigate_tree(tree_list, current_index, key)
        tree_list = traverse_json(json_data)  # Refresh tree

if __name__ == "__main__":
    main()