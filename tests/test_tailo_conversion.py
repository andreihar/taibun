from taibun.taibun import Converter
from utils import checker

c = Converter(system="Tailo", punctuation='none')
c_north = Converter(system="Tailo", dialect="north", punctuation='none')

def test_tailo_initials():
    bilabial = ["啡,pi","波,pho","毛,môo","猫,bâ"]
    checker(bilabial, c, c_north)
    alveolar = ["地,tē/tuē","唾,thò","早,tsá","厝,tshù","衫,su","耐,nāi","如,jû/lû","柳,liú"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["遮,tsia","手,tshiú","寫,siá","而,jî/lî"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求,kiû","去,khì","雅,ngá","語,gí/gú","喜,hí"]
    checker(velar, c, c_north)

def test_tailo_vowels_and_rhymes():
    front = ["衣,i","會,ē","圓,înn","楹,ênn"]
    checker(front, c, c_north)
    central = ["阿,o","亞,a","餡,ānn"]
    checker(central, c, c_north)
    back = ["禹,ú","烏,oo","張,tiunn","唔,onn"]
    checker(back, c, c_north)

def test_tailo_finals():
    nasal = ["音,im","寅,în","紅,âng"]
    checker(nasal, c, c_north)
    stop = ["葉,ia̍p","楬,at","惡,ok","曷,a̍h"]
    checker(stop, c, c_north)
    syllabic = ["姆,ḿ","黃,n̂g"]
    checker(syllabic, c, c_north)