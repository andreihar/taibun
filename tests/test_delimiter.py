from taibun.taibun import Converter
from utils import checker

def test_default():
	tailo = ["標價,phiau-kè","按呢,án-ne/án-ni","介紹人,kài-siāu-jîn/kài-siāu-lîn","祝你今仔日真好的日子,tsiok lí kin-á-ji̍t tsin-hó--ê ji̍t-tsí/tsiok lí kin-á-li̍t tsin-hó--ê li̍t-tsí","咱的食飯,lán--ê tsia̍h-pn̄g"]
	poj = ["標價,phiau-kè","按呢,án-ne/án-ni","介紹人,kài-siāu-jîn/kài-siāu-lîn","祝你今仔日真好的日子,chiok lí kin-á-ji̍t chin-hó--ê ji̍t-chí/chiok lí kin-á-li̍t chin-hó--ê li̍t-chí","咱的食飯,lán--ê chia̍h-pn̄g"]
	zhuyin = ["標價,ㄆㄧㄠ ㄍㆤ˪","按呢,ㄢˋ ㄋㆤ/ㄢˋ ㄋㄧ","介紹人,ㄍㄞ˪ ㄒㄧㄠ˫ ㆢㄧㄣˊ/ㄍㄞ˪ ㄒㄧㄠ˫ ㄌㄧㄣˊ","祝你今仔日真好的日子,ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㆢㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㆢㄧㆵ˙ ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㄌㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㄌㄧㆵ˙ ㄐㄧˋ","咱的食飯,ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙ ㄅㆭ˫"]
	tlpa = ["標價,phiau1 ke3","按呢,an2 ne1/an2 ni1","介紹人,kai3 siau7 jin5/kai3 siau7 lin5","祝你今仔日真好的日子,ciok4 li2 kin1 a2 jit8 cin1 ho2 e5 jit8 ci2/ciok4 li2 kin1 a2 lit8 cin1 ho2 e5 lit8 ci2","咱的食飯,lan2 e5 ciah8 png7"]
	pingyim = ["標價,piāogè","按呢,ǎnlnē/ǎnlnī","介紹人,gàisiâozzín/gàisiâolín","祝你今仔日真好的日子,ziōk lǐ gīnǎzzít zīnhǒ é zzítzǐ/ziōk lǐ gīnǎlít zīnhǒ é lítzǐ","咱的食飯,lǎn é ziáhbn̂g"]
	tongiong = ["標價,piāu-gê","按呢,an-ne/an-ni","介紹人,gài-siâu-rĭn/gài-siâu-lĭn","祝你今仔日真好的日子,ziok li gīn-a-rīt zīn-hor--ē rīt-zì/ziok li gīn-a-līt zīn-hor--ê līt-zì","咱的食飯,lan--ē ziâ-bn̄g"]

	checker(tailo, Converter(system="Tailo", punctuation='none'), Converter(system="Tailo", dialect="north", punctuation='none'))
	checker(poj, Converter(system="POJ", punctuation='none'), Converter(system="POJ", dialect="north", punctuation='none'))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none'), Converter(system="Zhuyin", dialect="north", punctuation='none'))
	checker(tlpa, Converter(system="TLPA", punctuation='none'), Converter(system="TLPA", dialect="north", punctuation='none'))
	checker(pingyim, Converter(system="Pingyim", punctuation='none'), Converter(system="Pingyim", dialect="north", punctuation='none'))
	checker(tongiong, Converter(system="Tongiong", punctuation='none'), Converter(system="Tongiong", dialect="north", punctuation='none'))

