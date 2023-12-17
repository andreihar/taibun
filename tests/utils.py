def checker(array, general_converter, north_converter):
    for word in array:
        hanji = word.split(',', 1)[0]
        transl = word.split(',', 1)[1].strip()
        if '/' in transl: transl = transl.split('/')
        else: transl = [transl]
        if len(transl) == 2:
            assert transl[0] == general_converter.get(hanji)
            assert transl[1] == north_converter.get(hanji)
        else:
            assert transl[0] == general_converter.get(hanji)