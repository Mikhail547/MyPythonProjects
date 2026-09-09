with open('24_31160.txt') as f:
    s = f.readline()
    t, m = '', ['']
    z2 = ['VV', 'LL', 'DD', 'IL', 'IC', 'ID', 'IM',
          'VX', 'VL', 'VC', 'VD', 'VM', 'XD', 'XM', 'LC', 'LD', 'LM', 'DM']
    z3 = ['IIV', 'IIX', 'VIX', 'VIV', 'IXI', 'IXX', 'IXV', 'IXL', 'IXC', 'IVI', 'CCM', 'CCD', 'XXL', 'XXC', 'LXC', 'DCM', 'CMC', 'CMM', 'XCM', 'XCD', 'CMD', 'DCD', 'CDC', 'XLX']
    z4 = [4*'I', 4*'X', 4*'C', 4*'M']
    for a in s:
        t += a
        if len(t) > 1 and t[-2:] in z2:
            t = t[-1]
        if len(t) > 2 and t[-3:] in z3:
            t = t[-2:]
        if len(t) >3 and t[-4:] in z4:
            t = t[-3:]
        if len(t) >= len(m[0]):
            if len(t) == len(m[0]):
                m.append(t)
            else:
                m = [t]

    m.sort()
    for a in m:
        print(a)
