from taibun.taibun import Converter
from utils import checker

hanji_data = ["標價","按呢","介紹人","祝你今仔日真好的日子","咱的食飯","公車遲到矣"]

def test_default():
	test_data = [
        (["phiau-kè","án-ne/án-ni","kài-siāu-jîn/kài-siāu-lîn","tsiok lí kin-á-ji̍t tsin-hó ê ji̍t-tsí/tsiok lí kin-á-li̍t tsin-hó ê li̍t-tsí","lán ê tsia̍h-pn̄g","kong-tshia tî-tò--ah"], "Tailo"),
		(["phiau-kè","án-ne/án-ni","kài-siāu-jîn/kài-siāu-lîn","chiok lí kin-á-ji̍t chin-hó ê ji̍t-chí/chiok lí kin-á-li̍t chin-hó ê li̍t-chí","lán ê chia̍h-pn̄g","kong-chhia tî-tò--ah"], "POJ"),
		(["ㄆㄧㄠ ㄍㆤ˪","ㄢˋ ㄋㆤ/ㄢˋ ㄋㄧ","ㄍㄞ˪ ㄒㄧㄠ˫ ㆢㄧㄣˊ/ㄍㄞ˪ ㄒㄧㄠ˫ ㄌㄧㄣˊ","ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㆢㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㆢㄧㆵ˙ ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㄌㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㄌㄧㆵ˙ ㄐㄧˋ","ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙ ㄅㆭ˫","ㄍㆲ ㄑㄧㄚ ㄉㄧˊ ㄉㄜ˪ ㄚ"], "Zhuyin"),
		(["phiau1 ke3","an2 ne1/an2 ni1","kai3 siau7 jin5/kai3 siau7 lin5","ciok4 li2 kin1 a2 jit8 cin1 ho2 e5 jit8 ci2/ciok4 li2 kin1 a2 lit8 cin1 ho2 e5 lit8 ci2","lan2 e5 ciah8 png7","kong1 chia1 ti5 to3 ah0"], "TLPA"),
		(["piāogè","ǎnlnē/ǎnlnī","gàisiâozzín/gàisiâolín","ziōk lǐ gīnǎzzít zīnhǒ é zzítzǐ/ziōk lǐ gīnǎlít zīnhǒ é lítzǐ","lǎn é ziáhbn̂g","gōngciā dídò ah"], "Pingyim"),
		(["piāu-gê","an-ne/an-ni","gài-siâu-rĭn/gài-siâu-lĭn","ziok li gīn-a-rīt zīn-hor ē rīt-zì/ziok li gīn-a-līt zīn-hor ê līt-zì","lan ē ziâ-bn̄g/lan ê ziâ-bn̄g","gōng-ciā dī-dôr--åh/gōng-ciā dî-dôr--åh"], "Tongiong"),
		(["pʰiau⁴⁴ ke¹¹/pʰiau⁵⁵ ke²¹","an⁵³ nẽ⁴⁴/an⁵¹ nĩ⁵⁵","kai¹¹ ɕiau²² dʑin²⁵/kai²¹ ɕiau³³ lin²⁴","tɕiɔk̚²¹ li⁵³ kin⁴⁴ a⁵³ dʑit̚⁵ tɕin⁴⁴ hə⁵³ e²⁵ dʑit̚⁵ tɕi⁵³/tɕiɔk̚³² li⁵¹ kin⁵⁵ a⁵¹ lit̚⁴ tɕin⁵⁵ ho⁵¹ e²⁴ lit̚⁴ tɕi⁵¹","lan⁵³ e²⁵ tɕiaʔ⁵ pŋ̍²²/lan⁵¹ e²⁴ tɕiaʔ⁴ pŋ̍³³","kɔŋ⁴⁴ tɕʰia⁴⁴ ti²⁵ tə¹¹ a/kɔŋ⁵⁵ tɕʰia⁵⁵ ti²⁴ to²¹ a"], "IPA")
    ]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none'), Converter(system=system, dialect="north", punctuation='none'))

