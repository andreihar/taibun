from taibun.taibun import Converter
from utils import checker

def test_mark():
	tailo = ["標價,phiau-kè","按呢,án-ne/án-ni","介紹人,kài-siāu-jîn/kài-siāu-lîn","八字,peh-jī/pueh-lī","圾洗,sap-sé/sap-sué","轄區,hat-khu","福建,Hok-kiàn","娘囝,niû-kiánn","毋免,m̄-bián","白話字,Pe̍h-uē-jī/Pe̍h-uē-lī","業產,gia̍p-sán","佛祖,Pu̍t-tsóo","木香,ba̍k-hiunn","姆婆,ḿ-pô"]
	poj = ["標價,phiau-kè","按呢,án-ne/án-ni","介紹人,kài-siāu-jîn/kài-siāu-lîn","八字,peh-jī/poeh-lī","圾洗,sap-sé/sap-sóe","轄區,hat-khu","福建,Hok-kiàn","娘囝,niû-kiáⁿ","毋免,m̄-bián","白話字,Pe̍h-ōe-jī/Pe̍h-ōe-lī","業產,gia̍p-sán","佛祖,Pu̍t-chó͘","木香,ba̍k-hiuⁿ","姆婆,ḿ-pô"]
	zhuyin = ["標價,ㄆㄧㄠ ㄍㆤ˪","按呢,ㄢˋ ㄋㆤ/ㄢˋ ㄋㄧ","介紹人,ㄍㄞ˪ ㄒㄧㄠ˫ ㆢㄧㄣˊ/ㄍㄞ˪ ㄒㄧㄠ˫ ㄌㄧㄣˊ","八字,ㄅㆤㆷ ㆢㄧ˫/ㄅㄨㆤㆷ ㄌㄧ˫","圾洗,ㄙㄚㆴ ㄙㆤˋ/ㄙㄚㆴ ㄙㄨㆤˋ","轄區,ㄏㄚㆵ ㄎㄨ","福建,ㄏㆦㆶ ㄍㄧㄢ˪","娘囝,ㄋㄧㄨˊ ㄍㄧㆩˋ","毋免,ㆬ˫ ㆠㄧㄢˋ","白話字,ㄅㆤㆷ˙ ㄨㆤ˫ ㆢㄧ˫/ㄅㆤㆷ˙ ㄨㆤ˫ ㄌㄧ˫","業產,ㆣㄧㄚㆴ˙ ㄙㄢˋ","佛祖,ㄅㄨ ㆵ˙ ㄗㆦˋ","木香,ㆠㄚㆶ˙ ㄏㄧㆫ","姆婆,ㆬˋ ㄅㄜˊ"]
	tlpa = ["標價,phiau1 ke3","按呢,an2 ne1/an2 ni1","介紹人,kai3 siau7 jin5/kai3 siau7 lin5","八字,peh4 ji7/pueh4 li7","圾洗,sap4 se2/sap4 sue2","轄區,hat4 khu1","福建,Hok4 kian3","娘囝,niu5 kiann2","毋免,m7 bian2","白話字,Peh8 ue7 ji7/Peh8 ue7 li7","業產,giap8 san2","佛祖,Put8 coo2","木香,bak8 hiunn1","姆婆,m2 po5"]
	tongiong = ["標價,piāu-gê","按呢,an-ne/an-ni","介紹人,gài-siâu-rĭn/gài-siâu-lĭn","八字,bè-rī/buè-lī","圾洗,sap-sè/sap-suè","轄區,hat-ku","福建,Hok-giân","娘囝,niū-giànn/niû-giànn","毋免,m̂-bhiàn","白話字,Bê-uê-rī/Bê-uê-lī","業產,ghiāp-sàn","佛祖,Būt-zòr","木香,bhāk-hiunn","姆婆,m-bŏr"]
	
	checker(tailo, Converter(system="Tailo", punctuation='none', format='mark'), Converter(system="Tailo", dialect="north", punctuation='none', format='mark'))
	checker(poj, Converter(system="POJ", punctuation='none', format='mark'), Converter(system="POJ", dialect="north", punctuation='none', format='mark'))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none', format='mark'), Converter(system="Zhuyin", dialect="north", punctuation='none', format='mark'))
	checker(tlpa, Converter(system="TLPA", punctuation='none', format='mark'), Converter(system="TLPA", dialect="north", punctuation='none', format='mark'))
	checker(tongiong, Converter(system="Tongiong", punctuation='none', format='mark'), Converter(system="Tongiong", dialect="north", punctuation='none', format='mark'))

