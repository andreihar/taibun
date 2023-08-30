from taibun.taibun import Converter
from utils import checker

def test_initials():
    c = Converter(system="Tai-lo", punctuation='none')
    c_north = Converter(system="Tai-lo", dialect="north", punctuation='none')

    bilabial = ["邊界,pian-kài","波浪,pho-lōng","毛病,môo-pēnn/môo-pīnn","文法,bûn-huat"]
    checker(bilabial, c, c_north)
    alveolar = ["地面,tē-bīn/tuē-bīn","通好,thang-hó","棕蓑,tsang-sui","出任,tshut-jīm/tshut-līm","衫仔裾,sann-á-ki/sann-á-ku","耐用,nāi-iōng","熱人,jua̍h-lâng/lua̍h-lâng","柳丁,liú-ting"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["尖鑽,tsiam-tsǹg","手爪,tshiú-jiáu/tshiú-niáu","寫字,siá-jī/siá-lī","入口,ji̍p-kháu/li̍p-kháu"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求情,kiû-tsîng","去倒,khì-tò","雅氣,ngá-khì","台語,Tâi-gí/Tâi-gú","喜酒,hí-tsiú"]
    checker(velar, c, c_north)

def test_vowels_and_rhymes():
    c = Converter(system="Tai-lo", punctuation='none')
    c_north = Converter(system="Tai-lo", dialect="north", punctuation='none')

    front = ["依附,i-hù","禮物,lé-bu̍t","圓環,înn-khuân","生做,senn-tsò/sinn-tsuè"]
    checker(front, c, c_north)
    central = ["高明,ko-bîng","查某,tsa-bóo","衫仔櫥,sann-á-tû"]
    checker(central, c, c_north)
    back = ["有名,ū-miâ","烏暗,oo-àm","張持,tiunn-tî","可惡,khó-ònn"]
    checker(back, c, c_north)

def test_finals():
    c = Converter(system="Tai-lo", punctuation='none')
    c_north = Converter(system="Tai-lo", dialect="north", punctuation='none')

    nasal = ["啉,lim","新鮮,sin-sian","門斗,mn̂g-táu"]
    checker(nasal, c, c_north)
    stop = ["墨汁,ba̍k-tsiap","木蝨,ba̍k-sat","中國,Tiong-kok","食飯,tsia̍h-pn̄g"]
    checker(stop, c, c_north)