def minimumSwaps(popularity):
    N = len(popularity)

    if not N:
        return 0 # need 0 swaps if there are no items

    p_pos = [*enumerate(popularity)]

    # sort in descending order
    p_pos = p_pos.sort(key= lambda p: p[1], reverse=True)

    # dictionary to keep visited information
    vis = { i : False for i in range(N)}

    res = 0 # default answer
    for i in range(N):

        if vis[i] and p_pos[i][0] == i: # already visited or in right place
            continue

        cycle_len = 0
        # start from the current node and check if have any cycle for this
        # get the number of nodes in this cycle
        # then this cycle can be swapped in (number of node in cycle) - 1
        # this mean if the cycle len is greateer than 2 if have cycle...
        j = i
        while not vis[j]: # iterate till we have completed a cycle
            vis[j] = True

            j = p_pos[j][0] # get the original position of the j in the given array
            cycle_len += 1

        # add to the total..
        if cycle_len > 0: # we have a cycle
            res += (cycle_len -1)

        return res