from taibun.taibun import Converter
from utils import checker, bilabial_c, alveolar_c, alveolo_palatal_c, velar_c, front_c, central_c, back_c, nasal_c, stop_c, syllabic_c, additional_c

c = Converter(system="Tailo", punctuation='none')
c_north = Converter(system="Tailo", dialect="north", punctuation='none')

def test_tailo_initials():
    bilabial = ['pi','pho','môo','bâ']
    checker(list(zip(bilabial_c, bilabial)), c, c_north)
    alveolar = ['tē/tuē','thò','tsá','tshù','su','nāi','jû/lû','liú']
    checker(list(zip(alveolar_c, alveolar)), c, c_north)
    alveolo_palatal = ['tsia','tshiú','siá','jî/lî']
    checker(list(zip(alveolo_palatal_c, alveolo_palatal)), c, c_north)
    velar = ['kiû','khì','ngá','gí/gú','hí']
    checker(list(zip(velar_c, velar)), c, c_north)

def test_tailo_vowels_and_rhymes():
    front = ['i','ē','înn','ênn']
    checker(list(zip(front_c, front)), c, c_north)
    central = ['o','a','ānn']
    checker(list(zip(central_c, central)), c, c_north)
    back = ['ú','oo','tiunn','onn']
    checker(list(zip(back_c, back)), c, c_north)

def test_tailo_finals():
    nasal = ['im','în','âng']
    checker(list(zip(nasal_c, nasal)), c, c_north)
    stop = ['ia̍p','at','ok','a̍h']
    checker(list(zip(stop_c, stop)), c, c_north)
    syllabic = ['ḿ','n̂g']
    checker(list(zip(syllabic_c, syllabic)), c, c_north)

