from taibun.taibun import Converter
from utils import checker

def test_zhuyin_initials():
    c = Converter(system="Zhuyin", punctuation='none')
    c_north = Converter(system="Zhuyin", dialect="north", punctuation='none')

    bilabial = ["邊,ㄅㄧㄢ","波,ㄆㄜ","毛,ㄇㆦˊ","文,ㆠㄨㄣˊ"]
    checker(bilabial, c, c_north)
    alveolar = ["地,ㄉㆤ˫/ㄉㄨㆤ˫","他,ㄊㆩ","曾,ㄗㄢ","出,ㄘㄨㆵ","衫,ㄙㆩ","耐,ㄋㄞ˫","熱衫,ㆡㄨㄚㆷ˙ ㄙㆩ/ㄌㄨㄚㆷ˙ ㄙㆩ","柳,ㄌㄧㄨˋ"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["尖,ㄐㄧㆰ","手,ㄑㄧㄨˋ","寫,ㄒㄧㄚˋ","入,ㆢㄧㆴ˙/ㄌㄧㆴ˙"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求,ㄍㄧㄨˊ","去,ㄎㄧ˪","雅,ㄫㄚˋ","語,ㆣㄧˋ/ㆣㄨˋ","喜,ㄏㄧˋ"]
    checker(velar, c, c_north)

def test_zhuyin_vowels_and_rhymes():
    c = Converter(system="Zhuyin", punctuation='none')
    c_north = Converter(system="Zhuyin", dialect="north", punctuation='none')

    front = ["衣,ㄧ","禮,ㄌㆤˋ","圓,ㆪˊ","生死,ㄙㆥ ㄒㄧˋ/ㄒㆪ ㄒㄧˋ"]
    checker(front, c, c_north)
    central = ["高,ㄍㄜ","查問,ㄗㄚ ㆠㄨㄣ˫","衫,ㄙㆩ"]
    checker(central, c, c_north)
    back = ["污,ㄨ","烏,ㆦ","張,ㄉㄧㆫ","唔,ㆧ"]
    checker(back, c, c_north)

def test_zhuyin_finals():
    c = Converter(system="Zhuyin", punctuation='none')
    c_north = Converter(system="Zhuyin", dialect="north", punctuation='none')

    nasal = ["啉,ㄌㄧㆬ","新,ㄒㄧㄣ","紅,ㄤˊ"]
    checker(nasal, c, c_north)
    stop = ["汁,ㄐㄧㄚㆴ","蝨,ㄙㄚㆵ","國,ㄍㆦㆶ","食,ㄐㄧㄚㆷ˙"]
    checker(stop, c, c_north)
    syllabic = ["姆,ㆬˋ","酸,ㄙㆭ"]
    checker(syllabic, c, c_north)