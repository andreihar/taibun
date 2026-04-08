import unittest

from taibun.taibun import Converter


class TestSingapore(unittest.TestCase):

    def test_tones(self):
        c = Converter(system='IPA', dialect='Singapore', punctuation='none')
        tones = ['衫', '短', '褲', '闊', '人', '鼻', '直']
        expected = ['sã⁴⁴', 'te⁴²', 'kʰɔ²¹', 'kʰuaʔ³²', 'laŋ²⁴', 'pʰĩ²²', 'tit̚⁴']

        for t, e in zip(tones, expected):
            self.assertEqual(c.get(t), e)

    def test_o_conversion(self):
        c = Converter(system='IPA', dialect='Singapore', punctuation='none')
        words = ['高', '唔', '烏', '王']
        expected = ['ko⁴⁴', 'ɔ̃⁴⁴', 'ɔ⁴⁴', 'ɔŋ²⁴']

        for w, e in zip(words, expected):
            self.assertEqual(c.get(w), e)

    def test_eng_conversion(self):
        hanji_data = ['用', '冰', '兵', '幸啊', '無閒', '無政府']
        test_data = [
            (['ēng', 'peng', 'peng', 'hēng--ah', 'bô-êng', 'bô tsèng-hú'], 'Tailo'),
            (['ēng', 'peng', 'peng', 'hēng--ah', 'bô-êng', 'bô chèng-hú'], 'POJ'),
            (['ㆤㄥ˫', 'ㄅㆤㄥ', 'ㄅㆤㄥ', 'ㄏㆤㄥ˫ ㄚ', 'ㆠㄜˊ ㆤㄥˊ', 'ㆠㄜˊ ㄗㆤㄥ˪ ㄏㄨˋ'], 'Zhuyin'),
            (['eng7', 'peng1', 'peng1', 'heng7 ah0', 'bo5 eng5', 'bo5 ceng3 hu2'], 'TLPA'),
            (['êng', 'bēng', 'bēng', 'hêng ah', 'bbóéng', 'bbó zènghǔ'], 'Pingyim'),
            (['ēng', 'beng', 'beng', 'hēng--åh', 'bhôr-ĕng', 'bhôr zèng-hù'], 'Tongiong'),
            (['eŋ²²', 'peŋ⁴⁴', 'peŋ⁴⁴', 'heŋ²² a', 'bo²⁴ eŋ²⁴', 'bo²⁴ tseŋ²¹ hu⁴²'], 'IPA')
        ]

        for transl, system in test_data:
            c = Converter(system=system, dialect='Singapore', punctuation='none')
            for h, e in zip(hanji_data, transl):
                self.assertEqual(c.get(h), e)

    def test_sandhi(self):
        sandhis = ['auto', 'none', 'exc_last', 'incl_last']
        expected = ['Tài-uân', 'Tâi-uân', 'Tài-uân', 'Tài-uàn']

        for s, e in zip(sandhis, expected):
            c = Converter(dialect='Singapore', punctuation='none', sandhi=s)
            self.assertEqual(c.get('台灣'), e)

    def test_additional_vocabulary(self):
        c = Converter(dialect='Singapore', punctuation='none')
        kos = ['我', '你', '甚物', '食物']
        expected = ['uá', 'lú', 'sīm-mi̍h', 'si̍t-bu̍t']

        for k, e in zip(kos, expected):
            self.assertEqual(c.get(k), e)

    def test_kopi(self):
        c = Converter(dialect='Singapore', punctuation='none')
        kos = ['咖啡', '烏咖啡', '咖啡杯', '咖哩', '咖咖仔']
        expected = ['ko-pi', 'oo-ko-pi', 'ko-pi-pue', 'ka-lí', 'ka-ka-á']

        for k, e in zip(kos, expected):
            self.assertEqual(c.get(k), e)