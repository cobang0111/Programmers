def solution(routes):
    answer = 0
    routes.sort()
    camera = []
    for r in routes:
        count = 0
        for c in camera:
            # Completely include
            if c[0] <= r[0] and c[1] >= r[1]:
                c[0] = r[0]
                c[1] = r[1]
                break
            # Right side include
            elif c[0] <= r[0] and c[1] >= r[0] and c[1] <= r[1]:
                c[0] = r[0]
                break
            # Left side include
            elif c[0] >= r[0] and c[0] <= r[1] and c[1] >= r[1]:
                c[1] = r[1]
                break
            # Already Pass the camera
            elif r[0] <= c[0] and r[1] >= c[1]:
                break
            count += 1
        if count == len(camera):
            camera.append(r)

    answer = len(camera)
    return answer
