from taibun.taibun import Converter
from utils import checker, bilabial_c, alveolar_c, alveolo_palatal_c, velar_c, front_c, central_c, back_c, nasal_c, stop_c, syllabic_c, additional_c

c = Converter(system="Tongiong", punctuation='none')
c_north = Converter(system="Tongiong", dialect="north", punctuation='none')

def test_tongiong_initials():
    bilabial = ['bi','por','mŏr','bhă']
    checker(list(zip(bilabial_c, bilabial)), c, c_north)
    alveolar = ['dē/duē','tôr','zà','cû','su','nāi','rŭ/lŭ','liù']
    checker(list(zip(alveolar_c, alveolar)), c, c_north)
    alveolo_palatal = ['zia','ciù','sià','rĭ/lĭ']
    checker(list(zip(alveolo_palatal_c, alveolo_palatal)), c, c_north)
    velar = ['giŭ','kî','ngà','ghì/ghù','hì']
    checker(list(zip(velar_c, velar)), c, c_north)

def test_tongiong_vowels_and_rhymes():
    front = ['i','ē','ĭnn','ĕnn']
    checker(list(zip(front_c, front)), c, c_north)
    central = ['or','a','ānn']
    checker(list(zip(central_c, central)), c, c_north)
    back = ['ù','or','diunn','onn']
    checker(list(zip(back_c, back)), c, c_north)

def test_tongiong_finals():
    nasal = ['im','ĭn','ăng']
    checker(list(zip(nasal_c, nasal)), c, c_north)
    stop = ['iap','āt','ōk','ah']
    checker(list(zip(stop_c, stop)), c, c_north)
    syllabic = ['m̀','n̆g']
    checker(list(zip(syllabic_c, syllabic)), c, c_north)

