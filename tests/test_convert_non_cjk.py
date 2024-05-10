from taibun.taibun import Converter
from utils import checker

hanji_data = ["khai-sí","khá-khì","kià-huê","bah-pau","hip-au","hit-hō","khak-sìn","lâm-bīn","bī-lâi","bi̍h-tshio̍h","gia̍p-bū","hua̍t-kim","ha̍k-sing"]
hanji_sentence = ["Thài-khong pîng-iú lín-hó! Lín tsia̍h-pá buē","Thôo kha tshing-khì--ah"]

def test_sandhi_default():
	test_data = [
        (["khai-sí","khá-khì","kià-huê","bah-pau","hip-au","hit-hō","khak-sìn","lâm-bīn","bī-lâi","bi̍h-tshio̍h","gia̍p-bū","hua̍t-kim","ha̍k-sing"], "Tailo"),
        (["khai-sí","khá-khì","kià-hôe","bah-pau","hip-au","hit-hō","khak-sìn","lâm-bīn","bī-lâi","bi̍h-chhio̍h","gia̍p-bū","hoa̍t-kim","ha̍k-seng"], "POJ"),
        (["ㄎㄞ ㄒㄧˋ","ㄎㄚˋ ㄎㄧ˪","ㄍㄧㄚ˪ ㄏㄨㆤˊ","ㆠㄚㆷ ㄅㄠ","ㄏㄧㆴ ㄠ","ㄏㄧㆵ ㄏㄜ˫","ㄎㄚㆶ ㄒㄧㄣ˪","ㄌㆰˊ ㆠㄧㄣ˫","ㆠㄧ˫ ㄌㄞˊ","ㆠㄧㆷ˙ ㄑㄧㄜㆷ˙","ㆣㄧㄚㆴ˙ ㆠㄨ˫","ㄏㄨㄚㆵ˙ ㄍㄧㆬ","ㄏㄚㆶ˙ ㄒㄧㄥ"], "Zhuyin"),
        (["khai1 si2","kha2 khi3","kia3 hue5","bah4 pau1","hip4 au1","hit4 ho7","khak4 sin3","lam5 bin7","bi7 lai5","bih8 chioh8","giap8 bu7","huat8 kim1","hak8 sing1"], "TLPA"),
        (["kāisǐ","kǎkì","giàhué","bbāhbāo","hīpāo","hīthô","kāksìn","lámbbîn","bbîlái","bbíhcióh","ggiápbbû","huátgīm","háksīng"], "Pingyim"),
        (["kāi-sì","ka-kî","già-huĕ","bhà-bau","hip-au","hit-hōr","kak-sîn","lām-bhīn/lâm-bhīn","bhî-lăi","bhî-cioh","ghiāp-bhū","huāt-gim","hāk-sing"], "Tongiong"),
        (["kʰai⁴⁴ ɕi⁵³/kʰai⁵⁵ ɕi⁵¹","kʰa⁵³ kʰi¹¹/kʰa⁵¹ kʰi²¹","kia¹¹ hue²⁵/kia²¹ hue²⁴","baʔ²¹ pau⁴⁴/baʔ³² pau⁵⁵","hip̚²¹ au⁴⁴/hip̚³² au⁵⁵","hit̚²¹ hə²²/hit̚³² ho³³","kʰak̚²¹ ɕin¹¹/kʰak̚³² ɕin²¹","lam²⁵ bin²²/lam²⁴ bin³³","bi²² lai²⁵/bi³³ lai²⁴","biʔ⁵ tɕʰiəʔ⁵/biʔ⁴ tɕʰioʔ⁴","giap̚⁵ bu²²/giap̚⁴ bu³³","huat̚⁵ kim⁴⁴/huat̚⁴ kim⁵⁵","hak̚⁵ ɕiɪŋ⁴⁴/hak̚⁴ ɕiɪŋ⁵⁵"], "IPA")
    ]
	for transl, system in test_data:
		data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
		checker(data, Converter(system=system, punctuation='none', convert_non_cjk=True), Converter(system=system, dialect="north", punctuation='none', convert_non_cjk=True))

