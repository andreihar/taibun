from taibun.taibun import Converter
from utils import checker

hanji_data = ["標價","按呢","介紹人","八字","圾洗","轄區","福建","娘囝","毋免","白話字","業產","佛祖","木香","姆婆"]

def test_mark():
	test_data = [
		(["phiau-kè","án-ne/án-ni","kài-siāu-jîn/kài-siāu-lîn","peh-jī/pueh-lī","sap-sé/sap-sué","hat-khu","Hok-kiàn","niû-kiánn","m̄-bián","Pe̍h-uē-jī/Pe̍h-uē-lī","gia̍p-sán","Pu̍t-tsóo","ba̍k-hiunn","ḿ-pô"], "Tailo"),
		(["phiau-kè","án-ne/án-ni","kài-siāu-jîn/kài-siāu-lîn","peh-jī/poeh-lī","sap-sé/sap-sóe","hat-khu","Hok-kiàn","niû-kiáⁿ","m̄-bián","Pe̍h-ōe-jī/Pe̍h-ōe-lī","gia̍p-sán","Pu̍t-chó͘","ba̍k-hiuⁿ","ḿ-pô"], "POJ"),
		(["ㄆㄧㄠ ㄍㆤ˪","ㄢˋ ㄋㆤ/ㄢˋ ㄋㄧ","ㄍㄞ˪ ㄒㄧㄠ˫ ㆢㄧㄣˊ/ㄍㄞ˪ ㄒㄧㄠ˫ ㄌㄧㄣˊ","ㄅㆤㆷ ㆢㄧ˫/ㄅㄨㆤㆷ ㄌㄧ˫","ㄙㄚㆴ ㄙㆤˋ/ㄙㄚㆴ ㄙㄨㆤˋ","ㄏㄚㆵ ㄎㄨ","ㄏㆦㆶ ㄍㄧㄢ˪","ㄋㄧㄨˊ ㄍㄧㆩˋ","ㆬ˫ ㆠㄧㄢˋ","ㄅㆤㆷ˙ ㄨㆤ˫ ㆢㄧ˫/ㄅㆤㆷ˙ ㄨㆤ˫ ㄌㄧ˫","ㆣㄧㄚㆴ˙ ㄙㄢˋ","ㄅㄨㆵ˙ ㄗㆦˋ","ㆠㄚㆶ˙ ㄏㄧㆫ","ㆬˋ ㄅㄜˊ"], "Zhuyin"),
		(["phiau1 ke3","an2 ne1/an2 ni1","kai3 siau7 jin5/kai3 siau7 lin5","peh4 ji7/pueh4 li7","sap4 se2/sap4 sue2","hat4 khu1","Hok4 kian3","niu5 kiann2","m7 bian2","Peh8 ue7 ji7/Peh8 ue7 li7","giap8 san2","Put8 coo2","bak8 hiunn1","m2 po5"], "TLPA"),
		(["piāogè","ǎnlnē/ǎnlnī","gàisiâozzín/gàisiâolín","bēhzzî/buēhlî","sāpsě/sāpsuě","hātkū","Hōkgiàn","lniúginǎ","m̂bbiǎn","Béhwêzzî/Béhwêlî","ggiápsǎn","Bútzoǒ","bbákhniū","m̌bó"], "Pingyim"),
		(["piāu-gê","an-ne/an-ni","gài-siâu-rĭn/gài-siâu-lĭn","bè-rī/buè-lī","sap-sè/sap-suè","hat-ku","Hok-giân","niū-giànn/niû-giànn","m̂-bhiàn","Bê-uê-rī/Bê-uê-lī","ghiāp-sàn","Būt-zòr","bhāk-hiunn","m-bŏr"], "Tongiong"),
		(["pʰiau⁴⁴ ke¹¹/pʰiau⁵⁵ ke²¹","an⁵³ nẽ⁴⁴/an⁵¹ nĩ⁵⁵","kai¹¹ ɕiau²² dʑin²⁵/kai²¹ ɕiau³³ lin²⁴","peʔ²¹ dʑi²²/pueʔ³² li³³","sap̚²¹ se⁵³/sap̚³² sue⁵¹","hat̚²¹ kʰu⁴⁴/hat̚³² kʰu⁵⁵","Hɔk̚²¹ kiɛn¹¹/Hɔk̚³² kiɛn²¹","nĩu²⁵ kiã⁵³/nĩu²⁴ kiã⁵¹","m̩²² biɛn⁵³/m̩³³ biɛn⁵¹","Peʔ⁵ ue²² dʑi²²/Peʔ⁴ ue³³ li³³","giap̚⁵ san⁵³/giap̚⁴ san⁵¹","Put̚⁵ tsɔ⁵³/Put̚⁴ tsɔ⁵¹","bak̚⁵ hiũ⁴⁴/bak̚⁴ hiũ⁵⁵","m̩⁵³ pə²⁵/m̩⁵¹ po²⁴"], "IPA")
	]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none', format='mark'), Converter(system=system, dialect="north", punctuation='none', format='mark'))

