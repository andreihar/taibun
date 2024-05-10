from taibun.taibun import Converter
from utils import checker, bilabial_c, alveolar_c, alveolo_palatal_c, velar_c, front_c, central_c, back_c, nasal_c, stop_c, syllabic_c, additional_c

c = Converter(system="POJ", punctuation='none')
c_north = Converter(system="POJ", dialect="north", punctuation='none')

def test_poj_initials():
    bilabial = ['pi','pho','mô͘','bâ']
    checker(list(zip(bilabial_c, bilabial)), c, c_north)
    alveolar = ['tē/tōe','thò','chá','chhù','su','nāi','jû/lû','liú']
    checker(list(zip(alveolar_c, alveolar)), c, c_north)
    alveolo_palatal = ['chia','chhiú','siá','jî/lî']
    checker(list(zip(alveolo_palatal_c, alveolo_palatal)), c, c_north)
    velar = ['kiû','khì','ngá','gí/gú','hí']
    checker(list(zip(velar_c, velar)), c, c_north)

def test_poj_vowels_and_rhymes():
    front = ['i','ē','îⁿ','êⁿ']
    checker(list(zip(front_c, front)), c, c_north)
    central = ['o','a','āⁿ']
    checker(list(zip(central_c, central)), c, c_north)
    back = ['ú','o͘','tiuⁿ','oⁿ']
    checker(list(zip(back_c, back)), c, c_north)

def test_poj_finals():
    nasal = ['im','în','âng']
    checker(list(zip(nasal_c, nasal)), c, c_north)
    stop = ['ia̍p','at','ok','a̍h']
    checker(list(zip(stop_c, stop)), c, c_north)
    syllabic = ['ḿ','n̂g']
    checker(list(zip(syllabic_c, syllabic)), c, c_north)

