from taibun.taibun import Converter
from utils import checker

c = Converter(system="TLPA", punctuation='none')
c_north = Converter(system="TLPA", dialect="north", punctuation='none')

def test_tlpa_initials():
    bilabial = ["邊,pian1","波,pho1","毛,moo5","文,bun5"]
    checker(bilabial, c, c_north)
    alveolar = ["地,te7/tue7","他,thann1","曾,can1","出,chut4","衫,sann1","耐,nai7","熱衫,juah8 sann1/luah8 sann1","柳,liu2"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["尖,ciam1","手,chiu2","寫,sia2","入,jip8/lip8"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求,kiu5","去,khi3","雅,nga2","語,gi2/gu2","喜,hi2"]
    checker(velar, c, c_north)

def test_tlpa_vowels_and_rhymes():
    front = ["衣,i1","禮,le2","圓,inn5","生死,senn1 si2/sinn1 si2"]
    checker(front, c, c_north)
    central = ["高,ko1","查問,ca1 bun7","衫,sann1"]
    checker(central, c, c_north)
    back = ["污,u1","烏,oo1","張,tiunn1","唔,onn1"]
    checker(back, c, c_north)

def test_tlpa_finals():
    nasal = ["啉,lim1","新,sin1","紅,ang5"]
    checker(nasal, c, c_north)
    stop = ["汁,ciap4","蝨,sat4","國,kok4","食,ciah8"]
    checker(stop, c, c_north)
    syllabic = ["姆,m2","酸,sng1"]
    checker(syllabic, c, c_north)