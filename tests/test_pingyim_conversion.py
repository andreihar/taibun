from taibun.taibun import Converter
from utils import checker, bilabial_c, alveolar_c, alveolo_palatal_c, velar_c, front_c, central_c, back_c, nasal_c, stop_c, syllabic_c, additional_c

c = Converter(system="Pingyim", punctuation='none')
c_north = Converter(system="Pingyim", dialect="north", punctuation='none')

def test_pingyim_initials():
    bilabial = ['bī','pō','bbnoó','bbá']
    checker(list(zip(bilabial_c, bilabial)), c, c_north)
    alveolar = ['dê/duê','tò','zǎ','cù','sū','lnâi','zzú/lú','liǔ']
    checker(list(zip(alveolar_c, alveolar)), c, c_north)
    alveolo_palatal = ['ziā','ciǔ','siǎ','zzí/lí']
    checker(list(zip(alveolo_palatal_c, alveolo_palatal)), c, c_north)
    velar = ['giú','kì','ggnǎ','ggǐ/ggǔ','hǐ']
    checker(list(zip(velar_c, velar)), c, c_north)

def test_pingyim_vowels_and_rhymes():
    front = ['yī','ê','ní','né']
    checker(list(zip(front_c, front)), c, c_north)
    central = ['ō','ā','nâ']
    checker(list(zip(central_c, central)), c, c_north)
    back = ['wǔ','oō','dniū','noō']
    checker(list(zip(back_c, back)), c, c_north)

def test_pingyim_finals():
    nasal = ['yīm','yín','áng']
    checker(list(zip(nasal_c, nasal)), c, c_north)
    stop = ['yáp','āt','ōk','áh']
    checker(list(zip(stop_c, stop)), c, c_north)
    syllabic = ['m̌','ńg']
    checker(list(zip(syllabic_c, syllabic)), c, c_north)

