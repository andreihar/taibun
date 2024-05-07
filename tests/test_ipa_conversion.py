from taibun.taibun import Converter
from utils import checker

c = Converter(system="IPA", punctuation='none')
c_north = Converter(system="IPA", dialect="north", punctuation='none')

def test_ipa_initials():
    bilabial = ["啡,pi⁴⁴/pi⁵⁵","波,pʰə⁴⁴/pʰo⁵⁵","毛,mɔ̃²⁵/mɔ̃²⁴","麻,ba²⁵/ba²⁴"]
    checker(bilabial, c, c_north)
    alveolar = ["地,te²²/tue³³","唾,tʰə¹¹/tʰo²¹","早,tsa⁵³/tsa⁵¹","厝,tsʰu¹¹/tsʰu²¹","思,su⁴⁴/su⁵⁵","耐,nãi²²/nãi³³","如,dzu²⁵/lu²⁴","柳,liu⁵³/liu⁵¹"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["遮,tɕia⁴⁴/tɕia⁵⁵","手,tɕʰiu⁵³/tɕʰiu⁵¹","寫,ɕia⁵³/ɕia⁵¹","而,dʑi²⁵/li²⁴"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求,kiu²⁵/kiu²⁴","去,kʰi¹¹/kʰi²¹","雅,ŋã⁵³/ŋã⁵¹","語,gi⁵³/gu⁵¹","喜,hi⁵³/hi⁵¹"]
    checker(velar, c, c_north)

def test_ipa_vowels_and_rhymes():
    front = ["衣,i⁴⁴/i⁵⁵","會,e²²/e³³","圓,ĩ²⁵/ĩ²⁴","楹,ẽ²⁵/ẽ²⁴"]
    checker(front, c, c_north)
    central = ["阿,ə⁴⁴/o⁵⁵","亞,a⁴⁴/a⁵⁵","餡,ã²²/ã³³"]
    checker(central, c, c_north)
    back = ["禹,u⁵³/u⁵¹","烏,ɔ⁴⁴/ɔ⁵⁵","張,tiũ⁴⁴/tiũ⁵⁵","唔,ɔ̃⁴⁴/ɔ̃⁵⁵"]
    checker(back, c, c_north)

def test_ipa_finals():
    nasal = ["音,im⁴⁴/im⁵⁵","寅,in²⁵/in²⁴","紅,aŋ²⁵/aŋ²⁴"]
    checker(nasal, c, c_north)
    stop = ["葉,iap̚⁵/iap̚⁴","楬,at̚²¹/at̚³²","惡,ɔk̚²¹/ɔk̚³²","曷,aʔ⁵/aʔ⁴"]
    checker(stop, c, c_north)
    syllabic = ["姆,m̩⁵³/m̩⁵¹","黃,ŋ̍²⁵/ŋ̍²⁴"]
    checker(syllabic, c, c_north)

def test_ipa_syllables_additional():
    additional = ["㨻,tsã²²/tsã³³","一概,it̚²¹ kʰai¹¹/it̚³² kʰai²¹","三層,sam⁴⁴ tsan¹¹/sam⁵⁵ tsan²¹","不屑,put̚²¹ sut̚²¹/put̚³² sut̚³²","丑,tʰiu⁵³/tʰiu⁵¹","丼,tɔm²⁵/tɔm²⁴","乎,hɔ̃ʔ/hɔ̃ʔ","乞食,kʰit̚²¹ tɕiaʔ⁵/kʰit̚³² tɕiaʔ⁴","亂鐘,luan²² tɕiɪŋ⁴⁴/luan³³ tɕiɪŋ⁵⁵","交落,ka⁴⁴ lauʔ⁵/ka⁵⁵ lauʔ⁴","人間,dʑin²⁵ kan⁴⁴/lin²⁴ kan⁵⁵","仰角,giɔŋ⁵³ kak̚²¹/giɔŋ⁵¹ kak̚³²","休克,hiu⁴⁴ kʰiɪk̚²¹/hiu⁵⁵ kʰiɪk̚³²","侮辱,bu⁵³ dʑiɔk̚⁵/bu⁵¹ liɔk̚⁴","停電,tʰiɪŋ²⁵ tiɛn²²/tʰiɪŋ²⁴ tiɛn³³","偝,ãi²²/iaŋ³³","傳接,tʰuan²⁵ tɕiap̚²¹/tʰuan²⁴ tɕiap̚³²","僥倖,hiau⁴⁴ hiɪŋ²²/hiau⁵⁵ hiɪŋ³³","儼硬,giam⁵³ ŋẽ²²/giam⁵¹ ŋĩ³³","兄哥,hiã⁴⁴ kə⁴⁴/hiã⁵⁵ ko⁵⁵","充作,tɕʰiɔŋ⁴⁴ tsɔk̚²¹/tɕʰiɔŋ⁵⁵ tsɔk̚³²","免費,biɛn⁵³ hui¹¹/biɛn⁵¹ hui²¹","入口,dʑip̚⁵ kʰau⁵³/lip̚⁴ kʰau⁵¹","八仙,pat̚²¹ ɕiɛn⁴⁴/pat̚³² ɕiɛn⁵⁵","八月節,peʔ²¹ gueʔ⁵ tseʔ²¹/pueʔ³² geʔ⁴ tsueʔ³²","冇浡,pʰã¹¹ pʰuʔ⁵/pʰã²¹ pʰuʔ⁴","冰雹,piɪŋ⁴⁴ pʰauʔ⁵/piɪŋ⁵⁵ pʰauʔ⁴","刐,tãi⁵³/tãi⁵¹","判斷,pʰuã¹¹ tuan¹¹/pʰuã²¹ tuan²¹","別莊,piɛt̚⁵ tsɔŋ⁴⁴/piɛt̚⁴ tsɔŋ⁵⁵","刮,kueʔ²¹/kuiʔ³²","剔斥,tʰak̚²¹ tʰiɪk̚²¹/tʰak̚³² tʰiɪk̚³²","割禮,kat̚²¹ le⁵³/kat̚³² le⁵¹","劃,ueʔ⁵/uiʔ⁴","加快,ka⁴⁴ kʰuai¹¹/ka⁵⁵ kʰuai²¹","劣,luat̚⁵/luat̚⁴","劫棺,kiap̚²¹ kuan⁴⁴/kiap̚³² kuan⁵⁵","匆促,tsʰɔŋ⁴⁴ tɕʰiɔk̚²¹/tsʰɔŋ⁵⁵ tɕʰiɔk̚³²","匹敵,pʰit̚²¹ tiɪk̚⁵/pʰit̚³² tiɪk̚⁴","半遂,puan¹¹ sui²²/puan²¹ sui³³","協和,hiap̚⁵ hə²⁵/hiap̚⁴ ho²⁴","卡片,kʰaʔ²¹ pʰĩ¹¹/kʰaʔ³² pʰĩ²¹","卯名,bau⁵³ miã²⁵/bau⁵¹ miã²⁴","卯落去,mãuʔ²¹ ləʔ⁵ kʰi¹¹/mãuʔ³² loʔ⁴ kʰi²¹","危險,gui²⁵ hiam⁵³/gui²⁴ hiam⁵¹","卵包,nŋ̍²² pau⁴⁴/nŋ̍³³ pau⁵⁵","參照,tsʰam⁴⁴ tɕiau¹¹/tsʰam⁵⁵ tɕiau²¹","合歡,hap̚⁵ huan⁴⁴/hap̚⁴ huan⁵⁵","含蓄,ham²⁵ tʰiɔk̚²¹/ham²⁴ tʰiɔk̚³²","吭,kʰŋ̍ʔ²¹/kʰŋ̍ʔ³²","吸汗,kʰip̚²¹ kuã²²/kʰip̚³² kuã³³","吻笑,bun⁵³ tɕʰiə¹¹/bun⁵¹ tɕʰio²¹","呃酸,eʔ²¹ sŋ̍⁴⁴/eʔ³² sŋ̍⁵⁵","呿,kʰuʔ²¹/kʰuʔ³²","品嘗,pʰin⁵³ ɕiɔŋ²⁵/pʰin⁵¹ ɕiɔŋ²⁴","哈啾,haʔ²¹ tɕʰiũ¹¹/haʔ³² tɕʰiũ²¹","哈氣,ha⁴⁴ kʰui¹¹/ha⁵⁵ kʰui²¹","哼呻,hãi⁴⁴ tsʰan⁴⁴/hãi⁵⁵ tsʰan⁵⁵","唉,haiʔ²¹/haiʔ³²","喀,kʰẽʔ⁵/kʰẽʔ⁴","喃,nãuʔ²¹/nãuʔ³²","喓,iaũ⁴⁴/iaũ⁵⁵","喔,ɔʔ/ɔʔ","喝令,huaʔ²¹ liɪŋ²²/huaʔ³² liɪŋ³³","喢,sãʔ²¹/sãʔ³²","嗙,pʰŋ̍ʔ²¹/pʰŋ̍ʔ³²","嗾,tsak̚⁵/tsak̚⁴","嘈嘈唸,tsʰauʔ⁵ tsʰauʔ⁵ liam²²/tsʰauʔ⁴ tsʰauʔ⁴ liam³³","嘐潲,hau⁴⁴ ɕiau²⁵/hau⁵⁵ ɕiau²⁴","噎,uʔ²¹/uʔ³²","噯,aiʔ²¹/aiʔ³²","噷,hm̩ʔ⁵/hm̩ʔ⁴","嚇驚,heʔ²¹ kiã⁴⁴/heʔ³² kiã⁵⁵","嚓,tɕʰiak̚⁵/tɕʰiak̚⁴","嚷,dʑiaŋ⁵³/liɔŋ⁵¹","嚾,uaŋ⁴⁴/uaŋ⁵⁵","囤糴,tun⁵³ tiaʔ⁵/tun⁵¹ tiaʔ⁴","困局,kʰun¹¹ kiɔk̚⁵/kʰun²¹ kiɔk̚⁴","圓參,ĩ²⁵ sɔm⁴⁴/ĩ²⁴ sɔm⁵⁵","在,tsai²²/tsai³³","坉塗,tʰun²² tʰɔ²⁵/tʰun³³ tʰɔ²⁴","坑谷,kʰẽ⁴⁴ kɔk̚²¹/kʰĩ⁵⁵ kɔk̚³²","坱埃,iɪŋ⁴⁴ ia⁴⁴/iɪŋ⁵⁵ ia⁵⁵","垃圾,laʔ²¹ sap̚²¹/laʔ³² sap̚³²","基金,ki⁴⁴ kim⁴⁴/ki⁵⁵ kim⁵⁵","堯韭,giau²⁵ ku⁵³/giau²⁴ ku⁵¹","塌替,tʰap̚²¹ tʰe¹¹/tʰap̚³² tʰue²¹","壁畫,piaʔ²¹ ue²²/piaʔ³² ue³³","壓模,ap̚²¹ bɔ²⁵/ap̚³² bɔ²⁴","外甥,gue²² ɕiɪŋ⁴⁴/gue³³ ɕiɪŋ⁵⁵","大山,Tua²² suã⁴⁴/Tua³³ suã⁵⁵","天光,tʰĩ⁴⁴ kŋ̍⁴⁴/tʰĩ⁵⁵ kŋ̍⁵⁵","天后,tʰiɛn⁴⁴ hiə²²/tʰiɛn⁵⁵ hio³³","太魯閣,Tʰai¹¹ lɔ⁵³ kəʔ²¹/Tʰai²¹ lɔ⁵¹ koʔ³²","央及,iaŋ⁴⁴ kip̚⁵/iaŋ⁵⁵ kip̚⁴","奇雙,kʰia⁴⁴ ɕiaŋ⁴⁴/kʰia⁵⁵ ɕiaŋ⁵⁵","奔喪,pʰun⁴⁴ sɔŋ⁴⁴/pʰun⁵⁵ sɔŋ⁵⁵","好客,hɔ̃¹¹ kʰeʔ²¹/hɔ̃²¹ kʰeʔ³²","妙,miãu²²/miãu³³","妝娗,tsŋ̍⁴⁴ tʰã²²/tsŋ̍⁵⁵ tʰã³³","妾,tɕʰiap̚²¹/tɕʰiap̚³²","姓,sẽ¹¹/ɕĩ²¹","媽媽,mã⁴⁴ mã⁴⁴/mã⁵⁵ mã⁵⁵","孵,pu²²/pu³³","學園,hak̚⁵ hŋ̍²⁵/hak̚⁴ hŋ̍²⁴","學歹,əʔ⁵ pʰãi⁵³/oʔ⁴ pʰãi⁵¹","孽,giɛt̚⁵/giɛt̚⁴","宅,tʰeʔ⁵/tʰeʔ⁴","安眠,an⁴⁴ bin²⁵/an⁵⁵ bin²⁴","寄來,kia¹¹ lai²⁵/kia²¹ lai²⁴","密實,bat̚⁵ tsat̚⁵/bat̚⁴ tsat̚⁴","專員,tsuan⁴⁴ uan²⁵/tsuan⁵⁵ uan²⁴","尿鈷,dʑiə²² kɔ⁵³/lio³³ kɔ⁵¹","屁,pʰui¹¹/pʰui²¹","屆時,kai¹¹ ɕi²⁵/kai²¹ ɕi²⁴","屈橋,kʰut̚²¹ kiə²⁵/kʰut̚³² kio²⁴","屏遮那,He¹¹ sen⁴⁴ nã⁵³/He²¹ sen⁵⁵ nã⁵¹","屐,kiaʔ⁵/kiaʔ⁴","岩鹽,gam²⁵ iam²⁵/gam²⁴ iam²⁴","岳父,gak̚⁵ hu²²/gak̚⁴ hu³³","年表,nĩ²⁵ piə⁵³/nĩ²⁴ pio⁵¹","店租,tiam¹¹ tsɔ⁴⁴/tiam²¹ tsɔ⁵⁵","庵廟,am⁴⁴ biə²²/am⁵⁵ bio³³","廿,dʑiap̚⁵/liap̚⁴","彪,piu⁴⁴/piu⁵⁵","彼樣,hit̚²¹ iũ²²/hit̚³² iũ³³","徼,kʰiə¹¹/kʰio²¹","忍心,dʑim⁵³ ɕim⁴⁴/lim⁵¹ ɕim⁵⁵","快活,kʰuĩ¹¹ uaʔ⁵/kʰuĩ²¹ uaʔ⁴","忽然,hut̚²¹ dʑiɛn²⁵/hut̚³² liɛn²⁴","怦,pʰẽ²²/pʰẽ³³","怯膽,kʰiap̚²¹ tã⁵³/kʰiap̚³² tã⁵¹","恐畏,kʰiɔŋ⁵³ ui¹¹/kʰiɔŋ⁵¹ ui²¹","惜略,ɕiəʔ²¹ liəʔ⁵/ɕioʔ³² lioʔ⁴","愕,gɔk̚⁵/gɔk̚⁴","愣,gaŋ²²/gaŋ³³","慼心,tsʰeʔ²¹ ɕim⁴⁴/tsʰueʔ³² ɕim⁵⁵","憚,tan²²/tan³³","懦,nɔ̃²²/nɔ̃³³","懷念,huai²⁵ liam²²/huai²⁴ liam³³","戇,gɔŋ²²/gɔŋ³³","扒飯,pe⁴⁴ pŋ̍²²/pe⁵⁵ pŋ̍³³","扭尻川,ŋiũ⁵³ kʰa⁴⁴ tsʰŋ̍⁴⁴/ŋiũ⁵¹ kʰa⁵⁵ tsʰŋ̍⁵⁵","抓癢,dʑiau¹¹ tɕiũ²²/liau²¹ tɕiũ³³","披埕,pʰi⁴⁴ tiã²⁵/pʰi⁵⁵ tiã²⁴","抹粉,buaʔ²¹ hun⁵³/buaʔ³² hun⁵¹","抾拾,kʰiəʔ²¹ ɕip̚⁵/kʰioʔ³² ɕip̚⁴","拆壇,tʰiaʔ²¹ tuã²⁵/tʰiaʔ³² tuã²⁴","拋出,pʰau⁴⁴ tsʰut̚²¹/pʰau⁵⁵ tsʰut̚³²","拋捎,pʰa⁴⁴ sa⁴⁴/pʰa⁵⁵ sa⁵⁵","拍插,pʰaʔ²¹ tsʰap̚²¹/pʰaʔ³² tsʰap̚³²","拖直,tʰua⁴⁴ tit̚⁵/tʰua⁵⁵ tit̚⁴","招倚,tɕiə⁴⁴ ua⁵³/tɕio⁵⁵ ua⁵¹","括流,kuaʔ²¹ lau²⁵/kuaʔ³² lau²⁴","指,tsãi⁵³/tsãi⁵¹","挓,tʰa¹¹/tʰa²¹","挕捒,hĩ¹¹ sak̚²¹/hĩ²¹ sak̚³²","挨餓,ai⁴⁴ gə²²/ai⁵⁵ go³³","掀冊,hiɛn⁴⁴ tsʰeʔ²¹/hiɛn⁵⁵ tsʰeʔ³²","掃蕩,sau¹¹ tɔŋ²²/sau²¹ tɔŋ³³","掇,tuaʔ²¹/tuaʔ³²","掙,tɕiã²²/tɕiã³³","掩目雞,ɔm⁴⁴ bak̚⁵ ke⁴⁴/ɔm⁵⁵ bak̚⁴ kue⁵⁵","插春,tsʰaʔ²¹ tsʰun⁴⁴/tsʰaʔ³² tsʰun⁵⁵","揬,tuʔ⁵/tuʔ⁴","搐,tiuʔ²¹/tiuʔ³²","搭嚇,taʔ²¹ hiãʔ²¹/taʔ³² hiãʔ³²","搭里霧,Ta²² li⁵³ buʔ²¹/Ta³³ li⁵¹ buʔ³²","摳,kʰaũʔ⁵/kʰaũʔ⁴","撇清,pʰiɛt̚²¹ tɕʰiɪŋ⁴⁴/pʰiɛt̚³² tɕʰiɪŋ⁵⁵","撓,ŋiãu⁵³/ŋiãu⁵¹","撤職,tʰiɛt̚²¹ tɕit̚²¹/tʰiɛt̚³² tɕit̚³²","擉,tiak̚⁵/tiak̚⁴","擔當,tam⁴⁴ tŋ̍⁴⁴/tam⁵⁵ tŋ̍⁵⁵","擗,pʰiak̚⁵/pʰiak̚⁴","攀登,pʰan⁴⁴ tiɪŋ⁴⁴/pʰan⁵⁵ tiɪŋ⁵⁵","攔閘,nuã²⁵ tsaʔ⁵/nuã²⁴ tsaʔ⁴","敱,kʰãi⁵³/kʰãi⁵¹","斟酒,tʰin²⁵ tɕiu⁵³/tʰin²⁴ tɕiu⁵¹","方興未艾,hɔŋ⁴⁴ hiɪŋ⁴⁴ bi²² ŋãi²²/hɔŋ⁵⁵ hiɪŋ⁵⁵ bi³³ ŋãi³³","昨,tsəʔ⁵/tsoʔ⁴","晚會,buan⁵³ hue²²/buan⁵¹ hue³³","晴,tsẽ²⁵/tsẽ²⁴","晾,nẽ²⁵/nẽ²⁴","曲線,kʰiɔk̚²¹ suã¹¹/kʰiɔk̚³² suã²¹","朗讀,lɔŋ⁵³ tʰɔk̚⁵/lɔŋ⁵¹ tʰɔk̚⁴","木業,bɔk̚⁵ giap̚⁵/bɔk̚⁴ giap̚⁴","末路,buat̚⁵ lɔ²²/buat̚⁴ lɔ³³","杵,tʰu⁵³/tʰu⁵¹","枴,kuai⁵³/kuai⁵¹","染,dʑiam⁵³/liam⁵¹","校閱,kau¹¹ uat̚⁵/kau²¹ uat̚⁴","核可,hiɪk̚⁵ kʰə⁵³/hiɪk̚⁴ kʰo⁵¹","桌屜,təʔ²¹ tʰuaʔ²¹/toʔ³² tʰuaʔ³²","榆,dʑiu²⁵/liu²⁴","標本,piau⁴⁴ pun⁵³/piau⁵⁵ pun⁵¹","樸實,pʰəʔ²¹ ɕit̚⁵/pʰoʔ³² ɕit̚⁴","橫扴,huãi²⁵ keʔ⁵/huĩ²⁴ keʔ⁴","檨,suãi²²/suãi³³","欶,suʔ²¹/suʔ³²","歇影,hiəʔ²¹ iã⁵³/hioʔ³² iã⁵¹","歌譜,kua⁴⁴ pʰɔ⁵³/kua⁵⁵ pʰɔ⁵¹","歡度,huã⁴⁴ tɔ²²/huã⁵⁵ tɔ³³","歪斜,uai⁴⁴ tsʰuaʔ⁵/uai⁵⁵ tsʰuaʔ⁴","每擺,muĩ⁵³ pai⁵³/muĩ⁵¹ pai⁵¹","沃雨,ak̚²¹ hɔ²²/ak̚³² hɔ³³","沉著,tim²⁵ tiɔk̚⁵/tim²⁴ tiɔk̚⁴","沒藥,but̚⁵ iəʔ⁵/but̚⁴ ioʔ⁴","沓,tauʔ⁵/tauʔ⁴","沓滴,tap̚⁵ tiʔ²¹/tap̚⁴ tiʔ³²","沖水,tɕʰiaŋ²⁵ tsui⁵³/tɕʰiaŋ²⁴ tsui⁵¹","沫,pʰueʔ⁵/pʰeʔ⁴","海蟹,hai⁵³ he²²/hai⁵¹ he³³","涼腔,liaŋ²⁵ kʰiaŋ⁴⁴/liaŋ²⁴ kʰiaŋ⁵⁵","添設,tʰiam⁴⁴ ɕiɛt̚²¹/tʰiam⁵⁵ ɕiɛt̚³²","渺茫,biau⁵³ bɔŋ²⁵/biau⁵¹ bɔŋ²⁴","湠叢,tʰuã¹¹ tsaŋ²⁵/tʰuã²¹ tsaŋ²⁴","滅無,biɛt̚⁵ bə²⁵/biɛt̚⁴ bo²⁴","漂浮,pʰiau⁴⁴ pʰu²⁵/pʰiau⁵⁵ pʰu²⁴","漉屎,lɔk̚²¹ sai⁵³/lɔk̚³² sai⁵¹","漚肥,au⁴⁴ pui²⁵/au⁵⁵ pui²⁴","漳,tɕiaŋ⁴⁴/tɕiaŋ⁵⁵","潑扇,pʰuaʔ²¹ ɕĩ¹¹/pʰuaʔ³² ɕĩ²¹","潑賤,pʰuat̚²¹ tɕian²²/pʰuat̚³² tɕian³³","潤餅,dzun²² piã⁵³/lun³³ piã⁵¹","澩,haũʔ⁵/haũʔ⁴","激力,kiɪk̚²¹ lat̚⁵/kiɪk̚³² lat̚⁴","濺,tsuã²²/tsuã³³","煏,piak̚²¹/piak̚³²","煠,saʔ⁵/saʔ⁴","煤,muẽ²⁵/muẽ²⁴","熁,hãʔ²¹/hãʔ³²","熊,him²⁵/him²⁴","熱烈,dʑiɛt̚⁵ liɛt̚⁵/liɛt̚⁴ liɛt̚⁴","爁,nãʔ²¹/nãʔ³²","爹,tia⁴⁴/tia⁵⁵","牚,tʰẽ¹¹/tʰẽ²¹","牛膝,giu²⁵ tɕʰiɪk̚²¹/giu²⁴ tɕʰiɪk̚³²","物,mĩʔ⁵/mŋ̍ʔ⁴","物代,mĩʔ²¹ tai²²/mĩʔ³² tai³³","牽強,kʰiɛn⁴⁴ kiɔŋ²⁵/kʰiɛn⁵⁵ kiɔŋ²⁴","牽磕,kʰan⁴⁴ kʰap̚⁵/kʰan⁵⁵ kʰap̚⁴","猛勇,biɪŋ⁵³ iɔŋ⁵³/biɪŋ⁵¹ iɔŋ⁵¹","玉環,giɪk̚⁵ kʰuan²⁵/giɪk̚⁴ kʰuan²⁴","玉蘭,giɔk̚⁵ lan²⁵/giɔk̚⁴ lan²⁴","玩具,guan⁵³ kʰu²²/guan⁵¹ kʰu³³","甘苦,kam⁴⁴ kʰɔ⁵³/kam⁵⁵ kʰɔ⁵¹","甪毛,lut̚²¹ mŋ̍²⁵/lut̚³² mŋ̍²⁴","番薯,han⁴⁴ tɕi²⁵/han⁵⁵ tsu²⁴","疊尖,tʰiap̚⁵ tɕiam⁴⁴/tʰiap̚⁴ tɕiam⁵⁵","疏散,sɔ⁴⁴ san¹¹/sɔ⁵⁵ san²¹","癮甲,giɛn¹¹ kaʔ²¹/giɛn²¹ kaʔ³²","百般,paʔ²¹ puã⁴⁴/paʔ³² puã⁵⁵","益蟲,iɪk̚²¹ tʰiɔŋ²⁵/iɪk̚³² tʰiɔŋ²⁴","益閣,iaʔ²¹ kəʔ²¹/iaʔ³² koʔ³²","監牢,kã⁴⁴ lə²⁵/kã⁵⁵ lo²⁴","相閃,ɕiə⁴⁴ ɕiam⁵³/ɕio⁵⁵ ɕiam⁵¹","眉額,bai²⁵ hiaʔ⁵/bai²⁴ hiaʔ⁴","看,kʰuã¹¹/kʰuã²¹","眩痧,hin²⁵ sua⁴⁴/hin²⁴ sua⁵⁵","眵,tsʰuʔ²¹/tsʰuʔ³²","眼福,gan⁵³ hɔk̚²¹/gan⁵¹ hɔk̚³²","睚,kãi²⁵/kãi²⁴","督察,tɔk̚²¹ tsʰat̚²¹/tɔk̚³² tsʰat̚³²","瞌,kʰeʔ²¹/kʰueʔ³²","砌,kiʔ²¹/kiʔ³²","研缽,giɪŋ⁵³ puaʔ²¹/giɪŋ⁵¹ puaʔ³²","破缺,pʰua¹¹ kʰiʔ²¹/pʰua²¹ kʰiʔ³²","硩,teʔ²¹/teʔ³²","碗頭箸尾,uã⁵³ tʰau²⁵ ti²² bue⁵³/uã⁵¹ tʰau²⁴ tu³³ be⁵¹","碧潭,pʰiɪk̚²¹ tʰam²⁵/pʰiɪk̚³² tʰam²⁴","確保,kʰak̚²¹ pə⁵³/kʰak̚³² po⁵¹","磨坩,bua²⁵ kʰã⁴⁴/bua²⁴ kʰã⁵⁵","礁石,ta⁴⁴ tɕiəʔ⁵/ta⁵⁵ tɕioʔ⁴","礎,tsʰɔ⁵³/tsʰɔ⁵¹","礙著,gai²² tiəʔ⁵/gai³³ tioʔ⁴","票箱,pʰiə¹¹ ɕiũ⁴⁴/pʰio²¹ ɕiũ⁵⁵","禿,tʰut̚²¹/tʰut̚³²","空空,kʰaŋ⁴⁴ kʰaŋ⁴⁴/kʰaŋ⁵⁵ kʰaŋ⁵⁵","突,tut̚⁵/tut̚⁴","笠,leʔ⁵/leʔ⁴","筆算,pit̚²¹ suan¹¹/pit̚³² suan²¹","簇,tsʰɔk̚²¹/tsʰɔk̚³²","簸,pua¹¹/pua²¹","籤王,tɕʰiam⁴⁴ ɔŋ²⁵/tɕʰiam⁵⁵ ɔŋ²⁴","粒,liap̚⁵/liap̚⁴","糠瘡,kʰŋ̍⁴⁴ tsʰŋ̍⁴⁴/kʰŋ̍⁵⁵ tsʰŋ̍⁵⁵","糶,tʰiə¹¹/tʰio²¹","紂,tiu²²/tiu³³","納采,lap̚⁵ tsʰai⁵³/lap̚⁴ tsʰai⁵¹","索梯,səʔ²¹ tʰui⁴⁴/soʔ³² tʰui⁵⁵","累積,lui⁵³ tɕiɪk̚²¹/lui⁵¹ tɕiɪk̚³²","紺,kʰɔŋ⁵³/kʰɔŋ⁵¹","結疤,kiɛt̚²¹ pa⁴⁴/kiɛt̚³² pa⁵⁵","絕對,tsuat̚⁵ tui¹¹/tsuat̚⁴ tui²¹","絨布,dʑiɔŋ²⁵ pɔ¹¹/liɔŋ²⁴ pɔ²¹","經繭,kẽ⁴⁴ kiɛn⁵³/kĩ⁵⁵ kiɛn⁵¹","綠色,liɪk̚⁵ ɕiɪk̚²¹/liɪk̚⁴ ɕiɪk̚³²","緝捕,tɕʰip̚²¹ pɔ⁵³/tɕʰip̚³² pɔ⁵¹","緟,tʰɔŋ²²/tʰɔŋ³³","編篡,piɛn⁴⁴ tsʰuan¹¹/piɛn⁵⁵ tsʰuan²¹","缺糧,kʰuat̚²¹ nĩu²⁵/kʰuat̚³² nĩu²⁴","美味,bi⁵³ bi²²/bi⁵¹ bi³³","翕熱,hip̚²¹ dzuaʔ⁵/hip̚³² luaʔ⁴","聘請,pʰiɪŋ¹¹ tɕʰiã⁵³/pʰiɪŋ²¹ tɕʰiã⁵¹","聽錯,tʰiã⁴⁴ tsʰə¹¹/tʰiã⁵⁵ tsʰo²¹","肉目,baʔ²¹ bak̚⁵/baʔ³² bak̚⁴","脈搏,mẽʔ⁵ pʰɔk̚²¹/mẽʔ⁴ pʰɔk̚³²","脫節,tʰuat̚²¹ tɕiat̚²¹/tʰuat̚³² tɕiat̚³²","腔調,kʰiũ⁴⁴ tiau²²/kʰiũ⁵⁵ tiau³³","腰骨,iə⁴⁴ kut̚²¹/io⁵⁵ kut̚³²","腳錢,kiəʔ²¹ tɕĩ²⁵/kioʔ³² tɕĩ²⁴","船運,tsun²⁵ un²²/tsun²⁴ un³³","色牙,ɕiɪk̚²¹ ga²⁵/ɕiɪk̚³² ga²⁴","茅草,mãu²⁵ tsʰau⁵³/mãu²⁴ tsʰau⁵¹","草笠仔,tsʰau⁵³ leʔ⁵ a⁵³/tsʰau⁵¹ lueʔ⁴ a⁵¹","莢,ŋẽʔ²¹/ŋẽʔ³²","落落,lak̚²¹ ləʔ⁵/lak̚³² loʔ⁴","蓆,tɕʰiəʔ⁵/tɕʰioʔ⁴","蔥藕,tsʰaŋ⁴⁴ ŋãu²²/tsʰaŋ⁵⁵ ŋãu³³","蕨貓,kueʔ²¹ niãu⁴⁴/kueʔ³² niãu⁵⁵","薄待,pɔk̚⁵ tʰai²²/pɔk̚⁴ tʰai³³","薄膜,pəʔ⁵ mɔ̃ʔ⁵/poʔ⁴ mɔ̃ʔ⁴","薑,kiũ⁴⁴/kiũ⁵⁵","藃,hiauʔ²¹/hiauʔ³²","藩屏,pʰuan⁴⁴ pin²⁵/pʰuan⁵⁵ pin²⁴","虹,kʰiɪŋ²²/kʰiɪŋ³³","蚻,tsuaʔ⁵/tsuaʔ⁴","蛤蜊,kap̚²¹ la²⁵/kap̚³² la²⁴","蜀七,ɕiɔk̚⁵ tɕʰit̚²¹/ɕiɔk̚⁴ tɕʰit̚³²","蜈蚣,gia²⁵ kaŋ⁴⁴/gia²⁴ kaŋ⁵⁵","蜜月,bit̚⁵ guat̚⁵/bit̚⁴ guat̚⁴","蝕秤,ɕiʔ⁵ tɕʰin¹¹/ɕiʔ⁴ tɕʰin²¹","蝛,bui⁴⁴/bui⁵⁵","蝨,sat̚²¹/sat̚³²","蟯桮,giə²⁵ pue⁴⁴/gio²⁴ pue⁵⁵","蟯蟯動,ŋiãuʔ⁵ ŋiãuʔ⁵ taŋ²²/ŋiãuʔ⁴ ŋiãuʔ⁴ taŋ³³","蟳,tɕim²⁵/tɕim²⁴","蟶坪,tʰan⁴⁴ pʰiã²⁵/tʰan⁵⁵ pʰiã²⁴","蠓罩,baŋ⁵³ tau¹¹/baŋ⁵¹ tau²¹","蠘,tɕʰiʔ⁵/tɕʰiʔ⁴","蠻皮病,ban²⁵ pʰue²⁵ pẽ²²/ban²⁴ pʰe²⁴ pĩ³³","血油,hueʔ²¹ iu²⁵/huiʔ³² iu²⁴","血緣,hiɛt̚²¹ iɛn²⁵/hiɛt̚³² iɛn²⁴","裂縫,liʔ⁵ pʰaŋ²²/liʔ⁴ pʰaŋ³³","裂隙,liaʔ²¹ kʰiaʔ²¹/liaʔ³² kʰiaʔ³²","褪,tʰŋ̍¹¹/tʰŋ̍²¹","褫奪,tʰi⁵³ tuat̚⁵/tʰi⁵¹ tuat̚⁴","襟章,kʰim⁴⁴ tɕiɔŋ⁴⁴/kʰim⁵⁵ tɕiɔŋ⁵⁵","襪束,bueʔ⁵ sɔk̚²¹/bueʔ⁴ sɔk̚³²","規暝,kui⁴⁴ mẽ²⁵/kui⁵⁵ mĩ²⁴","覕喙,biʔ²¹ tsʰui¹¹/biʔ³² tsʰui²¹","觸纏,tak̚²¹ tĩ²⁵/tak̚³² tĩ²⁴","訣說,kuat̚²¹ suat̚²¹/kuat̚³² suat̚³²","詰舌,kʰiɛt̚²¹ tɕiʔ⁵/kʰiɛt̚³² tɕiʔ⁴","誇張,kʰua⁴⁴ tiɔŋ⁴⁴/kʰua⁵⁵ tiɔŋ⁵⁵","諜,tiap̚⁵/tiap̚⁴","謔削,giəʔ⁵ ɕiaʔ²¹/gioʔ⁴ ɕiaʔ³²","謗大,pɔŋ¹¹ tua²²/pɔŋ²¹ tua³³","謙遜,kʰiam⁴⁴ sun¹¹/kʰiam⁵⁵ sun²¹","謬誤,biu²² gɔ²²/biu³³ gɔ³³","謼,hɔʔ²¹/hɔʔ³²","豐沛,pʰɔŋ⁴⁴ pʰai¹¹/pʰɔŋ⁵⁵ pʰai²¹","買囑,mãi⁵³ tɕiɔk̚²¹/mãi⁵¹ tɕiɔk̚³²","賴,lua²²/lua³³","赤疹,tɕʰiaʔ²¹ tɕin⁵³/tɕʰiaʔ³² tɕin⁵¹","超市,tɕʰiau⁴⁴ tɕʰi²²/tɕʰiau⁵⁵ tɕʰi³³","趖,sə²⁵/so²⁴","跋涉,puat̚⁵ ɕiap̚⁵/puat̚⁴ ɕiap̚⁴","跡,dʑiaʔ²¹/liaʔ³²","跤曲,kʰa⁴⁴ kʰiau⁴⁴/kʰa⁵⁵ kʰiau⁵⁵","跩,tsuãi²²/tsuãi³³","跳躂,tʰiau¹¹ tʰat̚²¹/tʰiau²¹ tʰat̚³²","躄倒,pʰiʔ²¹ tə⁵³/pʰiʔ³² to⁵¹","躡,nẽʔ²¹/nĩʔ³²","輕聲細說,kʰin⁴⁴ ɕiã⁴⁴ se¹¹ sueʔ²¹/kʰin⁵⁵ ɕiã⁵⁵ sue²¹ seʔ³²","轄境,hat̚²¹ kiɪŋ⁵³/hat̚³² kiɪŋ⁵¹","辟走,pʰiaʔ²¹ tsau⁵³/pʰiaʔ³² tsau⁵¹","迎神,ŋiã²⁵ ɕin²⁵/ŋiã²⁴ ɕin²⁴","迒,hã²²/hã³³","迫切,piɪk̚²¹ tɕʰiat̚²¹/piɪk̚³² tɕʰiat̚³²","迭,tiɛt̚⁵/tiɛt̚⁴","迸,piaŋ¹¹/piaŋ²¹","送達,saŋ¹¹ tat̚⁵/saŋ²¹ tat̚⁴","逝,tsua²²/tsua³³","遮勘,dʑia⁴⁴ kʰam¹¹/lia⁵⁵ kʰam²¹","邀約,iau⁴⁴ iɔk̚²¹/iau⁵⁵ iɔk̚³²","邑,ip̚²¹/ip̚³²","那通,nã⁵³ tʰaŋ⁴⁴/nã⁵¹ tʰaŋ⁵⁵","郁,hiɔk̚²¹/hiɔk̚³²","鄭,tẽ²²/tẽ³³","酷人,kʰɔk̚²¹ laŋ²⁵/kʰɔk̚³² laŋ²⁴","重青,taŋ²² tsʰẽ⁴⁴/taŋ³³ tɕʰĩ⁵⁵","釣艚,tiə¹¹ tsə²⁵/tio²¹ tso²⁴","銀髮,gin²⁵ huat̚²¹/gun²⁴ huat̚³²","銳減,dzue²² kiam⁵³/lue³³ kiam⁵¹","錚,tsʰã²²/tsʰã³³","錦繡,gim⁵³ ɕiu¹¹/gim⁵¹ ɕiu²¹","鎮煞,tin¹¹ suaʔ²¹/tin²¹ suaʔ³²","鏨,tsam²²/tsam³³","鐵塔,tʰiʔ²¹ tʰaʔ²¹/tʰiʔ³² tʰaʔ³²","鑠,ɕiak̚²¹/ɕiak̚³²","鑱,tɕʰim²⁵/tɕʰim²⁴","鑿,tsʰak̚⁵/tsʰak̚⁴","閂,tsʰuã¹¹/tsʰuã²¹","閱覽,iɛt̚⁵ lam⁵³/iɛt̚⁴ lam⁵¹","闊腹,kʰuaʔ²¹ pak̚²¹/kʰuaʔ³² pak̚³²","闖,tsʰuaŋ¹¹/tsʰuaŋ²¹","關車,kuãi⁴⁴ tɕʰia⁴⁴/kuĩ⁵⁵ tɕʰia⁵⁵","闡,tɕʰian⁵³/tɕʰian⁵¹","阿沙不魯,a⁴⁴ sa⁴⁴ puʔ²¹ luʔ²¹/a⁵⁵ sa⁵⁵ puʔ³² luʔ³²","陷,ham²²/ham³³","雜柴,tsap̚⁵ tsʰa²⁵/tsap̚⁴ tsʰa²⁴","雞齊根,ke⁴⁴ tse²⁵ kin⁴⁴/kue⁵⁵ tsue²⁴ kun⁵⁵","靴管,hia⁴⁴ kɔŋ⁵³/hia⁵⁵ kɔŋ⁵¹","項,haŋ²²/haŋ³³","領班,niã⁵³ pan⁴⁴/niã⁵¹ pan⁵⁵","額外,giaʔ⁵ gua²²/giaʔ⁴ gua³³","風吹日曝,hɔŋ⁴⁴ tsʰue⁴⁴ dʑit̚⁵ pʰak̚⁵/hɔŋ⁵⁵ tsʰe⁵⁵ lit̚⁴ pʰak̚⁴","香,hiũ⁴⁴/hiũ⁵⁵","香茅,hiaŋ⁴⁴ hm̩²⁵/hiaŋ⁵⁵ hm̩²⁴","香華,hiɔŋ⁴⁴ hua⁴⁴/hiɔŋ⁵⁵ hua⁵⁵","騙,pʰiɛn¹¹/pʰiɛn²¹","驕傲,kiau⁴⁴ ŋɔ̃²²/kiau⁵⁵ ŋɔ̃³³","鬧房,nãu²² paŋ²⁵/nãu³³ paŋ²⁴","鬱卒,ut̚²¹ tsut̚²¹/ut̚³² tsut̚³²","魠,tʰəʔ²¹/tʰoʔ³²","鱉,piʔ²¹/piʔ³²","鴆,tʰim⁴⁴/tʰim⁵⁵","鶴,həʔ⁵/hoʔ⁴","麥牙,beʔ⁵ ge²⁵/beʔ⁴ ge²⁴","麻衫,muã²⁵ sã⁴⁴/muã²⁴ sã⁵⁵","默契,biɪk̚⁵ kʰe¹¹/biɪk̚⁴ kʰue²¹","黜,tʰuʔ²¹/tʰuʔ³²","齴,giaŋ¹¹/giaŋ²¹","龐,pʰiaŋ²²/pʰiaŋ³³","𠢕,gau²⁵/gau²⁴","𠯗,tɕip̚⁵/tɕip̚⁴","𣁳,kʰat̚²¹/kʰat̚³²","𤆬,tsʰua²²/tsʰua³³","𧮙,tsʰəʔ²¹/tsʰoʔ³²","𧿳,pʰut̚⁵/pʰut̚⁴","𨂿,uãi⁵³/uãi⁵¹","𩚨,kʰiu²²/kʰiu³³","𩛩,kauʔ²¹/kauʔ³²"]
    checker(additional, c, c_north)