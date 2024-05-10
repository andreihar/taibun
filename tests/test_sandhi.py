from taibun.taibun import Converter
from utils import checker

hanji_data = ["開始","巧氣","寄回","肉包","翕甌","彼號","確信","南面","未來","篾蓆","業務","罰金","學生"]
hanji_sentence = ["太空朋友，恁好！恁食飽未"]
hanji_a = ["廟尪仔","翁某仔","肉幼仔","花搭仔","微微仔","慢慢仔","尾蝶仔","佇厝仔頂我咧行","塗跤清氣矣","阮佇厝外攏講台語","佇公園內睏","遮有⾞禍無","這隻狗仔不時會吠"]

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

def test_add_auto():
    test_data = [
        (["biò-āng-á","āng-boo-á","bá-iu-á","huē-ta-á","bī-bī-á/bì-bī-á","bàn-bān-á","bue-iā-á/be-iā-á","tì tshú á tíng gua 咧 kiânn","thôo kha tshīng-khì--ah","guan tì tshù guā lang kang-tāi gí/guan tì tshù guā lang kang-tài gú","tì kōng-hn̂g lāi khùn","tsia iú ⾞ è bô","tse tsiá kau-á pu̍t-sī è puī/tse tsiá kau-á pu̍t-sì è puī"], "Tailo"),
        (["biò-āng-á","āng-bo͘-á","bá-iu-á","hōe-ta-á","bī-bī-á/bì-bī-á","bàn-bān-á","boe-iā-á/be-iā-á","tì chhú á téng goa 咧 kiâⁿ","thô͘ kha chhēng-khì--ah","goan tì chhù gōa lang kang-tāi gí/goan tì chhù gōa lang kang-tài gú","tì kōng-hn̂g lāi khùn","chia iú ⾞ è bô","che chiá kau-á pu̍t-sī è pūi/che chiá kau-á pu̍t-sì è pūi"], "POJ"),
        (["ㆠㄧㄜ˪ ㄤ˫ ㄚˋ","ㄤ˫ ㆠㆦ ㄚˋ","ㆠㄚˋ ㄧㄨ ㄚˋ","ㄏㄨㆤ˫ ㄉㄚ ㄚˋ","ㆠㄧ˫ ㆠㄧ˫ ㄚˋ/ㆠㄧ˪ ㆠㄧ˫ ㄚˋ","ㆠㄢ˪ ㆠㄢ˫ ㄚˋ","ㆠㄨㆤ ㄧㄚ˫ ㄚˋ/ㆠㆤ ㄧㄚ˫ ㄚˋ","ㄉㄧ˪ ㄘㄨˋ ㄚˋ ㄉㄧㄥˋ ㆣㄨㄚ 咧 ㄍㄧㆩˊ","ㄊㆦˊ ㄎㄚ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ","ㆣㄨㄢ ㄉㄧ˪ ㄘㄨ˪ ㆣㄨㄚ˫ ㄌㄤ ㄍㄤ ㄉㄞ˫ ㆣㄧˋ/ㆣㄨㄢ ㄉㄧ˪ ㄘㄨ˪ ㆣㄨㄚ˫ ㄌㄤ ㄍㄤ ㄉㄞ˪ ㆣㄨˋ","ㄉㄧ˪ ㄍㆲ˫ ㄏㆭˊ ㄌㄞ˫ ㄎㄨㄣ˪","ㄐㄧㄚ ㄧㄨˋ ⾞ ㆤ˪ ㆠㄜˊ","ㄗㆤ ㄐㄧㄚˋ ㄍㄠ ㄚˋ ㄅㄨㆵ˙ ㄒㄧ˫ ㆤ˪ ㄅㄨㄧ˫/ㄗㆤ ㄐㄧㄚˋ ㄍㄠ ㄚˋ ㄅㄨㆵ˙ ㄒㄧ˪ ㆤ˪ ㄅㄨㄧ˫"], "Zhuyin"),
        (["bio3 ang7 a2","ang7 boo1 a2","ba2 iu1 a2","hue7 ta1 a2","bi7 bi7 a2/bi3 bi7 a2","ban3 ban7 a2","bue1 ia7 a2/be1 ia7 a2","ti3 chu2 a2 ting2 gua1 咧 kiann5","thoo5 kha1 ching7 khi3 ah0","guan1 ti3 chu3 gua7 lang1 kang1 tai7 gi2/guan1 ti3 chu3 gua7 lang1 kang1 tai3 gu2","ti3 kong7 hng5 lai7 khun3","cia1 iu2 ⾞ e3 bo5","ce1 cia2 kau1 a2 put8 si7 e3 pui7/ce1 cia2 kau1 a2 put8 si3 e3 pui7"], "TLPA"),
        (["bbiòângǎ","ângbboōǎ","bbǎyūǎ","huêdāǎ","bbîbbîǎ/bbìbbîǎ","bbànbbânǎ","bbuēyâǎ/bbēyâǎ","dì cǔ ǎ dǐng gguā 咧 giná","toó kā cîngkì ah","gguān dì cù gguâ lāng gāngdâi ggǐ/gguān dì cù gguâ lāng gāngdài ggǔ","dì gônghńg lâi kùn","ziā yǔ ⾞ è bbó","zē ziǎ gāoǎ bútsî è buî/zē ziǎ gāoǎ bútsì è buî"], "Pingyim"),
        (["bhiôr-āng-à","āng-bhor-à","bhà-iu-à","huē-da-à","bhī-bhī-à/bhî-bhī-à","bhân-bhān-à","bhue-iā-à/bhe-iā-à","dî cù à dìng ghua 咧 giănn","tŏr ka cīng-kî--åh","ghuan dî cû ghuā lang gang-dāi ghì/ghuan dî cû ghuā lang gang-dâi ghù","dî gōng-hn̆g lāi kûn","zia iù ⾞ ê bhŏr","ze zià gau-à but-sī ê buī/ze zià gau-à but-sî ê buī"], "Tongiong"),
        (["biə¹¹ aŋ²² a⁵³/bio²¹ aŋ³³ a⁵¹","aŋ²² bɔ⁴⁴ a⁵³/aŋ³³ bɔ⁵⁵ a⁵¹","ba⁵³ iu⁴⁴ a⁵³/ba⁵¹ iu⁵⁵ a⁵¹","hue²² ta⁴⁴ a⁵³/hue³³ ta⁵⁵ a⁵¹","bi²² bi²² a⁵³/bi²¹ bi³³ a⁵¹","ban¹¹ ban²² a⁵³/ban²¹ ban³³ a⁵¹","bue⁴⁴ ia²² a⁵³/be⁵⁵ ia³³ a⁵¹","ti¹¹ tsʰu⁵³ a⁵³ tiɪŋ⁵³ gua⁴⁴ 咧 kiã²⁵/ti²¹ tsʰu⁵¹ a⁵¹ tiɪŋ⁵¹ gua⁵⁵ 咧 kiã²⁴","tʰɔ²⁵ kʰa⁴⁴ tɕʰiɪŋ²² kʰi¹¹ a/tʰɔ²⁴ kʰa⁵⁵ tɕʰiɪŋ³³ kʰi²¹ a","guan⁴⁴ ti¹¹ tsʰu¹¹ gua²² laŋ⁴⁴ kaŋ⁴⁴ tai²² gi⁵³/guan⁵⁵ ti²¹ tsʰu²¹ gua³³ laŋ⁵⁵ kaŋ⁵⁵ tai²¹ gu⁵¹","ti¹¹ kɔŋ²² hŋ̍²⁵ lai²² kʰun¹¹/ti²¹ kɔŋ³³ hŋ̍²⁴ lai³³ kʰun²¹","tɕia⁴⁴ iu⁵³ ⾞ e¹¹ bə²⁵/tɕia⁵⁵ iu⁵¹ ⾞ e²¹ bo²⁴","tse⁴⁴ tɕia⁵³ kau⁴⁴ a⁵³ put̚⁵ ɕi²² e¹¹ pui²²/tse⁵⁵ tɕia⁵¹ kau⁵⁵ a⁵¹ put̚⁴ ɕi²¹ e²¹ pui³³"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_a, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='auto'), Converter(system=system, dialect="north", punctuation='none', sandhi='auto'))

def test_add_none():
    test_data = [
        (["biō-ang-á","ang-bóo-á","bah-iù-á","hue-tah-á","bî-bî-á","bān-bān-á","bué-ia̍h-á/bé-ia̍h-á","tī tshù á tíng guá 咧 kiânn","thôo kha tshing-khì--ah","guán tī tshù guā láng káng-tâi gí/guán tī tshù guā láng káng-tâi gú","tī kong-hn̂g lāi khùn","tsia iú ⾞ ē bô","tse tsiah káu-á put-sî ē puī"], "Tailo"),
        (["biō-ang-á","ang-bó͘-á","bah-iù-á","hoe-tah-á","bî-bî-á","bān-bān-á","bóe-ia̍h-á/bé-ia̍h-á","tī chhù á téng góa 咧 kiâⁿ","thô͘ kha chheng-khì--ah","goán tī chhù gōa láng káng-tâi gí/goán tī chhù gōa láng káng-tâi gú","tī kong-hn̂g lāi khùn","chia iú ⾞ ē bô","che chiah káu-á put-sî ē pūi"], "POJ"),
        (["ㆠㄧㄜ˫ ㄤ ㄚˋ","ㄤ ㆠㆦˋ ㄚˋ","ㆠㄚㆷ ㄧㄨ˪ ㄚˋ","ㄏㄨㆤ ㄉㄚㆷ ㄚˋ","ㆠㄧˊ ㆠㄧˊ ㄚˋ","ㆠㄢ˫ ㆠㄢ˫ ㄚˋ","ㆠㄨㆤˋ ㄧㄚㆷ˙ ㄚˋ/ㆠㆤˋ ㄧㄚㆷ˙ ㄚˋ","ㄉㄧ˫ ㄘㄨ˪ ㄚˋ ㄉㄧㄥˋ ㆣㄨㄚˋ 咧 ㄍㄧㆩˊ","ㄊㆦˊ ㄎㄚ ㄑㄧㄥ ㄎㄧ˪ ㄚ","ㆣㄨㄢˋ ㄉㄧ˫ ㄘㄨ˪ ㆣㄨㄚ˫ ㄌㄤˋ ㄍㄤˋ ㄉㄞˊ ㆣㄧˋ/ㆣㄨㄢˋ ㄉㄧ˫ ㄘㄨ˪ ㆣㄨㄚ˫ ㄌㄤˋ ㄍㄤˋ ㄉㄞˊ ㆣㄨˋ","ㄉㄧ˫ ㄍㆲ ㄏㆭˊ ㄌㄞ˫ ㄎㄨㄣ˪","ㄐㄧㄚ ㄧㄨˋ ⾞ ㆤ˫ ㆠㄜˊ","ㄗㆤ ㄐㄧㄚㆷ ㄍㄠˋ ㄚˋ ㄅㄨㆵ ㄒㄧˊ ㆤ˫ ㄅㄨㄧ˫"], "Zhuyin"),
        (["bio7 ang1 a2","ang1 boo2 a2","bah4 iu3 a2","hue1 tah4 a2","bi5 bi5 a2","ban7 ban7 a2","bue2 iah8 a2/be2 iah8 a2","ti7 chu3 a2 ting2 gua2 咧 kiann5","thoo5 kha1 ching1 khi3 ah0","guan2 ti7 chu3 gua7 lang2 kang2 tai5 gi2/guan2 ti7 chu3 gua7 lang2 kang2 tai5 gu2","ti7 kong1 hng5 lai7 khun3","cia1 iu2 ⾞ e7 bo5","ce1 ciah4 kau2 a2 put4 si5 e7 pui7"], "TLPA"),
        (["bbiôāngǎ","āngbboǒǎ","bbāhyùǎ","huēdāhǎ","bbíbbíǎ","bbânbbânǎ","bbuěyáhǎ/bběyáhǎ","dî cù ǎ dǐng gguǎ 咧 giná","toó kā cīngkì ah","gguǎn dî cù gguâ lǎng gǎngdái ggǐ/gguǎn dî cù gguâ lǎng gǎngdái ggǔ","dî gōnghńg lâi kùn","ziā yǔ ⾞ ê bbó","zē ziāh gǎoǎ būtsí ê buî"], "Pingyim"),
        (["bhiōr-ang-à","ang-bhòr-à","bhāh-iû-à","hue-dāh-à","bhĭ-bhĭ-à","bhān-bhān-à","bhuè-iah-à/bhè-iah-à","dī cû à dìng ghuà 咧 giănn","tŏr ka cing-kî--åh","ghuàn dī cû ghuā làng gàng-dăi ghì/ghuàn dī cû ghuā làng gàng-dăi ghù","dī gong-hn̆g lāi kûn","zia iù ⾞ ē bhŏr","ze ziāh gàu-à būt-sĭ ē buī"], "Tongiong"),
        (["biə²² aŋ⁴⁴ a⁵³/bio³³ aŋ⁵⁵ a⁵¹","aŋ⁴⁴ bɔ⁵³ a⁵³/aŋ⁵⁵ bɔ⁵¹ a⁵¹","baʔ²¹ iu¹¹ a⁵³/baʔ³² iu²¹ a⁵¹","hue⁴⁴ taʔ²¹ a⁵³/hue⁵⁵ taʔ³² a⁵¹","bi²⁵ bi²⁵ a⁵³/bi²⁴ bi²⁴ a⁵¹","ban²² ban²² a⁵³/ban³³ ban³³ a⁵¹","bue⁵³ iaʔ⁵ a⁵³/be⁵¹ iaʔ⁴ a⁵¹","ti²² tsʰu¹¹ a⁵³ tiɪŋ⁵³ gua⁵³ 咧 kiã²⁵/ti³³ tsʰu²¹ a⁵¹ tiɪŋ⁵¹ gua⁵¹ 咧 kiã²⁴","tʰɔ²⁵ kʰa⁴⁴ tɕʰiɪŋ⁴⁴ kʰi¹¹ a/tʰɔ²⁴ kʰa⁵⁵ tɕʰiɪŋ⁵⁵ kʰi²¹ a","guan⁵³ ti²² tsʰu¹¹ gua²² laŋ⁵³ kaŋ⁵³ tai²⁵ gi⁵³/guan⁵¹ ti³³ tsʰu²¹ gua³³ laŋ⁵¹ kaŋ⁵¹ tai²⁴ gu⁵¹","ti²² kɔŋ⁴⁴ hŋ̍²⁵ lai²² kʰun¹¹/ti³³ kɔŋ⁵⁵ hŋ̍²⁴ lai³³ kʰun²¹","tɕia⁴⁴ iu⁵³ ⾞ e²² bə²⁵/tɕia⁵⁵ iu⁵¹ ⾞ e³³ bo²⁴","tse⁴⁴ tɕiaʔ²¹ kau⁵³ a⁵³ put̚²¹ ɕi²⁵ e²² pui²²/tse⁵⁵ tɕiaʔ³² kau⁵¹ a⁵¹ put̚³² ɕi²⁴ e³³ pui³³"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_a, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='none'), Converter(system=system, dialect="north", punctuation='none', sandhi='none'))

def test_add_exc_last():
    test_data = [
        (["biò-āng-á","āng-boo-á","bá-iú-á","huē-tá-á","bī-bī-á/bì-bì-á","bàn-bàn-á","bue-ià-á/be-ià-á","tì tshú a ting gua 咧 kiânn","thōo khā tshīng-khì--ah/thòo khā tshīng-khì--ah","guan tì tshú guà lang kang-tāi gí/guan tì tshú guà lang kang-tài gú","tì kōng-hn̄g lài khùn/tì kōng-hǹg lài khùn","tsiā iu ⾞ è bô","tsē tsiá kau-a pu̍t-sī è puī/tsē tsiá kau-a pu̍t-sì è puī"], "Tailo"),
        (["biò-āng-á","āng-bo͘-á","bá-iú-á","hōe-tá-á","bī-bī-á/bì-bì-á","bàn-bàn-á","boe-ià-á/be-ià-á","tì chhú a teng goa 咧 kiâⁿ","thō͘ khā chhēng-khì--ah/thò͘ khā chhēng-khì--ah","goan tì chhú gòa lang kang-tāi gí/goan tì chhú gòa lang kang-tài gú","tì kōng-hn̄g lài khùn/tì kōng-hǹg lài khùn","chiā iu ⾞ è bô","chē chiá kau-a pu̍t-sī è pūi/chē chiá kau-a pu̍t-sì è pūi"], "POJ"),
        (["ㆠㄧㄜ˪ ㄤ˫ ㄚˋ","ㄤ˫ ㆠㆦ ㄚˋ","ㆠㄚˋ ㄧㄨˋ ㄚˋ","ㄏㄨㆤ˫ ㄉㄚˋ ㄚˋ","ㆠㄧ˫ ㆠㄧ˫ ㄚˋ/ㆠㄧ˪ ㆠㄧ˪ ㄚˋ","ㆠㄢ˪ ㆠㄢ˪ ㄚˋ","ㆠㄨㆤ ㄧㄚ˪ ㄚˋ/ㆠㆤ ㄧㄚ˪ ㄚˋ","ㄉㄧ˪ ㄘㄨˋ ㄚ ㄉㄧㄥ ㆣㄨㄚ 咧 ㄍㄧㆩˊ","ㄊㆦ˫ ㄎㄚ˫ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ/ㄊㆦ˪ ㄎㄚ˫ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ","ㆣㄨㄢ ㄉㄧ˪ ㄘㄨˋ ㆣㄨㄚ˪ ㄌㄤ ㄍㄤ ㄉㄞ˫ ㆣㄧˋ/ㆣㄨㄢ ㄉㄧ˪ ㄘㄨˋ ㆣㄨㄚ˪ ㄌㄤ ㄍㄤ ㄉㄞ˪ ㆣㄨˋ","ㄉㄧ˪ ㄍㆲ˫ ㄏㆭ˫ ㄌㄞ˪ ㄎㄨㄣ˪/ㄉㄧ˪ ㄍㆲ˫ ㄏㆭ˪ ㄌㄞ˪ ㄎㄨㄣ˪","ㄐㄧㄚ˫ ㄧㄨ ⾞ ㆤ˪ ㆠㄜˊ","ㄗㆤ˫ ㄐㄧㄚˋ ㄍㄠ ㄚ ㄅㄨㆵ˙ ㄒㄧ˫ ㆤ˪ ㄅㄨㄧ˫/ㄗㆤ˫ ㄐㄧㄚˋ ㄍㄠ ㄚ ㄅㄨㆵ˙ ㄒㄧ˪ ㆤ˪ ㄅㄨㄧ˫"], "Zhuyin"),
        (["bio3 ang7 a2","ang7 boo1 a2","ba2 iu2 a2","hue7 ta2 a2","bi7 bi7 a2/bi3 bi3 a2","ban3 ban3 a2","bue1 ia3 a2/be1 ia3 a2","ti3 chu2 a1 ting1 gua1 咧 kiann5","thoo7 kha7 ching7 khi3 ah0/thoo3 kha7 ching7 khi3 ah0","guan1 ti3 chu2 gua3 lang1 kang1 tai7 gi2/guan1 ti3 chu2 gua3 lang1 kang1 tai3 gu2","ti3 kong7 hng7 lai3 khun3/ti3 kong7 hng3 lai3 khun3","cia7 iu1 ⾞ e3 bo5","ce7 cia2 kau1 a1 put8 si7 e3 pui7/ce7 cia2 kau1 a1 put8 si3 e3 pui7"], "TLPA"),
        (["bbiòângǎ","ângbboōǎ","bbǎyǔǎ","huêdǎǎ","bbîbbîǎ/bbìbbìǎ","bbànbbànǎ","bbuēyàǎ/bbēyàǎ","dì cǔ ā dīng gguā 咧 giná","toô kâ cîngkì ah/toò kâ cîngkì ah","gguān dì cǔ gguà lāng gāngdâi ggǐ/gguān dì cǔ gguà lāng gāngdài ggǔ","dì gônghn̂g lài kùn/dì gônghǹg lài kùn","ziâ yū ⾞ è bbó","zê ziǎ gāoā bútsî è buî/zê ziǎ gāoā bútsì è buî"], "Pingyim"),
        (["bhiôr-āng-à","āng-bhor-à","bhà-iù-à","huē-dà-à","bhī-bhī-à/bhî-bhî-à","bhân-bhân-à","bhue-iâ-à/bhe-iâ-à","dî cù a ding ghua 咧 giănn","tōr kā cīng-kî--åh/tôr kā cīng-kî--åh","ghuan dî cù ghuâ lang gang-dāi ghì/ghuan dî cù ghuâ lang gang-dâi ghù","dî gōng-hn̄g lâi kûn/dî gōng-hn̂g lâi kûn","ziā iu ⾞ ê bhŏr","zē zià gau-a but-sī ê buī/zē zià gau-a but-sî ê buī"], "Tongiong"),
        (["biə¹¹ aŋ²² a⁵³/bio²¹ aŋ³³ a⁵¹","aŋ²² bɔ⁴⁴ a⁵³/aŋ³³ bɔ⁵⁵ a⁵¹","ba⁵³ iu⁵³ a⁵³/ba⁵¹ iu⁵¹ a⁵¹","hue²² ta⁵³ a⁵³/hue³³ ta⁵¹ a⁵¹","bi²² bi²² a⁵³/bi²¹ bi²¹ a⁵¹","ban¹¹ ban¹¹ a⁵³/ban²¹ ban²¹ a⁵¹","bue⁴⁴ ia¹¹ a⁵³/be⁵⁵ ia²¹ a⁵¹","ti¹¹ tsʰu⁵³ a⁴⁴ tiɪŋ⁴⁴ gua⁴⁴ 咧 kiã²⁵/ti²¹ tsʰu⁵¹ a⁵⁵ tiɪŋ⁵⁵ gua⁵⁵ 咧 kiã²⁴","tʰɔ²² kʰa²² tɕʰiɪŋ²² kʰi¹¹ a/tʰɔ²¹ kʰa³³ tɕʰiɪŋ³³ kʰi²¹ a","guan⁴⁴ ti¹¹ tsʰu⁵³ gua¹¹ laŋ⁴⁴ kaŋ⁴⁴ tai²² gi⁵³/guan⁵⁵ ti²¹ tsʰu⁵¹ gua²¹ laŋ⁵⁵ kaŋ⁵⁵ tai²¹ gu⁵¹","ti¹¹ kɔŋ²² hŋ̍²² lai¹¹ kʰun¹¹/ti²¹ kɔŋ³³ hŋ̍²¹ lai²¹ kʰun²¹","tɕia²² iu⁴⁴ ⾞ e¹¹ bə²⁵/tɕia³³ iu⁵⁵ ⾞ e²¹ bo²⁴","tse²² tɕia⁵³ kau⁴⁴ a⁴⁴ put̚⁵ ɕi²² e¹¹ pui²²/tse³³ tɕia⁵¹ kau⁵⁵ a⁵⁵ put̚⁴ ɕi²¹ e²¹ pui³³"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_a, transl)]
        checker(data, Converter(system=system, punctuation='none', sandhi='exc_last'), Converter(system=system, dialect="north", punctuation='none', sandhi='exc_last'))

def test_add_incl_last():
    test_data = [
        (["biò-āng-a","āng-boo-a","bá-iú-a","huē-tá-a","bī-bī-a/bì-bì-a","bàn-bàn-a","bue-ià-a/be-ià-a","tì tshú a ting gua 咧 kiānn/tì tshú a ting gua 咧 kiànn","thōo khā tshīng-khì--ah/thòo khā tshīng-khì--ah","guan tì tshú guà lang kang-tāi gi/guan tì tshú guà lang kang-tài gu","tì kōng-hn̄g lài khún/tì kōng-hǹg lài khún","tsiā iu ⾞ è bō/tsiā iu ⾞ è bò","tsē tsiá kau-a pu̍t-sī è puì/tsē tsiá kau-a pu̍t-sì è puì"], "Tailo"),
        (["biò-āng-a","āng-bo͘-a","bá-iú-a","hōe-tá-a","bī-bī-a/bì-bì-a","bàn-bàn-a","boe-ià-a/be-ià-a","tì chhú a teng goa 咧 kiāⁿ/tì chhú a teng goa 咧 kiàⁿ","thō͘ khā chhēng-khì--ah/thò͘ khā chhēng-khì--ah","goan tì chhú gòa lang kang-tāi gi/goan tì chhú gòa lang kang-tài gu","tì kōng-hn̄g lài khún/tì kōng-hǹg lài khún","chiā iu ⾞ è bō/chiā iu ⾞ è bò","chē chiá kau-a pu̍t-sī è pùi/chē chiá kau-a pu̍t-sì è pùi"], "POJ"),
        (["ㆠㄧㄜ˪ ㄤ˫ ㄚ","ㄤ˫ ㆠㆦ ㄚ","ㆠㄚˋ ㄧㄨˋ ㄚ","ㄏㄨㆤ˫ ㄉㄚˋ ㄚ","ㆠㄧ˫ ㆠㄧ˫ ㄚ/ㆠㄧ˪ ㆠㄧ˪ ㄚ","ㆠㄢ˪ ㆠㄢ˪ ㄚ","ㆠㄨㆤ ㄧㄚ˪ ㄚ/ㆠㆤ ㄧㄚ˪ ㄚ","ㄉㄧ˪ ㄘㄨˋ ㄚ ㄉㄧㄥ ㆣㄨㄚ 咧 ㄍㄧㆩ˫/ㄉㄧ˪ ㄘㄨˋ ㄚ ㄉㄧㄥ ㆣㄨㄚ 咧 ㄍㄧㆩ˪","ㄊㆦ˫ ㄎㄚ˫ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ/ㄊㆦ˪ ㄎㄚ˫ ㄑㄧㄥ˫ ㄎㄧ˪ ㄚ","ㆣㄨㄢ ㄉㄧ˪ ㄘㄨˋ ㆣㄨㄚ˪ ㄌㄤ ㄍㄤ ㄉㄞ˫ ㆣㄧ/ㆣㄨㄢ ㄉㄧ˪ ㄘㄨˋ ㆣㄨㄚ˪ ㄌㄤ ㄍㄤ ㄉㄞ˪ ㆣㄨ","ㄉㄧ˪ ㄍㆲ˫ ㄏㆭ˫ ㄌㄞ˪ ㄎㄨㄣˋ/ㄉㄧ˪ ㄍㆲ˫ ㄏㆭ˪ ㄌㄞ˪ ㄎㄨㄣˋ","ㄐㄧㄚ˫ ㄧㄨ ⾞ ㆤ˪ ㆠㄜ˫/ㄐㄧㄚ˫ ㄧㄨ ⾞ ㆤ˪ ㆠㄜ˪","ㄗㆤ˫ ㄐㄧㄚˋ ㄍㄠ ㄚ ㄅㄨㆵ˙ ㄒㄧ˫ ㆤ˪ ㄅㄨㄧ˪/ㄗㆤ˫ ㄐㄧㄚˋ ㄍㄠ ㄚ ㄅㄨㆵ˙ ㄒㄧ˪ ㆤ˪ ㄅㄨㄧ˪"], "Zhuyin"),
        (["bio3 ang7 a1","ang7 boo1 a1","ba2 iu2 a1","hue7 ta2 a1","bi7 bi7 a1/bi3 bi3 a1","ban3 ban3 a1","bue1 ia3 a1/be1 ia3 a1","ti3 chu2 a1 ting1 gua1 咧 kiann7/ti3 chu2 a1 ting1 gua1 咧 kiann3","thoo7 kha7 ching7 khi3 ah0/thoo3 kha7 ching7 khi3 ah0","guan1 ti3 chu2 gua3 lang1 kang1 tai7 gi1/guan1 ti3 chu2 gua3 lang1 kang1 tai3 gu1","ti3 kong7 hng7 lai3 khun2/ti3 kong7 hng3 lai3 khun2","cia7 iu1 ⾞ e3 bo7/cia7 iu1 ⾞ e3 bo3","ce7 cia2 kau1 a1 put8 si7 e3 pui3/ce7 cia2 kau1 a1 put8 si3 e3 pui3"], "TLPA"),
        (["bbiòângā","ângbboōā","bbǎyǔā","huêdǎā","bbîbbîā/bbìbbìā","bbànbbànā","bbuēyàā/bbēyàā","dì cǔ ā dīng gguā 咧 ginâ/dì cǔ ā dīng gguā 咧 ginà","toô kâ cîngkì ah/toò kâ cîngkì ah","gguān dì cǔ gguà lāng gāngdâi ggī/gguān dì cǔ gguà lāng gāngdài ggū","dì gônghn̂g lài kǔn/dì gônghǹg lài kǔn","ziâ yū ⾞ è bbô/ziâ yū ⾞ è bbò","zê ziǎ gāoā bútsî è buì/zê ziǎ gāoā bútsì è buì"], "Pingyim"),
        (["bhiôr-āng-a","āng-bhor-a","bhà-iù-a","huē-dà-a","bhī-bhī-a/bhî-bhî-a","bhân-bhân-a","bhue-iâ-a/bhe-iâ-a","dî cù a ding ghua 咧 giānn/dî cù a ding ghua 咧 giânn","tōr kā cīng-kî--åh/tôr kā cīng-kî--åh","ghuan dî cù ghuâ lang gang-dāi ghi/ghuan dî cù ghuâ lang gang-dâi ghu","dî gōng-hn̄g lâi kùn/dî gōng-hn̂g lâi kùn","ziā iu ⾞ ê bhōr/ziā iu ⾞ ê bhôr","zē zià gau-a but-sī ê buî/zē zià gau-a but-sî ê buî"], "Tongiong"),
        (["biə¹¹ aŋ²² a⁴⁴/bio²¹ aŋ³³ a⁵⁵","aŋ²² bɔ⁴⁴ a⁴⁴/aŋ³³ bɔ⁵⁵ a⁵⁵","ba⁵³ iu⁵³ a⁴⁴/ba⁵¹ iu⁵¹ a⁵⁵","hue²² ta⁵³ a⁴⁴/hue³³ ta⁵¹ a⁵⁵","bi²² bi²² a⁴⁴/bi²¹ bi²¹ a⁵⁵","ban¹¹ ban¹¹ a⁴⁴/ban²¹ ban²¹ a⁵⁵","bue⁴⁴ ia¹¹ a⁴⁴/be⁵⁵ ia²¹ a⁵⁵","ti¹¹ tsʰu⁵³ a⁴⁴ tiɪŋ⁴⁴ gua⁴⁴ 咧 kiã²²/ti²¹ tsʰu⁵¹ a⁵⁵ tiɪŋ⁵⁵ gua⁵⁵ 咧 kiã²¹","tʰɔ²² kʰa²² tɕʰiɪŋ²² kʰi¹¹ a/tʰɔ²¹ kʰa³³ tɕʰiɪŋ³³ kʰi²¹ a","guan⁴⁴ ti¹¹ tsʰu⁵³ gua¹¹ laŋ⁴⁴ kaŋ⁴⁴ tai²² gi⁴⁴/guan⁵⁵ ti²¹ tsʰu⁵¹ gua²¹ laŋ⁵⁵ kaŋ⁵⁵ tai²¹ gu⁵⁵","ti¹¹ kɔŋ²² hŋ̍²² lai¹¹ kʰun⁵³/ti²¹ kɔŋ³³ hŋ̍²¹ lai²¹ kʰun⁵¹","tɕia²² iu⁴⁴ ⾞ e¹¹ bə²²/tɕia³³ iu⁵⁵ ⾞ e²¹ bo²¹","tse²² tɕia⁵³ kau⁴⁴ a⁴⁴ put̚⁵ ɕi²² e¹¹ pui¹¹/tse³³ tɕia⁵¹ kau⁵⁵ a⁵⁵ put̚⁴ ɕi²¹ e²¹ pui²¹"], "IPA")
    ]
    for transl, system in test_data:
        data = [f"{h},{t}" for h, t in zip(hanji_a, transl)]
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