def test_hyphen():
	tailo = ["標價,phiau-kè","按呢,án-ne/án-ni","介紹人,kài-siāu-jîn/kài-siāu-lîn","祝你今仔日真好的日子,tsiok lí kin-á-ji̍t tsin-hó--ê ji̍t-tsí/tsiok lí kin-á-li̍t tsin-hó--ê li̍t-tsí","咱的食飯,lán--ê tsia̍h-pn̄g"]
	poj = ["標價,phiau-kè","按呢,án-ne/án-ni","介紹人,kài-siāu-jîn/kài-siāu-lîn","祝你今仔日真好的日子,chiok lí kin-á-ji̍t chin-hó--ê ji̍t-chí/chiok lí kin-á-li̍t chin-hó--ê li̍t-chí","咱的食飯,lán--ê chia̍h-pn̄g"]
	zhuyin = ["標價,ㄆㄧㄠ-ㄍㆤ˪","按呢,ㄢˋ-ㄋㆤ/ㄢˋ-ㄋㄧ","介紹人,ㄍㄞ˪-ㄒㄧㄠ˫-ㆢㄧㄣˊ/ㄍㄞ˪-ㄒㄧㄠ˫-ㄌㄧㄣˊ","祝你今仔日真好的日子,ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ-ㄚˋ-ㆢㄧㆵ˙ ㄐㄧㄣ-ㄏㄜˋ ㆤˊ ㆢㄧㆵ˙-ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ-ㄚˋ-ㄌㄧㆵ˙ ㄐㄧㄣ-ㄏㄜˋ ㆤˊ ㄌㄧㆵ˙-ㄐㄧˋ","咱的食飯,ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙-ㄅㆭ˫"]
	tlpa = ["標價,phiau1-ke3","按呢,an2-ne1/an2-ni1","介紹人,kai3-siau7-jin5/kai3-siau7-lin5","祝你今仔日真好的日子,ciok4 li2 kin1-a2-jit8 cin1-ho2 e5 jit8-ci2/ciok4 li2 kin1-a2-lit8 cin1-ho2 e5 lit8-ci2","咱的食飯,lan2 e5 ciah8-png7"]
	pingyim = ["標價,piāo-gè","按呢,ǎn-lnē/ǎn-lnī","介紹人,gài-siâo-zzín/gài-siâo-lín","祝你今仔日真好的日子,ziōk lǐ gīn-ǎ-zzít zīn-hǒ é zzít-zǐ/ziōk lǐ gīn-ǎ-lít zīn-hǒ é lít-zǐ","咱的食飯,lǎn é ziáh-bn̂g"]
	tongiong = ["標價,piāu-gê","按呢,an-ne/an-ni","介紹人,gài-siâu-rĭn/gài-siâu-lĭn","祝你今仔日真好的日子,ziok li gīn-a-rīt zīn-hor--ē rīt-zì/ziok li gīn-a-līt zīn-hor--ê līt-zì","咱的食飯,lan--ē ziâ-bn̄g"]

	checker(tailo, Converter(system="Tailo", punctuation='none', delimiter='-'), Converter(system="Tailo", dialect="north", punctuation='none', delimiter='-'))
	checker(poj, Converter(system="POJ", punctuation='none', delimiter='-'), Converter(system="POJ", dialect="north", punctuation='none', delimiter='-'))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none', delimiter='-'), Converter(system="Zhuyin", dialect="north", punctuation='none', delimiter='-'))
	checker(tlpa, Converter(system="TLPA", punctuation='none', delimiter='-'), Converter(system="TLPA", dialect="north", punctuation='none', delimiter='-'))
	checker(pingyim, Converter(system="Pingyim", punctuation='none', delimiter='-'), Converter(system="Pingyim", dialect="north", punctuation='none', delimiter='-'))
	checker(tongiong, Converter(system="Tongiong", punctuation='none', delimiter='-'), Converter(system="Tongiong", dialect="north", punctuation='none', delimiter='-'))

def test_space():
	tailo = ["標價,phiau kè","按呢,án ne/án ni","介紹人,kài siāu jîn/kài siāu lîn","祝你今仔日真好的日子,tsiok lí kin á ji̍t tsin hó--ê ji̍t tsí/tsiok lí kin á li̍t tsin hó--ê li̍t tsí","咱的食飯,lán--ê tsia̍h pn̄g"]
	poj = ["標價,phiau kè","按呢,án ne/án ni","介紹人,kài siāu jîn/kài siāu lîn","祝你今仔日真好的日子,chiok lí kin á ji̍t chin hó--ê ji̍t chí/chiok lí kin á li̍t chin hó--ê li̍t chí","咱的食飯,lán--ê chia̍h pn̄g"]
	zhuyin = ["標價,ㄆㄧㄠ ㄍㆤ˪","按呢,ㄢˋ ㄋㆤ/ㄢˋ ㄋㄧ","介紹人,ㄍㄞ˪ ㄒㄧㄠ˫ ㆢㄧㄣˊ/ㄍㄞ˪ ㄒㄧㄠ˫ ㄌㄧㄣˊ","祝你今仔日真好的日子,ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㆢㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㆢㄧㆵ˙ ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㄌㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㄌㄧㆵ˙ ㄐㄧˋ","咱的食飯,ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙ ㄅㆭ˫"]
	tlpa = ["標價,phiau1 ke3","按呢,an2 ne1/an2 ni1","介紹人,kai3 siau7 jin5/kai3 siau7 lin5","祝你今仔日真好的日子,ciok4 li2 kin1 a2 jit8 cin1 ho2 e5 jit8 ci2/ciok4 li2 kin1 a2 lit8 cin1 ho2 e5 lit8 ci2","咱的食飯,lan2 e5 ciah8 png7"]
	pingyim = ["標價,piāo gè","按呢,ǎn lnē/ǎn lnī","介紹人,gài siâo zzín/gài siâo lín","祝你今仔日真好的日子,ziōk lǐ gīn ǎ zzít zīn hǒ é zzít zǐ/ziōk lǐ gīn ǎ lít zīn hǒ é lít zǐ","咱的食飯,lǎn é ziáh bn̂g"]
	tongiong = ["標價,piāu gê","按呢,an ne/an ni","介紹人,gài siâu rĭn/gài siâu lĭn","祝你今仔日真好的日子,ziok li gīn a rīt zīn hor--ē rīt zì/ziok li gīn a līt zīn hor--ê līt zì","咱的食飯,lan--ē ziâ bn̄g"]

	checker(tailo, Converter(system="Tailo", punctuation='none', delimiter=' '), Converter(system="Tailo", dialect="north", punctuation='none', delimiter=' '))
	checker(poj, Converter(system="POJ", punctuation='none', delimiter=' '), Converter(system="POJ", dialect="north", punctuation='none', delimiter=' '))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none', delimiter=' '), Converter(system="Zhuyin", dialect="north", punctuation='none', delimiter=' '))
	checker(tlpa, Converter(system="TLPA", punctuation='none', delimiter=' '), Converter(system="TLPA", dialect="north", punctuation='none', delimiter=' '))
	checker(pingyim, Converter(system="Pingyim", punctuation='none', delimiter=' '), Converter(system="Pingyim", dialect="north", punctuation='none', delimiter=' '))
	checker(tongiong, Converter(system="Tongiong", punctuation='none', delimiter=' '), Converter(system="Tongiong", dialect="north", punctuation='none', delimiter=' '))

