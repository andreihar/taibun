from taibun.taibun import Converter, Tokeniser, is_cjk, to_traditional

def test_convert_simplified():
	c = Converter()
	assert(c.get('我爱学语言')) == 'Guá ài o̍h gí-giân'

def test_is_cjk():
	assert is_cjk('漢') == True
	assert is_cjk('a') == False
	assert is_cjk('。') == False
	assert is_cjk('𠢕') == True
	assert is_cjk('福建') == True
	assert is_cjk('𥴊仔賴') == True
	assert is_cjk('福建a') == False

def test_to_traditional():
	assert '漢字是用來寫幾若種現代佮古代語文个書寫文字系統' == to_traditional('汉字是用来写幾若种现代佮古代语文个书写文字系统')


def test_suffix():
	t = Tokeniser()
	assert ['咱', '的', '食飯', '是', '誠好', '食'] == t.tokenise("咱的食飯是誠好食")
	assert ['卯死', '矣'] == t.tokenise("卯死矣")

def test_simplified():
	t = Tokeniser()
	assert ['汉字', '是', '用来', '写', '几', '若', '种', '现代', '佮', '古代', '语文', '个', '书写', '文字', '系统', '。'] == t.tokenise('汉字是用来写几若种现代佮古代语文个书写文字系统。')
	assert ['现代', '个', '中国', '、', '日本', '、', '韩国', '、', '台湾', '拢', '有', '使用', '汉字'] == t.tokenise('现代个中国、日本、韩国、台湾拢有使用汉字')