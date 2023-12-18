from taibun.taibun import Converter
from utils import checker

def test_default():
	tailo = ["開始,khai-sí","巧氣,khá-khì","寄回,kià-huê/kià-hê","肉包,bah-pau","翕甌,hip-au","彼號,hit-hō","確信,khak-sìn","南面,lâm-bīn","未來,bī-lâi","篾蓆,bi̍h-tshio̍h","業務,gia̍p-bū","罰金,hua̍t-kim","學生,ha̍k-sing"]
	poj = ["開始,khai-sí","巧氣,khá-khì","寄回,kià-hôe/kià-hê","肉包,bah-pau","翕甌,hip-au","彼號,hit-hō","確信,khak-sìn","南面,lâm-bīn","未來,bī-lâi","篾蓆,bi̍h-chhio̍h","業務,gia̍p-bū","罰金,hoa̍t-kim","學生,ha̍k-seng"]
	zhuyin = ["開始,ㄎㄞ ㄒㄧˋ","巧氣,ㄎㄚˋ ㄎㄧ˪","寄回,ㄍㄧㄚ˪ ㄏㄨㆤˊ/ㄍㄧㄚ˪ ㄏㆤˊ","肉包,ㆠㄚㆷ ㄅㄠ","翕甌,ㄏㄧㆴ ㄠ","彼號,ㄏㄧㆵ ㄏㄜ˫","確信,ㄎㄚㆶ ㄒㄧㄣ˪","南面,ㄌㆰˊ ㆠㄧㄣ˫","未來,ㆠㄧ˫ ㄌㄞˊ","篾蓆,ㆠㄧㆷ˙ ㄑㄧㄜㆷ˙","業務,ㆣㄧㄚㆴ˙ ㆠㄨ˫","罰金,ㄏㄨㄚㆵ˙ ㄍㄧㆬ","學生,ㄏㄚㆶ˙ ㄒㄧㄥ"]
	tlpa = ["開始,khai1 si2","巧氣,kha2 khi3","寄回,kia3 hue5/kia3 he5","肉包,bah4 pau1","翕甌,hip4 au1","彼號,hit4 ho7","確信,khak4 sin3","南面,lam5 bin7","未來,bi7 lai5","篾蓆,bih8 chioh8","業務,giap8 bu7","罰金,huat8 kim1","學生,hak8 sing1"]
	pingyim = ["開始,kāisǐ","巧氣,kǎkì","寄回,giàhué/giàhé","肉包,bbāhbāo","翕甌,hīpāo","彼號,hīthô","確信,kāksìn","南面,lámbbîn","未來,bbîlái","篾蓆,bbíhcióh","業務,ggiápbbû","罰金,huátgīm","學生,háksīng"]
	tongiong = ["開始,kāi-sì","巧氣,ka-kî","寄回,già-huĕ/già-hĕ","肉包,bhà-bau","翕甌,hip-au","彼號,hit-hōr","確信,kak-sîn","南面,lām-bhīn/lâm-bhīn","未來,bhî-lăi","篾蓆,bhî-cioh","業務,ghiāp-bhū","罰金,huāt-gim","學生,hāk-sing"]

	checker(tailo, Converter(system="Tailo", punctuation='none'), Converter(system="Tailo", dialect="north", punctuation='none'))
	checker(poj, Converter(system="POJ", punctuation='none'), Converter(system="POJ", dialect="north", punctuation='none'))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none'), Converter(system="Zhuyin", dialect="north", punctuation='none'))
	checker(tlpa, Converter(system="TLPA", punctuation='none'), Converter(system="TLPA", dialect="north", punctuation='none'))
	checker(pingyim, Converter(system="Pingyim", punctuation='none'), Converter(system="Pingyim", dialect="north", punctuation='none'))
	checker(tongiong, Converter(system="Tongiong", punctuation='none'), Converter(system="Tongiong", dialect="north", punctuation='none'))

