from taibun.taibun import Converter
from utils import checker

c = Converter(system="Tongiong", punctuation='none')
c_north = Converter(system="Tongiong", dialect="north", punctuation='none')

def test_tailo_initials():
    bilabial = ["邊,bian","波,por","毛,mŏr","文,bhŭn"]
    checker(bilabial, c, c_north)
    alveolar = ["地,dē/duē","他,tann","曾,zan","出,cūt","衫,sann","耐,nāi","熱衫,ruâ-sann/luâ-sann","柳,liù"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["尖,ziam","手,ciù","寫,sià","入,rip/lip"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求,giŭ","去,kî","雅,ngà","語,ghì/ghù","喜,hì"]
    checker(velar, c, c_north)

def test_tailo_vowels_and_rhymes():
    front = ["衣,i","禮,lè","圓,ĭnn","生死,sēnn-sì/sīnn-sì"]
    checker(front, c, c_north)
    central = ["高,gor","查問,zā-bhūn","衫,sann"]
    checker(central, c, c_north)
    back = ["污,u","烏,or","張,diunn","唔,onn"]
    checker(back, c, c_north)

def test_tailo_finals():
    nasal = ["啉,lim","新,sin","紅,ăng"]
    checker(nasal, c, c_north)
    stop = ["汁,ziāp","蝨,sāt","國,gōk","食,ziah"]
    checker(stop, c, c_north)
    syllabic = ["姆,m̀","酸,sng"]
    checker(syllabic, c, c_north)