def test_poj_syllables_additional():
    additional = ["chāⁿ","it-khài","sam-chàn","put-sut","thiú","tôm","--hohⁿ","khit-chia̍h","loān-cheng","ka-la̍uh","jîn-kan/lîn-kan","gióng-kak","hiu-khek","bú-jio̍k/bú-lio̍k","thêng-tiān","āiⁿ/iāng","thoân-chiap","hiau-hēng","giám-ngē/giám-ngī","hiaⁿ-ko","chhiong-chok","bián-hùi","ji̍p-kháu/li̍p-kháu","pat-sian","peh-goe̍h-cheh/poeh-ge̍h-choeh","phàⁿ-phu̍h","peng-pha̍uh","táiⁿ","phoànn-toàn","pia̍t-chong","koeh/kuih","thak-thek","kat-lé","oe̍h/u̍ih","ka-khoài","loa̍t","kiap-koan","chhong-chhiok","phit-te̍k","poàn-sūi","hia̍p-hô","khah-phìⁿ","báu-miâ","mauh-lo̍h-khì","gûi-hiám","nn̄g-pau","chham-chiàu","ha̍p-hoan","hâm-thiok","khngh","khip-koānn","bún-chhiò","eh-sng","khuh","phín-siông","hah-chhiùⁿ","ha-khùi","haiⁿ-chhan","haih","khe̍hⁿ","nauh","iauⁿ","--o͘h","hoah-lēng","sahⁿ","phngh","cha̍k","chha̍uh-chha̍uh-liām","hau-siâu","uh","aih","hm̍h","heh-kiaⁿ","chhia̍k","jiáng/lióng","oang","tún-tia̍h","khùn-kio̍k","îⁿ-som","chāi","thūn-thô͘","kheⁿ-kok/khiⁿ-kok","eng-ia","lah-sap","ki-kim","giâu-kú","thap-thè/thap-thòe","piah-ōe","ap-bô͘","gōe-seng","Tōa-soann","thiⁿ-kng","thian-hiō","Thài-ló͘-koh","iang-ki̍p","khia-siang","phun-song","hòⁿ-kheh","miāu","chng-thāⁿ","chhiap","sèⁿ/sìⁿ","ma-ma","pū","ha̍k-hn̂g","o̍h-pháiⁿ/o̍h-phái","gia̍t","the̍h","an-bîn","kià-lâi","ba̍t-cha̍t","choan-oân","jiō-kó͘/liō-kó͘","phùi","kài-sî","khut-kiô","pîn chia ná","kia̍h","gâm-iâm","ga̍k-hū","nî-pió","tiàm-cho͘","am-biō","jia̍p/lia̍p","piu","hit-iūⁿ","khiò","jím-sim/lím-sim","khùiⁿ-oa̍h","hut-jiân/hut-liân","phēⁿ","khiap-táⁿ","khióng-ùi","sioh-lio̍h","go̍k","gāng","chheh-sim/chhoeh-sim","tān","nō͘","hoâi-liām","gōng","pe-pn̄g","ngiú-kha-chhng","jiàu-chiūⁿ/liàu-chiūⁿ","phi-tiâⁿ","boah-hún","khioh-si̍p","thiah-toânn","phau-chhut","pha-sa","phah-chhap","thoa-ti̍t","chio-óa","koah-lâu","cháiⁿ","thà","hìⁿ-sak","ai-gō","hian-chheh","sàu-tōng","toah","chiāⁿ","om-ba̍k-ke/om-ba̍k-koe","chhah-chhun","tu̍h","tiuh","tah-hiahⁿ","Tah-lí-bū","kha̍uhⁿ","phiat-chheng","ngiáu","thiat-chit","tia̍k","tam-tng","phia̍k","phan-teng","nôa-cha̍h","kháiⁿ","thîn-chiú","hong-heng-bī-ngāi","cho̍h","boán-hōe/boán-hē","chêⁿ/chîⁿ","nê","khiok-soànn","lóng-tho̍k","bo̍k-gia̍p","boa̍t-lō͘","thú","koái","jiám/liám","kàu-oa̍t","he̍k-khó","toh-thoah","jiû/liû","piau-pún","phoh-si̍t","hoâiⁿ-ke̍h/hûiⁿ-ke̍h","soāiⁿ","suh","hioh-iáⁿ","koa-phó͘","hoann-tō͘","oai-chhoa̍h","múi-pái","ak-hō͘","tîm-tio̍k","bu̍t-io̍h","ta̍uh","ta̍p-tih","chhiâng-chúi","phoe̍h/phe̍h","hái-hē","liâng-khiong","thiam-siat","biáu-bông","thoànn-châng","bia̍t-bô","phiau-phû","lok-sái","au-pûi","chiang","phoah-sìⁿ","phoat-chiān","jūn-piáⁿ/lūn-piáⁿ","ha̍uhⁿ","kek-la̍t","choānn","piak","sa̍h","môe","hahⁿ","hîm","jia̍t-lia̍t/lia̍t-lia̍t","nah","tia","thèⁿ","giû-chhek","mi̍h/mn̍gh","mih-tāi","khian-kiông","khan-kha̍p","béng-ióng","ge̍k-khoân","gio̍k-lân","goán-khū","kam-khó͘","lut-mn̂g","han-chî/han-chû","thia̍p-chiam","so͘-sàn","giàn-kah","pah-poann","ek-thiông","iah-koh","kaⁿ-lô","sio-siám","bâi-hia̍h","khoànn","hîn-soa","chhuh","gán-hok","kâiⁿ","tok-chhat","kheh/khoeh","kih","géng-poah","phòa-khih","teh","oánn-thâu-tī-bóe/oánn-thâu-tū-bé","phek-thâm","khak-pó","bôa-khaⁿ","ta-chio̍h","chhó͘","gāi-tio̍h","phiò-siuⁿ","thut","khang-khang","tu̍t","le̍h/loe̍h","pit-soàn","chhok","pòa","chhiam-ông","lia̍p","khng-chhng","thiò","tiū","la̍p-chhái","soh-thui","lúi-chek","khóng","kiat-pa","choa̍t-tùi","jiông-pò͘/liông-pò͘","keⁿ-kián/kiⁿ-kián","le̍k-sek","chhip-pó͘","thōng","pian-chhoàn","khoat-niû","bí-bī","hip-joa̍h/hip-loa̍h","phèng-chhiáⁿ","thiaⁿ-chhò","bah-ba̍k","me̍h-phok","thoat-chiat","khiuⁿ-tiāu","io-kut","kioh-chîⁿ","chûn-ūn","sek-gâ","mâu-chháu","chháu-le̍h-á/chháu-loe̍h-á","ngeh","lak-lo̍h","chhio̍h","chhang-ngāu","koeh-niau","po̍k-thāi","po̍h-mo̍͘h","kiuⁿ","hiauh","phoan-pîn","khēng","choa̍h","kap-lâ","sio̍k-chhit","giâ-kang","bi̍t-goa̍t","si̍h-chhìn","bui","sat","giô-poe","ngia̍uh-ngia̍uh-tāng","chîm","than-phiâⁿ","báng-tàu","chhi̍h","bân-phôe-pēⁿ/bân-phê-pīⁿ","hoeh-iû/huih-iû","hiat-iân","li̍h-phāng","liah-khiah","thǹg","thí-toa̍t","khim-chiong","boe̍h-sok","kui-mê/kui-mî","bih-chhùi","tak-tîⁿ","koat-soat","khiat-chi̍h","khoa-tiong","tia̍p","gio̍h-siah","pòng-tōa","khiam-sùn","biū-gō͘","ho͘h","phong-phài","mái-chiok","lōa","chhiah-chín","chhiau-chhī","sô","poa̍t-sia̍p","jiah/liah","kha-khiau","choāiⁿ","thiàu-that","phih-tó","neh/nih","khin-siaⁿ-sè-soeh/khin-siaⁿ-sòe-seh","hat-kéng","phek-cháu","ngiâ-sîn","hāⁿ","pek-chhiat","tia̍t","piàng","sàng-ta̍t","chōa","jia-khàm/lia-khàm","iau-iok","ip","ná-thang","hiok","tēⁿ","khok-lâng","tāng-chheⁿ/tāng-chhiⁿ","tiò-chô","gîn-hoat/gûn-hoat","jōe-kiám/lōe-kiám","chhāⁿ","gím-siù","tìn-soah","chām","thih-thah","siak","chhîm","chha̍k","chhoànn","ia̍t-lám","khoah-pak","chhoàng","koaiⁿ-chhia/kuiⁿ-chhia","chhián","a-sa-puh-luh","hām","cha̍p-chhâ","ke-chê-kin/koe-chôe-kun","hia-kóng","hāng","niá-pan","gia̍h-gōa","hong-chhoe-ji̍t-pha̍k/hong-chhe-li̍t-pha̍k","hiuⁿ","hiang-hm̂","hiong-hoa","phiàn","kiau-ngō͘","nāu-pâng","ut-chut","thoh","pih","thim","ho̍h","be̍h-gê","môa-saⁿ","be̍k-khè/be̍k-khòe","thuh","giàng","phiāng","gâu","chi̍p","khat","chhōa","chhoh","phu̍t","oáiⁿ","khiū","kauh"]
    checker(list(zip(additional_c, additional)), c, c_north)