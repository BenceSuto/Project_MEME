def print_menu(title, list_options, exit_message):
    print(title+' :')
    for index, menu in enumerate(list_options, 1):
        print("("+str(index)+") "+menu)
    print("(0) "+exit_message)


def get_inputs(list_labels, title):
    inputs = []

    print(title)
    for i in range(len(list_labels)):
        inputs.append(input(list_labels[i]))
    return inputs
