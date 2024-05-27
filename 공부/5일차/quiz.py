def std_weight(height, gender):
    if gender == "남자":
        height /= 100
        my = height * height * 22
        print("당신의 키의({}cm) 표준 체중은 {:.2f}입니다 ".format(height*100,my))
    elif gender == "여자":
        height /= 100
        my = height * height * 21
        print("당신의 키의({}cm) 표준 체중은 {:.2f}입니다 ".format(height*100,my))

std_weight(170, "남자")