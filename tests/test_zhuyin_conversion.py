from taibun.taibun import Converter

def test_hanji_to_zhuyin():
	c = Converter(system="zhuyin")
	c_north = Converter(system="zhuyin", dialect="north")
	with open('tests/TestsZhuyin.csv', 'r', encoding='utf-8') as file:
		words = file.readlines()
	checker(words, c, c_north)

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