def test_number():
	tailo = ["標價,phiau1-ke3","按呢,an2-ne1/an2-ni1","介紹人,kai3-siau7-jin5/kai3-siau7-lin5","八字,peh4-ji7/pueh4-li7","圾洗,sap4-se2/sap4-sue2","轄區,hat4-khu1","福建,Hok4-kian3","娘囝,niu5-kiann2","毋免,m7-bian2","白話字,Peh8-ue7-ji7/Peh8-ue7-li7","業產,giap8-san2","佛祖,Put8-tsoo2","木香,bak8-hiunn1","姆婆,m2-po5"]
	poj = ["標價,phiau1-ke3","按呢,an2-ne1/an2-ni1","介紹人,kai3-siau7-jin5/kai3-siau7-lin5","八字,peh4-ji7/poeh4-li7","圾洗,sap4-se2/sap4-soe2","轄區,hat4-khu1","福建,Hok4-kian3","娘囝,niu5-kiaⁿ2","毋免,m7-bian2","白話字,Peh8-oe7-ji7/Peh8-oe7-li7","業產,giap8-san2","佛祖,Put8-cho2","木香,bak8-hiuⁿ1","姆婆,m2-po5"]
	zhuyin = ["標價,ㄆㄧㄠ1 ㄍㆤ3","按呢,ㄢ2 ㄋㆤ1/ㄢ2 ㄋㄧ1","介紹人,ㄍㄞ3 ㄒㄧㄠ7 ㆢㄧㄣ5/ㄍㄞ3 ㄒㄧㄠ7 ㄌㄧㄣ5","八字,ㄅㆤㆷ4 ㆢㄧ7/ㄅㄨㆤㆷ4 ㄌㄧ7","圾洗,ㄙㄚㆴ4 ㄙㆤ2/ㄙㄚㆴ4  ㄙㄨㆤ2","轄區,ㄏㄚㆵ4 ㄎㄨ1","福建,ㄏㆦㆶ4 ㄍㄧㄢ3","娘囝,ㄋㄧㄨ5 ㄍㄧㆩ2","毋免,ㆬ7 ㆠㄧㄢ2","白話字,ㄅㆤㆷ8 ㄨㆤ7 ㆢㄧ7/ㄅㆤㆷ8 ㄨㆤ7 ㄌㄧ7","業產,ㆣㄧㄚㆴ8 ㄙㄢ2","佛祖,ㄅㄨㆵ8 ㄗㆦ2","木香,ㆠㄚㆶ8 ㄏㄧㆫ1","姆婆,ㆬ2 ㄅㄜ5"]
	tlpa = ["標價,phiau1 ke3","按呢,an2 ne1/an2 ni1","介紹人,kai3 siau7 jin5/kai3 siau7 lin5","八字,peh4 ji7/pueh4 li7","圾洗,sap4 se2/sap4 sue2","轄區,hat4 khu1","福建,Hok4 kian3","娘囝,niu5 kiann2","毋免,m7 bian2","白話字,Peh8 ue7 ji7/Peh8 ue7 li7","業產,giap8 san2","佛祖,Put8 coo2","木香,bak8 hiunn1","姆婆,m2 po5"]
	tongiong = ["標價,piau7-ge3","按呢,an1-ne1/an1-ni1","介紹人,gai2-siau3-rin5/gai2-siau3-lin5","八字,be2-ri7/bue2-li7","圾洗,sap8-se2/sap8-sue2","轄區,hat8-ku1","福建,Hok8-gian3"," 娘囝,niu7-giann2/niu3-giann2","毋免,m3-bhian2","白話字,Be3-ue3-ri7/Be3-ue3-li7","業產,ghiap4-san2","佛祖,But4-zor2","木香,bhak4-hiunn1","姆婆,m1-bor5"]

	checker(tailo, Converter(system="Tailo", punctuation='none', format='number'), Converter(system="Tailo", dialect="north", punctuation='none', format='number'))
	checker(poj, Converter(system="POJ", punctuation='none', format='number'), Converter(system="POJ", dialect="north", punctuation='none', format='number'))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none', format='number'), Converter(system="Zhuyin", dialect="north", punctuation='none', format='number'))
	checker(tlpa, Converter(system="TLPA", punctuation='none', format='number'), Converter(system="TLPA", dialect="north", punctuation='none', format='number'))
	checker(tongiong, Converter(system="Tongiong", punctuation='none', format='number'), Converter(system="Tongiong", dialect="north", punctuation='none', format='number'))