def test_true():
	tailo = ["開始,khāi-sí","巧氣,kha-khì","寄回,kiá-huê/kiá-hê","肉包,bá-pau","翕甌,hi̍p-au","彼號,hi̍t-hō","確信,kha̍k-sìn","南面,lām-bīn/làm-bīn","未來,bì-lâi","篾蓆,bì-tshio̍h","業務,giap-bū","罰金,huat-kim","學生,hak-sing"]
	poj = ["開始,khāi-sí","巧氣,kha-khì","寄回,kiá-hôe/kiá-hê","肉包,bá-pau","翕甌,hi̍p-au","彼號,hi̍t-hō","確信,kha̍k-sìn","南面,lām-bīn/làm-bīn","未來,bì-lâi","篾蓆,bì-chhio̍h","業務,giap-bū","罰金,hoat-kim","學生,hak-seng"]
	zhuyin = ["開始,ㄎㄞ˫ ㄒㄧˋ","巧氣,ㄎㄚ ㄎㄧ˪","寄回,ㄍㄧㄚˋ ㄏㄨㆤˊ/ㄍㄧㄚˋ ㄏㆤˊ","肉包,ㆠㄚˋ ㄅㄠ","翕甌,ㄏㄧㆴ˙ ㄠ","彼號,ㄏㄧㆵ˙ ㄏㄜ˫","確信,ㄎㄚㆶ˙ ㄒㄧㄣ˪","南面,ㄌㆰ˫ ㆠㄧㄣ˫/ㄌㆰ˪ ㆠㄧㄣ˫","未來,ㆠㄧ˪ ㄌㄞˊ","篾蓆,ㆠㄧ˪ ㄑㄧㄜㆷ˙","業務,ㆣㄧㄚㆴ ㆠㄨ˫","罰金,ㄏㄨㄚㆵ ㄍㄧㆬ","學生,ㄏㄚㆶ ㄒㄧㄥ"]
	tlpa = ["開始,khai7 si2","巧氣,kha1 khi3","寄回,kia2 hue5/kia2 he5","肉包,ba2 pau1","翕甌,hip8 au1","彼號,hit8 ho7","確信,khak8 sin3","南面,lam7 bin7/lam3 bin7","未來,bi3 lai5","篾蓆,bi3 chioh8","業務,giap4 bu7","罰金,huat4 kim1","學生,hak4 sing1"]
	pingyim = ["開始,kâisǐ","巧氣,kākì","寄回,giǎhué/giǎhé","肉包,bbǎbāo","翕甌,hípāo","彼號,híthô","確信,káksìn","南面,lâmbbîn/làmbbîn","未來,bbìlái","篾蓆,bbìcióh","業務,ggiāpbbû","罰金,huātgīm","學生,hāksīng"]
	tongiong = ["開始,kāi-sì","巧氣,ka-kî","寄回,già-huĕ/già-hĕ","肉包,bhà-bau","翕甌,hip-au","彼號,hit-hōr","確信,kak-sîn","南面,lām-bhīn/lâm-bhīn","未來,bhî-lăi","篾蓆,bhî-cioh","業務,ghiāp-bhū","罰金,huāt-gim","學生,hāk-sing"]

	checker(tailo, Converter(system="Tailo", punctuation='none', sandhi=True), Converter(system="Tailo", dialect="north", punctuation='none', sandhi=True))
	checker(poj, Converter(system="POJ", punctuation='none', sandhi=True), Converter(system="POJ", dialect="north", punctuation='none', sandhi=True))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none', sandhi=True), Converter(system="Zhuyin", dialect="north", punctuation='none', sandhi=True))
	checker(tlpa, Converter(system="TLPA", punctuation='none', sandhi=True), Converter(system="TLPA", dialect="north", punctuation='none', sandhi=True))
	checker(pingyim, Converter(system="Pingyim", punctuation='none', sandhi=True), Converter(system="Pingyim", dialect="north", punctuation='none', sandhi=True))
	checker(tongiong, Converter(system="Tongiong", punctuation='none', sandhi=True), Converter(system="Tongiong", dialect="north", punctuation='none', sandhi=True))

