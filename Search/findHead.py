def findHead(ar):
    head = ar[0] 
    for index, value in enumerate(ar):
        if value < head:
            return index
    return 0