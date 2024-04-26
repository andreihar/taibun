from taibun.taibun import Converter
from utils import checker

hanji_data = ["開始","巧氣","寄回","肉包","翕甌","彼號","確信","南面","未來","篾蓆","業務","罰金","學生"]
hanji_sentence = ["太空朋友，恁好！恁食飽未"]
hanji_a = ["廟尪仔","翁某仔","肉幼仔","花搭仔","微微仔","慢慢仔","尾蝶仔"]

def test_default():
	test_data = [
        (["khai-sí","khá-khì","kià-huê/kià-hê","bah-pau","hip-au","hit-hō","khak-sìn","lâm-bīn","bī-lâi","bi̍h-tshio̍h","gia̍p-bū","hua̍t-kim","ha̍k-sing"], "Tailo"),
        (["khai-sí","khá-khì","kià-hôe/kià-hê","bah-pau","hip-au","hit-hō","khak-sìn","lâm-bīn","bī-lâi","bi̍h-chhio̍h","gia̍p-bū","hoa̍t-kim","ha̍k-seng"], "POJ"),
        (["ㄎㄞ ㄒㄧˋ","ㄎㄚˋ ㄎㄧ˪","ㄍㄧㄚ˪ ㄏㄨㆤˊ/ㄍㄧㄚ˪ ㄏㆤˊ","ㆠㄚㆷ ㄅㄠ","ㄏㄧㆴ ㄠ","ㄏㄧㆵ ㄏㄜ˫","ㄎㄚㆶ ㄒㄧㄣ˪","ㄌㆰˊ ㆠㄧㄣ˫","ㆠㄧ˫ ㄌㄞˊ","ㆠㄧㆷ˙ ㄑㄧㄜㆷ˙","ㆣㄧㄚㆴ˙ ㆠㄨ˫","ㄏㄨㄚㆵ˙ ㄍㄧㆬ","ㄏㄚㆶ˙ ㄒㄧㄥ"], "Zhuyin"),
        (["khai1 si2","kha2 khi3","kia3 hue5/kia3 he5","bah4 pau1","hip4 au1","hit4 ho7","khak4 sin3","lam5 bin7","bi7 lai5","bih8 chioh8","giap8 bu7","huat8 kim1","hak8 sing1"], "TLPA"),
        (["kāisǐ","kǎkì","giàhué/giàhé","bbāhbāo","hīpāo","hīthô","kāksìn","lámbbîn","bbîlái","bbíhcióh","ggiápbbû","huátgīm","háksīng"], "Pingyim"),
        (["kāi-sì","ka-kî","già-huĕ/già-hĕ","bhà-bau","hip-au","hit-hōr","kak-sîn","lām-bhīn/lâm-bhīn","bhî-lăi","bhî-cioh","ghiāp-bhū","huāt-gim","hāk-sing"], "Tongiong"),
        (["kʰai⁴⁴ ɕi⁵³/kʰai⁵⁵ ɕi⁵¹","kʰa⁵³ kʰi¹¹/kʰa⁵¹ kʰi²¹","kia¹¹ hue²⁵/kia²¹ he²⁴","baʔ²¹ pau⁴⁴/baʔ³² pau⁵⁵","hip̚²¹ au⁴⁴/hip̚³² au⁵⁵","hit̚²¹ hə²²/hit̚³² ho³³","kʰak̚²¹ ɕin¹¹/kʰak̚³² ɕin²¹","lam²⁵ bin²²/lam²⁴ bin³³","bi²² lai²⁵/bi³³ lai²⁴","biʔ⁵ tɕʰiəʔ⁵/biʔ⁴ tɕʰioʔ⁴","giap̚⁵ bu²²/giap̚⁴ bu³³","huat̚⁵ kim⁴⁴/huat̚⁴ kim⁵⁵","hak̚⁵ ɕiɪŋ⁴⁴/hak̚⁴ ɕiɪŋ⁵⁵"], "IPA")
    ]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none'), Converter(system=system, dialect="north", punctuation='none'))

