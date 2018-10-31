def findMaxPoints(players):
    maxPoints = []
    qbs = [0]
    rbs = [0, 0, 0]
    wrs = [0, 0, 0]
    tes = [0, 0, 0]
    dst = [0]
    k   = [0]
    for p in players:
        used = False
        points = p[1]
        for slot in p[2]:
            if slot == 0:
                    qbs.append(points)
            if slot == 2:
                    rbs.append(points)
            if slot == 4:
                    wrs.append(points)
            if slot == 6:
                    tes.append(points)
            if slot == 16:
                    dst.append(points)
            if slot == 17:
                    k.append(points)


    qbs.sort(reverse=True)
    rbs.sort(reverse=True)
    wrs.sort(reverse=True)
    tes.sort(reverse=True)
    dst.sort(reverse=True)
    k.sort(reverse=True)


    maxPoints.append(qbs[0])
    maxPoints.append(rbs[0])
    maxPoints.append(rbs[1])
    maxPoints.append(wrs[0])
    maxPoints.append(wrs[1])
    maxPoints.append(tes[0])
    maxPoints.append(max(rbs[2], wrs[2], tes[1]))
    maxPoints.append(dst[0])
    maxPoints.append(k[0])

    return sum(maxPoints)
