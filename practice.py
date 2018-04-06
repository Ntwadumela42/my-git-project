"""Finding the index of the median value"""

def med_value(input):
    import statistics
    return input.index(statistics.median(input))


