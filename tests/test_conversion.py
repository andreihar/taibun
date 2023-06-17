import unittest
import taibun

class TestConversion(unittest.TestCase):

    def test_hanji_to_poj(self):
        hanji = "先生講、學生恬恬聽。"
        system = "POJ"
        expected = "Sian-siⁿ kóng, ha̍k-seng tiām-tiām thiaⁿ."
        result = taibun.get(hanji, system=system)
        self.assertEquals(result, expected)

    def test_hanji_to_tailo(self):
        hanji = "先生講、學生恬恬聽。"
        system = "Tai-lo"
        expected = "Sian-sinn kóng, ha̍k-sing tiām-tiām thiann."
        result = taibun.get(hanji, system=system)
        self.assertEquals(result, expected)

    def test_hanji_to_zhuyin(self):
        hanji = "先生講、學生恬恬聽。"
        system = "zhuyin"
        expected = "ㄒㄧㄢ ㄒㆪ ㄍㆲˋ, ㄏㄚㆶ˙ ㄒㄧㄥ ㄉㄧㆰ˫ ㄉㄧㆰ˫ ㄊㄧㆩ."
        result = taibun.get(hanji, system=system)
        self.assertEquals(result, expected)

    def test_tailo_to_zhuyin(self):
        import json
        zhuyin = json.load(open('test_zhuyin.json', encoding='utf-8'))
        for i in zhuyin:
            self.assertEquals(taibun.tailo_to_zhuyin(i), zhuyin[i])