def test_number():
	test_data = [
		(["phiau1-ke3","an2-ne1/an2-ni1","kai3-siau7-jin5/kai3-siau7-lin5","peh4-ji7/pueh4-li7","sap4-se2/sap4-sue2","hat4-khu1","Hok4-kian3","niu5-kiann2","m7-bian2","Peh8-ue7-ji7/Peh8-ue7-li7","giap8-san2","Put8-tsoo2","bak8-hiunn1","m2-po5"], "Tailo"),
		(["phiau1-ke3","an2-ne1/an2-ni1","kai3-siau7-jin5/kai3-siau7-lin5","peh4-ji7/poeh4-li7","sap4-se2/sap4-soe2","hat4-khu1","Hok4-kian3","niu5-kiaⁿ2","m7-bian2","Peh8-oe7-ji7/Peh8-oe7-li7","giap8-san2","Put8-cho2","bak8-hiuⁿ1","m2-po5"], "POJ"),
		(["ㄆㄧㄠ1 ㄍㆤ3","ㄢ2 ㄋㆤ1/ㄢ2 ㄋㄧ1","ㄍㄞ3 ㄒㄧㄠ7 ㆢㄧㄣ5/ㄍㄞ3 ㄒㄧㄠ7 ㄌㄧㄣ5","ㄅㆤㆷ4 ㆢㄧ7/ㄅㄨㆤㆷ4 ㄌㄧ7","ㄙㄚㆴ4 ㄙㆤ2/ㄙㄚㆴ4 ㄙㄨㆤ2","ㄏㄚㆵ4 ㄎㄨ1","ㄏㆦㆶ4 ㄍㄧㄢ3","ㄋㄧㄨ5 ㄍㄧㆩ2","ㆬ7 ㆠㄧㄢ2","ㄅㆤㆷ8 ㄨㆤ7 ㆢㄧ7/ㄅㆤㆷ8 ㄨㆤ7 ㄌㄧ7","ㆣㄧㄚㆴ8 ㄙㄢ2","ㄅㄨㆵ8 ㄗㆦ2","ㆠㄚㆶ8 ㄏㄧㆫ1","ㆬ2 ㄅㄜ5"], "Zhuyin"),
		(["phiau1 ke3","an2 ne1/an2 ni1","kai3 siau7 jin5/kai3 siau7 lin5","peh4 ji7/pueh4 li7","sap4 se2/sap4 sue2","hat4 khu1","Hok4 kian3","niu5 kiann2","m7 bian2","Peh8 ue7 ji7/Peh8 ue7 li7","giap8 san2","Put8 coo2","bak8 hiunn1","m2 po5"], "TLPA"),
		(["piao1ge3","an2lne1/an2lni1","gai3siao7zzin5/gai3siao7lin5","beh4zzi7/bueh4li7","sap4se2/sap4sue2","hat4ku1","Hok4gian3","lniu5gina2","m7bbian2","Beh8we7zzi7/Beh8we7li7","ggiap8san2","But8zoo2","bbak8hniu1","m2bo5"], "Pingyim"),
		(["piau7-ge3","an1-ne1/an1-ni1","gai2-siau3-rin5/gai2-siau3-lin5","be2-ri7/bue2-li7","sap8-se2/sap8-sue2","hat8-ku1","Hok8-gian3","niu7-giann2/niu3-giann2","m3-bhian2","Be3-ue3-ri7/Be3-ue3-li7","ghiap4-san2","But4-zor2","bhak4-hiunn1","m1-bor5"], "Tongiong"),
		(["pʰiau1 ke3","an2 nẽ1/an2 nĩ1","kai3 ɕiau7 dʑin5/kai3 ɕiau7 lin5","peʔ4 dʑi7/pueʔ4 li7","sap̚4 se2/sap̚4 sue2","hat̚4 kʰu1","Hɔk̚4 kiɛn3","nĩu5 kiã2","m̩7 biɛn2","Peʔ8 ue7 dʑi7/Peʔ8 ue7 li7","giap̚8 san2","Put̚8 tsɔ2","bak̚8 hiũ1","m̩2 pə5/m̩2 po5"], "IPA")
	]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none', format='number'), Converter(system=system, dialect="north", punctuation='none', format='number'))