def test_hyphen():
	test_data = [
		(["phiau-kè","án-ne/án-ni","kài-siāu-jîn/kài-siāu-lîn","tsiok lí kin-á-ji̍t tsin-hó ê ji̍t-tsí/tsiok lí kin-á-li̍t tsin-hó ê li̍t-tsí","lán ê tsia̍h-pn̄g","kong-tshia tî-tò--ah"], "Tailo"),
		(["phiau-kè","án-ne/án-ni","kài-siāu-jîn/kài-siāu-lîn","chiok lí kin-á-ji̍t chin-hó ê ji̍t-chí/chiok lí kin-á-li̍t chin-hó ê li̍t-chí","lán ê chia̍h-pn̄g","kong-chhia tî-tò--ah"], "POJ"),
		(["ㄆㄧㄠ-ㄍㆤ˪","ㄢˋ-ㄋㆤ/ㄢˋ-ㄋㄧ","ㄍㄞ˪-ㄒㄧㄠ˫-ㆢㄧㄣˊ/ㄍㄞ˪-ㄒㄧㄠ˫-ㄌㄧㄣˊ","ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ-ㄚˋ-ㆢㄧㆵ˙ ㄐㄧㄣ-ㄏㄜˋ ㆤˊ ㆢㄧㆵ˙-ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ-ㄚˋ-ㄌㄧㆵ˙ ㄐㄧㄣ-ㄏㄜˋ ㆤˊ ㄌㄧㆵ˙-ㄐㄧˋ","ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙-ㄅㆭ˫","ㄍㆲ-ㄑㄧㄚ ㄉㄧˊ-ㄉㄜ˪ ㄚ"], "Zhuyin"),
		(["phiau1-ke3","an2-ne1/an2-ni1","kai3-siau7-jin5/kai3-siau7-lin5","ciok4 li2 kin1-a2-jit8 cin1-ho2 e5 jit8-ci2/ciok4 li2 kin1-a2-lit8 cin1-ho2 e5 lit8-ci2","lan2 e5 ciah8-png7","kong1-chia1 ti5-to3 ah0"], "TLPA"),
		(["piāo-gè","ǎn-lnē/ǎn-lnī","gài-siâo-zzín/gài-siâo-lín","ziōk lǐ gīn-ǎ-zzít zīn-hǒ é zzít-zǐ/ziōk lǐ gīn-ǎ-lít zīn-hǒ é lít-zǐ","lǎn é ziáh-bn̂g","gōng-ciā dí-dò ah"], "Pingyim"),
		(["piāu-gê","an-ne/an-ni","gài-siâu-rĭn/gài-siâu-lĭn","ziok li gīn-a-rīt zīn-hor ē rīt-zì/ziok li gīn-a-līt zīn-hor ê līt-zì","lan ē ziâ-bn̄g/lan ê ziâ-bn̄g","gōng-ciā dī-dôr--åh/gōng-ciā dî-dôr--åh"], "Tongiong"),
		(["pʰiau⁴⁴-ke¹¹/pʰiau⁵⁵-ke²¹","an⁵³-nẽ⁴⁴/an⁵¹-nĩ⁵⁵","kai¹¹-ɕiau²²-dʑin²⁵/kai²¹-ɕiau³³-lin²⁴","tɕiɔk̚²¹ li⁵³ kin⁴⁴-a⁵³-dʑit̚⁵ tɕin⁴⁴-hə⁵³ e²⁵ dʑit̚⁵-tɕi⁵³/tɕiɔk̚³² li⁵¹ kin⁵⁵-a⁵¹-lit̚⁴ tɕin⁵⁵-ho⁵¹ e²⁴ lit̚⁴-tɕi⁵¹","lan⁵³ e²⁵ tɕiaʔ⁵-pŋ̍²²/lan⁵¹ e²⁴ tɕiaʔ⁴-pŋ̍³³","kɔŋ⁴⁴-tɕʰia⁴⁴ ti²⁵-tə¹¹ a/kɔŋ⁵⁵-tɕʰia⁵⁵ ti²⁴-to²¹ a"], "IPA")
	]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none', delimiter='-'), Converter(system=system, dialect="north", punctuation='none', delimiter='-'))

