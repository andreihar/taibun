from taibun.taibun import Converter

def test_tones():
    c = Converter(system='IPA', dialect='Singapore', punctuation='none')
    tones = {"衫":"sã⁴⁴","短":"te⁴²","褲":"kʰɔ²¹","闊":"kʰuaʔ³²","人":"laŋ²⁴","鼻":"pʰĩ²²","直":"tit̚⁴"}
    for tone, expected in tones.items():
        assert c.get(tone) == expected

def test_o_conversion():
    c = Converter(system='IPA', dialect='Singapore', punctuation='none')
    o_words = {"高":"ko⁴⁴","唔":"ɔ̃⁴⁴","烏":"ɔ⁴⁴","王":"ɔŋ²⁴"}
    for word, expected in o_words.items():
        assert c.get(word) == expected

from taibun.taibun import Converter

def test_eng_conversion():
    hanji_data = ["用","冰","兵","幸啊","無閒","無政府"]
    test_data = [
        (["ēng","peng","peng","hēng--ah","bô-êng","bô tsèng-hú"], "Tailo"),
        (["ēng","peng","peng","hēng--ah","bô-êng","bô chèng-hú"], "POJ"),
        (["ㆤㄥ˫","ㄅㆤㄥ","ㄅㆤㄥ","ㄏㆤㄥ˫ ㄚ","ㆠㄜˊ ㆤㄥˊ","ㆠㄜˊ ㄗㆤㄥ˪ ㄏㄨˋ"], "Zhuyin"),
        (["eng7","peng1","peng1","heng7 ah0","bo5 eng5","bo5 ceng3 hu2"], "TLPA"),
        (["êng","bēng","bēng","hêng ah","bbóéng","bbó zènghǔ"], "Pingyim"),
        (["ēng","beng","beng","hēng--åh","bhôr-ĕng","bhôr zèng-hù"], "Tongiong"),
        (["eŋ²²","peŋ⁴⁴","peŋ⁴⁴","heŋ²² a","bo²⁴ eŋ²⁴","bo²⁴ tseŋ²¹ hu⁴²"], "IPA")
    ]
    for transl, system in test_data:
        data = list(zip(hanji_data, transl))
        c = Converter(system=system, dialect='Singapore', punctuation='none')
        for hanji, expected in data:
            assert c.get(hanji) == expected

def test_sandhi():
    sandhis = ["auto","none","exc_last","incl_last"]
    expected_results = ["Tài-uân","Tâi-uân","Tài-uân","Tài-uàn"]
    for sandhi, expected in zip(sandhis, expected_results):
        c = Converter(dialect='Singapore', punctuation='none', sandhi=sandhi)
        assert c.get('台灣') == expected

def test_additional_vocabulary():
    c = Converter(dialect='Singapore', punctuation='none')
    kos = ["我","你","甚物","食物"]
    expected_results = ["uá","lú","sīm-mi̍h","si̍t-bu̍t"]
    for ko, expected in zip(kos, expected_results):
        assert c.get(ko) == expected

def test_kopi():
    c = Converter(dialect='Singapore', punctuation='none')
    kos = ["咖啡","烏咖啡","咖啡杯","咖哩","咖咖仔"]
    expected_results = ["ko-pi","oo-ko-pi","ko-pi-pue","ka-lí","ka-ka-á"]
    for ko, expected in zip(kos, expected_results):
        assert c.get(ko) == expected