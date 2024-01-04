from taibun.taibun import Converter
from utils import checker

hanji_data = ["標價","按呢","介紹人","祝你今仔日真好的日子","咱的食飯"]

def test_default():
	test_data = [
        (["phiau-kè","án-ne/án-ni","kài-siāu-jîn/kài-siāu-lîn","tsiok lí kin-á-ji̍t tsin-hó--ê ji̍t-tsí/tsiok lí kin-á-li̍t tsin-hó--ê li̍t-tsí","lán--ê tsia̍h-pn̄g"], "Tailo"),
		(["phiau-kè","án-ne/án-ni","kài-siāu-jîn/kài-siāu-lîn","chiok lí kin-á-ji̍t chin-hó--ê ji̍t-chí/chiok lí kin-á-li̍t chin-hó--ê li̍t-chí","lán--ê chia̍h-pn̄g"], "POJ"),
		(["ㄆㄧㄠ ㄍㆤ˪","ㄢˋ ㄋㆤ/ㄢˋ ㄋㄧ","ㄍㄞ˪ ㄒㄧㄠ˫ ㆢㄧㄣˊ/ㄍㄞ˪ ㄒㄧㄠ˫ ㄌㄧㄣˊ","ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㆢㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㆢㄧㆵ˙ ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㄌㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㄌㄧㆵ˙ ㄐㄧˋ","ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙ ㄅㆭ˫"], "Zhuyin"),
		(["phiau1 ke3","an2 ne1/an2 ni1","kai3 siau7 jin5/kai3 siau7 lin5","ciok4 li2 kin1 a2 jit8 cin1 ho2 e5 jit8 ci2/ciok4 li2 kin1 a2 lit8 cin1 ho2 e5 lit8 ci2","lan2 e5 ciah8 png7"], "TLPA"),
		(["piāogè","ǎnlnē/ǎnlnī","gàisiâozzín/gàisiâolín","ziōk lǐ gīnǎzzít zīnhǒ é zzítzǐ/ziōk lǐ gīnǎlít zīnhǒ é lítzǐ","lǎn é ziáhbn̂g"], "Pingyim"),
		(["piāu-gê","an-ne/an-ni","gài-siâu-rĭn/gài-siâu-lĭn","ziok li gīn-a-rīt zīn-hòr--e̊ rīt-zì/ziok li gīn-a-līt zīn-hòr--e̊ līt-zì","làn--e̊ ziâ-bn̄g"], "Tongiong")
    ]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none'), Converter(system=system, dialect="north", punctuation='none'))

def test_hyphen():
	test_data = [
		(["phiau-kè","án-ne/án-ni","kài-siāu-jîn/kài-siāu-lîn","tsiok lí kin-á-ji̍t tsin-hó--ê ji̍t-tsí/tsiok lí kin-á-li̍t tsin-hó--ê li̍t-tsí","lán--ê tsia̍h-pn̄g"], "Tailo"),
		(["phiau-kè","án-ne/án-ni","kài-siāu-jîn/kài-siāu-lîn","chiok lí kin-á-ji̍t chin-hó--ê ji̍t-chí/chiok lí kin-á-li̍t chin-hó--ê li̍t-chí","lán--ê chia̍h-pn̄g"], "POJ"),
		(["ㄆㄧㄠ-ㄍㆤ˪","ㄢˋ-ㄋㆤ/ㄢˋ-ㄋㄧ","ㄍㄞ˪-ㄒㄧㄠ˫-ㆢㄧㄣˊ/ㄍㄞ˪-ㄒㄧㄠ˫-ㄌㄧㄣˊ","ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ-ㄚˋ-ㆢㄧㆵ˙ ㄐㄧㄣ-ㄏㄜˋ ㆤˊ ㆢㄧㆵ˙-ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ-ㄚˋ-ㄌㄧㆵ˙ ㄐㄧㄣ-ㄏㄜˋ ㆤˊ ㄌㄧㆵ˙-ㄐㄧˋ","ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙-ㄅㆭ˫"], "Zhuyin"),
		(["phiau1-ke3","an2-ne1/an2-ni1","kai3-siau7-jin5/kai3-siau7-lin5","ciok4 li2 kin1-a2-jit8 cin1-ho2 e5 jit8-ci2/ciok4 li2 kin1-a2-lit8 cin1-ho2 e5 lit8-ci2","lan2 e5 ciah8-png7"], "TLPA"),
		(["piāo-gè","ǎn-lnē/ǎn-lnī","gài-siâo-zzín/gài-siâo-lín","ziōk lǐ gīn-ǎ-zzít zīn-hǒ é zzít-zǐ/ziōk lǐ gīn-ǎ-lít zīn-hǒ é lít-zǐ","lǎn é ziáh-bn̂g"], "Pingyim"),
		(["piāu-gê","an-ne/an-ni","gài-siâu-rĭn/gài-siâu-lĭn","ziok li gīn-a-rīt zīn-hòr--e̊ rīt-zì/ziok li gīn-a-līt zīn-hòr--e̊ līt-zì","làn--e̊ ziâ-bn̄g"], "Tongiong")
	]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none', delimiter='-'), Converter(system=system, dialect="north", punctuation='none', delimiter='-'))