def test_space():
	test_data = [
		(["phiau kè","án ne/án ni","kài siāu jîn/kài siāu lîn","tsiok lí kin á ji̍t tsin hó ê ji̍t tsí/tsiok lí kin á li̍t tsin hó ê li̍t tsí","lán ê tsia̍h pn̄g","kong tshia tî tò--ah"], "Tailo"),
		(["phiau kè","án ne/án ni","kài siāu jîn/kài siāu lîn","chiok lí kin á ji̍t chin hó ê ji̍t chí/chiok lí kin á li̍t chin hó ê li̍t chí","lán ê chia̍h pn̄g","kong chhia tî tò--ah"], "POJ"),
		(["ㄆㄧㄠ ㄍㆤ˪","ㄢˋ ㄋㆤ/ㄢˋ ㄋㄧ","ㄍㄞ˪ ㄒㄧㄠ˫ ㆢㄧㄣˊ/ㄍㄞ˪ ㄒㄧㄠ˫ ㄌㄧㄣˊ","ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㆢㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㆢㄧㆵ˙ ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣ ㄚˋ ㄌㄧㆵ˙ ㄐㄧㄣ ㄏㄜˋ ㆤˊ ㄌㄧㆵ˙ ㄐㄧˋ","ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙ ㄅㆭ˫","ㄍㆲ ㄑㄧㄚ ㄉㄧˊ ㄉㄜ˪ ㄚ"], "Zhuyin"),
		(["phiau1 ke3","an2 ne1/an2 ni1","kai3 siau7 jin5/kai3 siau7 lin5","ciok4 li2 kin1 a2 jit8 cin1 ho2 e5 jit8 ci2/ciok4 li2 kin1 a2 lit8 cin1 ho2 e5 lit8 ci2","lan2 e5 ciah8 png7","kong1 chia1 ti5 to3 ah0"], "TLPA"),
		(["piāo gè","ǎn lnē/ǎn lnī","gài siâo zzín/gài siâo lín","ziōk lǐ gīn ǎ zzít zīn hǒ é zzít zǐ/ziōk lǐ gīn ǎ lít zīn hǒ é lít zǐ","lǎn é ziáh bn̂g","gōng ciā dí dò ah"], "Pingyim"),
		(["piāu gê","an ne/an ni","gài siâu rĭn/gài siâu lĭn","ziok li gīn a rīt zīn hor ē rīt zì/ziok li gīn a līt zīn hor ê līt zì","lan ē ziâ bn̄g/lan ê ziâ bn̄g","gōng ciā dī dôr--åh/gōng ciā dî dôr--åh"], "Tongiong"),
		(["pʰiau⁴⁴ ke¹¹/pʰiau⁵⁵ ke²¹","an⁵³ nẽ⁴⁴/an⁵¹ nĩ⁵⁵","kai¹¹ ɕiau²² dʑin²⁵/kai²¹ ɕiau³³ lin²⁴","tɕiɔk̚²¹ li⁵³ kin⁴⁴ a⁵³ dʑit̚⁵ tɕin⁴⁴ hə⁵³ e²⁵ dʑit̚⁵ tɕi⁵³/tɕiɔk̚³² li⁵¹ kin⁵⁵ a⁵¹ lit̚⁴ tɕin⁵⁵ ho⁵¹ e²⁴ lit̚⁴ tɕi⁵¹","lan⁵³ e²⁵ tɕiaʔ⁵ pŋ̍²²/lan⁵¹ e²⁴ tɕiaʔ⁴ pŋ̍³³","kɔŋ⁴⁴ tɕʰia⁴⁴ ti²⁵ tə¹¹ a/kɔŋ⁵⁵ tɕʰia⁵⁵ ti²⁴ to²¹ a"], "IPA")
	]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none', delimiter=' '), Converter(system=system, dialect="north", punctuation='none', delimiter=' '))