def test_auto():
    test_data = [
        (["khāi-sí","kha-khì","kiá-huê/kiá-hê","bá-pau","hi̍p-au","hi̍t-hō","kha̍k-sìn","lām-bīn/làm-bīn","bì-lâi","bì-tshio̍h","giap-bū","huat-kim","hak-sing"], "Tailo"),
        (["khāi-sí","kha-khì","kiá-hôe/kiá-hê","bá-pau","hi̍p-au","hi̍t-hō","kha̍k-sìn","lām-bīn/làm-bīn","bì-lâi","bì-chhio̍h","giap-bū","hoat-kim","hak-seng"], "POJ"),
        (["ㄎㄞ˫ ㄒㄧˋ","ㄎㄚ ㄎㄧ˪","ㄍㄧㄚˋ ㄏㄨㆤˊ/ㄍㄧㄚˋ ㄏㆤˊ","ㆠㄚˋ ㄅㄠ","ㄏㄧㆴ˙ ㄠ","ㄏㄧㆵ˙ ㄏㄜ˫","ㄎㄚㆶ˙ ㄒㄧㄣ˪","ㄌㆰ˫ ㆠㄧㄣ˫/ㄌㆰ˪ ㆠㄧㄣ˫","ㆠㄧ˪ ㄌㄞˊ","ㆠㄧ˪ ㄑㄧㄜㆷ˙","ㆣㄧㄚㆴ ㆠㄨ˫","ㄏㄨㄚㆵ ㄍㄧㆬ","ㄏㄚㆶ ㄒㄧㄥ"], "Zhuyin"),
        (["khai7 si2","kha1 khi3","kia2 hue5/kia2 he5","ba2 pau1","hip8 au1","hit8 ho7","khak8 sin3","lam7 bin7/lam3 bin7","bi3 lai5","bi3 chioh8","giap4 bu7","huat4 kim1","hak4 sing1"], "TLPA"),
        (["kâisǐ","kākì","giǎhué/giǎhé","bbǎbāo","hípāo","híthô","káksìn","lâmbbîn/làmbbîn","bbìlái","bbìcióh","ggiāpbbû","huātgīm","hāksīng"], "Pingyim"),
        (["kāi-sì","ka-kî","già-huĕ/già-hĕ","bhà-bau","hip-au","hit-hōr","kak-sîn","lām-bhīn/lâm-bhīn","bhî-lăi","bhî-cioh","ghiāp-bhū","huāt-gim","hāk-sing"], "Tongiong"),
        (["kʰai²² ɕi⁵³/kʰai³³ ɕi⁵¹","kʰa⁴⁴ kʰi¹¹/kʰa⁵⁵ kʰi²¹","kia⁵³ hue²⁵/kia⁵¹ he²⁴","ba⁵³ pau⁴⁴/ba⁵¹ pau⁵⁵","hip̚⁵ au⁴⁴/hip̚⁴ au⁵⁵","hit̚⁵ hə²²/hit̚⁴ ho³³","kʰak̚⁵ ɕin¹¹/kʰak̚⁴ ɕin²¹","lam²² bin²²/lam²¹ bin³³","bi¹¹ lai²⁵/bi²¹ lai²⁴","bi¹¹ tɕʰiəʔ⁵/bi²¹ tɕʰioʔ⁴","giap̚²¹ bu²²/giap̚³² bu³³","huat̚²¹ kim⁴⁴/huat̚³² kim⁵⁵","hak̚²¹ ɕiɪŋ⁴⁴/hak̚³² ɕiɪŋ⁵⁵"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='auto'), Converter(system=system, dialect="north", punctuation='none', sandhi='auto'))

def test_none():
    test_data = [
        (["khai-sí","khá-khì","kià-huê/kià-hê","bah-pau","hip-au","hit-hō","khak-sìn","lâm-bīn","bī-lâi","bi̍h-tshio̍h","gia̍p-bū","hua̍t-kim","ha̍k-sing"], "Tailo"),
        (["khai-sí","khá-khì","kià-hôe/kià-hê","bah-pau","hip-au","hit-hō","khak-sìn","lâm-bīn","bī-lâi","bi̍h-chhio̍h","gia̍p-bū","hoa̍t-kim","ha̍k-seng"], "POJ"),
        (["ㄎㄞ ㄒㄧˋ","ㄎㄚˋ ㄎㄧ˪","ㄍㄧㄚ˪ ㄏㄨㆤˊ/ㄍㄧㄚ˪ ㄏㆤˊ","ㆠㄚㆷ ㄅㄠ","ㄏㄧㆴ ㄠ","ㄏㄧㆵ ㄏㄜ˫","ㄎㄚㆶ ㄒㄧㄣ˪","ㄌㆰˊ ㆠㄧㄣ˫","ㆠㄧ˫ ㄌㄞˊ","ㆠㄧㆷ˙ ㄑㄧㄜㆷ˙","ㆣㄧㄚㆴ˙ ㆠㄨ˫","ㄏㄨㄚㆵ˙ ㄍㄧㆬ","ㄏㄚㆶ˙ ㄒㄧㄥ"], "Zhuyin"),
        (["khai1 si2","kha2 khi3","kia3 hue5/kia3 he5","bah4 pau1","hip4 au1","hit4 ho7","khak4 sin3","lam5 bin7","bi7 lai5","bih8 chioh8","giap8 bu7","huat8 kim1","hak8 sing1"], "TLPA"),
        (["kāisǐ","kǎkì","giàhué/giàhé","bbāhbāo","hīpāo","hīthô","kāksìn","lámbbîn","bbîlái","bbíhcióh","ggiápbbû","huátgīm","háksīng"], "Pingyim"),
        (["kai-sì","kà-kî","giâ-huĕ/giâ-hĕ","bhāh-bau","hīp-au","hīt-hōr","kāk-sîn","lăm-bhīn","bhī-lăi","bhih-cioh","ghiap-bhū","huat-gim","hak-sing"], "Tongiong"),
        (["kʰai⁴⁴ ɕi⁵³/kʰai⁵⁵ ɕi⁵¹","kʰa⁵³ kʰi¹¹/kʰa⁵¹ kʰi²¹","kia¹¹ hue²⁵/kia²¹ he²⁴","baʔ²¹ pau⁴⁴/baʔ³² pau⁵⁵","hip̚²¹ au⁴⁴/hip̚³² au⁵⁵","hit̚²¹ hə²²/hit̚³² ho³³","kʰak̚²¹ ɕin¹¹/kʰak̚³² ɕin²¹","lam²⁵ bin²²/lam²⁴ bin³³","bi²² lai²⁵/bi³³ lai²⁴","biʔ⁵ tɕʰiəʔ⁵/biʔ⁴ tɕʰioʔ⁴","giap̚⁵ bu²²/giap̚⁴ bu³³","huat̚⁵ kim⁴⁴/huat̚⁴ kim⁵⁵","hak̚⁵ ɕiɪŋ⁴⁴/hak̚⁴ ɕiɪŋ⁵⁵"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='none'), Converter(system=system, dialect="north", punctuation='none', sandhi='none'))

def test_exc_last():
    test_data = [
        (["khāi-sí","kha-khì","kiá-huê/kiá-hê","bá-pau","hi̍p-au","hi̍t-hō","kha̍k-sìn","lām-bīn/làm-bīn","bì-lâi","bì-tshio̍h","giap-bū","huat-kim","hak-sing"], "Tailo"),
        (["khāi-sí","kha-khì","kiá-hôe/kiá-hê","bá-pau","hi̍p-au","hi̍t-hō","kha̍k-sìn","lām-bīn/làm-bīn","bì-lâi","bì-chhio̍h","giap-bū","hoat-kim","hak-seng"], "POJ"),
        (["ㄎㄞ˫ ㄒㄧˋ","ㄎㄚ ㄎㄧ˪","ㄍㄧㄚˋ ㄏㄨㆤˊ/ㄍㄧㄚˋ ㄏㆤˊ","ㆠㄚˋ ㄅㄠ","ㄏㄧㆴ˙ ㄠ","ㄏㄧㆵ˙ ㄏㄜ˫","ㄎㄚㆶ˙ ㄒㄧㄣ˪","ㄌㆰ˫ ㆠㄧㄣ˫/ㄌㆰ˪ ㆠㄧㄣ˫","ㆠㄧ˪ ㄌㄞˊ","ㆠㄧ˪ ㄑㄧㄜㆷ˙","ㆣㄧㄚㆴ ㆠㄨ˫","ㄏㄨㄚㆵ ㄍㄧㆬ","ㄏㄚㆶ ㄒㄧㄥ"], "Zhuyin"),
        (["khai7 si2","kha1 khi3","kia2 hue5/kia2 he5","ba2 pau1","hip8 au1","hit8 ho7","khak8 sin3","lam7 bin7/lam3 bin7","bi3 lai5","bi3 chioh8","giap4 bu7","huat4 kim1","hak4 sing1"], "TLPA"),
        (["kâisǐ","kākì","giǎhué/giǎhé","bbǎbāo","hípāo","híthô","káksìn","lâmbbîn/làmbbîn","bbìlái","bbìcióh","ggiāpbbû","huātgīm","hāksīng"], "Pingyim"),
        (["kāi-sì","ka-kî","già-huĕ/già-hĕ","bhà-bau","hip-au","hit-hōr","kak-sîn","lām-bhīn/lâm-bhīn","bhî-lăi","bhî-cioh","ghiāp-bhū","huāt-gim","hāk-sing"], "Tongiong"),
        (["kʰai²² ɕi⁵³/kʰai³³ ɕi⁵¹","kʰa⁴⁴ kʰi¹¹/kʰa⁵⁵ kʰi²¹","kia⁵³ hue²⁵/kia⁵¹ he²⁴","ba⁵³ pau⁴⁴/ba⁵¹ pau⁵⁵","hip̚⁵ au⁴⁴/hip̚⁴ au⁵⁵","hit̚⁵ hə²²/hit̚⁴ ho³³","kʰak̚⁵ ɕin¹¹/kʰak̚⁴ ɕin²¹","lam²² bin²²/lam²¹ bin³³","bi¹¹ lai²⁵/bi²¹ lai²⁴","bi¹¹ tɕʰiəʔ⁵/bi²¹ tɕʰioʔ⁴","giap̚²¹ bu²²/giap̚³² bu³³","huat̚²¹ kim⁴⁴/huat̚³² kim⁵⁵","hak̚²¹ ɕiɪŋ⁴⁴/hak̚³² ɕiɪŋ⁵⁵"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='exc_last'), Converter(system=system, dialect="north", punctuation='none', sandhi='exc_last'))

def test_incl_last():
    test_data = [
        (["khāi-si","kha-khí","kiá-huē/kiá-hè","bá-pāu","hi̍p-āu","hi̍t-hò","kha̍k-sín","lām-bìn/làm-bìn","bì-lāi/bì-lài","bì-tshiò","giap-bù","huat-kīm","hak-sīng"], "Tailo"),
        (["khāi-si","kha-khí","kiá-hōe/kiá-hè","bá-pāu","hi̍p-āu","hi̍t-hò","kha̍k-sín","lām-bìn/làm-bìn","bì-lāi/bì-lài","bì-chhiò","giap-bù","hoat-kīm","hak-sēng"], "POJ"),
        (["ㄎㄞ˫ ㄒㄧ","ㄎㄚ ㄎㄧˋ","ㄍㄧㄚˋ ㄏㄨㆤ˫/ㄍㄧㄚˋ ㄏㆤ˪","ㆠㄚˋ ㄅㄠ˫","ㄏㄧㆴ˙ ㄠ˫","ㄏㄧㆵ˙ ㄏㄜ˪","ㄎㄚㆶ˙ ㄒㄧㄣˋ","ㄌㆰ˫ ㆠㄧㄣ˪/ㄌㆰ˪ ㆠㄧㄣ˪","ㆠㄧ˪ ㄌㄞ˫/ㆠㄧ˪ ㄌㄞ˪","ㆠㄧ˪ ㄑㄧㄜ˪","ㆣㄧㄚㆴ ㆠㄨ˪","ㄏㄨㄚㆵ ㄍㄧㆬ˫","ㄏㄚㆶ ㄒㄧㄥ˫"], "Zhuyin"),
        (["khai7 si1","kha1 khi2","kia2 hue7/kia2 he3","ba2 pau7","hip8 au7","hit8 ho3","khak8 sin2","lam7 bin3/lam3 bin3","bi3 lai7/bi3 lai3","bi3 chio3","giap4 bu3","huat4 kim7","hak4 sing7"], "TLPA"),
        (["kâisī","kākǐ","giǎhuê/giǎhè","bbǎbâo","hípâo","híthò","káksǐn","lâmbbìn/làmbbìn","bbìlâi/bbìlài","bbìciò","ggiāpbbù","huātgîm","hāksîng"], "Pingyim"),
        (["kāi-si","ka-kì","già-huē/già-hê","bhà-bāu","hip-āu","hit-hôr","kak-sìn","lām-bhîn/lâm-bhîn","bhî-lāi/bhî-lâi","bhî-ciôr","ghiāp-bhû","huāt-gīm","hāk-sīng"], "Tongiong"),
        (["kʰai²² ɕi⁴⁴/kʰai³³ ɕi⁵⁵","kʰa⁴⁴ kʰi⁵³/kʰa⁵⁵ kʰi⁵¹","kia⁵³ hue²²/kia⁵¹ he²¹","ba⁵³ pau²²/ba⁵¹ pau³³","hip̚⁵ au²²/hip̚⁴ au³³","hit̚⁵ hə¹¹/hit̚⁴ ho²¹","kʰak̚⁵ ɕin⁵³/kʰak̚⁴ ɕin⁵¹","lam²² bin¹¹/lam²¹ bin²¹","bi¹¹ lai²²/bi²¹ lai²¹","bi¹¹ tɕʰiə¹¹/bi²¹ tɕʰio²¹","giap̚²¹ bu¹¹/giap̚³² bu²¹","huat̚²¹ kim²²/huat̚³² kim³³","hak̚²¹ ɕiɪŋ²²/hak̚³² ɕiɪŋ³³"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='incl_last'), Converter(system=system, dialect="north", punctuation='none', sandhi='incl_last'))

def test_a_auto():
    test_data = [
        (["biò-āng-á","āng-boo-á","bá-iu-á","huē-ta-á","bī-bī-á/bì-bī-á","bàn-bān-á","bue-iā-á/be-iā-á"], "Tailo"),
        (["biò-āng-á","āng-bo͘-á","bá-iu-á","hōe-ta-á","bī-bī-á/bì-bī-á","bàn-bān-á","boe-iā-á/be-iā-á"], "POJ"),
        (["ㆠㄧㄜ˪ ㄤ˫ ㄚˋ","ㄤ˫ ㆠㆦ ㄚˋ","ㆠㄚˋ ㄧㄨ ㄚˋ","ㄏㄨㆤ˫ ㄉㄚ ㄚˋ","ㆠㄧ˫ ㆠㄧ˫ ㄚˋ/ㆠㄧ˪ ㆠㄧ˫ ㄚˋ","ㆠㄢ˪ ㆠㄢ˫ ㄚˋ","ㆠㄨㆤ ㄧㄚ˫ ㄚˋ/ㆠㆤ ㄧㄚ˫ ㄚˋ"], "Zhuyin"),
        (["bio3 ang7 a2","ang7 boo1 a2","ba2 iu1 a2","hue7 ta1 a2","bi7 bi7 a2/bi3 bi7 a2","ban3 ban7 a2","bue1 ia7 a2/be1 ia7 a2"], "TLPA"),
        (["bbiòângǎ","ângbboōǎ","bbǎyūǎ","huêdāǎ","bbîbbîǎ/bbìbbîǎ","bbànbbânǎ","bbuēyâǎ/bbēyâǎ"], "Pingyim"),
        (["bhiôr-āng-à","āng-bhor-à","bhà-iu-à","huē-da-à","bhī-bhī-à/bhî-bhī-à","bhân-bhān-à","bhue-iā-à/bhe-iā-à"], "Tongiong"),
        (["biə¹¹ aŋ²² a⁵³/bio²¹ aŋ³³ a⁵¹","aŋ²² bɔ⁴⁴ a⁵³/aŋ³³ bɔ⁵⁵ a⁵¹","ba⁵³ iu⁴⁴ a⁵³/ba⁵¹ iu⁵⁵ a⁵¹","hue²² ta⁴⁴ a⁵³/hue³³ ta⁵⁵ a⁵¹","bi²² bi²² a⁵³/bi²¹ bi³³ a⁵¹","ban¹¹ ban²² a⁵³/ban²¹ ban³³ a⁵¹","bue⁴⁴ ia²² a⁵³/be⁵⁵ ia³³ a⁵¹"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='auto'), Converter(system=system, dialect="north", punctuation='none', sandhi='auto'))

def test_a_none():
    test_data = [
        (["biō-ang-á","ang-bóo-á","bah-iù-á","hue-tah-á","bî-bî-á","bān-bān-á","bué-ia̍h-á/bé-ia̍h-á"], "Tailo"),
        (["biō-ang-á","ang-bó͘-á","bah-iù-á","hoe-tah-á","bî-bî-á","bān-bān-á","bóe-ia̍h-á/bé-ia̍h-á"], "POJ"),
        (["ㆠㄧㄜ˫ ㄤ ㄚˋ","ㄤ ㆠㆦˋ ㄚˋ","ㆠㄚㆷ ㄧㄨ˪ ㄚˋ","ㄏㄨㆤ ㄉㄚㆷ ㄚˋ","ㆠㄧˊ ㆠㄧˊ ㄚˋ","ㆠㄢ˫ ㆠㄢ˫ ㄚˋ","ㆠㄨㆤˋ ㄧㄚㆷ˙ ㄚˋ/ㆠㆤˋ ㄧㄚㆷ˙ ㄚˋ"], "Zhuyin"),
        (["bio7 ang1 a2","ang1 boo2 a2","bah4 iu3 a2","hue1 tah4 a2","bi5 bi5 a2","ban7 ban7 a2","bue2 iah8 a2/be2 iah8 a2"], "TLPA"),
        (["bbiôāngǎ","āngbboǒǎ","bbāhyùǎ","huēdāhǎ","bbíbbíǎ","bbânbbânǎ","bbuěyáhǎ/bběyáhǎ"], "Pingyim"),
        (["bhiōr-ang-à","ang-bhòr-à","bhāh-iû-à","hue-dāh-à","bhĭ-bhĭ-à","bhān-bhān-à","bhuè-iah-à/bhè-iah-à"], "Tongiong"),
        (["biə²² aŋ⁴⁴ a⁵³/bio³³ aŋ⁵⁵ a⁵¹","aŋ⁴⁴ bɔ⁵³ a⁵³/aŋ⁵⁵ bɔ⁵¹ a⁵¹","baʔ²¹ iu¹¹ a⁵³/baʔ³² iu²¹ a⁵¹","hue⁴⁴ taʔ²¹ a⁵³/hue⁵⁵ taʔ³² a⁵¹","bi²⁵ bi²⁵ a⁵³/bi²⁴ bi²⁴ a⁵¹","ban²² ban²² a⁵³/ban³³ ban³³ a⁵¹","bue⁵³ iaʔ⁵ a⁵³/be⁵¹ iaʔ⁴ a⁵¹"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='none'), Converter(system=system, dialect="north", punctuation='none', sandhi='none'))

def test_a_exc_last():
    test_data = [
        (["biò-āng-á","āng-boo-á","bá-iú-á","huē-tá-á","bī-bī-á/bì-bì-á","bàn-bàn-á","bue-ià-á/be-ià-á"], "Tailo"),
        (["biò-āng-á","āng-bo͘-á","bá-iú-á","hōe-tá-á","bī-bī-á/bì-bì-á","bàn-bàn-á","boe-ià-á/be-ià-á"], "POJ"),
        (["ㆠㄧㄜ˪ ㄤ˫ ㄚˋ","ㄤ˫ ㆠㆦ ㄚˋ","ㆠㄚˋ ㄧㄨˋ ㄚˋ","ㄏㄨㆤ˫ ㄉㄚˋ ㄚˋ","ㆠㄧ˫ ㆠㄧ˫ ㄚˋ/ㆠㄧ˪ ㆠㄧ˪ ㄚˋ","ㆠㄢ˪ ㆠㄢ˪ ㄚˋ","ㆠㄨㆤ ㄧㄚ˪ ㄚˋ/ㆠㆤ ㄧㄚ˪ ㄚˋ"], "Zhuyin"),
        (["bio3 ang7 a2","ang7 boo1 a2","ba2 iu2 a2","hue7 ta2 a2","bi7 bi7 a2/bi3 bi3 a2","ban3 ban3 a2","bue1 ia3 a2/be1 ia3 a2"], "TLPA"),
        (["bbiòângǎ","ângbboōǎ","bbǎyǔǎ","huêdǎǎ","bbîbbîǎ/bbìbbìǎ","bbànbbànǎ","bbuēyàǎ/bbēyàǎ"], "Pingyim"),
        (["bhiôr-āng-à","āng-bhor-à","bhà-iù-à","huē-dà-à","bhī-bhī-à/bhî-bhî-à","bhân-bhân-à","bhue-iâ-à/bhe-iâ-à"], "Tongiong"),
        (["biə¹¹ aŋ²² a⁵³/bio²¹ aŋ³³ a⁵¹","aŋ²² bɔ⁴⁴ a⁵³/aŋ³³ bɔ⁵⁵ a⁵¹","ba⁵³ iu⁵³ a⁵³/ba⁵¹ iu⁵¹ a⁵¹","hue²² ta⁵³ a⁵³/hue³³ ta⁵¹ a⁵¹","bi²² bi²² a⁵³/bi²¹ bi²¹ a⁵¹","ban¹¹ ban¹¹ a⁵³/ban²¹ ban²¹ a⁵¹","bue⁴⁴ ia¹¹ a⁵³/be⁵⁵ ia²¹ a⁵¹"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='exc_last'), Converter(system=system, dialect="north", punctuation='none', sandhi='exc_last'))

def test_a_incl_last():
    test_data = [
        (["biò-āng-a","āng-boo-a","bá-iú-a","huē-tá-a","bī-bī-a/bì-bì-a","bàn-bàn-a","bue-ià-a/be-ià-a"], "Tailo"),
        (["biò-āng-a","āng-bo͘-a","bá-iú-a","hōe-tá-a","bī-bī-a/bì-bì-a","bàn-bàn-a","boe-ià-a/be-ià-a"], "POJ"),
        (["ㆠㄧㄜ˪ ㄤ˫ ㄚ","ㄤ˫ ㆠㆦ ㄚ","ㆠㄚˋ ㄧㄨˋ ㄚ","ㄏㄨㆤ˫ ㄉㄚˋ ㄚ","ㆠㄧ˫ ㆠㄧ˫ ㄚ/ㆠㄧ˪ ㆠㄧ˪ ㄚ","ㆠㄢ˪ ㆠㄢ˪ ㄚ","ㆠㄨㆤ ㄧㄚ˪ ㄚ/ㆠㆤ ㄧㄚ˪ ㄚ"], "Zhuyin"),
        (["bio3 ang7 a1","ang7 boo1 a1","ba2 iu2 a1","hue7 ta2 a1","bi7 bi7 a1/bi3 bi3 a1","ban3 ban3 a1","bue1 ia3 a1/be1 ia3 a1"], "TLPA"),
        (["bbiòângā","ângbboōā","bbǎyǔā","huêdǎā","bbîbbîā/bbìbbìā","bbànbbànā","bbuēyàā/bbēyàā"], "Pingyim"),
        (["bhiôr-āng-a","āng-bhor-a","bhà-iù-a","huē-dà-a","bhī-bhī-a/bhî-bhî-a","bhân-bhân-a","bhue-iâ-a/bhe-iâ-a"], "Tongiong"),
        (["biə¹¹ aŋ²² a⁴⁴/bio²¹ aŋ³³ a⁵⁵","aŋ²² bɔ⁴⁴ a⁴⁴/aŋ³³ bɔ⁵⁵ a⁵⁵","ba⁵³ iu⁵³ a⁴⁴/ba⁵¹ iu⁵¹ a⁵⁵","hue²² ta⁵³ a⁴⁴/hue³³ ta⁵¹ a⁵⁵","bi²² bi²² a⁴⁴/bi²¹ bi²¹ a⁵⁵","ban¹¹ ban¹¹ a⁴⁴/ban²¹ ban²¹ a⁵⁵","bue⁴⁴ ia¹¹ a⁴⁴/be⁵⁵ ia²¹ a⁵⁵"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='incl_last'), Converter(system=system, dialect="north", punctuation='none', sandhi='incl_last'))

def test_sentence_auto():
    test_data = [
        (["Thái-khōng pīng-iú, lin-hó! Lin tsià-pa buē/Thái-khōng pìng-iú, lin-hó! Lin tsià-pa bē"], "Tailo"),
        (["Thái-khōng pēng-iú, lin-hó! Lin chià-pa bōe/Thái-khōng pèng-iú, lin-hó! Lin chià-pa bē"], "POJ"),
        (["ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˫ ㄧㄨˋ, ㄌㄧㄣ ㄏㄜˋ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㄨㆤ˫/ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˪ ㄧㄨˋ, ㄌㄧㄣ ㄏㄜˋ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㆤ˫"], "Zhuyin"),
        (["Thai2 khong7 ping7 iu2, lin1 ho2! Lin1 cia3 pa1 bue7/Thai2 khong7 ping3 iu2, lin1 ho2! Lin1 cia3 pa1 be7"], "TLPA"),
        (["Tǎikông bîngyǔ, līnhǒ! Līn ziàbā bbuê/Tǎikông bìngyǔ, līnhǒ! Līn ziàbā bbê"], "Pingyim"),
        (["Tài-kōng bīng-iù, lin-hòr! Lin ziâ-ba bhuē/Tài-kōng bîng-iù, lin-hòr! Lin ziâ-ba bhē"], "Tongiong"),
        (["Tʰai⁵³ kʰɔŋ²² piɪŋ²² iu⁵³, lin⁴⁴ hə⁵³! Lin⁴⁴ tɕia¹¹ pa⁴⁴ bue²²/Tʰai⁵¹ kʰɔŋ³³ piɪŋ²¹ iu⁵¹, lin⁵⁵ ho⁵¹! Lin⁵⁵ tɕia²¹ pa⁵⁵ be³³"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, sandhi='auto'), Converter(system=system, dialect="north", sandhi='auto'))

def test_sentence_none():
    test_data = [
        (["Thài-khong pîng-iú, lín-hó! Lín tsia̍h-pá buē/Thài-khong pîng-iú, lín-hó! Lín tsia̍h-pá bē"], "Tailo"),
        (["Thài-khong pêng-iú, lín-hó! Lín chia̍h-pá bōe/Thài-khong pêng-iú, lín-hó! Lín chia̍h-pá bē"], "POJ"),
        (["ㄊㄞ˪ ㄎㆲ ㄅㄧㄥˊ ㄧㄨˋ, ㄌㄧㄣˋ ㄏㄜˋ! ㄌㄧㄣˋ ㄐㄧㄚㆷ˙ ㄅㄚˋ ㆠㄨㆤ˫/ㄊㄞ˪ ㄎㆲ ㄅㄧㄥˊ ㄧㄨˋ, ㄌㄧㄣˋ ㄏㄜˋ! ㄌㄧㄣˋ ㄐㄧㄚㆷ˙ ㄅㄚˋ ㆠㆤ˫"], "Zhuyin"),
        (["Thai3 khong1 ping5 iu2, lin2 ho2! Lin2 ciah8 pa2 bue7/Thai3 khong1 ping5 iu2, lin2 ho2! Lin2 ciah8 pa2 be7"], "TLPA"),
        (["Tàikōng bíngyǔ, lǐnhǒ! Lǐn ziáhbǎ bbuê/Tàikōng bíngyǔ, lǐnhǒ! Lǐn ziáhbǎ bbê"], "Pingyim"),
        (["Tâi-kong bĭng-iù, lìn-hòr! Lìn ziah-bà bhuē/Tâi-kong bĭng-iù, lìn-hòr! Lìn ziah-bà bhē"], "Tongiong"),
        (["Tʰai¹¹ kʰɔŋ⁴⁴ piɪŋ²⁵ iu⁵³, lin⁵³ hə⁵³! Lin⁵³ tɕiaʔ⁵ pa⁵³ bue²²/Tʰai²¹ kʰɔŋ⁵⁵ piɪŋ²⁴ iu⁵¹, lin⁵¹ ho⁵¹! Lin⁵¹ tɕiaʔ⁴ pa⁵¹ be³³"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, sandhi='none'), Converter(system=system, dialect="north", sandhi='none'))

def test_sentence_exc_last():
    test_data = [
        (["Thái-khōng pīng-iu, lin-ho! Lin tsià-pa buē/Thái-khōng pìng-iu, lin-ho! Lin tsià-pa bē"], "Tailo"),
        (["Thái-khōng pēng-iu, lin-ho! Lin chià-pa bōe/Thái-khōng pèng-iu, lin-ho! Lin chià-pa bē"], "POJ"),
        (["ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˫ ㄧㄨ, ㄌㄧㄣ ㄏㄜ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㄨㆤ˫/ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˪ ㄧㄨ, ㄌㄧㄣ ㄏㄜ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㆤ˫"], "Zhuyin"),
        (["Thai2 khong7 ping7 iu1, lin1 ho1! Lin1 cia3 pa1 bue7/Thai2 khong7 ping3 iu1, lin1 ho1! Lin1 cia3 pa1 be7"], "TLPA"),
        (["Tǎikông bîngyū, līnhō! Līn ziàbā bbuê/Tǎikông bìngyū, līnhō! Līn ziàbā bbê"], "Pingyim"),
        (["Tài-kōng bīng-iu, lin-hor! Lin ziâ-ba bhuē/Tài-kōng bîng-iu, lin-hor! Lin ziâ-ba bhē"], "Tongiong"),
        (["Tʰai⁵³ kʰɔŋ²² piɪŋ²² iu⁴⁴, lin⁴⁴ hə⁴⁴! Lin⁴⁴ tɕia¹¹ pa⁴⁴ bue²²/Tʰai⁵¹ kʰɔŋ³³ piɪŋ²¹ iu⁵⁵, lin⁵⁵ ho⁵⁵! Lin⁵⁵ tɕia²¹ pa⁵⁵ be³³"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, sandhi='exc_last'), Converter(system=system, dialect="north", sandhi='exc_last'))

def test_sentence_incl_last():
    test_data = [
        (["Thái-khōng pīng-iu, lin-ho! Lin tsià-pa buè/Thái-khōng pìng-iu, lin-ho! Lin tsià-pa bè"], "Tailo"),
        (["Thái-khōng pēng-iu, lin-ho! Lin chià-pa bòe/Thái-khōng pèng-iu, lin-ho! Lin chià-pa bè"], "POJ"),
        (["ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˫ ㄧㄨ, ㄌㄧㄣ ㄏㄜ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㄨㆤ˪/ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˪ ㄧㄨ, ㄌㄧㄣ ㄏㄜ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㆤ˪"], "Zhuyin"),
        (["Thai2 khong7 ping7 iu1, lin1 ho1! Lin1 cia3 pa1 bue3/Thai2 khong7 ping3 iu1, lin1 ho1! Lin1 cia3 pa1 be3"], "TLPA"),
        (["Tǎikông bîngyū, līnhō! Līn ziàbā bbuè/Tǎikông bìngyū, līnhō! Līn ziàbā bbè"], "Pingyim"),
        (["Tài-kōng bīng-iu, lin-hor! Lin ziâ-ba bhuê/Tài-kōng bîng-iu, lin-hor! Lin ziâ-ba bhê"], "Tongiong"),
        (["Tʰai⁵³ kʰɔŋ²² piɪŋ²² iu⁴⁴, lin⁴⁴ hə⁴⁴! Lin⁴⁴ tɕia¹¹ pa⁴⁴ bue¹¹/Tʰai⁵¹ kʰɔŋ³³ piɪŋ²¹ iu⁵⁵, lin⁵⁵ ho⁵⁵! Lin⁵⁵ tɕia²¹ pa⁵⁵ be²¹"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, sandhi='incl_last'), Converter(system=system, dialect="north", sandhi='incl_last'))