def test_pingyim_syllables_additional():
    additional = ["znâ","yītkài","sāmzàn","būtsūt","tiǔ","dóm","hnooh","kītziáh","luânzīng","gāláoh","zzíngān/língān","ggiǒnggāk","hiūkīk","bbǔzziók/bbǔliók","tíngdiân","nâi/yâng","tuánziāp","hiāohîng","ggiǎmggnê/ggiǎmggnî","hināgō","ciōngzōk","bbiǎnhuì","zzípkǎo/lípkǎo","bātsiān","bēhgguéhzēh/buēhggéhzuēh","pnàpúh","bīngpáoh","dnǎi","punàduàn","biátzōng","guēh/guīh","tāktīk","gātlě","wéh/wíh","gākuài","luát","giāpguān","cōngciōk","pītdík","buànsuî","hiáphó","kāhpnì","bbǎobbniá","bbnāohlóhkì","gguíhiǎm","n̂gbāo","cāmziào","háphuān","hámtiōk","kggn̄h","kīpgunâ","bbǔnciò","ēhsn̄g","kūh","pǐnsióng","hāhcniù","hākuì","hnāicān","hāih","knéh","lnāoh","yāolnn","ooh","huāhlîng","snāh","pggn̄h","zák","cáohcáohliâm","hāosiáo","wūh","āih","hbbńh","hēhginā","ciák","zziǎng/liǒng","wāng","dǔndiáh","kùngiók","nísōm","zâi","tûntoó","knēgōk/knīgōk","yīngyā","lāhsāp","gīgīm","ggiáogǔ","tāptè/tāptuè","biāhwê","āpbboó","gguêsīng","Duâsunā","tnīgn̄g","tiānhiô","Tàiloǒgōh","yānggíp","kiāsiāng","pūnsōng","hnoòkēh","bbniâo","zn̄gtnâ","ciāp","snè/snì","bbnābbnā","bû","hákhńg","óhpnǎi/óhpǎi","ggiát","téh","ānbbín","giàlái","bbátzát","zuānwán","zziôgoǒ/liôgoǒ","puì","gàisí","kūtgió","bín ziā lnǎ","giáh","ggámyám","ggákhû","lníbiǒ","diàmzoō","āmbbiô","zziáp/liáp","biū","hītniû","kiò","zzǐmsīm/lǐmsīm","kunìwáh","hūtzzián/hūtlián","pnê","kiāpdnǎ","kiǒngwì","siōhlióh","ggók","ggâng","cēhsīm/cuēhsīm","dân","lnoô","huáiliâm","ggông","bēbn̂g","ggniǔkācn̄g","zziàozniû/liàozniû","pīdiná","bbuāhhǔn","kiōhsíp","tiāhduná","pāocūt","pāsā","pāhcāp","tuādít","ziōwǎ","guāhláo","znǎi","tà","hnìsāk","āiggô","hiāncēh","sàodông","duāh","zinâ","ōmbbákgē/ōmbbákguē","cāhcūn","dúh","diūh","dāhhināh","Dāhlǐbbû","káolnlnh","piātcīng","ggniǎo","tiātzīt","diák","dāmdn̄g","piák","pāndīng","lnuázáh","knǎi","tínziǔ","hōnghīngbbîggnâi","zóh","bbuǎnhuê/bbuǎnhê","zné/zní","lné","kiōksunà","lǒngtók","bbókggiáp","bbuátloô","tǔ","guǎi","zziǎm/liǎm","gàowát","híkkǒ","dōhtuāh","zziú/liú","biāobǔn","pōhsít","hunáigéh/hunígéh","sunâi","sūh","hiōhyinǎ","guāpoǒ","hunādoô","wāicuáh","bbnuǐbǎi","ākhoô","dímdiók","bbútyóh","dáoh","dápdīh","ciángzuǐ","puéh/péh","hǎihê","liángkiōng","tiāmsiāt","bbiǎobbóng","tunàzáng","bbiátbbó","piāopú","lōksǎi","āobuí","ziāng","puāhsnì","puātziân","zzûnbinǎ/lûnbinǎ","háolnlnh","gīklát","zunâ","biāk","sáh","bbnué","hnāh","hím","zziátliát/liátliát","lnāh","diā","tnè","ggiúcīk","bbníh/ḿggnh","bbnīhdâi","kiāngióng","kānkáp","bbǐngyǒng","ggíkkuán","ggióklán","gguǎnkû","gāmkoǒ","lūtmńg","hānzí/hānzú","tiápziām","soōsàn","ggiàngāh","bāhbunā","yīktióng","yāhgōh","gnāló","siōsiǎm","bbáihiáh","kunà","hínsuā","cūh","ggǎnhōk","gnái","dōkcāt","kēh/kuēh","gīh","ggǐngbuāh","puàkīh","dēh","wunǎtáodîbbuě/wunǎtáodûbbě","pīktám","kākbǒ","bbuáknā","dāzióh","coǒ","ggâidióh","piòsniū","tūt","kāngkāng","dút","léh/luéh","bītsuàn","cōk","buà","ciāmóng","liáp","kn̄gcn̄g","tiò","diû","lápcǎi","sōhtuī","luǐzīk","kǒng","giātbā","zuátduì","zzióngboò/lióngboò","gnēgiǎn/gnīgiǎn","líksīk","cīpboǒ","tông","biāncuàn","kuātlniú","bbǐbbî","hīpzzuáh/hīpluáh","pìngcinǎ","tinācò","bbāhbbák","bbnéhpōk","tuātziāt","kniūdiâo","yōgūt","giōhzní","zúnwûn","sīkggá","bbnáocǎo","cǎoléhǎ/cǎoluéhǎ","ggnēh","lāklóh","cióh","cāngggnâo","guēhlniāo","bóktâi","bóhbbnoóh","gniū","hiāoh","puānbín","kîng","zuáh","gāplá","siókcīt","ggiágāng","bbítgguát","síhcìn","bbuī","sāt","ggióbuē","ggniáohggniáohdâng","zím","tānpiná","bbǎngdào","cíh","bbánpuébnê/bbánpébnî","huēhyú/huīhyú","hiātyán","líhpâng","liāhkiāh","tǹg","tǐduát","kīmziōng","bbuéhsōk","guībbné/guībbní","bbīhcuì","dākdní","guātsuāt","kiātzíh","kuādiōng","diáp","ggióhsiāh","bòngduâ","kiāmsùn","bbiûggoô","hoōh","pōngpài","bbnǎiziōk","luâ","ciāhzǐn","ciāocî","só","buátsiáp","zziāh/liāh","kākiāo","zunâi","tiàotāt","pīhdǒ","lnēh/lnīh","kīnsināsèsuēh/kīnsināsuèsēh","hātgǐng","pīkzǎo","ggniásín","hnâ","bīkciāt","diát","biàng","sàngdát","zuâ","zziākàm/liākàm","yāoyōk","yīp","lnǎtāng","hiōk","dnê","kōkláng","dângcnē/dângcnī","diòzó","ggínhuāt/ggúnhuāt","zzuêgiǎm/luêgiǎm","cnâ","ggǐmsiù","dìnsuāh","zâm","tīhtāh","siāk","cím","cák","cunà","yátlǎm","kuāhbāk","cuàng","gunāiciā/gunīciā","ciǎn","āsābūhlūh","hâm","zápcá","gēzégīn/guēzuégūn","hiāgǒng","hâng","lniǎbān","ggiáhgguâ","hōngcuēzzítpák/hōngcēlítpák","hniū","hiānghḿ","hiōnghuā","piàn","giāoggnoô","lnâobáng","wūtzūt","tōh","bīh","tīm","hóh","bbéhggé","bbnuásnā","bbíkkè/bbíkkuè","tūh","ggiàng","piâng","ggáo","zíp","kāt","cuâ","cōh","pút","wunǎi","kiû","gāoh"]
    checker(list(zip(additional_c, additional)), c, c_north)