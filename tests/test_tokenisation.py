from taibun.taibun import Tokeniser

def test_hanji_to_zhuyin():
	t = Tokeniser()
	assert ['太空', '朋友', '，', '恁好', '！', '恁', '食飽', '未', '？'] == t.tokenise("太空朋友，恁好！恁食飽未？")