__author__ = 'roohy'

import numpy as np

def makeTable(entry, alpha = 0.1):
    if alpha > 1 or alpha<0:
        alpha = 0.1
    length = len(entry)
    map = {}
    for i in range(0,length):
        map[entry[i]['url']] = i

    matrix = [[0 for x in range(0,length)] for y in range(0,length)]

    for i in range(0,length):
        tempBool = 0
        for site in entry[i]['links']:
            matrix[i][map[site]] = 1
            tempBool += 1
        for d in matrix[i]:
            if tempBool:
                d = (d/tempBool)
            else:
                d = 1/length
            d *= (1-alpha)
            d += alpha/length
    return matrix

def findEigens(matrix):
    mat = np.matrix(matrix)
    transposed = np.matrix.transpose(mat)
    eigenvalues,eigenvectors = np.linalg.eig(transposed)
    for i in range(0,len(eigenvalues)):
        if eigenvalues[i] == 1:
            return eigenvectors[i].tolist()


def ranks(entry,alpha):
    matrix = makeTable(entry,alpha)
    rankList = findEigens(matrix)
    return rankList

