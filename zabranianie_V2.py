def zabranianie(macierz, wybrane):
    for i, odcinek1 in enumerate(wybrane):
        part = [odcinek1[0], odcinek1[1]]
        zmiana = True
        while zmiana:
            zmiana = False
            for j, odcinek2 in enumerate(wybrane):
                if i == j:
                    pass
                else:
                    if part[0] == odcinek2[1] and odcinek2[0] not in part:
                        part.insert(0, odcinek2[0])
                        zmiana = True
                    elif odcinek2[0] == part[-1] and odcinek2[1] not in part:
                        part.append(odcinek2[1])
                        zmiana = True
        if len(part) < len(macierz):
            macierz[part[0]][part[-1]] = float('inf')
        return part
            # print(part)

# import numpy as np
# mat1 = [[float("inf"),1,0,2,2],
#        [3,float("inf"),2,0,1],
#        [1,2,float("inf"),2,0],
#        [4,0,3,float("inf"),4],
#        [0,2,7,0,float("inf")]]
# print(np.array(mat1))
# matrix = np.array([
#     [float('inf'), 3, 5, 1, 1, 6, 1],
#     [1, float('inf'), 3, 2, 2, 1, 4],
#     [4, 2, float('inf'), 5, 2, 3, 2],
#     [1, 3, 5, float('inf'), 1, 5, 3],
#     [2, 6, 1, 3, float('inf'), 2, 1],
#     [5, 1, 2, 3, 5, float('inf'), 2],
#     [1, 2, 4, 1, 3, 2, float('inf')]
# ])
# print(zabranianie(mat1, [[0, 2], [3, 1], [1, 0]]))
# print(np.array(mat1))
# print(zabranianie(matrix, [[0, 2], [3, 1], [1, 0], [5, 6], [6, 4]]))
# print(matrix)