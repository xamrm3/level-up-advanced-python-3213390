def pairwise_offset(sequence, fillvalue="*", offset=0):
    cpy1 = list(sequence) + [fillvalue] * offset
    cpy2 = [fillvalue] * offset + list(sequence)
    return zip(cpy1, cpy2)
