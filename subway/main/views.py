from django.shortcuts import render
from .models import Lines
from .models import MetroMap

mapData = MetroMap.mapData


def index(request):
    return render(request, 'main/index.html', {"t0": mapData[0][2], "l0": mapData[0][3],
                                               "t1": mapData[1][2], "l1": mapData[1][3],
                                               "t2": mapData[2][2], "l2": mapData[2][3],
                                               "t3": mapData[3][2], "l3": mapData[3][3],
                                               "t4": mapData[4][2], "l4": mapData[4][3],
                                               "t5": mapData[5][2], "l5": mapData[5][3],
                                               "t6": mapData[6][2], "l6": mapData[6][3],
                                               "t7": mapData[7][2], "l7": mapData[7][3],
                                               "t8": mapData[8][2], "l8": mapData[8][3],
                                               "t9": mapData[9][2], "l9": mapData[9][3],
                                               "t10": mapData[10][2], "l10": mapData[10][3],
                                               "t11": mapData[11][2], "l11": mapData[11][3],
                                               "t12": mapData[12][2], "l12": mapData[12][3],
                                               "t13": mapData[13][2], "l13": mapData[13][3],
                                               "t14": mapData[14][2], "l14": mapData[14][3],
                                               "t15": mapData[15][2], "l15": mapData[15][3],
                                               "t16": mapData[16][2], "l16": mapData[16][3],
                                               "t17": mapData[17][2], "l17": mapData[17][3],

                                               "t18": mapData[18][2], "l18": mapData[18][3],
                                               "t19": mapData[19][2], "l19": mapData[19][3],
                                               "t20": mapData[20][2], "l20": mapData[20][3],
                                               "t21": mapData[21][2], "l21": mapData[21][3],
                                               "t22": mapData[22][2], "l22": mapData[22][3],
                                               "t23": mapData[23][2], "l23": mapData[23][3],
                                               "t24": mapData[24][2], "l24": mapData[24][3],
                                               "t25": mapData[25][2], "l25": mapData[25][3],
                                               "t26": mapData[26][2], "l26": mapData[26][3],
                                               "t27": mapData[27][2], "l27": mapData[27][3],
                                               "t28": mapData[28][2], "l28": mapData[28][3],
                                               "t29": mapData[29][2], "l29": mapData[29][3],
                                               })


def about(request):
    return render(request, 'main/about.html')


print(mapData[0][2], mapData[0][3],
      mapData[1][2], mapData[1][3],
      mapData[2][2], mapData[2][3],
      mapData[3][2], mapData[3][3])

print(mapData[0][0], mapData[0][1], mapData[0][2], mapData[0][3])