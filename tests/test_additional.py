import unittest

from taibun.taibun import Converter, is_cjk, to_simplified, to_traditional


class TestAdditional(unittest.TestCase):
    def test_convert_simplified(self):
        c = Converter()
        self.assertEqual(c.get('我爱学语言'), 'Guá ài o̍h gí-giân')

    def test_to_traditional(self):
        simplified = ['干休', '干杯', '干部', '周密', '周期', '天后', '大后日', '不只', '船只', '台语', '寝台车', '台面', '风台', '两个', '个人']
        traditional = ['干休', '乾杯', '幹部', '周密', '週期', '天后', '大後日', '不只', '船隻', '台語', '寢臺車', '檯面', '風颱', '兩个', '個人']

        for s, t in zip(simplified, traditional):
            self.assertEqual(to_traditional(s), t)

    def test_vars(self):
        c = Converter(punctuation='none')
        inputs = ['木蝨', '爲啥物', '白癡', '牛肉麪', '臺北人', '聲説', '研鉢', '踊躍']
        expected = ['ba̍k-sat', 'uī-siánn-mi̍h', 'pe̍h-tshi', 'gû-bah-mī', 'Tâi-pak-lâng', 'siann-sueh', 'gíng-puah', 'ióng-io̍k']

        for i, e in zip(inputs, expected):
            self.assertEqual(c.get(i), e)

    def test_to_simplified(self):
        traditional = ['干休', '乾杯', '幹部', '周密', '週期', '天后', '大後日', '不只', '船隻', '台語', '寢臺車', '檯面', '風颱', '兩个', '個人']
        simplified = ['干休', '干杯', '干部', '周密', '周期', '天后', '大后日', '不只', '船只', '台语', '寝台车', '台面', '风台', '两个', '个人']

        for t, s in zip(traditional, simplified):
            self.assertEqual(to_simplified(t), s)

    def test_is_cjk(self):
        inputs = ['漢', 'a', '。', '𠢕', '福建', '𥴊仔賴', '福建a']
        expected = [True, False, False, True, True, True, False]

        for i, e in zip(inputs, expected):
            self.assertEqual(is_cjk(i), e)