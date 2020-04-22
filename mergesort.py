def mergesort(mlist):
    if len(mlist) > 1:
        mid = len(mlist) //2
        lefthalf = mlist[:mid]
        righthalf = mlist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        merge(mlist, lefthalf, righthalf)
def merge(mlist, lefthalf, righthalf):
    li =0
    ri=0
    sorti=0
    while li < len(lefthalf) and ri < len(righthalf):
        if lefthalf[li] < righthalf[ri]:
            mlist[sorti] = lefthalf[li]
            li += 1
        else:
            mlist[sorti] = righthalf[ri]
            ri += 1
        #endif
        sorti += 1
    #endwhile

    while li < len(lefthalf):
        mlist[sorti] = lefthalf[li]
        li += 1
        sorti += 1
    #endwhile

    while ri < len(righthalf):
        mlist[sorti] = righthalf[ri]
        ri += 1
        sorti += 1
    #endwhile
#endif
#endprocedure
mergelist = [21, 8, 1, 13, 2, 3, 1, 5]
mergesort(mergelist)
print(mergelist)
