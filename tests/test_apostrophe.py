import unittest

from utils import checker

from taibun.taibun import Converter

hanji_data = ["一概", "三層", "不屑", "朋友", "海蟹", "癮甲", "草笠仔"]

class TestConvertNonCJK(unittest.TestCase):

    def test_apostrophe_default(self):
        test_data = [
            (["it-khài","sam-tsàn","put-sut","pîng-iú","hái-hē","giàn-kah","tsháu-le̍h-á/tsháu-lue̍h-á"], "Tailo"),
            (["it-khài","sam-chàn","put-sut","pêng-iú","hái-hē","giàn-kah","chháu-le̍h-á/chháu-loe̍h-á"], "POJ"),
            (["ㄧㆵ ㄎㄞ˪","ㄙㆰ ㄗㄢ˪","ㄅㄨㆵ ㄙㄨㆵ","ㄅㄧㄥˊ ㄧㄨˋ","ㄏㄞˋ ㄏㆤ˫","ㆣㄧㄢ˪ ㄍㄚㆷ","ㄘㄠˋ ㄌㆤㆷ˙ ㄚˋ/ㄘㄠˋ ㄌㄨㆤㆷ˙ ㄚˋ"], "Zhuyin"),
            (["it4 khai3","sam1 can3","put4 sut4","ping5 iu2","hai2 he7","gian3 kah4","chau2 leh8 a2/chau2 lueh8 a2"], "TLPA"),
            (["yītkài","sāmzàn","būtsūt","bíngyǔ","hǎi'hê","ggiàn'gāh","cǎoléh'ǎ/cǎoluéh'ǎ"], "Pingyim"),
            (["it-kâi","sām-zân","but-sūt","bīng-iù/bîng-iù","hai-hē","ghiàn-gāh","cau-lē-à/cau-luē-à"], "Tongiong"),
            (["it̚²¹ kʰai¹¹/it̚³² kʰai²¹","sam⁴⁴ tsan¹¹/sam⁵⁵ tsan²¹","put̚²¹ sut̚²¹/put̚³² sut̚³²","piɪŋ²⁵ iu⁵³/piɪŋ²⁴ iu⁵¹","hai⁵³ he²²/hai⁵¹ he³³","giɛn¹¹ kaʔ²¹/giɛn²¹ kaʔ³²","tsʰau⁵³ leʔ⁵ a⁵³/tsʰau⁵¹ lueʔ⁴ a⁵¹"], "IPA")
        ]
        for transl, system in test_data:
            data = list(zip(hanji_data, transl))
            checker(self, data, Converter(system=system, punctuation='none', apostrophe=True), Converter(system=system, dialect="north", punctuation='none', apostrophe=True))

    def test_apostrophe_delimiter(self):
        test_data = [
            (["itkhài","samtsàn","put'sut","pîng'iú","hái'hē","giànkah","tsháule̍h'á/tsháulue̍h'á"], "Tailo"),
            (["itkhài","samchàn","putsut","pêng'iú","hái'hē","giànkah","chháule̍h'á/chháuloe̍h'á"], "POJ"),
            (["ㄧㆵㄎㄞ˪","ㄙㆰㄗㄢ˪","ㄅㄨㆵㄙㄨㆵ","ㄅㄧㄥˊㄧㄨˋ","ㄏㄞˋㄏㆤ˫","ㆣㄧㄢ˪ㄍㄚㆷ","ㄘㄠˋㄌㆤㆷ˙ㄚˋ/ㄘㄠˋㄌㄨㆤㆷ˙ㄚˋ"], "Zhuyin"),
            (["it4khai3","sam1can3","put4sut4","ping5iu2","hai2he7","gian3kah4","chau2leh8a2/chau2lueh8a2"], "TLPA"),
            (["yītkài","sāmzàn","būtsūt","bíngyǔ","hǎi'hê","ggiàn'gāh","cǎoléh'ǎ/cǎoluéh'ǎ"], "Pingyim"),
            (["itkâi","sāmzân","butsūt","bīng'iù/bîng'iù","hai'hē","ghiàn'gāh","caulēà/cauluēà"], "Tongiong"),
            (["it̚²¹kʰai¹¹/it̚³²kʰai²¹","sam⁴⁴tsan¹¹/sam⁵⁵tsan²¹","put̚²¹sut̚²¹/put̚³²sut̚³²","piɪŋ²⁵iu⁵³/piɪŋ²⁴iu⁵¹","hai⁵³he²²/hai⁵¹he³³","giɛn¹¹kaʔ²¹/giɛn²¹kaʔ³²","tsʰau⁵³leʔ⁵a⁵³/tsʰau⁵¹lueʔ⁴a⁵¹"], "IPA")
        ]
        for transl, system in test_data:
            data = list(zip(hanji_data, transl))
            checker(self, data, Converter(system=system, punctuation='none', apostrophe=True, delimiter=''), Converter(system=system, dialect="north", punctuation='none', apostrophe=True, delimiter=''))

    def test_apostrophe_delimiter_number(self):
        test_data = [
            (["it4khai3","sam1tsan3","put4sut4","ping5iu2","hai2he7","gian3kah4","tshau2leh8a2/tshau2lueh8a2"], "Tailo"),
            (["it4khai3","sam1chan3","put4sut4","peng5iu2","hai2he7","gian3kah4","chhau2leh8a2/chhau2loeh8a2"], "POJ"),
            (["ㄧㆵ4ㄎㄞ3","ㄙㆰ1ㄗㄢ3","ㄅㄨㆵ4ㄙㄨㆵ4","ㄅㄧㄥ5ㄧㄨ2","ㄏㄞ2ㄏㆤ7","ㆣㄧㄢ3ㄍㄚㆷ4","ㄘㄠ2ㄌㆤㆷ8ㄚ2/ㄘㄠ2ㄌㄨㆤㆷ8ㄚ2"], "Zhuyin"),
            (["it4khai3","sam1can3","put4sut4","ping5iu2","hai2he7","gian3kah4","chau2leh8a2/chau2lueh8a2"], "TLPA"),
            (["yit4kai3","sam1zan3","but4sut4","bing5yu2","hai2he7","ggian3gah4","cao2leh8a2/cao2lueh8a2"], "Pingyim"),
            (["it8kai3","sam7zan3","but8sut4","bing7iu2/bing3iu2","hai1he7","ghian2gah4","cau1le7a2/cau1lue7a2"], "Tongiong"),
            (["it̚4kʰai3","sam1tsan3","put̚4sut̚4","piɪŋ5iu2","hai2he7","giɛn3kaʔ4","tsʰau2leʔ8a2/tsʰau2lueʔ8a2"], "IPA")
        ]
        for transl, system in test_data:
            data = list(zip(hanji_data, transl))
            checker(self, data, Converter(system=system, punctuation='none', apostrophe=True, delimiter='', format='number'), Converter(system=system, dialect="north", punctuation='none', apostrophe=True, delimiter='', format='number'))

    def test_apostrophe_delimiter_strip(self):
        test_data = [
            (["itkhai","samtsan","put'sut","ping'iu","hai'he","giankah","tshauleh'a/tshaulueh'a"], "Tailo"),
            (["itkhai","samchan","putsut","peng'iu","hai'he","giankah","chhauleh'a/chhauloeh'a"], "POJ"),
            (["ㄧㆵㄎㄞ","ㄙㆰㄗㄢ","ㄅㄨㆵㄙㄨㆵ","ㄅㄧㄥㄧㄨ","ㄏㄞㄏㆤ","ㆣㄧㄢㄍㄚㆷ","ㄘㄠㄌㆤㆷㄚ/ㄘㄠㄌㄨㆤㆷㄚ"], "Zhuyin"),
            (["itkhai","samcan","putsut","ping'iu","hai'he","giankah","chauleh'a/chaulueh'a"], "TLPA"),
            (["yitkai","samzan","butsut","bingyu","hai'he","ggian'gah","caoleh'a/caolueh'a"], "Pingyim"),
            (["itkai","samzan","butsut","bing'iu","hai'he","ghian'gah","caulea/cauluea"], "Tongiong"),
            (["it̚kʰai","samtsan","put̚sut̚","piɪŋiu","haihe","giɛnkaʔ","tsʰauleʔa/tsʰaulueʔa"], "IPA")
        ]
        for transl, system in test_data:
            data = list(zip(hanji_data, transl))
            checker(self, data, Converter(system=system, punctuation='none', apostrophe=True, delimiter='', format='strip'), Converter(system=system, dialect="north", punctuation='none', apostrophe=True, delimiter='', format='strip'))