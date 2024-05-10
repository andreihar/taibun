from taibun.taibun import Converter, is_cjk, to_traditional, to_simplified

def test_convert_simplified():
	c = Converter()
	assert(c.get('我爱学语言')) == 'Guá ài o̍h gí-giân'

def test_to_traditional():
	assert to_traditional('干休') == '干休'
	assert to_traditional('干杯') == '乾杯'
	assert to_traditional('干部') == '幹部'
	assert to_traditional('周密') == '周密'
	assert to_traditional('周期') == '週期'
	assert to_traditional('天后') == '天后'
	assert to_traditional('大后日') == '大後日'
	assert to_traditional('不只') == '不只'
	assert to_traditional('船只') == '船隻'
	assert to_traditional('台语') == '台語'
	assert to_traditional('寝台车') == '寢臺車'
	assert to_traditional('台面') == '檯面'
	assert to_traditional('风台') == '風颱'
	assert to_traditional('两个') == '兩个'
	assert to_traditional('个人') == '個人'

def test_vars():
	c = Converter(punctuation='none')
	assert(c.get('木蝨')) == 'ba̍k-sat'
	assert(c.get('爲啥物')) == 'uī-siánn-mi̍h'
	assert(c.get('白癡')) == 'pe̍h-tshi'
	assert(c.get('牛肉麪')) == 'gû-bah-mī'
	assert(c.get('臺北人')) == 'Tâi-pak-lâng'
	assert(c.get('聲説')) == 'siann-sueh'
	assert(c.get('研鉢')) == 'gíng-puah'
	assert(c.get('踊躍')) == 'ióng-io̍k'

def test_to_simplified():
    assert to_simplified('干休') == '干休'
    assert to_simplified('乾杯') == '干杯'
    assert to_simplified('幹部') == '干部'
    assert to_simplified('周密') == '周密'
    assert to_simplified('週期') == '周期'
    assert to_simplified('天后') == '天后'
    assert to_simplified('大後日') == '大后日'
    assert to_simplified('不只') == '不只'
    assert to_simplified('船隻') == '船只'
    assert to_simplified('台語') == '台语'
    assert to_simplified('寢臺車') == '寝台车'
    assert to_simplified('檯面') == '台面'
    assert to_simplified('風颱') == '风台'
    assert to_simplified('兩个') == '两个'
    assert to_simplified('個人') == '个人'

def test_is_cjk():
	assert is_cjk('漢') == True
	assert is_cjk('a') == False
	assert is_cjk('。') == False
	assert is_cjk('𠢕') == True
	assert is_cjk('福建') == True
	assert is_cjk('𥴊仔賴') == True
	assert is_cjk('福建a') == False