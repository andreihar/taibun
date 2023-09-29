from taibun.taibun import Converter
from utils import checker

def test_format():
	tailo = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,Tse sī Tâi-lâm, kán-tshing "lâm" (Pe̍h-uē-jī: Tâi-lâm; tsù-im hû-hō: ㄊㄞˊ ㄋㄢˊ, kok-gí: Táinán). 1623 nî, Hô-lân tī Tâi-lâm kīn-hái tiong ê an-pîng khí-ki tē. 1624 nî, Hô-lân thè tshut Phênn-ôo liáu-āu, tuì-tsia ê khai-huat, kiàn-siat liáu Jia̍t-lân-jia-siânn (Fort Zeelandia)./Tse sī Tâi-lâm, kán-tshing "lâm" (Pe̍h-uē-lī: Tâi-lâm; tsù-im hû-hō: ㄊㄞˊ ㄋㄢˊ, kok-gú: Táinán). 1623 nî, Hô-lân tī Tâi-lâm kūn-hái tiong ê an-pîng khí-ki tuē. 1624 nî, Hô-lân thè tshut Phênn-ôo liáu-āu, tuì-tsia ê khai-huat, kiàn-siat liáu Lia̍t-lân-lia-siânn (Fort Zeelandia).']
	poj = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,Che sī Tâi-lâm, kán-chheng "lâm" (Pe̍h-ōe-jī: Tâi-lâm; chù-im hû-hō: ㄊㄞˊ ㄋㄢˊ, kok-gí: Táinán). 1623 nî, Hô-lân tī Tâi-lâm kīn-hái tiong ê an-pêng khí-ki tē. 1624 nî, Hô-lân thè chhut Phêⁿ-ô͘ liáu-āu, tùi-chia ê khai-hoat, kiàn-siat liáu Jia̍t-lân-jia-siâⁿ (Fort Zeelandia)./Che sī Tâi-lâm, kán-chheng "lâm" (Pe̍h-ōe-lī: Tâi-lâm; chù-im hû-hō: ㄊㄞˊ ㄋㄢˊ, kok-gú: Táinán). 1623 nî, Hô-lân tī Tâi-lâm kūn-hái tiong ê an-pêng khí-ki tōe. 1624 nî, Hô-lân thè chhut Phêⁿ-ô͘ liáu-āu, tùi-chia ê khai-hoat, kiàn-siat liáu Lia̍t-lân-lia-siâⁿ (Fort Zeelandia).']
	zhuyin = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,ㄗㆤ ㄒㄧ˫ ㄉㄞˊ ㄌㆰˊ, ㄍㄢˋ ㄑㄧㄥ "ㄌㆰˊ" (ㄅㆤㆷ˙ ㄨㆤ˫ ㆢㄧ˫: Tâi-lâm; ㄗㄨ˪ ㄧㆬ ㄏㄨˊ ㄏㄜ˫: ㄊㄞˊ ㄋㄢˊ, ㄍㆦㆶ ㆣㄧˋ: Táinán). 1623 ㄋ ㄧˊ, ㄏㄜˊ ㄌㄢˊ ㄉㄧ˫ ㄉㄞˊ ㄌㆰˊ ㄍㄧㄣ˫ ㄏㄞˋ ㄉㄧㆲ ㆤˊ ㄢ ㄅㄧㄥˊ ㄎㄧˋ ㄍㄧ ㄉㆤ˫. 1624 ㄋㄧˊ, ㄏㄜˊ ㄌㄢˊ ㄊㆤ˪ ㄘㄨㆵ ㄆㆥˊ ㆦˊ ㄌㄧㄠˋ ㄠ˫, ㄉㄨㄧ˪ ㄐㄧㄚ ㆤˊ ㄎㄞ ㄏㄨㄚㆵ, ㄍㄧㄢ˪ ㄒㄧㄚㆵ ㄌㄧㄠˋ ㆢㄧㄚㆵ˙ ㄌㄢˊ ㆢㄧㄚ ㄒㄧㆩˊ (Fort Zeelandia)./ㄗㆤ ㄒㄧ˫ ㄉㄞˊ ㄌㆰˊ, ㄍㄢˋ ㄑㄧㄥ "ㄌㆰˊ" (ㄅㆤㆷ˙ ㄨㆤ˫ ㄌㄧ˫: Tâi-lâm;  ㄗㄨ˪ ㄧㆬ ㄏㄨˊ ㄏㄜ˫: ㄊㄞˊ ㄋㄢˊ, ㄍㆦㆶ ㆣㄨˋ: Táinán). 1623 ㄋㄧˊ, ㄏㄜˊ ㄌㄢˊ ㄉㄧ˫ ㄉㄞˊ ㄌㆰˊ ㄍㄨㄣ˫ ㄏㄞˋ ㄉㄧㆲ ㆤˊ ㄢ ㄅㄧㄥˊ ㄎㄧˋ ㄍㄧ ㄉㄨㆤ˫. 1624 ㄋㄧˊ, ㄏㄜˊ ㄌㄢˊ ㄊㆤ˪ ㄘㄨㆵ ㄆㆥˊ ㆦˊ ㄌㄧㄠˋ ㄠ˫, ㄉㄨㄧ˪ ㄐㄧㄚ ㆤˊ ㄎㄞ ㄏㄨㄚㆵ, ㄍㄧㄢ˪ ㄒㄧㄚㆵ ㄌㄧㄠˋ ㄌㄧㄚㆵ˙ ㄌㄢˊ ㄌㄧㄚ ㄒㄧㆩˊ (Fort Zeelandia).']
	tlpa = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,Ce1 si7 Tai5 lam5, kan2 ching1 "lam5" (Peh8 ue7 ji7: Tâi-lâm; cu3 im1 hu5 ho7: ㄊㄞˊ ㄋㄢˊ, kok4 gi2: Táinán). 1623 ni5, Ho5 lan5 ti7 Tai5 lam5 kin7 hai2 tiong1 e5 an1 ping5 khi2 ki1 te7. 1624 ni5, Ho5 lan5 the3 chut4 Phenn5 oo5 liau2 au7, tui3 cia1 e5 khai1 huat4, kian3 siat4 liau2 Jiat8 lan5 jia1 siann5 (Fort Zeelandia)./Ce1 si7 Tai5 lam5, kan2 ching1 "lam5" (Peh8 ue7 li7: Tâi-lâm; cu3 im1 hu5 ho7: ㄊㄞˊ ㄋㄢˊ, kok4 gu2: Táinán). 1623 ni5, Ho5 lan5 ti7 Tai5 lam5 kun7 hai2 tiong1 e5 an1 ping5 khi2 ki1 tue7. 1624 ni5, Ho5 lan5 the3 chut4 Phenn5 oo5 liau2 au7, tui3 cia1 e5 khai1 huat4, kian3 siat4 liau2 Liat8 lan5 lia1 siann5 (Fort Zeelandia).']
	pingyim = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,Zē sî Dáilám, gǎncīng "lám" (Béhwêzzî: Tâi-lâm; zùyīm húhô: ㄊㄞˊ ㄋㄢˊ, gōkggǐ: Táinán). 1623 lní, Hólán dî Dáilám gînhǎi diōng é ānbíng kǐgī dê. 1624 lní, Hólán tè cūt Pnéoó liǎoâo, duìziā é kāihuāt, giànsiāt liǎo Zziátlánzziāsiná (Fort Zeelandia)./Zē sî Dáilám, gǎncīng "lám" (Béhwêlî: Tâi-lâm; zùyīm húhô:  ㄊㄞˊ ㄋㄢˊ, gōkggǔ: Táinán). 1623 lní, Hólán dî Dáilám gûnhǎi diōng é ānbíng kǐgī duê. 1624 lní, Hólán tè cūt Pnéoó liǎoâo, duìziā é kāihuāt, giànsiāt liǎo Liátlánliāsiná (Fort Zeelandia).']
	tongiong = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,Ze sī Dāi-lăm, gan-cing "lăm" (Bê-uê-rī: Tâi-lâm; zù-im hū-hōr: ㄊㄞˊ ㄋㄢˊ, gok-ghì: Táinán). 1623 nĭ, Hōr-lăn dī Dāi-lăm gîn-hài diong ĕ ān-bĭng ki-gi dē. 1624 nĭ, Hōr-lăn tê cūt Pēnn-ŏr liau-āu, duì-zia ĕ kāi-huāt, giàn-siāt liàu Riāt-lān-riā-siănn (Fort Zeelandia)./Ze sī Dâi-lăm, gan-cing "lăm" (Bê-uê-lī: Tâi-lâm; zù-im hû-hōr: ㄊㄞˊ ㄋㄢˊ, gok-ghù: Táinán). 1623 nĭ, Hôr-lăn dī Dâi-lăm gûn-hài diong ĕ ān-bĭng ki-gi duē. 1624 nĭ, Hôr-lăn tê cūt Pênn-ŏr liau-āu, duì-zia ĕ kāi-huāt, giàn-siāt liàu Liāt-lân-liā-siănn (Fort Zeelandia).']
	
	checker(tailo, Converter(system="Tailo", punctuation='format'), Converter(system="Tailo", dialect="north", punctuation='format'))
	checker(poj, Converter(system="POJ", punctuation='format'), Converter(system="POJ", dialect="north", punctuation='format'))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='format'), Converter(system="Zhuyin", dialect="north", punctuation='format'))
	checker(tlpa, Converter(system="TLPA", punctuation='format'), Converter(system="TLPA", dialect="north", punctuation='format'))
	checker(pingyim, Converter(system="Pingyim", punctuation='format'), Converter(system="Pingyim", dialect="north", punctuation='format'))
	checker(tongiong, Converter(system="Tongiong", punctuation='format'), Converter(system="Tongiong", dialect="north", punctuation='format'))

