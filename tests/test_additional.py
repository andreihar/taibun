from taibun.taibun import Converter, is_cjk, to_traditional, to_simplified

def test_convert_simplified():
	c = Converter()
	assert(c.get('我爱学语言')) == 'Guá ài o̍h gí-giân'

def test_to_traditional():
	assert '漢字是台灣用來寫幾若種現代佮古代語文个書寫文字系統' == to_traditional('汉字是台湾用来写几若种现代佮古代语文个书写文字系统')

def test_to_simplified():
	assert '汉字是台湾用来写几若种现代佮古代语文个书写文字系统' == to_simplified('漢字是臺灣用來寫幾若種現代佮古代語文个書寫文字系統')

def test_is_cjk():
	assert is_cjk('漢') == True
	assert is_cjk('a') == False
	assert is_cjk('。') == False
	assert is_cjk('𠢕') == True
	assert is_cjk('福建') == True
	assert is_cjk('𥴊仔賴') == True
	assert is_cjk('福建a') == False