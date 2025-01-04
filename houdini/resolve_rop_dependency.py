import hou

class CustomFetchNode():

    def __init__(self, node):
        self.node = node
        self.name = node.name()
        self.inputs = []

    def __str__(self):
        return self.name

    def addInput(self, custome_fetch_node):
        self.inputs.append(custome_fetch_node)

    def inputs(self):
        return self.inputs()


def getAncestors(node, ordered_list=None, current_thread=None):
    if not ordered_list:
        ordered_list = []
    if not current_thread:
        current_thread = []

    for input in node.inputs:
        current_thread.append(input.name)
        if len(input.inputs) == 0:
            # Reaching the end of the road, add it to the list
            current_thread = [c for c in current_thread if c not in ordered_list]
            if current_thread:
                ordered_list += current_thread
                current_thread = []
        elif input.name in ordered_list:
            # Found the anchor point, insert it
            index = ordered_list.index(input.name)
            [ordered_list.insert(index, n)  for n in reversed(current_thread) if n not in ordered_list]

            # Reset thread
            current_thread = []

        ordered_list, current_thread = getAncestors(input, ordered_list, current_thread)

    return ordered_list, current_thread



root_node = hou.node('/obj/OUT')
ordered_list, current_thread = getAncestors(root_node)

print(ordered_list)

