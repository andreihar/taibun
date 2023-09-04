from taibun.taibun import Converter
from utils import checker

c = Converter(system="Pingyim", punctuation='none')
c_north = Converter(system="Pingyim", dialect="north", punctuation='none')

def test_pingyim_initials():
    bilabial = ["邊,biān","波,pō","毛,bbnoó","文,bbún"]
    checker(bilabial, c, c_north)
    alveolar = ["地,dê/duê","他,tnā","曾,zān","出,cūt","衫,snā","耐,nâi","熱衫,zzuáhsnā/luáhsnā","柳,liǔ"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["尖,ziām","手,ciǔ","寫,siǎ","入,zzíp/líp"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求,giú","去,kì","雅,ggnǎ","語,ggǐ/ggǔ","喜,hǐ"]
    checker(velar, c, c_north)

def test_pingyim_vowels_and_rhymes():
    front = ["衣,yī","禮,lě","圓,ní","生死,snēsí/snīsí"]
    checker(front, c, c_north)
    central = ["高,gō","查問,zábûn","衫,snā"]
    checker(central, c, c_north)
    back = ["污,ū","烏,oō","張,dniū","唔,noō"]
    checker(back, c, c_north)

def test_pingyim_finals():
    nasal = ["啉,līm","新,sīn","紅,áng"]
    checker(nasal, c, c_north)
    stop = ["汁,ziāp","蝨,sāt","國,gōk","食,ziáh"]
    checker(stop, c, c_north)
    syllabic = ["姆,m̌","酸,sn̄g"]
    checker(syllabic, c, c_north)