def test_space():
	test_data = [
		(["phiau kè","án ne/án ni","kài siāu jîn/kài siāu lîn","tsiok lí kin á ji̍t tsin hó--ê ji̍t tsí/tsiok lí kin á li̍t tsin hó--ê li̍t tsí","lán--ê tsia̍h pn̄g"], "Tailo"),
		(["phiau kè","án ne/án ni","kài siāu jîn/kài siāu lîn","chiok lí kin á ji̍t chin hó--ê ji̍t chí/chiok lí kin á li̍t chin hó--ê li̍t chí","lán--ê chia̍h pn̄g"], "POJ"),
		(["ㄆㄧㄠ ㄍㆤ˪","ㄢˋ ㄋㆤ/ㄢˋ ㄋㄧ","ㄍㄞ˪ ㄒㄧㄠ˫ ㆢㄧㄣˊ/ㄍㄞ˪ ㄒㄧㄠ˫ ㄌㄧㄣˊ","ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㆢㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㆢㄧㆵ˙ ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㄌㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㄌㄧㆵ˙ ㄐㄧˋ","ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙ ㄅㆭ˫"], "Zhuyin"),
		(["phiau1 ke3","an2 ne1/an2 ni1","kai3 siau7 jin5/kai3 siau7 lin5","ciok4 li2 kin1 a2 jit8 cin1 ho2 e5 jit8 ci2/ciok4 li2 kin1 a2 lit8 cin1 ho2 e5 lit8 ci2","lan2 e5 ciah8 png7"], "TLPA"),
		(["piāo gè","ǎn lnē/ǎn lnī","gài siâo zzín/gài siâo lín","ziōk lǐ gīn ǎ zzít zīn hǒ é zzít zǐ/ziōk lǐ gīn ǎ lít zīn hǒ é lít zǐ","lǎn é ziáh bn̂g"], "Pingyim"),
		(["piāu gê","an ne/an ni","gài siâu rĭn/gài siâu lĭn","ziok li gīn a rīt zīn hòr--e̊ rīt zì/ziok li gīn a līt zīn hòr--e̊ līt zì","làn--e̊ ziâ bn̄g"], "Tongiong")
	]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none', delimiter=' '), Converter(system=system, dialect="north", punctuation='none', delimiter=' '))

def test_nospace():
	test_data = [
		(["phiaukè","ánne/ánni","kàisiāujîn/kàisiāulîn","tsiok lí kináji̍t tsinhó--ê ji̍ttsí/tsiok lí kináli̍t tsinhó--ê li̍ttsí","lán--ê tsia̍hpn̄g"], "Tailo"),
		(["phiaukè","ánne/ánni","kàisiāujîn/kàisiāulîn","chiok lí kináji̍t chinhó--ê ji̍tchí/chiok lí kináli̍t chinhó--ê li̍tchí","lán--ê chia̍hpn̄g"], "POJ"),
		(["ㄆㄧㄠㄍㆤ˪","ㄢˋㄋㆤ/ㄢˋㄋㄧ","ㄍㄞ˪ㄒㄧㄠ˫ㆢㄧㄣˊ/ㄍㄞ˪ㄒㄧㄠ˫ㄌㄧㄣˊ","ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣㄚˋㆢㄧㆵ˙ ㄐㄧㄣㄏㄜˋ ㆤˊ ㆢㄧㆵ˙ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣㄚˋㄌㄧㆵ˙ ㄐㄧㄣㄏㄜˋ ㆤˊ ㄌㄧㆵ˙ㄐㄧˋ","ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙ㄅㆭ˫"], "Zhuyin"),
		(["phiau1ke3","an2ne1/an2ni1","kai3siau7jin5/kai3siau7lin5","ciok4 li2 kin1a2jit8 cin1ho2 e5 jit8ci2/ciok4 li2 kin1a2lit8 cin1ho2 e5 lit8ci2","lan2 e5 ciah8png7"], "TLPA"),
		(["piāogè","ǎnlnē/ǎnlnī","gàisiâozzín/gàisiâolín","ziōk lǐ gīnǎzzít zīnhǒ é zzítzǐ/ziōk lǐ gīnǎlít zīnhǒ é lítzǐ","lǎn é ziáhbn̂g"], "Pingyim"),
		(["piāugê","anne/anni","gàisiâurĭn/gàisiâulĭn","ziok li gīnarīt zīnhòr--e̊ rītzì/ziok li gīnalīt zīnhòr--e̊ lītzì","làn--e̊ ziâbn̄g"], "Tongiong")
	]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none', delimiter=''), Converter(system=system, dialect="north", punctuation='none', delimiter=''))