def test_false():
	tailo = ["開始,khai-sí","巧氣,khá-khì","寄回,kià-huê/kià-hê","肉包,bah-pau","翕甌,hip-au","彼號,hit-hō","確信,khak-sìn","南面,lâm-bīn","未來,bī-lâi","篾蓆,bi̍h-tshio̍h","業務,gia̍p-bū","罰金,hua̍t-kim","學生,ha̍k-sing"]
	poj = ["開始,khai-sí","巧氣,khá-khì","寄回,kià-hôe/kià-hê","肉包,bah-pau","翕甌,hip-au","彼號,hit-hō","確信,khak-sìn","南面,lâm-bīn","未來,bī-lâi","篾蓆,bi̍h-chhio̍h","業務,gia̍p-bū","罰金,hoa̍t-kim","學生,ha̍k-seng"]
	zhuyin = ["開始,ㄎㄞ ㄒㄧˋ","巧氣,ㄎㄚˋ ㄎㄧ˪","寄回,ㄍㄧㄚ˪ ㄏㄨㆤˊ/ㄍㄧㄚ˪ ㄏㆤˊ","肉包,ㆠㄚㆷ ㄅㄠ","翕甌,ㄏㄧㆴ ㄠ","彼號,ㄏㄧㆵ ㄏㄜ˫","確信,ㄎㄚㆶ ㄒㄧㄣ˪","南面,ㄌㆰˊ ㆠㄧㄣ˫","未來,ㆠㄧ˫ ㄌㄞˊ","篾蓆,ㆠㄧㆷ˙ ㄑㄧㄜㆷ˙","業務,ㆣㄧㄚㆴ˙ ㆠㄨ˫","罰金,ㄏㄨㄚㆵ˙ ㄍㄧㆬ","學生,ㄏㄚㆶ˙ ㄒㄧㄥ"]
	tlpa = ["開始,khai1 si2","巧氣,kha2 khi3","寄回,kia3 hue5/kia3 he5","肉包,bah4 pau1","翕甌,hip4 au1","彼號,hit4 ho7","確信,khak4 sin3","南面,lam5 bin7","未來,bi7 lai5","篾蓆,bih8 chioh8","業務,giap8 bu7","罰金,huat8 kim1","學生,hak8 sing1"]
	pingyim = ["開始,kāisǐ","巧氣,kǎkì","寄回,giàhué/giàhé","肉包,bbāhbāo","翕甌,hīpāo","彼號,hīthô","確信,kāksìn","南面,lámbbîn","未來,bbîlái","篾蓆,bbíhcióh","業務,ggiápbbû","罰金,huátgīm","學生,háksīng"]
	tongiong = ["開始,kai-sì","巧氣,kà-kî","寄回,giâ-huĕ/giâ-hĕ","肉包,bhāh-bau","翕甌,hīp-au","彼號,hīt-hōr","確信,kāk-sîn","南面,lăm-bhīn","未來,bhī-lăi","篾蓆,bhih-cioh","業務,ghiap-bhū","罰金,huat-gim","學生,hak-sing"]

	checker(tailo, Converter(system="Tailo", punctuation='none', sandhi=False), Converter(system="Tailo", dialect="north", punctuation='none', sandhi=False))
	checker(poj, Converter(system="POJ", punctuation='none', sandhi=False), Converter(system="POJ", dialect="north", punctuation='none', sandhi=False))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none', sandhi=False), Converter(system="Zhuyin", dialect="north", punctuation='none', sandhi=False))
	checker(tlpa, Converter(system="TLPA", punctuation='none', sandhi=False), Converter(system="TLPA", dialect="north", punctuation='none', sandhi=False))
	checker(pingyim, Converter(system="Pingyim", punctuation='none', sandhi=False), Converter(system="Pingyim", dialect="north", punctuation='none', sandhi=False))
	checker(tongiong, Converter(system="Tongiong", punctuation='none', sandhi=False), Converter(system="Tongiong", dialect="north", punctuation='none', sandhi=False))

def test_sentence():
	tailo = ["太空朋友，恁好！恁食飽未？,Thái-khōng pīng-iú, lin-hó! Lin tsià-pa buē?/Thái-khōng pìng-iú, lin-hó! Lin tsià-pa bē?"]
	poj = ["太空朋友，恁好！恁食飽未？,Thái-khōng pēng-iú, lin-hó! Lin chià-pa bōe?/Thái-khōng pèng-iú, lin-hó! Lin chià-pa bē?"]
	zhuyin = ["太空朋友，恁好！恁食飽未？,ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˫ ㄧㄨˋ, ㄌㄧㄣ ㄏㄜˋ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㄨㆤ˫?/ㄊㄞˋ ㄎㆲ˫ ㄅㄧㄥ˪ ㄧㄨˋ, ㄌㄧㄣ ㄏㄜˋ! ㄌㄧㄣ ㄐㄧㄚ˪ ㄅㄚ ㆠㆤ˫?"]
	tlpa = ["太空朋友，恁好！恁食飽未？,Thai2 khong7 ping7 iu2, lin1 ho2! Lin1 cia3 pa1 bue7?/Thai2 khong7 ping3 iu2, lin1 ho2! Lin1 cia3 pa1 be7?"]
	pingyim = ["太空朋友，恁好！恁食飽未？,Tǎikông bîngyǔ, līnhǒ! Līn ziàbā bbuê?/Tǎikông bìngyǔ, līnhǒ! Līn ziàbā bbê?"]
	tongiong = ["太空朋友，恁好！恁食飽未？,Tài-kōng bīng-iù, lin-hòr! Lin ziâ-ba bhuē?/Tài-kōng bîng-iù, lin-hòr! Lin ziâ-ba bhē?"]

	checker(tailo, Converter(system="Tailo", sandhi=True), Converter(system="Tailo", dialect="north", sandhi=True))
	checker(poj, Converter(system="POJ", sandhi=True), Converter(system="POJ", dialect="north", sandhi=True))
	checker(zhuyin, Converter(system="Zhuyin", sandhi=True), Converter(system="Zhuyin", dialect="north", sandhi=True))
	checker(tlpa, Converter(system="TLPA", sandhi=True), Converter(system="TLPA", dialect="north", sandhi=True))
	checker(pingyim, Converter(system="Pingyim", sandhi=True), Converter(system="Pingyim", dialect="north", sandhi=True))
	checker(tongiong, Converter(system="Tongiong", sandhi=True), Converter(system="Tongiong", dialect="north", sandhi=True))