from taibun.taibun import Tokeniser

def test_general():
	t = Tokeniser()
	assert ['太空', '朋友', '，', '恁好', '！', '恁', '食飽', '未', '？'] == t.tokenise("太空朋友，恁好！恁食飽未？")
	assert ['漢字', '（', '閩南語', '注音', ':', 'ㄏㄢˋ', 'ㆡㄧˉ', '；', '白話字', ':', 'Hàn-jī', '；'] == t.tokenise('漢字（閩南語注音: ㄏㄢˋ ㆡㄧˉ；白話字: Hàn-jī；')

def test_suffix():
	t = Tokeniser()
	assert ['咱', '的', '食飯', '是', '誠好', '食'] == t.tokenise("咱的食飯是誠好食")
	assert ['卯死', '矣'] == t.tokenise("卯死矣")

def test_simplified():
	t = Tokeniser()
	assert ['汉字', '是', '用来', '写', '几', '若', '种', '现代', '佮', '古代', '语文', '个', '书写', '文字', '系统', '。'] == t.tokenise('汉字是用来写几若种现代佮古代语文个书写文字系统。')
	assert ['现代', '个', '中国', '、', '日本', '、', '韩国', '、', '台湾', '拢', '有', '使用', '汉字'] == t.tokenise('现代个中国、日本、韩国、台湾拢有使用汉字')