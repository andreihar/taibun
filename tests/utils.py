def checker(array, general_converter, north_converter):
    for word in array:
        hanji = word.split(',')[0]
        zhuyin = word.split(',')[1].strip()
        if '/' in zhuyin: zhuyin = zhuyin.split('/')
        else: zhuyin = [zhuyin]
        if len(zhuyin) == 2:
            assert zhuyin[0] == general_converter.get(hanji)
            assert zhuyin[1] == north_converter.get(hanji)
        else:
            assert zhuyin[0] == general_converter.get(hanji)