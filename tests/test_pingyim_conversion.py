import unittest

from utils import (additional_c, alveolar_c, alveolo_palatal_c, back_c,
                   bilabial_c, central_c, checker, front_c, nasal_c, stop_c,
                   syllabic_c, velar_c)

from taibun.taibun import Converter

c = Converter(system="Pingyim", punctuation='none')
c_north = Converter(system="Pingyim", dialect="north", punctuation='none')

class TestPingyimConversion(unittest.TestCase):

    def test_pingyim_initials(self):
        bilabial = ['bī','pō','bbnoó','bbá']
        checker(self, list(zip(bilabial_c, bilabial)), c, c_north)
        alveolar = ['dê/duê','tò','zǎ','cù','sū','lnâi','zzú/lú','liǔ']
        checker(self, list(zip(alveolar_c, alveolar)), c, c_north)
        alveolo_palatal = ['ziā','ciǔ','siǎ','zzí/lí']
        checker(self, list(zip(alveolo_palatal_c, alveolo_palatal)), c, c_north)
        velar = ['giú','kì','ggnǎ','ggǐ/ggǔ','hǐ']
        checker(self, list(zip(velar_c, velar)), c, c_north)

    def test_pingyim_vowels_and_rhymes(self):
        front = ['yī','ê','yní','né']
        checker(self, list(zip(front_c, front)), c, c_north)
        central = ['ō','ā','nâ']
        checker(self, list(zip(central_c, central)), c, c_north)
        back = ['wǔ','oō','dniū','noō']
        checker(self, list(zip(back_c, back)), c, c_north)

    def test_pingyim_finals(self):
        nasal = ['yīm','yín','áng']
        checker(self, list(zip(nasal_c, nasal)), c, c_north)
        stop = ['yáp','āt','ōk','áh']
        checker(self, list(zip(stop_c, stop)), c, c_north)
        syllabic = ['m̌','ńg']
        checker(self, list(zip(syllabic_c, syllabic)), c, c_north)

    def test_pingyim_y_and_w(self):
        y = ['伊', '因', '音', '英', '乙', '邑', '腋', '枵', '演', '央', '擁', '圓', '營', '喓', '羊']
        y_ground = ["yī","yīn","yīm","yīng","yīt","yīp","yík","yāo","yǎn","yāng","yǒng","yní","yná","ynāo","ynú"]
        checker(self, list(zip(y, y_ground)), c, c_north)
        w = ['有', '溫', '熨', '彎', '歪', '位', '衛', '碗', '𨂿']
        w_ground = ["wû","wūn","wūt","wān","wāi","wî","wê","wnǎ","wnǎi"]
        checker(self, list(zip(w, w_ground)), c, c_north)

    def test_pingyim_syllables_additional(self):
        additional = ["znâ","yītkài","sāmzàn","būtsūt","tiǔ","dóm","hnooh","kītziáh","luânzīng","gāláoh","zzíngān/lín'gān","ggiǒnggāk","hiūkīk","bbǔzziók/bbǔliók","tíngdiân","nâi/yâng","tuánziāp","hiāohîng","ggiǎmggnê/ggiǎmggnî","hniāgō","ciōngzōk","bbiǎnhuì","zzípkǎo/lípkǎo","bātsiān","bēhgguéhzēh/buēhggéhzuēh","pnàpúh","bīngpáoh","dnǎi","pnuàduàn","biátzōng","guēh/guīh","tāktīk","gātlě","wéh/wíh","gākuài","luát","giāpguān","cōngciōk","pītdík","buànsuî","hiáphó","kāhpnì","bbǎobbniá","bbnāohlóhkì","gguíhiǎm","n̂gbāo","cāmziào","háphuān","hámtiōk","kggn̄h","kīpgnuâ","bbǔnciò","ēhsn̄g","kūh","pǐnsióng","hāhcniù","hākuì","hnāicān","hāih","knéh","lnāoh","ynāo","ooh","huāhlîng","snāh","pggn̄h","zák","cáohcáohliâm","hāosiáo","wūh","āih","hḿh","hēhgniā","ciák","zziǎng/liǒng","wāng","dǔndiáh","kùngiók","ynísōm","zâi","tûntoó","knēgōk/knīgōk","yīngyā","lāhsāp","gīgīm","ggiáogǔ","tāptè/tāptuè","biāhwê","āpbboó","gguêsīng","Duâsnuā","tnīgn̄g","tiānhiô","Tàiloǒgōh","yānggíp","kiāsiāng","pūnsōng","hnoòkēh","bbniâo","zn̄gtnâ","ciāp","snè/snì","bbnābbnā","bû","hákhńg","óhpnǎi/óhpǎi","ggiát","téh","ānbbín","giàlái","bbátzát","zuānwán","zziôgoǒ/liôgoǒ","puì","gàisí","kūtgió","bín ziā lnǎ","giáh","ggámyám","ggákhû","lníbiǒ","diàmzoō","āmbbiô","zziáp/liáp","biū","hītynû","kiò","zzǐmsīm/lǐmsīm","knuìwáh","hūtzzián/hūtlián","pnê","kiāpdnǎ","kiǒngwì","siōhlióh","ggók","ggâng","cēhsīm/cuēhsīm","dân","lnoô","huáiliâm","ggông","bēbn̂g","ggniǔkācn̄g","zziàozniû/liàozniû","pīdniá","bbuāhhǔn","kiōhsíp","tiāhdnuá","pāocūt","pāsā","pāhcāp","tuādít","ziōwǎ","guāhláo","znǎi","tà","hnìsāk","āiggô","hiāncēh","sàodông","duāh","zniâ","ōmbbákgē/ōmbbákguē","cāhcūn","dúh","diūh","dāhhniāh","Dāhlǐbbû","knáoh","piātcīng","ggniǎo","tiātzīt","diák","dāmdn̄g","piák","pāndīng","lnuázáh","knǎi","tínziǔ","hōnghīngbbîggnâi","zóh","bbuǎnhuê/bbuǎnhê","zné/zní","lné","kiōksnuà","lǒngtók","bbókggiáp","bbuátloô","tǔ","guǎi","zziǎm/liǎm","gàowát","híkkǒ","dōhtuāh","zziú/liú","biāobǔn","pōhsít","hnuáigéh/hnuígéh","snuâi","sūh","hiōhynǎ","guāpoǒ","hnuādoô","wāicuáh","bbnuǐbǎi","ākhoô","dímdiók","bbútyóh","dáoh","dápdīh","ciángzuǐ","puéh/péh","hǎi'hê","liángkiōng","tiāmsiāt","bbiǎobbóng","tnuàzáng","bbiátbbó","piāopú","lōksǎi","āobuí","ziāng","puāhsnì","puātziân","zzûnbniǎ/lûnbniǎ","hnáoh","gīklát","znuâ","biāk","sáh","bbnué","hnāh","hím","zziátliát/liátliát","lnāh","diā","tnè","ggiúcīk","bbníh/ḿggnh","bbnīhdâi","kiāngióng","kānkáp","bbǐngyǒng","ggíkkuán","ggióklán","gguǎnkû","gāmkoǒ","lūtmńg","hānzí/hānzú","tiápziām","soōsàn","ggiàn'gāh","bāhbnuā","yīktióng","yāhgōh","gnāló","siōsiǎm","bbáihiáh","knuà","hínsuā","cūh","ggǎnhōk","gnái","dōkcāt","kēh/kuēh","gīh","ggǐngbuāh","puàkīh","dēh","wnǎtáodîbbuě/wnǎtáodûbbě","pīktám","kākbǒ","bbuáknā","dāzióh","coǒ","ggâidióh","piòsniū","tūt","kāngkāng","dút","léh/luéh","bītsuàn","cōk","buà","ciāmóng","liáp","kn̄gcn̄g","tiò","diû","lápcǎi","sōhtuī","luǐzīk","kǒng","giātbā","zuátduì","zzióngboò/lióngboò","gnēgiǎn/gnīgiǎn","líksīk","cīpboǒ","tông","biāncuàn","kuātlniú","bbǐbbî","hīpzzuáh/hīpluáh","pìngcniǎ","tniācò","bbāhbbák","bbnéhpōk","tuātziāt","kniūdiâo","yōgūt","giōhzní","zúnwûn","sīkggá","bbnáocǎo","cǎoléh'ǎ/cǎoluéh'ǎ","ggnēh","lāklóh","cióh","cāngggnâo","guēhlniāo","bóktâi","bóhbbnoóh","gniū","hiāoh","puānbín","kîng","zuáh","gāplá","siókcīt","ggiágāng","bbítgguát","síhcìn","bbuī","sāt","ggióbuē","ggniáohggniáohdâng","zím","tānpniá","bbǎngdào","cíh","bbánpuébnê/bbánpébnî","huēhyú/huīhyú","hiātyán","líhpâng","liāhkiāh","tǹg","tǐduát","kīmziōng","bbuéhsōk","guībbné/guībbní","bbīhcuì","dākdní","guātsuāt","kiātzíh","kuādiōng","diáp","ggióhsiāh","bòngduâ","kiāmsùn","bbiûggoô","hoōh","pōngpài","bbnǎiziōk","luâ","ciāhzǐn","ciāocî","só","buátsiáp","zziāh/liāh","kākiāo","znuâi","tiàotāt","pīhdǒ","lnēh/lnīh","kīnsniāsèsuēh/kīnsniāsuèsēh","hātgǐng","pīkzǎo","ggniásín","hnâ","bīkciāt","diát","biàng","sàngdát","zuâ","zziākàm/liākàm","yāoyōk","yīp","lnǎtāng","hiōk","dnê","kōkláng","dângcnē/dângcnī","diòzó","ggínhuāt/ggúnhuāt","zzuêgiǎm/luêgiǎm","cnâ","ggǐmsiù","dìnsuāh","zâm","tīhtāh","siāk","cím","cák","cnuà","yátlǎm","kuāhbāk","cuàng","gnuāiciā/gnuīciā","ciǎn","āsābūhlūh","hâm","zápcá","gēzégīn/guēzuégūn","hiāgǒng","hâng","lniǎbān","ggiáhgguâ","hōngcuēzzítpák/hōngcēlítpák","hniū","hiānghḿ","hiōnghuā","piàn","giāoggnoô","lnâobáng","wūtzūt","tōh","bīh","tīm","hóh","bbéhggé","bbnuásnā","bbíkkè/bbíkkuè","tūh","ggiàng","piâng","ggáo","zíp","kāt","cuâ","cōh","pút","wnǎi","kiû","gāoh"]
        checker(self, list(zip(additional_c, additional)), c, c_north)