def test_none():
	tailo = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,tse sī Tâi-lâm，kán-tshing「lâm」（Pe̍h-uē-jī：Tâi-lâm；tsù-im hû-hō：ㄊㄞˊ ㄋㄢˊ，kok-gí：Táinán）。1623 nî，Hô-lân tī Tâi-lâm kīn-hái tiong ê an-pîng khí-ki tē。1624 nî，Hô-lân thè tshut Phênn-ôo liáu-āu，tuì-tsia ê khai-huat，kiàn-siat liáu Jia̍t-lân-jia-siânn（Fort Zeelandia）。/tse sī Tâi-lâm，kán-tshing 「lâm」（Pe̍h-uē-lī：Tâi-lâm；tsù-im hû-hō：ㄊㄞˊ ㄋㄢˊ，kok-gú：Táinán）。1623 nî，Hô-lân tī Tâi-lâm kūn-hái tiong ê an-pîng khí-ki tuē。1624 nî，Hô-lân thè tshut Phênn-ôo liáu-āu，tuì-tsia ê khai-huat，kiàn-siat liáu Lia̍t-lân-lia-siânn（Fort Zeelandia）。']
	poj = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,che sī Tâi-lâm，kán-chheng「lâm」（Pe̍h-ōe-jī：Tâi-lâm；chù-im hû-hō：ㄊㄞˊ ㄋㄢˊ，kok-gí：Táinán）。1623 nî，Hô-lân tī Tâi-lâm kīn-hái tiong ê an-pêng khí-ki tē。1624 nî，Hô-lân thè chhut Phêⁿ-ô͘ liáu-āu，tùi-chia ê khai-hoat，kiàn-siat liáu Jia̍t-lân-jia-siâⁿ（Fort Zeelandia）。/che sī Tâi-lâm，kán-chheng「lâm」（Pe̍h-ōe-lī：Tâi-lâm；chù-im hû-hō：ㄊㄞˊ ㄋㄢˊ，kok-gú：Táinán）。1623 nî，Hô-lân tī Tâi-lâm kūn-hái tiong ê an-pêng khí-ki tōe。1624 nî，Hô-lân thè chhut Phêⁿ-ô͘ liáu-āu，tùi-chia ê khai-hoat，kiàn-siat liáu Lia̍t-lân-lia-siâⁿ（Fort Zeelandia）。']
	zhuyin = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,ㄗㆤ ㄒㄧ˫ ㄉㄞˊ ㄌㆰˊ，ㄍㄢˋ ㄑㄧㄥ「ㄌㆰˊ」（ㄅㆤㆷ˙ ㄨㆤ˫ ㆢㄧ˫：Tâi-lâm；ㄗㄨ˪ ㄧㆬ ㄏㄨˊ ㄏㄜ˫：ㄊㄞˊ ㄋㄢˊ，ㄍㆦㆶ ㆣㄧˋ：Táinán）。1623  ㄋㄧˊ，ㄏㄜˊ ㄌㄢˊ ㄉㄧ˫ ㄉㄞˊ ㄌㆰˊ ㄍㄧㄣ˫ ㄏㄞˋ ㄉㄧㆲ ㆤˊ ㄢ ㄅㄧㄥˊ ㄎㄧˋ ㄍㄧ ㄉㆤ˫。1624 ㄋㄧˊ，ㄏㄜˊ ㄌㄢˊ ㄊㆤ˪ ㄘㄨㆵ ㄆㆥˊ ㆦˊ ㄌㄧㄠˋ ㄠ˫，ㄉㄨㄧ˪ ㄐㄧㄚ  ㆤˊ ㄎㄞ ㄏㄨㄚㆵ，ㄍㄧㄢ˪ ㄒㄧㄚㆵ ㄌㄧㄠˋ ㆢㄧㄚㆵ˙ ㄌㄢˊ ㆢㄧㄚ ㄒㄧㆩˊ（Fort Zeelandia）。/ㄗㆤ ㄒㄧ˫ ㄉㄞˊ ㄌㆰˊ，ㄍㄢˋ ㄑㄧㄥ「ㄌㆰˊ」（ㄅㆤㆷ˙ ㄨㆤ˫ ㄌㄧ˫：Tâi-lâm；ㄗㄨ˪ ㄧㆬ ㄏㄨˊ ㄏㄜ˫：ㄊㄞˊ ㄋㄢˊ，ㄍㆦㆶ ㆣㄨˋ：Táinán）。1623 ㄋㄧˊ，ㄏㄜˊ ㄌㄢˊ ㄉㄧ˫ ㄉㄞˊ ㄌㆰˊ ㄍㄨㄣ˫ ㄏㄞˋ ㄉㄧㆲ ㆤˊ ㄢ ㄅㄧㄥˊ ㄎㄧˋ ㄍㄧ ㄉㄨㆤ˫。1624 ㄋㄧˊ，ㄏㄜˊ ㄌㄢˊ ㄊㆤ˪ ㄘㄨㆵ ㄆㆥˊ ㆦˊ ㄌㄧㄠˋ ㄠ˫，ㄉㄨㄧ˪ ㄐㄧㄚ ㆤˊ ㄎㄞ ㄏㄨㄚㆵ，ㄍㄧㄢ˪ ㄒㄧㄚㆵ ㄌㄧㄠˋ ㄌㄧㄚㆵ˙ ㄌㄢˊ ㄌㄧㄚ ㄒㄧㆩˊ（Fort Zeelandia）。']
	tlpa = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,ce1 si7 Tai5 lam5，kan2 ching1「lam5」（Peh8 ue7 ji7：Tâi-lâm；cu3 im1 hu5 ho7：ㄊㄞˊ ㄋㄢˊ，kok4 gi2：Táinán）。1623 ni5，Ho5 lan5 ti7 Tai5 lam5 kin7 hai2 tiong1 e5 an1 ping5 khi2 ki1 te7。1624 ni5，Ho5 lan5 the3 chut4 Phenn5 oo5 liau2 au7，tui3 cia1 e5 khai1 huat4，kian3 siat4 liau2 Jiat8 lan5 jia1 siann5（Fort Zeelandia）。/ce1 si7 Tai5 lam5，kan2 ching1「lam5」（Peh8 ue7 li7：Tâi-lâm；cu3 im1 hu5 ho7：ㄊㄞˊ ㄋㄢˊ，kok4 gu2：Táinán）。1623 ni5，Ho5 lan5 ti7 Tai5 lam5 kun7 hai2 tiong1 e5 an1 ping5 khi2 ki1 tue7。1624 ni5，Ho5 lan5 the3 chut4 Phenn5 oo5 liau2 au7，tui3 cia1 e5 khai1 huat4，kian3 siat4 liau2 Liat8 lan5 lia1 siann5（Fort Zeelandia）。']
	pingyim = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,zē sî Dáilám，gǎncīng「lám」（Béhwêzzî：Tâi-lâm；zùyīm húhô：ㄊㄞˊ ㄋㄢˊ，gōkggǐ：Táinán）。1623 lní，Hólán dî Dáilám gînhǎi diōng é ānbíng kǐgī dê。1624 lní，Hólán tè cūt Pnéoó liǎoâo，duìziā é kāihuāt，giànsiāt liǎo Zziátlánzziāsiná（Fort Zeelandia）。/zē sî Dáilám，gǎncīng「lám」（Béhwêlî：Tâi-lâm；zùyīm húhô：ㄊㄞˊ ㄋㄢˊ，gōkggǔ：Táinán）。1623 lní，Hólán dî Dáilám gûnhǎi diōng é ānbíng kǐgī duê。1624 lní，Hólán tè cūt Pnéoó liǎoâo，duìziā é kāihuāt，giànsiāt liǎo Liátlánliāsiná（Fort Zeelandia）。']
	tongiong = ['這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。1623年，荷蘭佇臺南近海中个安平起基地。1624年，荷蘭退出澎湖了後，對遮个開發，建設了熱蘭遮城（Fort Zeelandia）。,ze sī Dāi-lăm，gan-cing「lăm」（Bê-uê-rī：Tâi-lâm；zù-im hū-hōr：ㄊㄞˊ ㄋㄢˊ，gok-ghì：Táinán）。1623 nĭ，Hōr-lăn dī Dāi-lăm gîn-hài diong ĕ ān-bĭng ki-gi dē。1624 nĭ，Hōr-lăn tê cūt Pēnn-ŏr liau-āu，duì-zia ĕ kāi-huāt，giàn-siāt liàu Riāt-lān-riā-siănn（Fort Zeelandia）。/ze sī Dâi-lăm，gan-cing「lăm」（Bê-uê-lī：Tâi-lâm；zù-im hû-hōr：ㄊㄞˊ ㄋㄢˊ，gok-ghù：Táinán）。1623 nĭ，Hôr-lăn dī Dâi-lăm gûn-hài diong ĕ ān-bĭng ki-gi duē。1624 nĭ，Hôr-lăn tê cūt Pênn-ŏr liau-āu，duì-zia ĕ kāi-huāt，giàn-siāt liàu Liāt-lân-liā-siănn（Fort Zeelandia）。']
	
	checker(tailo, Converter(system="Tailo", punctuation='none'), Converter(system="Tailo", dialect="north", punctuation='none'))
	checker(poj, Converter(system="POJ", punctuation='none'), Converter(system="POJ", dialect="north", punctuation='none'))
	checker(zhuyin, Converter(system="Zhuyin", punctuation='none'), Converter(system="Zhuyin", dialect="north", punctuation='none'))
	checker(tlpa, Converter(system="TLPA", punctuation='none'), Converter(system="TLPA", dialect="north", punctuation='none'))
	checker(pingyim, Converter(system="Pingyim", punctuation='none'), Converter(system="Pingyim", dialect="north", punctuation='none'))
	checker(tongiong, Converter(system="Tongiong", punctuation='none'), Converter(system="Tongiong", dialect="north", punctuation='none'))