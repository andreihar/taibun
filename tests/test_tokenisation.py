from taibun.taibun import Tokeniser

def test_hanji_to_zhuyin():
	t = Tokeniser()
	assert ['太空', '朋友', '，', '恁好', '！', '恁', '食飽', '未', '？'] == t.tokenise("太空朋友，恁好！恁食飽未？")

def test_suffix():
	t = Tokeniser()
	assert ['咱', '的', '食飯', '是', '誠好', '食'] == t.tokenise("咱的食飯是誠好食")
	assert ['卯死', '矣'] == t.tokenise("卯死矣")