def test_nospace():
	tailo = ["標價,phiaukè","按呢,ánne/ánni","介紹人,kàisiāujîn/kàisiāulîn","祝你今仔日真好的日子,tsiok lí kináji̍t tsinhó--ê ji̍ttsí/tsiok lí kináli̍t tsinhó--ê li̍ttsí","咱的食飯,lán--ê tsia̍hpn̄g"]
	poj = ["標價,phiaukè","按呢,ánne/ánni","介紹人,kàisiāujîn/kàisiāulîn","祝你今仔日真好的日子,chiok lí kináji̍t chinhó--ê ji̍tchí/chiok lí kináli̍t chinhó--ê li̍tchí","咱的食飯,lán--ê chia̍hpn̄g"]
	zhuyin = ["標價,ㄆㄧㄠㄍㆤ˪","按呢,ㄢˋㄋㆤ/ㄢˋㄋㄧ","介紹人,ㄍㄞ˪ㄒㄧㄠ˫ㆢㄧㄣˊ/ㄍㄞ˪ㄒㄧㄠ˫ㄌㄧㄣˊ","祝你今仔日真好的日子,ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣㄚˋㆢㄧㆵ˙ ㄐㄧㄣㄏㄜˋ ㆤˊ ㆢㄧㆵ˙ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣㄚˋㄌㄧㆵ˙ ㄐㄧㄣㄏㄜˋ ㆤˊ ㄌㄧㆵ˙ㄐㄧˋ","咱的食飯,ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙ㄅㆭ˫"]
	tlpa = ["標價,phiau1ke3","按呢,an2ne1/an2ni1","介紹人,kai3siau7jin5/kai3siau7lin5","祝你今仔日真好的日子,ciok4 li2 kin1a2jit8 cin1ho2 e5 jit8ci2/ciok4 li2 kin1a2lit8 cin1ho2 e5 lit8ci2","咱的食飯,lan2 e5 ciah8png7"]
	pingyim = ["標價,piāogè","按呢,ǎnlnē/ǎnlnī","介紹人,gàisiâozzín/gàisiâolín","祝你今仔日真好的日子,ziōk lǐ gīnǎzzít zīnhǒ é zzítzǐ/ziōk lǐ gīnǎlít zīnhǒ é lítzǐ","咱的食飯,lǎn é ziáhbn̂g"]
	tongiong = ["標價,piāugê","按呢,anne/anni","介紹人,gàisiâurĭn/gàisiâulĭn","祝你今仔日真好的日子,ziok li gīnarīt zīnhor--ē rītzì/ziok li gīnalīt zīnhor--ê lītzì","咱的食飯,lan--ē ziâbn̄g"]

	checker(tailo, Converter(system="Tailo", punctuation='none', delimiter=''), Converter(system="Tailo", dialect="north", punctuation='none', delimiter=''))
	checker(poj, Converter(system="POJ", punctuation='none', delimiter=''), Converter(system="POJ", dialect="north", punctuation='none', delimiter=''))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none', delimiter=''), Converter(system="Zhuyin", dialect="north", punctuation='none', delimiter=''))
	checker(tlpa, Converter(system="TLPA", punctuation='none', delimiter=''), Converter(system="TLPA", dialect="north", punctuation='none', delimiter=''))
	checker(pingyim, Converter(system="Pingyim", punctuation='none', delimiter=''), Converter(system="Pingyim", dialect="north", punctuation='none', delimiter=''))
	checker(tongiong, Converter(system="Tongiong", punctuation='none', delimiter=''), Converter(system="Tongiong", dialect="north", punctuation='none', delimiter=''))