def test_tailo_syllables_additional():
    additional = ["tsānn","it-khài","sam-tsàn","put-sut","thiú","tôm","--honnh","khit-tsia̍h","luān-tsing","ka-la̍uh","jîn-kan/lîn-kan","gióng-kak","hiu-khik","bú-jio̍k/bú-lio̍k","thîng-tiān","āinn/iāng","thuân-tsiap","hiau-hīng","giám-ngē/giám-ngī","hiann-ko","tshiong-tsok","bián-huì","ji̍p-kháu/li̍p-kháu","pat-sian","peh-gue̍h-tseh/pueh-ge̍h-tsueh","phànn-phu̍h","ping-pha̍uh","táinn","phuànn-tuàn","pia̍t-tsong","kueh/kuih","thak-thik","kat-lé","ue̍h/ui̍h","ka-khuài","lua̍t","kiap-kuan","tshong-tshiok","phit-ti̍k","puàn-suī","hia̍p-hô","khah-phìnn","báu-miâ","mauh-lo̍h-khì","guî-hiám","nn̄g-pau","tsham-tsiàu","ha̍p-huan","hâm-thiok","khngh","khip-kuānn","bún-tshiò","eh-sng","khuh","phín-siông","hah-tshiùnn","ha-khuì","hainn-tshan","haih","khe̍nnh","nauh","iaunn","--ooh","huah-līng","sannh","phngh","tsa̍k","tsha̍uh-tsha̍uh-liām","hau-siâu","uh","aih","hm̍h","heh-kiann","tshia̍k","jiáng/lióng","uang","tún-tia̍h","khùn-kio̍k","înn-som","tsāi","thūn-thôo","khenn-kok/khinn-kok","ing-ia","lah-sap","ki-kim","giâu-kú","thap-thè/thap-thuè","piah-uē","ap-bôo","guē-sing","Tuā-suann","thinn-kng","thian-hiō","Thài-lóo-koh","iang-ki̍p","khia-siang","phun-song","hònn-kheh","miāu","tsng-thānn","tshiap","sènn/sìnn","ma-ma","pū","ha̍k-hn̂g","o̍h-pháinn/o̍h-phái","gia̍t","the̍h","an-bîn","kià-lâi","ba̍t-tsa̍t","tsuan-uân","jiō-kóo/liō-kóo","phuì","kài-sî","khut-kiô","pîn tsia ná","kia̍h","gâm-iâm","ga̍k-hū","nî-pió","tiàm-tsoo","am-biō","jia̍p/lia̍p","piu","hit-iūnn","khiò","jím-sim/lím-sim","khuìnn-ua̍h","hut-jiân/hut-liân","phēnn","khiap-tánn","khióng-uì","sioh-lio̍h","go̍k","gāng","tsheh-sim/tshueh-sim","tān","nōo","huâi-liām","gōng","pe-pn̄g","ngiú-kha-tshng","jiàu-tsiūnn/liàu-tsiūnn","phi-tiânn","buah-hún","khioh-si̍p","thiah-tuânn","phau-tshut","pha-sa","phah-tshap","thua-ti̍t","tsio-uá","kuah-lâu","tsáinn","thà","hìnn-sak","ai-gō","hian-tsheh","sàu-tōng","tuah","tsiānn","om-ba̍k-ke/om-ba̍k-kue","tshah-tshun","tu̍h","tiuh","tah-hiannh","Tah-lí-bū","kha̍unnh","phiat-tshing","ngiáu","thiat-tsit","tia̍k","tam-tng","phia̍k","phan-ting","nuâ-tsa̍h","kháinn","thîn-tsiú","hong-hing-bī-ngāi","tso̍h","buán-huē/buán-hē","tsênn/tsînn","nê","khiok-suànn","lóng-tho̍k","bo̍k-gia̍p","bua̍t-lōo","thú","kuái","jiám/liám","kàu-ua̍t","hi̍k-khó","toh-thuah","jiû/liû","piau-pún","phoh-si̍t","huâinn-ke̍h/huînn-ke̍h","suāinn","suh","hioh-iánn","kua-phóo","huann-tōo","uai-tshua̍h","muí-pái","ak-hōo","tîm-tio̍k","bu̍t-io̍h","ta̍uh","ta̍p-tih","tshiâng-tsuí","phue̍h/phe̍h","hái-hē","liâng-khiong","thiam-siat","biáu-bông","thuànn-tsâng","bia̍t-bô","phiau-phû","lok-sái","au-puî","tsiang","phuah-sìnn","phuat-tsiān","jūn-piánn/lūn-piánn","ha̍unnh","kik-la̍t","tsuānn","piak","sa̍h","muê","hannh","hîm","jia̍t-lia̍t/lia̍t-lia̍t","nah","tia","thènn","giû-tshik","mi̍h/mn̍gh","mih-tāi","khian-kiông","khan-kha̍p","bíng-ióng","gi̍k-khuân","gio̍k-lân","guán-khū","kam-khóo","lut-mn̂g","han-tsî/han-tsû","thia̍p-tsiam","soo-sàn","giàn-kah","pah-puann","ik-thiông","iah-koh","kann-lô","sio-siám","bâi-hia̍h","khuànn","hîn-sua","tshuh","gán-hok","kâinn","tok-tshat","kheh/khueh","kih","gíng-puah","phuà-khih","teh","uánn-thâu-tī-bué/uánn-thâu-tū-bé","phik-thâm","khak-pó","buâ-khann","ta-tsio̍h","tshóo","gāi-tio̍h","phiò-siunn","thut","khang-khang","tu̍t","le̍h/lue̍h","pit-suàn","tshok","puà","tshiam-ông","lia̍p","khng-tshng","thiò","tiū","la̍p-tshái","soh-thui","luí-tsik","khóng","kiat-pa","tsua̍t-tuì","jiông-pòo/liông-pòo","kenn-kián/kinn-kián","li̍k-sik","tship-póo","thōng","pian-tshuàn","khuat-niû","bí-bī","hip-jua̍h/hip-lua̍h","phìng-tshiánn","thiann-tshò","bah-ba̍k","me̍h-phok","thuat-tsiat","khiunn-tiāu","io-kut","kioh-tsînn","tsûn-ūn","sik-gâ","mâu-tsháu","tsháu-le̍h-á/tsháu-lue̍h-á","ngeh","lak-lo̍h","tshio̍h","tshang-ngāu","kueh-niau","po̍k-thāi","po̍h-mo̍oh","kiunn","hiauh","phuan-pîn","khīng","tsua̍h","kap-lâ","sio̍k-tshit","giâ-kang","bi̍t-gua̍t","si̍h-tshìn","bui","sat","giô-pue","ngia̍uh-ngia̍uh-tāng","tsîm","than-phiânn","báng-tàu","tshi̍h","bân-phuê-pēnn/bân-phê-pīnn","hueh-iû/huih-iû","hiat-iân","li̍h-phāng","liah-khiah","thǹg","thí-tua̍t","khim-tsiong","bue̍h-sok","kui-mê/kui-mî","bih-tshuì","tak-tînn","kuat-suat","khiat-tsi̍h","khua-tiong","tia̍p","gio̍h-siah","pòng-tuā","khiam-sùn","biū-gōo","hooh","phong-phài","mái-tsiok","luā","tshiah-tsín","tshiau-tshī","sô","pua̍t-sia̍p","jiah/liah","kha-khiau","tsuāinn","thiàu-that","phih-tó","neh/nih","khin-siann-sè-sueh/khin-siann-suè-seh","hat-kíng","phik-tsáu","ngiâ-sîn","hānn","pik-tshiat","tia̍t","piàng","sàng-ta̍t","tsuā","jia-khàm/lia-khàm","iau-iok","ip","ná-thang","hiok","tēnn","khok-lâng","tāng-tshenn/tāng-tshinn","tiò-tsô","gîn-huat/gûn-huat","juē-kiám/luē-kiám","tshānn","gím-siù","tìn-suah","tsām","thih-thah","siak","tshîm","tsha̍k","tshuànn","ia̍t-lám","khuah-pak","tshuàng","kuainn-tshia/kuinn-tshia","tshián","a-sa-puh-luh","hām","tsa̍p-tshâ","ke-tsê-kin/kue-tsuê-kun","hia-kóng","hāng","niá-pan","gia̍h-guā","hong-tshue-ji̍t-pha̍k/hong-tshe-li̍t-pha̍k","hiunn","hiang-hm̂","hiong-hua","phiàn","kiau-ngōo","nāu-pâng","ut-tsut","thoh","pih","thim","ho̍h","be̍h-gê","muâ-sann","bi̍k-khè/bi̍k-khuè","thuh","giàng","phiāng","gâu","tsi̍p","khat","tshuā","tshoh","phu̍t","uáinn","khiū","kauh"]
    checker(list(zip(additional_c, additional)), c, c_north)