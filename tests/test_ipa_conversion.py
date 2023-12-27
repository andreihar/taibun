from taibun.taibun import Converter
from utils import checker

c = Converter(system="IPA", punctuation='none')
c_north = Converter(system="IPA", dialect="north", punctuation='none')

def test_ipa_initials():
    bilabial = ["邊,piɛn⁴⁴/piɛn⁵⁵","波,pʰə⁴⁴/pʰɔ⁵⁵","毛,mɔ̃²⁵/mɔ̃²⁴","文,bun²⁵/bun²⁴"]
    checker(bilabial, c, c_north)
    alveolar = ["地,te²²/tue³³","他,tʰã⁴⁴/tʰã⁵⁵","曾,tsan⁴⁴/tsan⁵⁵","出,tsʰut̚²¹/tsʰut̚³²","衫,sã⁴⁴/sã⁵⁵","耐,nãi²²/nãi³³","熱衫,dzuaʔ⁵ sã⁴⁴/luaʔ⁴ sã⁵⁵","柳,liu⁵³/liu⁵¹"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["尖,tɕiam⁴⁴/tɕiam⁵⁵","手,tɕʰiu⁵³/tɕʰiu⁵¹","寫,ɕia⁵³/ɕia⁵¹","入,dʑip̚⁵/lip̚⁴"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求,kiu²⁵/kiu²⁴","去,kʰi¹¹/kʰi²¹","雅,ŋã⁵³/ŋã⁵¹","語,gi⁵³/gu⁵¹","喜,hi⁵³/hi⁵¹"]
    checker(velar, c, c_north)

def test_ipa_vowels_and_rhymes():
    front = ["衣,i⁴⁴/i⁵⁵","禮,le⁵³/le⁵¹","圓,ĩ²⁵/ĩ²⁴","生死,sẽ⁴⁴ ɕi⁵³/ɕĩ⁵⁵ ɕi⁵¹"]
    checker(front, c, c_north)
    central = ["高,kə⁴⁴/ko⁵⁵","查問,tsa⁴⁴ bun²²/tsa⁵⁵ bun³³","衫,sã⁴⁴/sã⁵⁵"]
    checker(central, c, c_north)
    back = ["污,u⁴⁴/u⁵⁵","烏,ɔ⁴⁴/ɔ⁵⁵","張,tiũ⁴⁴/tiũ⁵⁵","唔,ɔ̃⁴⁴/ɔ̃⁵⁵"]
    checker(back, c, c_north)

def test_ipa_finals():
    nasal = ["啉,lim⁴⁴/lim⁵⁵","新,ɕin⁴⁴/ɕin⁵⁵","紅,aŋ²⁵/aŋ²⁴"]
    checker(nasal, c, c_north)
    stop = ["汁,tɕiap̚²¹/tɕiap̚³²","蝨,sat̚²¹/sat̚³²","國,kɔk̚²¹/kɔk̚³²","食,tɕiaʔ⁵/tɕiaʔ⁴"]
    checker(stop, c, c_north)
    syllabic = ["姆,m̩⁵³/m̩⁵¹","酸,sŋ̍⁴⁴/sŋ̍⁵⁵"]
    checker(syllabic, c, c_north)

def test_ipa_additional():
    additional = ['聽,tʰiã⁴⁴/tʰiã⁵⁵','歹,pʰãi⁵³/pʰãi⁵¹','山/suã⁴⁴/suã⁵⁵','秧,ŋ̍⁴⁴/ŋ̍⁵⁵','甚物,ɕim²² mĩʔ⁵/ɕim³³ mŋ̍ʔ⁴','吉,kiɛt̚²¹/kiɛt̚³²','貓,niãu⁴⁴/niãu⁵⁵','名,miã²⁵/miã²⁴','然,dʑiɛn²⁵/liɛn²⁴','熱目,dʑiɛt̚⁵ bak̚⁵/liɛt̚⁴ bak̚⁴','兩,nŋ̍²²/nŋ̍³³','婸,giaŋ⁴⁴/giaŋ⁵⁵']
    checker(additional, c, c_north)