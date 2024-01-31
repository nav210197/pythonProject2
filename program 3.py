gender = input("Enter Your gender female or male ")
hb_level = float(input("Enter your hb"))
if gender == "female":
    if 117 <= hb_level <= 155:
        print("Normal hb level for adult females")
    elif hb_level < 117:
        print("low hb level for adult females")
    else: print("High hb level for adult females")
else:
    if 134 <= hb_level <= 167:
        print("Normal hb level for adult males")
    elif hb_level < 134:
            print("low hb level for adult males")
    else:
            print("High hb level for adult males")