def test_strip():
	tailo = ["標價,phiau-ke","按呢,an-ne/an-ni","介紹人,kai-siau-jin/kai-siau-lin","八字,peh-ji/pueh-li","圾洗,sap-se/sap-sue","轄區,hat-khu","福建,Hok-kian","娘囝,niu-kiann","毋免,m-bian","白話字,Peh-ue-ji/Peh-ue-li","業產,giap-san","佛祖,Put-tsoo","木香,bak-hiunn","姆婆,m-po"]
	poj = ["標價,phiau-ke","按呢,an-ne/an-ni","介紹人,kai-siau-jin/kai-siau-lin","八字,peh-ji/poeh-li","圾洗,sap-se/sap-soe","轄區,hat-khu","福建,Hok-kian","娘囝,niu-kiaⁿ","毋免,m-bian","白話字,Peh-oe-ji/Peh-oe-li","業產,giap-san","佛祖,Put-cho","木香,bak-hiuⁿ","姆婆,m-po"]
	zhuyin = ["標價,ㄆㄧㄠ ㄍㆤ","按呢,ㄢ ㄋㆤ/ㄢ ㄋㄧ","介紹人,ㄍㄞ ㄒㄧㄠ ㆢㄧㄣ/ㄍㄞ ㄒㄧㄠ ㄌㄧㄣ","八字,ㄅㆤㆷ ㆢㄧ/ㄅㄨㆤㆷ ㄌㄧ","圾洗,ㄙㄚㆴ ㄙㆤ/ㄙㄚㆴ ㄙㄨㆤ","轄區,ㄏㄚㆵ ㄎㄨ","福建,ㄏㆦㆶ ㄍㄧㄢ","娘囝,ㄋㄧㄨ ㄍㄧㆩ","毋免,ㆬ ㆠㄧㄢ","白話字,ㄅㆤㆷ ㄨㆤ ㆢㄧ/ㄅㆤㆷ ㄨㆤ ㄌㄧ","業產,ㆣㄧㄚㆴ ㄙㄢ","佛祖,ㄅㄨㆵ ㄗㆦ","木香,ㆠㄚㆶ ㄏㄧ ㆫ","姆婆,ㆬ ㄅㄜ"]
	tlpa = ["標價,phiau ke","按呢,an ne/an ni","介紹人,kai siau jin/kai siau lin","八字,peh ji/pueh li","圾洗,sap se/sap sue","轄區,hat khu","福建,Hok kian","娘囝,niu kiann","毋免,m bian","白話字,Peh ue ji/Peh ue li","業產,giap san","佛祖,Put coo","木香,bak hiunn","姆婆,m po"]
	tongiong = ["標價,piau-ge","按呢,an-ne/an-ni","介紹人,gai-siau-rin/gai-siau-lin","八字,be-ri/bue-li","圾洗,sap-se/sap-sue","轄區,hat-ku","福建,Hok-gian","娘囝,niu-giann","毋免,m-bhian","白話字,Be-ue-ri/Be-ue-li","業產,ghiap-san","佛祖,But-zor","木香,bhak-hiunn","姆婆,m-bor"]

	checker(tailo, Converter(system="Tailo", punctuation='none', format='strip'), Converter(system="Tailo", dialect="north", punctuation='none', format='strip'))
	checker(poj, Converter(system="POJ", punctuation='none', format='strip'), Converter(system="POJ", dialect="north", punctuation='none', format='strip'))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none', format='strip'), Converter(system="Zhuyin", dialect="north", punctuation='none', format='strip'))
	checker(tlpa, Converter(system="TLPA", punctuation='none', format='strip'), Converter(system="TLPA", dialect="north", punctuation='none', format='strip'))
	checker(tongiong, Converter(system="Tongiong", punctuation='none', format='strip'), Converter(system="Tongiong", dialect="north", punctuation='none', format='strip'))