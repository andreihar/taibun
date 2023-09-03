from taibun.taibun import Converter
from utils import checker

def test_tailo_initials():
    c = Converter(system="Tailo", punctuation='none')
    c_north = Converter(system="Tailo", dialect="north", punctuation='none')

    bilabial = ["邊,pian","波,pho","毛,môo","文,bûn"]
    checker(bilabial, c, c_north)
    alveolar = ["地,tē/tuē","他,thann","曾,tsan","出,tshut","衫,sann","耐,nāi","熱衫,jua̍h-sann/lua̍h-sann","柳,liú"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["尖,tsiam","手,tshiú","寫,siá","入,ji̍p/li̍p"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求,kiû","去,khì","雅,ngá","語,gí/gú","喜,hí"]
    checker(velar, c, c_north)

def test_tailo_vowels_and_rhymes():
    c = Converter(system="Tailo", punctuation='none')
    c_north = Converter(system="Tailo", dialect="north", punctuation='none')

    front = ["衣,i","禮,lé","圓,înn","生死,senn-sí/sinn-sí"]
    checker(front, c, c_north)
    central = ["高,ko","查問,tsa-būn","衫,sann"]
    checker(central, c, c_north)
    back = ["污,u","烏,oo","張,tiunn","唔,onn"]
    checker(back, c, c_north)

def test_tailo_finals():
    c = Converter(system="Tailo", punctuation='none')
    c_north = Converter(system="Tailo", dialect="north", punctuation='none')

    nasal = ["啉,lim","新,sin","紅,âng"]
    checker(nasal, c, c_north)
    stop = ["汁,tsiap","蝨,sat","國,kok","食,tsia̍h"]
    checker(stop, c, c_north)
    syllabic = ["姆,ḿ","酸,sng"]
    checker(syllabic, c, c_north)