def test_strip():
	test_data = [
		(["phiau-ke","an-ne/an-ni","kai-siau-jin/kai-siau-lin","peh-ji/pueh-li","sap-se/sap-sue","hat-khu","Hok-kian","niu-kiann","m-bian","Peh-ue-ji/Peh-ue-li","giap-san","Put-tsoo","bak-hiunn","m-po"], "Tailo"),
		(["phiau-ke","an-ne/an-ni","kai-siau-jin/kai-siau-lin","peh-ji/poeh-li","sap-se/sap-soe","hat-khu","Hok-kian","niu-kiaⁿ","m-bian","Peh-oe-ji/Peh-oe-li","giap-san","Put-cho","bak-hiuⁿ","m-po"], "POJ"),
		(["ㄆㄧㄠ ㄍㆤ","ㄢ ㄋㆤ/ㄢ ㄋㄧ","ㄍㄞ ㄒㄧㄠ ㆢㄧㄣ/ㄍㄞ ㄒㄧㄠ ㄌㄧㄣ","ㄅㆤㆷ ㆢㄧ/ㄅㄨㆤㆷ ㄌㄧ","ㄙㄚㆴ ㄙㆤ/ㄙㄚㆴ ㄙㄨㆤ","ㄏㄚㆵ ㄎㄨ","ㄏㆦㆶ ㄍㄧㄢ","ㄋㄧㄨ ㄍㄧㆩ","ㆬ ㆠㄧㄢ","ㄅㆤㆷ ㄨㆤ ㆢㄧ/ㄅㆤㆷ ㄨㆤ ㄌㄧ","ㆣㄧㄚㆴ ㄙㄢ","ㄅㄨㆵ ㄗㆦ","ㆠㄚㆶ ㄏㄧㆫ","ㆬ ㄅㄜ"], "Zhuyin"),
		(["phiau ke","an ne/an ni","kai siau jin/kai siau lin","peh ji/pueh li","sap se/sap sue","hat khu","Hok kian","niu kiann","m bian","Peh ue ji/Peh ue li","giap san","Put coo","bak hiunn","m po"], "TLPA"),
		(["piaoge","anlne/anlni","gaisiaozzin/gaisiaolin","behzzi/buehli","sapse/sapsue","hatku","Hokgian","lniugina","mbbian","Behwezzi/Behweli","ggiapsan","Butzoo","bbakhniu","mbo"], "Pingyim"),
		(["piau-ge","an-ne/an-ni","gai-siau-rin/gai-siau-lin","be-ri/bue-li","sap-se/sap-sue","hat-ku","Hok-gian","niu-giann","m-bhian","Be-ue-ri/Be-ue-li","ghiap-san","But-zor","bhak-hiunn","m-bor"], "Tongiong"),
		(["pʰiau ke","an nẽ/an nĩ","kai ɕiau dʑin/kai ɕiau lin","peʔ dʑi/pueʔ li","sap̚ se/sap̚ sue","hat̚ kʰu","Hɔk̚ kiɛn","nĩu kiã","m̩ biɛn","Peʔ ue dʑi/Peʔ ue li","giap̚ san","Put̚ tsɔ","bak̚ hiũ","m̩ pə/m̩ po"], "IPA")
	]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none', format='strip'), Converter(system=system, dialect="north", punctuation='none', format='strip'))