def test_nospace():
	test_data = [
		(["phiaukè","ánne/ánni","kàisiāujîn/kàisiāulîn","tsiok lí kináji̍t tsinhó ê ji̍ttsí/tsiok lí kináli̍t tsinhó ê li̍ttsí","lán ê tsia̍hpn̄g","kongtshia tîtò--ah"], "Tailo"),
		(["phiaukè","ánne/ánni","kàisiāujîn/kàisiāulîn","chiok lí kináji̍t chinhó ê ji̍tchí/chiok lí kináli̍t chinhó ê li̍tchí","lán ê chia̍hpn̄g","kongchhia tîtò--ah"], "POJ"),
		(["ㄆㄧㄠㄍㆤ˪","ㄢˋㄋㆤ/ㄢˋㄋㄧ","ㄍㄞ˪ㄒㄧㄠ˫ㆢㄧㄣˊ/ㄍㄞ˪ㄒㄧㄠ˫ㄌㄧㄣˊ","ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣㄚˋㆢㄧㆵ˙ ㄐㄧㄣㄏㄜˋ ㆤˊ ㆢㄧㆵ˙ㄐㄧˋ/ㄐㄧㆦㆶ ㄌㄧˋ ㄍㄧㄣㄚˋㄌㄧㆵ˙ ㄐㄧㄣㄏㄜˋ ㆤˊ ㄌㄧㆵ˙ㄐㄧˋ","ㄌㄢˋ ㆤˊ ㄐㄧㄚㆷ˙ㄅㆭ˫","ㄍㆲㄑㄧㄚ ㄉㄧˊㄉㄜ˪ ㄚ"], "Zhuyin"),
		(["phiau1ke3","an2ne1/an2ni1","kai3siau7jin5/kai3siau7lin5","ciok4 li2 kin1a2jit8 cin1ho2 e5 jit8ci2/ciok4 li2 kin1a2lit8 cin1ho2 e5 lit8ci2","lan2 e5 ciah8png7","kong1chia1 ti5to3 ah0"], "TLPA"),
		(["piāogè","ǎnlnē/ǎnlnī","gàisiâozzín/gàisiâolín","ziōk lǐ gīnǎzzít zīnhǒ é zzítzǐ/ziōk lǐ gīnǎlít zīnhǒ é lítzǐ","lǎn é ziáhbn̂g","gōngciā dídò ah"], "Pingyim"),
		(["piāugê","anne/anni","gàisiâurĭn/gàisiâulĭn","ziok li gīnarīt zīnhor ē rītzì/ziok li gīnalīt zīnhor ê lītzì","lan ē ziâbn̄g/lan ê ziâbn̄g","gōngciā dīdôr--åh/gōngciā dîdôr--åh"], "Tongiong"),
		(["pʰiau⁴⁴ke¹¹/pʰiau⁵⁵ke²¹","an⁵³nẽ⁴⁴/an⁵¹nĩ⁵⁵","kai¹¹ɕiau²²dʑin²⁵/kai²¹ɕiau³³lin²⁴","tɕiɔk̚²¹ li⁵³ kin⁴⁴a⁵³dʑit̚⁵ tɕin⁴⁴hə⁵³ e²⁵ dʑit̚⁵tɕi⁵³/tɕiɔk̚³² li⁵¹ kin⁵⁵a⁵¹lit̚⁴ tɕin⁵⁵ho⁵¹ e²⁴ lit̚⁴tɕi⁵¹","lan⁵³ e²⁵ tɕiaʔ⁵pŋ̍²²/lan⁵¹ e²⁴ tɕiaʔ⁴pŋ̍³³","kɔŋ⁴⁴tɕʰia⁴⁴ ti²⁵tə¹¹ a/kɔŋ⁵⁵tɕʰia⁵⁵ ti²⁴to²¹ a"], "IPA")
	]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none', delimiter=''), Converter(system=system, dialect="north", punctuation='none', delimiter=''))