
row_perm = "12 7 15 11 6 9 1 2 0 3 14 4 13 5 8 10"
col_perm = "5 15 7 13 3 1 9 10 2 14 4 8 11 12 0 6"


slp = """t00 = x04 + x12
y01 = x01 + t00
y02 = x02 + t00
y03 = y01 + x04 + y02
y09 = t00 + y03
t06 = x07 + x15
y07 = x09 + t06
y10 = x08 + t06
y04 = x07 + x08 + x09
y15 = t06 + y04
t12 = x05 + x06
y12 = x00 + t12
y13 = x03 + t12
y05 = y12 + x05 + y13
y06 = t12 + y05
t18 = x10 + x14
y00 = x11 + t18
y14 = x13 + t18
y08 = y14 + x11 + x14
y11 = t18 + y08"""

col_dict = {"x" + str(k).zfill(2): "x" + str(v).zfill(2) for k, v in enumerate(col_perm.split(" "))}
row_dict = {"y" + str(k).zfill(2): "y" + str(v).zfill(2) for k, v in enumerate(row_perm.split(" "))}

for line in slp.split("\n"):
    lhs, rhs = line.strip().split(' = ')
    
    if 'x' in lhs:
        lhs = col_dict[lhs]
    elif 'y' in lhs:
        lhs = row_dict[lhs]
    
    rhs_new = []

    if '+' not in rhs:
        if 'x' in rhs:
            rhs_new.append(col_dict[rhs])
        elif 'y' in rhs:
            rhs_new.append(row_dict[rhs])
    else:
        for i in rhs.split(' + '):
            if 'x' in i:
                rhs_new.append(col_dict[i])
            elif 'y' in i:
                rhs_new.append(row_dict[i])
            else:
                rhs_new.append(i)
    
    if len(rhs_new) == 1:
        print(lhs + " = " + rhs_new[0])
    else:
        print(lhs + " = " + ' + '.join(rhs_new))
