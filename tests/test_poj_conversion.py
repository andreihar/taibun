from taibun.taibun import Converter
from utils import checker

def test_poj_initials():
    c = Converter(system="POJ", punctuation='none')
    c_north = Converter(system="POJ", dialect="north", punctuation='none')

    bilabial = ["邊,pian","波,pho","毛,mô͘","文,bûn"]
    checker(bilabial, c, c_north)
    alveolar = ["地,tē/tōe","他,thaⁿ","曾,chan","出,chhut","衫,saⁿ","耐,nāi","熱衫,joa̍h-saⁿ/loa̍h-saⁿ","柳,liú"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["尖,chiam","手,chhiú","寫,siá","入,ji̍p/li̍p"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求,kiû","去,khì","雅,ngá","語,gí/gú","喜,hí"]
    checker(velar, c, c_north)

def test_poj_vowels_and_rhymes():
    c = Converter(system="POJ", punctuation='none')
    c_north = Converter(system="POJ", dialect="north", punctuation='none')

    front = ["衣,i","禮,lé","圓,îⁿ","生死,seⁿ-sí/siⁿ-sí"]
    checker(front, c, c_north)
    central = ["高,ko","查問,cha-būn","衫,saⁿ"]
    checker(central, c, c_north)
    back = ["污,u","烏,o͘","張,tiuⁿ","唔,oⁿ"]
    checker(back, c, c_north)

def test_poj_finals():
    c = Converter(system="POJ", punctuation='none')
    c_north = Converter(system="POJ", dialect="north", punctuation='none')

    nasal = ["啉,lim","新,sin","紅,âng"]
    checker(nasal, c, c_north)
    stop = ["汁,chiap","蝨,sat","國,kok","食,chia̍h"]
    checker(stop, c, c_north)
    syllabic = ["姆,ḿ","酸,sng"]
    checker(syllabic, c, c_north)