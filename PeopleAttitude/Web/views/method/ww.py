import json
import math
import numpy


def getData(path_one,path_two):
    def resolveJson(path):
        file = open(path, "rb")
        temp = json.load(file)
        request = temp['people']
        for r in request:
            request2 = r
            list = request2.get("pose_keypoints")
            return list

    def getPoint(l, point):
        b = numpy.array(l).reshape(18, 3)
        return (numpy.shape(b))

    def VectorCosineandSummary(x, y):
        vc = []
        for i in range(1, len(x) - 2):
            xc1 = x[i] - x[i - 1]
            xc2 = x[i + 1] - x[i]
            yc1 = y[i] - y[i - 1]
            yc2 = y[i + 1] - y[i]
            if (math.sqrt(xc1 ** 2 + yc1 ** 2) * math.sqrt(xc2 ** 2 + yc2 ** 2)) != 0:
                vc.append((xc1 * xc2 + yc1 * yc2) / (math.sqrt(xc1 ** 2 + yc1 ** 2) * math.sqrt(xc2 ** 2 + yc2 ** 2)))
            else:
                i = i + 1
        b = len(vc)
        # print (b)
        sum = 0
        for i in vc:
            sum = sum + abs(i)
        return abs(sum / b) * 100

    result_one = resolveJson(path_one)
    result_two = resolveJson(path_two)
    point_one = [[] for i in range(18)]
    point_two = [[] for i in range(18)]
    if getPoint(result_one,point_one) == getPoint(result_two,point_two):
        num = VectorCosineandSummary(result_one, result_two)
    else:
        num = print ('error')
    return num