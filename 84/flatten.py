def flatten(list_of_lists):
    flat_list = []

    for item in list_of_lists:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list