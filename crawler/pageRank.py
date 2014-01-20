__author__ = 'roohy'

import numpy as np

def makeTable(entry, alpha = 0.1):
    if alpha > 1 or alpha<0:
        alpha = 0.1
    length = len(entry)
    map = {}
    for i in range(0,length):
        map[entry[i]['url']] = i
    #print("map", map)

    matrix = [[0.0 for x in range(0,length)] for y in range(0,length)]

    # print('map is ',map)
    for i in range(0,length):
        tempBool = 0 # this checks the number of pages this page is linking to
        for site in entry[i]['links']:
            # print('site is', site)
            if site in map: #if the link is actually crawled. sometimes we push a link into queue but due to the limit it never will be crawled
                matrix[i][map[site]] = 1
                tempBool += 1
        for d in range(0,len(matrix[i])):
            if tempBool:
                matrix[i][d] = (matrix[i][d]/tempBool)
            else:
                matrix[i][d] = 1/length
            matrix[i][d] *= (1-alpha)
            matrix[i][d] += alpha/length
        #print ("i deraye is", matrix[i])
    #print("matrix is ",matrix)
    return matrix

def findEigens(matrix):
    mat = np.matrix(matrix)
    # print("matrix is: ", mat)
    transposed = np.matrix.transpose(mat)
    #print("trans is :")
    #print(transposed)
    eigenvalues,eigenvectors = np.linalg.eig(transposed)
    # eig_vals_sorted = np.sort(eigenvalues)
    # eig_vecs_sorted = eigenvectors[eigenvalues.argsort()]
    # print ( 'eigens ', eig_vals_sorted)
    #print ( 'eigens ', eigenvectors)
    # return eig_vecs_sorted[-1].tolist()[0]
    for i in range(0,len(eigenvalues)):
        if  (type(eigenvalues[i])!= complex or (type(eigenvalues[i])== complex and eigenvalues[i].imag == 0)) and  round(eigenvalues[i],5) > 0.99 and  round(eigenvalues[i],5) < 1.01:
            # print("found it ",eigenvalues[i])
            return eigenvectors[i].tolist()[0]


def ranks(entry,alpha):
    matrix = makeTable(entry,alpha)
    rankList = findEigens(matrix)
    return rankList

