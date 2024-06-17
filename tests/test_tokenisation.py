from taibun.taibun import Tokeniser

def test_general():
	t = Tokeniser()
	assert ['太空', '朋友', '，', '恁好', '！', '恁', '食飽', '未', '？'] == t.tokenise("太空朋友，恁好！恁食飽未？")
	assert ['漢字', '（', '閩南語', '注音', ':', 'ㄏㄢˋ', 'ㆡㄧˉ', '；', '白話字', ':', 'Hàn-jī', '；'] == t.tokenise('漢字（閩南語注音: ㄏㄢˋ ㆡㄧˉ；白話字: Hàn-jī；')

def test_best_solution_tokenisation():
    t = Tokeniser()
    assert ['中國', '人民', '共和國'] == t.tokenise("中國人民共和國")
    assert ['中國人', '民雄', '協會'] == t.tokenise('中國人民雄協會')
    assert ['花蓮', '市議員'] == t.tokenise('花蓮市議員')

def test_suffix():
	t = Tokeniser()
	assert ['咱的', '食飯', '是', '誠', '好食'] == t.tokenise("咱的食飯是誠好食")
	assert ['卯死', '矣'] == t.tokenise("卯死矣")

def test_simplified():
	t = Tokeniser()
	assert ['汉字', '是', '用来', '写', '几若', '种', '现代', '佮', '古代', '语文', '个', '书写', '文字', '系统', '。'] == t.tokenise('汉字是用来写几若种现代佮古代语文个书写文字系统。')
	assert ['现代', '个', '中国', '、', '日本', '、', '韩国', '、', '台湾', '拢', '有', '使用', '汉字'] == t.tokenise('现代个中国、日本、韩国、台湾拢有使用汉字')

def test_false():
	t = Tokeniser(False)
	assert ['漢字', '是', '用來', '寫', '幾若', '種', '現代', '佮', '古代', '語文', '个', '書寫', '文字', '系統', '。'] == t.tokenise('汉字是用来写几若种现代佮古代语文个书写文字系统。')
	assert ['現代', '个', '中國', '、', '日本', '、', '韓國', '、', '台灣', '攏', '有', '使用', '漢字'] == t.tokenise('现代个中国、日本、韩国、台湾拢有使用汉字')