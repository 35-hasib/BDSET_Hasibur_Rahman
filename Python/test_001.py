def find_ED(y1,y2,y3):
    x = [
        [170,70,30],
        [180,80,25],
        [160,60,35],
        [175,75,28],
        [165,65,31]
        ]
    out = []
    for i in range(len(x)):
        ED = (x[i][0]-y1)**2 + (x[i][1]-y2)**2 + (x[i][2]-y3)**2
        ED = ED ** 0.5
        out.append(ED)
    return out


print(find_ED(172,72,29))