def test_tongiong_syllables_additional():
    additional = ["zānn","it-kâi","sām-zân","but-sūt","tiù","dŏm","--ho̊nnh","kit-ziah","luân-zing","gā-lauh","rīn-gan/lîn-gan","ghiong-gāk","hiū-kīk","bhu-riok/bhu-liok","tīng-diān/tîng-diān","āinn/iāng","tuān-ziāp/tuân-ziāp","hiāu-hīng","ghiam-ngē/ghiam-ngī","hiānn-gor","ciōng-zōk","bhian-huî","rīp-kàu/līp-kàu","bat-sian","bè-ghuê-zēh/buè-ghê-zuēh","pànn-puh","bīng-pauh","dàinn","puànn-duân","biāt-zong","guēh/guīh","tak-tīk","gat-lè","ueh/uih","gā-kuâi","luat","giap-guan","cōng-ciōk","pit-dik","buàn-suī","hiāp-hŏr","kà-pînn","bhau-miă","màu-lôr-kî","ghuī-hiàm/ghuî-hiàm","nn̂g-bau","cām-ziâu","hāp-huan","hām-tiōk/hâm-tiōk","kn̄gh","kip-guānn","bhun-ciôr","è-sng","kūh","pin-siŏng","hà-ciûnn","hā-kuî","hāinn-can","hāih","kennh","nāuh","iaunn","--o̊h","huà-līng","sānnh","pn̄gh","zak","câu-câu-liām","hāu-siău","ūh","āih","hmh","hè-giann","ciak","riàng/liòng","uang","dun-diah","kùn-giok","īnn-som/înn-som","zāi","tûn-tŏr","kēnn-gōk/kīnn-gōk","īng-ia","là-sāp","gī-gim","ghiāu-gù/ghiâu-gù","tap-tê/tap-tuê","bià-uē","ap-bhŏr","ghuê-sing","Duâ-suann","tīnn-gng","tiān-hiōr","Tài-lor-gōh","iāng-gip","kiā-siang","pūn-song","hònn-kēh","miāu","zn̄g-tānn","ciāp","sênn/sînn","mā-ma","bū","hāk-hn̆g","ôr-pàinn/ôr-pài","ghiat","teh","ān-bhĭn","già-lăi","bhāt-zat","zuān-uăn","riôr-gòr/liôr-gòr","puî","gài-sĭ","kut-giŏr","bīn zia nà/bîn zia nà","giah","ghām-iăm/ghâm-iăm","ghāk-hū","nī-biòr/nî-biòr","diàm-zor","ām-bhiōr","riap/liap","biu","hit-iūnn","kiôr","rim-sim/lim-sim","kuìnn-uah","hut-riăn/hut-liăn","pēnn","kiap-dànn","kiong-uî","siòr-lioh","ghok","ghāng","cè-sim/cuè-sim","dān","nōr","huāi-liām/huâi-liām","ghōng","bē-bn̄g","ngiu-kā-cng","riàu-ziūnn/liàu-ziūnn","pī-diănn","bhuà-hùn","kiòr-sip","tià-duănn","pāu-cūt","pā-sa","pà-cāp","tuā-dit","ziōr-uà","guà-lău","zàinn","tâ","hìnn-sāk","āi-ghōr","hiān-cēh","sàu-dōng","duāh","ziānn","ōm-bhāk-ge/ōm-bhāk-gue","cà-cun","duh","diūh","dà-hiānnh","Dà-li-bhū","kaunnh","piat-cing","ngiàu","tiat-zīt","diak","dām-dng","piak","pān-ding","nuā-zah/nuâ-zah","kàinn","tīn-ziù/tîn-ziù","hōng-hīng-bhî-ngāi","zoh","bhuan-huē/bhuan-hē","zĕnn/zĭnn","nĕ","kiok-suânn","long-tok","bhōk-ghiap","bhuāt-lōr","tù","guài","riàm/liàm","gàu-uat","hīk-kòr","dòr-tuāh","riŭ/liŭ","biāu-bùn","pòr-sit","huāinn-geh/huînn-geh","suāinn","sūh","hiòr-iànn","guā-pòr","huānn-dōr","uāi-cuah","mui-bài","ak-hōr","dīm-diok/dîm-diok","bhūt-ioh","dauh","dāp-dīh","ciāng-zuì/ciâng-zuì","pueh/peh","hai-hē","liāng-kiong/liâng-kiong","tiām-siāt","bhiau-bhŏng","tuànn-zăng","bhiāt-bhŏr","piāu-pŭ","lok-sài","āu-buĭ","ziang","puà-sînn","puat-ziān","rûn-biànn/lûn-biànn","haunnh","gik-lat","zuānn","biāk","sah","muĕ","hānnh","hĭm","riāt-liat/liāt-liat","nāh","dia","tênn","ghiū-cīk/ghiû-cīk","mih/mngh","mì-dāi","kiān-giŏng","kān-kap","bhing-iòng","ghīk-kuăn","ghiōk-lăn","ghuan-kū","gām-kòr","lut-mn̆g","hān-zĭ/hān-zŭ","tiāp-ziam","sōr-sân","ghiàn-gāh","bà-buann","ik-tiŏng","ià-gōh","gānn-lŏr","siōr-siàm","bhāi-hiah/bhâi-hiah","kuânn","hīn-sua/hîn-sua","cūh","ghan-hōk","găinn","dok-cāt","kēh/kuēh","gīh","ghing-buāh","puà-kīh","dēh","uann-tāu-dî-bhuè/uann-tâu-dû-bhè","pik-tăm","kak-bòr","bhuā-kann/bhuâ-kann","dā-zioh","còr","ghâi-dioh","piòr-siunn","tūt","kāng-kang","dut","leh/lueh","bit-suân","cōk","buâ","ciām-ŏng","liap","kn̄g-cng","tiôr","diū","lāp-cài","sòr-tui","lui-zīk","kòng","giat-ba","zuāt-duî","riōng-bôr/liông-bôr","gēnn-giàn/gīnn-giàn","līk-sīk","cip-bòr","tōng","biān-cuân","kuat-niŭ","bhi-bhī","hip-ruah/hip-luah","pìng-ciànn","tiānn-côr","bhà-bhak","mê-pōk","tuat-ziāt","kiūnn-diāu","iōr-gūt","giòr-zĭnn","zūn-ūn/zûn-ūn","sik-ghă","māu-càu/mâu-càu","cau-lē-à/cau-luē-à","ngēh","lak-loh","cioh","cāng-ngāu","guè-niau","bōk-tāi","bôr-moh","giunn","hiāuh","puān-bĭn","kīng","zuah","gap-lă","siōk-cīt","ghiā-gang/ghiâ-gang","bhīt-ghuat","sî-cîn","bhui","sāt","ghiōr-bue/ghiôr-bue","ngiâu-ngiâu-dāng","zĭm","tān-piănn","bhang-dâu","cih","bhān-puē-bēnn/bhân-pê-bīnn","huè-iŭ/huì-iŭ","hiat-iăn","lî-pāng","lià-kiāh","tn̂g","ti-duat","kīm-ziong","bhuê-sōk","guī-mĕ/guī-mĭ","bhì-cuî","dak-dĭnn","guat-suāt","kiat-zih","kuā-diong","diap","ghiôr-siāh","bòng-duā","kiām-sûn","bhiû-ghōr","hōh","pōng-pâi","mai-ziōk","luā","cià-zìn","ciāu-cī","sŏr","buāt-siap","riāh/liāh","kā-kiau","zuāinn","tiàu-tāt","pì-dòr","nēh/nīh","kīn-siānn-sè-suēh/kīn-siānn-suè-sēh","hat-gìng","pik-zàu","ngiā-sĭn/ngiâ-sĭn","hānn","bik-ciāt","diat","biâng","sàng-dat","zuā","riā-kâm/liā-kâm","iāu-iōk","īp","na-tang","hiōk","dēnn","kok-lăng","dâng-cenn/dâng-cinn","diòr-zŏr","ghīn-huāt/ghûn-huāt","ruê-giàm/luê-giàm","cānn","ghim-siû","dìn-suāh","zām","tì-tāh","siāk","cĭm","cak","cuânn","iāt-làm","kuà-bāk","cuâng","guāinn-cia/guīnn-cia","ciàn","ā-sā-bù-lūh","hām","zāp-că","gē-zē-gin/guē-zuê-gun","hiā-gòng","hāng","nia-ban","ghiâ-ghuā","hōng-cuē-rīt-pak/hōng-cē-līt-pak","hiunn","hiāng-hm̆","hiōng-hua","piân","giāu-ngōr","nâu-băng","ut-zūt","tōh","bīh","tim","hoh","bhê-ghĕ","muā-sann/muâ-sann","bhīk-kê/bhīk-kuê","tūh","ghiâng","piāng","ghău","zip","kāt","cuā","cōh","put","uàinn","kiū","gāuh"]
    checker(list(zip(additional_c, additional)), c, c_north)