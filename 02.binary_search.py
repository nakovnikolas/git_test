def binary_search(list, start, end, search):
    #find the mid point
    if end >= start:
        mid = start + (end - start) // 2
    
    #split the list based on the searched item
    if list[mid] == search:
        return f'The searched item: {str(search)} is at position: {str(mid + 1)}'
    elif list[mid] > search:
        return binary_search(list, start, mid-1, search)
    elif list[mid] < search:
        return binary_search(list, mid+1, end, search)
    else:
        return f'The searched item: {str(search)} is not in the list'
    
    
