import unittest

from taibun.taibun import Tokeniser


class TestTokenisation(unittest.TestCase):

    def test_general(self):
        t = Tokeniser()

        inputs = ["太空朋友，恁好！恁食飽未？", "漢字（閩南語注音: ㄏㄢˋ ㆡㄧˉ；白話字: Hàn-jī；"]
        expected = [['太空', '朋友', '，', '恁好', '！', '恁', '食飽', '未', '？'], ['漢字', '（', '閩南語', '注音', ':', 'ㄏㄢˋ', 'ㆡㄧˉ', '；', '白話字', ':', 'Hàn-jī', '；']]

        for i, e in zip(inputs, expected):
            self.assertEqual(t.tokenise(i), e)

    def test_best_solution_tokenisation(self):
        t = Tokeniser()

        inputs = ["中國人民共和國", "中國人民雄協會", "花蓮市議員"]
        expected = [['中國', '人民', '共和國'], ['中國人', '民雄', '協會'], ['花蓮', '市議員']]

        for i, e in zip(inputs, expected):
            self.assertEqual(t.tokenise(i), e)

    def test_suffix(self):
        t = Tokeniser()

        inputs = ["咱的食飯是誠好食", "卯死矣"]
        expected = [['咱的', '食飯', '是', '誠', '好食'], ['卯死', '矣']]

        for i, e in zip(inputs, expected):
            self.assertEqual(t.tokenise(i), e)

    def test_simplified(self):
        t = Tokeniser()

        inputs = ['汉字是用来写几若种现代佮古代语文个书写文字系统。', '现代个中国、日本、韩国、台湾拢有使用汉字']
        expected = [['汉字', '是', '用来', '写', '几若', '种', '现代', '佮', '古代', '语文', '个', '书写', '文字', '系统', '。'], ['现代', '个', '中国', '、', '日本', '、', '韩国', '、', '台湾', '拢', '有', '使用', '汉字']]

        for i, e in zip(inputs, expected):
            self.assertEqual(t.tokenise(i), e)

    def test_false(self):
        t = Tokeniser(False)

        inputs = ['汉字是用来写几若种现代佮古代语文个书写文字系统。', '现代个中国、日本、韩国、台湾拢有使用汉字']
        expected = [['漢字', '是', '用來', '寫', '幾若', '種', '現代', '佮', '古代', '語文', '个', '書寫', '文字', '系統', '。'], ['現代', '个', '中國', '、', '日本', '、', '韓國', '、', '台灣', '攏', '有', '使用', '漢字']]

        for i, e in zip(inputs, expected):
            self.assertEqual(t.tokenise(i), e)