def test_sandhi_auto():
    test_data = [
        (["khāi-sí","kha-khì","kiá-huê","bá-pau","hi̍p-au","hi̍t-hō","kha̍k-sìn","lām-bīn/làm-bīn","bì-lâi","bì-tshio̍h","giap-bū","huat-kim","hak-sing"], "Tailo"),
        (["khāi-sí","kha-khì","kiá-hôe","bá-pau","hi̍p-au","hi̍t-hō","kha̍k-sìn","lām-bīn/làm-bīn","bì-lâi","bì-chhio̍h","giap-bū","hoat-kim","hak-seng"], "POJ"),
        (["ㄎㄞ˫ ㄒㄧˋ","ㄎㄚ ㄎㄧ˪","ㄍㄧㄚˋ ㄏㄨㆤˊ","ㆠㄚˋ ㄅㄠ","ㄏㄧㆴ˙ ㄠ","ㄏㄧㆵ˙ ㄏㄜ˫","ㄎㄚㆶ˙ ㄒㄧㄣ˪","ㄌㆰ˫ ㆠㄧㄣ˫/ㄌㆰ˪ ㆠㄧㄣ˫","ㆠㄧ˪ ㄌㄞˊ","ㆠㄧ˪ ㄑㄧㄜㆷ˙","ㆣㄧㄚㆴ ㆠㄨ˫","ㄏㄨㄚㆵ ㄍㄧㆬ","ㄏㄚㆶ ㄒㄧㄥ"], "Zhuyin"),
        (["khai7 si2","kha1 khi3","kia2 hue5","ba2 pau1","hip8 au1","hit8 ho7","khak8 sin3","lam7 bin7/lam3 bin7","bi3 lai5","bi3 chioh8","giap4 bu7","huat4 kim1","hak4 sing1"], "TLPA"),
        (["kâisǐ","kākì","giǎhué","bbǎbāo","hípāo","híthô","káksìn","lâmbbîn/làmbbîn","bbìlái","bbìcióh","ggiāpbbû","huātgīm","hāksīng"], "Pingyim"),
        (["kāi-sì","ka-kî","già-huĕ","bhà-bau","hip-au","hit-hōr","kak-sîn","lām-bhīn/lâm-bhīn","bhî-lăi","bhî-cioh","ghiāp-bhū","huāt-gim","hāk-sing"], "Tongiong"),
        (["kʰai²² ɕi⁵³/kʰai³³ ɕi⁵¹","kʰa⁴⁴ kʰi¹¹/kʰa⁵⁵ kʰi²¹","kia⁵³ hue²⁵/kia⁵¹ hue²⁴","ba⁵³ pau⁴⁴/ba⁵¹ pau⁵⁵","hip̚⁵ au⁴⁴/hip̚⁴ au⁵⁵","hit̚⁵ hə²²/hit̚⁴ ho³³","kʰak̚⁵ ɕin¹¹/kʰak̚⁴ ɕin²¹","lam²² bin²²/lam²¹ bin³³","bi¹¹ lai²⁵/bi²¹ lai²⁴","bi¹¹ tɕʰiəʔ⁵/bi²¹ tɕʰioʔ⁴","giap̚²¹ bu²²/giap̚³² bu³³","huat̚²¹ kim⁴⁴/huat̚³² kim⁵⁵","hak̚²¹ ɕiɪŋ⁴⁴/hak̚³² ɕiɪŋ⁵⁵"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='auto', convert_non_cjk=True), Converter(system=system, dialect="north", punctuation='none', sandhi='auto', convert_non_cjk=True))

def test_sandhi_none():
    test_data = [
        (["khai-sí","khá-khì","kià-huê","bah-pau","hip-au","hit-hō","khak-sìn","lâm-bīn","bī-lâi","bi̍h-tshio̍h","gia̍p-bū","hua̍t-kim","ha̍k-sing"], "Tailo"),
        (["khai-sí","khá-khì","kià-hôe","bah-pau","hip-au","hit-hō","khak-sìn","lâm-bīn","bī-lâi","bi̍h-chhio̍h","gia̍p-bū","hoa̍t-kim","ha̍k-seng"], "POJ"),
        (["ㄎㄞ ㄒㄧˋ","ㄎㄚˋ ㄎㄧ˪","ㄍㄧㄚ˪ ㄏㄨㆤˊ","ㆠㄚㆷ ㄅㄠ","ㄏㄧㆴ ㄠ","ㄏㄧㆵ ㄏㄜ˫","ㄎㄚㆶ ㄒㄧㄣ˪","ㄌㆰˊ ㆠㄧㄣ˫","ㆠㄧ˫ ㄌㄞˊ","ㆠㄧㆷ˙ ㄑㄧㄜㆷ˙","ㆣㄧㄚㆴ˙ ㆠㄨ˫","ㄏㄨㄚㆵ˙ ㄍㄧㆬ","ㄏㄚㆶ˙ ㄒㄧㄥ"], "Zhuyin"),
        (["khai1 si2","kha2 khi3","kia3 hue5","bah4 pau1","hip4 au1","hit4 ho7","khak4 sin3","lam5 bin7","bi7 lai5","bih8 chioh8","giap8 bu7","huat8 kim1","hak8 sing1"], "TLPA"),
        (["kāisǐ","kǎkì","giàhué","bbāhbāo","hīpāo","hīthô","kāksìn","lámbbîn","bbîlái","bbíhcióh","ggiápbbû","huátgīm","háksīng"], "Pingyim"),
        (["kai-sì","kà-kî","giâ-huĕ","bhāh-bau","hīp-au","hīt-hōr","kāk-sîn","lăm-bhīn","bhī-lăi","bhih-cioh","ghiap-bhū","huat-gim","hak-sing"], "Tongiong"),
        (["kʰai⁴⁴ ɕi⁵³/kʰai⁵⁵ ɕi⁵¹","kʰa⁵³ kʰi¹¹/kʰa⁵¹ kʰi²¹","kia¹¹ hue²⁵/kia²¹ hue²⁴","baʔ²¹ pau⁴⁴/baʔ³² pau⁵⁵","hip̚²¹ au⁴⁴/hip̚³² au⁵⁵","hit̚²¹ hə²²/hit̚³² ho³³","kʰak̚²¹ ɕin¹¹/kʰak̚³² ɕin²¹","lam²⁵ bin²²/lam²⁴ bin³³","bi²² lai²⁵/bi³³ lai²⁴","biʔ⁵ tɕʰiəʔ⁵/biʔ⁴ tɕʰioʔ⁴","giap̚⁵ bu²²/giap̚⁴ bu³³","huat̚⁵ kim⁴⁴/huat̚⁴ kim⁵⁵","hak̚⁵ ɕiɪŋ⁴⁴/hak̚⁴ ɕiɪŋ⁵⁵"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='none', convert_non_cjk=True), Converter(system=system, dialect="north", punctuation='none', sandhi='none', convert_non_cjk=True))

def test_sandhi_exc_last():
    test_data = [
        (["khāi-sí","kha-khì","kiá-huê","bá-pau","hi̍p-au","hi̍t-hō","kha̍k-sìn","lām-bīn/làm-bīn","bì-lâi","bì-tshio̍h","giap-bū","huat-kim","hak-sing"], "Tailo"),
        (["khāi-sí","kha-khì","kiá-hôe","bá-pau","hi̍p-au","hi̍t-hō","kha̍k-sìn","lām-bīn/làm-bīn","bì-lâi","bì-chhio̍h","giap-bū","hoat-kim","hak-seng"], "POJ"),
        (["ㄎㄞ˫ ㄒㄧˋ","ㄎㄚ ㄎㄧ˪","ㄍㄧㄚˋ ㄏㄨㆤˊ","ㆠㄚˋ ㄅㄠ","ㄏㄧㆴ˙ ㄠ","ㄏㄧㆵ˙ ㄏㄜ˫","ㄎㄚㆶ˙ ㄒㄧㄣ˪","ㄌㆰ˫ ㆠㄧㄣ˫/ㄌㆰ˪ ㆠㄧㄣ˫","ㆠㄧ˪ ㄌㄞˊ","ㆠㄧ˪ ㄑㄧㄜㆷ˙","ㆣㄧㄚㆴ ㆠㄨ˫","ㄏㄨㄚㆵ ㄍㄧㆬ","ㄏㄚㆶ ㄒㄧㄥ"], "Zhuyin"),
        (["khai7 si2","kha1 khi3","kia2 hue5","ba2 pau1","hip8 au1","hit8 ho7","khak8 sin3","lam7 bin7/lam3 bin7","bi3 lai5","bi3 chioh8","giap4 bu7","huat4 kim1","hak4 sing1"], "TLPA"),
        (["kâisǐ","kākì","giǎhué","bbǎbāo","hípāo","híthô","káksìn","lâmbbîn/làmbbîn","bbìlái","bbìcióh","ggiāpbbû","huātgīm","hāksīng"], "Pingyim"),
        (["kāi-sì","ka-kî","già-huĕ","bhà-bau","hip-au","hit-hōr","kak-sîn","lām-bhīn/lâm-bhīn","bhî-lăi","bhî-cioh","ghiāp-bhū","huāt-gim","hāk-sing"], "Tongiong"),
        (["kʰai²² ɕi⁵³/kʰai³³ ɕi⁵¹","kʰa⁴⁴ kʰi¹¹/kʰa⁵⁵ kʰi²¹","kia⁵³ hue²⁵/kia⁵¹ hue²⁴","ba⁵³ pau⁴⁴/ba⁵¹ pau⁵⁵","hip̚⁵ au⁴⁴/hip̚⁴ au⁵⁵","hit̚⁵ hə²²/hit̚⁴ ho³³","kʰak̚⁵ ɕin¹¹/kʰak̚⁴ ɕin²¹","lam²² bin²²/lam²¹ bin³³","bi¹¹ lai²⁵/bi²¹ lai²⁴","bi¹¹ tɕʰiəʔ⁵/bi²¹ tɕʰioʔ⁴","giap̚²¹ bu²²/giap̚³² bu³³","huat̚²¹ kim⁴⁴/huat̚³² kim⁵⁵","hak̚²¹ ɕiɪŋ⁴⁴/hak̚³² ɕiɪŋ⁵⁵"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='exc_last', convert_non_cjk=True), Converter(system=system, dialect="north", punctuation='none', sandhi='exc_last', convert_non_cjk=True))

def test_sandhi_incl_last():
    test_data = [
        (["khāi-si","kha-khí","kiá-huē/kiá-huè","bá-pāu","hi̍p-āu","hi̍t-hò","kha̍k-sín","lām-bìn/làm-bìn","bì-lāi/bì-lài","bì-tshiò","giap-bù","huat-kīm","hak-sīng"], "Tailo"),
        (["khāi-si","kha-khí","kiá-hōe/kiá-hòe","bá-pāu","hi̍p-āu","hi̍t-hò","kha̍k-sín","lām-bìn/làm-bìn","bì-lāi/bì-lài","bì-chhiò","giap-bù","hoat-kīm","hak-sēng"], "POJ"),
        (["ㄎㄞ˫ ㄒㄧ","ㄎㄚ ㄎㄧˋ","ㄍㄧㄚˋ ㄏㄨㆤ˫/ㄍㄧㄚˋ ㄏㄨㆤ˪","ㆠㄚˋ ㄅㄠ˫","ㄏㄧㆴ˙ ㄠ˫","ㄏㄧㆵ˙ ㄏㄜ˪","ㄎㄚㆶ˙ ㄒㄧㄣˋ","ㄌㆰ˫ ㆠㄧㄣ˪/ㄌㆰ˪ ㆠㄧㄣ˪","ㆠㄧ˪ ㄌㄞ˫/ㆠㄧ˪ ㄌㄞ˪","ㆠㄧ˪ ㄑㄧㄜ˪","ㆣㄧㄚㆴ ㆠㄨ˪","ㄏㄨㄚㆵ ㄍㄧㆬ˫","ㄏㄚㆶ ㄒㄧㄥ˫"], "Zhuyin"),
        (["khai7 si1","kha1 khi2","kia2 hue7/kia2 hue3","ba2 pau7","hip8 au7","hit8 ho3","khak8 sin2","lam7 bin3/lam3 bin3","bi3 lai7/bi3 lai3","bi3 chio3","giap4 bu3","huat4 kim7","hak4 sing7"], "TLPA"),
        (["kâisī","kākǐ","giǎhuê/giǎhuè","bbǎbâo","hípâo","híthò","káksǐn","lâmbbìn/làmbbìn","bbìlâi/bbìlài","bbìciò","ggiāpbbù","huātgîm","hāksîng"], "Pingyim"),
        (["kāi-si","ka-kì","già-huē/già-huê","bhà-bāu","hip-āu","hit-hôr","kak-sìn","lām-bhîn/lâm-bhîn","bhî-lāi/bhî-lâi","bhî-ciôr","ghiāp-bhû","huāt-gīm","hāk-sīng"], "Tongiong"),
        (["kʰai²² ɕi⁴⁴/kʰai³³ ɕi⁵⁵","kʰa⁴⁴ kʰi⁵³/kʰa⁵⁵ kʰi⁵¹","kia⁵³ hue²²/kia⁵¹ hue²¹","ba⁵³ pau²²/ba⁵¹ pau³³","hip̚⁵ au²²/hip̚⁴ au³³","hit̚⁵ hə¹¹/hit̚⁴ ho²¹","kʰak̚⁵ ɕin⁵³/kʰak̚⁴ ɕin⁵¹","lam²² bin¹¹/lam²¹ bin²¹","bi¹¹ lai²²/bi²¹ lai²¹","bi¹¹ tɕʰiə¹¹/bi²¹ tɕʰio²¹","giap̚²¹ bu¹¹/giap̚³² bu²¹","huat̚²¹ kim²²/huat̚³² kim³³","hak̚²¹ ɕiɪŋ²²/hak̚³² ɕiɪŋ³³"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_data, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='incl_last', convert_non_cjk=True), Converter(system=system, dialect="north", punctuation='none', sandhi='incl_last', convert_non_cjk=True))

def test_sentence_auto():
    test_data = [
        (["Thái-khōng pīng-iu lin-ho! Lin tsià-pa buē/Thái-khōng pìng-iu lin-ho! Lin tsià-pa buē","Thōo khā tshīng-khì--ah/Thòo khā tshīng-khì--ah"], "Tailo"),
        (["Thái-khōng pēng-iu lin-ho! Lin chià-pa bōe/Thái-khōng pèng-iu lin-ho! Lin chià-pa bōe","Thō͘ khā chhēng-khì--ah/Thò͘ khā chhēng-khì--ah"], "POJ"),
        (["ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˫ ㄧㄨ ㄌㄧㄣ ㄏㄜ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㄨㆤ˫/ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˪ ㄧㄨ ㄌㄧㄣ ㄏㄜ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㄨㆤ˫","ㄊㆦ˫ ㄎㄚ˫ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ/ㄊㆦ˪ ㄎㄚ˫ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ"], "Zhuyin"),
        (["Thai2 khong7 ping7 iu1 lin1 ho1! Lin1 cia3 pa1 bue7/Thai2 khong7 ping3 iu1 lin1 ho1! Lin1 cia3 pa1 bue7","Thoo7 kha7 ching7 khi3 ah0/Thoo3 kha7 ching7 khi3 ah0"], "TLPA"),
        (["Tǎikông bîngyū līnhō! Līn ziàbā bbuê/Tǎikông bìngyū līnhō! Līn ziàbā bbuê","Toô kâ cîngkìah/Toò kâ cîngkìah"], "Pingyim"),
        (["Tài-kōng bīng-iu lin-hor! Lin ziâ-ba bhuē/Tài-kōng bîng-iu lin-hor! Lin ziâ-ba bhuē","Tōr kā cīng-kî--åh/Tôr kā cīng-kî--åh"], "Tongiong"),
        (["Tʰai⁵³ kʰɔŋ²² piɪŋ²² iu⁴⁴ lin⁴⁴ hə⁴⁴! Lin⁴⁴ tɕia¹¹ pa⁴⁴ bue²²/Tʰai⁵¹ kʰɔŋ³³ piɪŋ²¹ iu⁵⁵ lin⁵⁵ ho⁵⁵! Lin⁵⁵ tɕia²¹ pa⁵⁵ bue³³","Tʰɔ²² kʰa²² tɕʰiɪŋ²² kʰi¹¹ a/Tʰɔ²¹ kʰa³³ tɕʰiɪŋ³³ kʰi²¹ a"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, sandhi='auto', convert_non_cjk=True), Converter(system=system, dialect="north", sandhi='auto', convert_non_cjk=True))

def test_sentence_none():
    test_data = [
        (["Thài-khong pîng-iú lín-hó! Lín tsia̍h-pá buē","Thôo kha tshing-khì--ah"], "Tailo"),
        (["Thài-khong pêng-iú lín-hó! Lín chia̍h-pá bōe","Thô͘ kha chheng-khì--ah"], "POJ"),
        (["ㄊㄞ˪ ㄎㆲ ㄅㄧㄥˊ ㄧㄨˋ ㄌㄧㄣˋ ㄏㄜˋ! ㄌㄧㄣˋ ㄐㄧㄚㆷ˙ ㄅㄚˋ ㆠㄨㆤ˫","ㄊㆦˊ ㄎㄚ ㄑㄧㄥ ㄎㄧ˪ ㄚ"], "Zhuyin"),
        (["Thai3 khong1 ping5 iu2 lin2 ho2! Lin2 ciah8 pa2 bue7","Thoo5 kha1 ching1 khi3 ah0"], "TLPA"),
        (["Tàikōng bíngyǔ lǐnhǒ! Lǐn ziáhbǎ bbuê","Toó kā cīngkìah"], "Pingyim"),
        (["Tâi-kong bĭng-iù lìn-hòr! Lìn ziah-bà bhuē","Tŏr ka cing-kî--åh"], "Tongiong"),
        (["Tʰai¹¹ kʰɔŋ⁴⁴ piɪŋ²⁵ iu⁵³ lin⁵³ hə⁵³! Lin⁵³ tɕiaʔ⁵ pa⁵³ bue²²/Tʰai²¹ kʰɔŋ⁵⁵ piɪŋ²⁴ iu⁵¹ lin⁵¹ ho⁵¹! Lin⁵¹ tɕiaʔ⁴ pa⁵¹ bue³³","Tʰɔ²⁵ kʰa⁴⁴ tɕʰiɪŋ⁴⁴ kʰi¹¹ a/Tʰɔ²⁴ kʰa⁵⁵ tɕʰiɪŋ⁵⁵ kʰi²¹ a"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, sandhi='none', convert_non_cjk=True), Converter(system=system, dialect="north", sandhi='none', convert_non_cjk=True))

def test_sentence_exc_last():
    test_data = [
        (["Thái-khōng pīng-iu lin-ho! Lin tsià-pa buē/Thái-khōng pìng-iu lin-ho! Lin tsià-pa buē","Thōo khā tshīng-khì--ah/Thòo khā tshīng-khì--ah"], "Tailo"),
        (["Thái-khōng pēng-iu lin-ho! Lin chià-pa bōe/Thái-khōng pèng-iu lin-ho! Lin chià-pa bōe","Thō͘ khā chhēng-khì--ah/Thò͘ khā chhēng-khì--ah"], "POJ"),
        (["ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˫ ㄧㄨ ㄌㄧㄣ ㄏㄜ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㄨㆤ˫/ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˪ ㄧㄨ ㄌㄧㄣ ㄏㄜ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㄨㆤ˫","ㄊㆦ˫ ㄎㄚ˫ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ/ㄊㆦ˪ ㄎㄚ˫ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ"], "Zhuyin"),
        (["Thai2 khong7 ping7 iu1 lin1 ho1! Lin1 cia3 pa1 bue7/Thai2 khong7 ping3 iu1 lin1 ho1! Lin1 cia3 pa1 bue7","Thoo7 kha7 ching7 khi3 ah0/Thoo3 kha7 ching7 khi3 ah0"], "TLPA"),
        (["Tǎikông bîngyū līnhō! Līn ziàbā bbuê/Tǎikông bìngyū līnhō! Līn ziàbā bbuê","Toô kâ cîngkìah/Toò kâ cîngkìah"], "Pingyim"),
        (["Tài-kōng bīng-iu lin-hor! Lin ziâ-ba bhuē/Tài-kōng bîng-iu lin-hor! Lin ziâ-ba bhuē","Tōr kā cīng-kî--åh/Tôr kā cīng-kî--åh"], "Tongiong"),
        (["Tʰai⁵³ kʰɔŋ²² piɪŋ²² iu⁴⁴ lin⁴⁴ hə⁴⁴! Lin⁴⁴ tɕia¹¹ pa⁴⁴ bue²²/Tʰai⁵¹ kʰɔŋ³³ piɪŋ²¹ iu⁵⁵ lin⁵⁵ ho⁵⁵! Lin⁵⁵ tɕia²¹ pa⁵⁵ bue³³","Tʰɔ²² kʰa²² tɕʰiɪŋ²² kʰi¹¹ a/Tʰɔ²¹ kʰa³³ tɕʰiɪŋ³³ kʰi²¹ a"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, sandhi='exc_last', convert_non_cjk=True), Converter(system=system, dialect="north", sandhi='exc_last', convert_non_cjk=True))

def test_sentence_incl_last():
    test_data = [
        (["Thái-khōng pīng-iu lin-ho! Lin tsià-pa buè/Thái-khōng pìng-iu lin-ho! Lin tsià-pa buè","Thōo khā tshīng-khì--ah/Thòo khā tshīng-khì--ah"], "Tailo"),
        (["Thái-khōng pēng-iu lin-ho! Lin chià-pa bòe/Thái-khōng pèng-iu lin-ho! Lin chià-pa bòe","Thō͘ khā chhēng-khì--ah/Thò͘ khā chhēng-khì--ah"], "POJ"),
        (["ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˫ ㄧㄨ ㄌㄧㄣ ㄏㄜ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㄨㆤ˪/ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˪ ㄧㄨ ㄌㄧㄣ ㄏㄜ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㄨㆤ˪","ㄊㆦ˫ ㄎㄚ˫ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ/ㄊㆦ˪ ㄎㄚ˫ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ"], "Zhuyin"),
        (["Thai2 khong7 ping7 iu1 lin1 ho1! Lin1 cia3 pa1 bue3/Thai2 khong7 ping3 iu1 lin1 ho1! Lin1 cia3 pa1 bue3","Thoo7 kha7 ching7 khi3 ah0/Thoo3 kha7 ching7 khi3 ah0"], "TLPA"),
        (["Tǎikông bîngyū līnhō! Līn ziàbā bbuè/Tǎikông bìngyū līnhō! Līn ziàbā bbuè","Toô kâ cîngkìah/Toò kâ cîngkìah"], "Pingyim"),
        (["Tài-kōng bīng-iu lin-hor! Lin ziâ-ba bhuê/Tài-kōng bîng-iu lin-hor! Lin ziâ-ba bhuê","Tōr kā cīng-kî--åh/Tôr kā cīng-kî--åh"], "Tongiong"),
        (["Tʰai⁵³ kʰɔŋ²² piɪŋ²² iu⁴⁴ lin⁴⁴ hə⁴⁴! Lin⁴⁴ tɕia¹¹ pa⁴⁴ bue¹¹/Tʰai⁵¹ kʰɔŋ³³ piɪŋ²¹ iu⁵⁵ lin⁵⁵ ho⁵⁵! Lin⁵⁵ tɕia²¹ pa⁵⁵ bue²¹","Tʰɔ²² kʰa²² tɕʰiɪŋ²² kʰi¹¹ a/Tʰɔ²¹ kʰa³³ tɕʰiɪŋ³³ kʰi²¹ a"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_sentence, transl)]
        checker(data, Converter(system=system, sandhi='incl_last', convert_non_cjk=True), Converter(system=system, dialect="north", sandhi='incl_last', convert_non_cjk=True))