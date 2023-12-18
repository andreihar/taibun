def checker(array, general_converter, north_converter):
    for word in array:
        hanji, transl = word.split(',', 1)
        transl = transl.strip().split('/')
        assert transl[0] == general_converter.get(hanji)
        if len(transl) > 1:
            assert transl[1] == north_converter.get(hanji)