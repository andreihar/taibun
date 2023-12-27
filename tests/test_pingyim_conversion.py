from taibun.taibun import Converter
from utils import checker

c = Converter(system="Pingyim", punctuation='none')
c_north = Converter(system="Pingyim", dialect="north", punctuation='none')

def test_pingyim_initials():
    bilabial = ["啡,bī","波,pō","毛,bbnoó","猫,bbá"]
    checker(bilabial, c, c_north)
    alveolar = ["地,dê/duê","唾,tò","早,zǎ","厝,cù","思,sū","耐,lnâi","如,zzú/lú","柳,liǔ"]
    checker(alveolar, c, c_north)
    alveolo_palatal = ["遮,ziā","手,ciǔ","寫,siǎ","而,zzí/lí"]
    checker(alveolo_palatal, c, c_north)
    velar = ["求,giú","去,kì","雅,ggnǎ","語,ggǐ/ggǔ","喜,hǐ"]
    checker(velar, c, c_north)

def test_pingyim_vowels_and_rhymes():
    front = ["衣,yī","會,ê","圓,ní","楹,né"]
    checker(front, c, c_north)
    central = ["阿,ō","亞,ā","餡,nâ"]
    checker(central, c, c_north)
    back = ["禹,wǔ","烏,oō","張,dniū","唔,noō"]
    checker(back, c, c_north)

def test_pingyim_finals():
    nasal = ["音,yīm","寅,yín","紅,áng"]
    checker(nasal, c, c_north)
    stop = ["葉,yáp","楬,āt","惡,ōk","曷,áh"]
    checker(stop, c, c_north)
    syllabic = ["姆,m̌","黃,ńg"]
    checker(syllabic, c, c_north)

def test_pingyim_syllables_additional():
    additional = ["㨻,znâ","一概,yītkài","三層,sāmzàn","不屑,būtsūt","丑,tiǔ","丼,dóm","乎,hnoōh","乞食,kītziáh","亂鐘,luânzīng","交落,gāláoh","人間,zzíngān/língān","仰角,ggiǒnggāk","休克,hiūkīk","侮辱,bbǔzziók/bbǔliók","停電,tíngdiân","偝,nâi/yâng","傳接,tuánziāp","僥倖,hiāohîng","儼硬,ggiǎmggnê/ggiǎmggnî","兄哥,hināgō","充作,ciōngzōk","免費,bbiǎnhuì","入口,zzípkǎo/lípkǎo","八仙,bātsiān","八月節,bēhgguéhzēh/buēhggéhzuēh","冇浡,pnàpúh","冰雹,bīngpáoh","刐,dnǎi","判斷,punàduàn","別莊,biátzōng","刮,guēh/guīh","剔斥,tāktīk","割禮,gātlě","劃,wéh/wíh","加快,gākuài","劣,luát","劫棺,giāpguān","匆促,cōngciōk","匹敵,pītdík","半遂,buànsuî","協和,hiáphó","卡片,kāhpnì","卯名,bbǎobbniá","卯落去,bbnāohlóhkì","危險,gguíhiǎm","卵包,n̂gbāo","參照,cāmziào","合歡,háphuān","含蓄,hámtiōk","吭,kggn̄h","吸汗,kīpgunâ","吻笑,bbǔnciò","呃酸,ēhsn̄g","呿,kūh","品嘗,pǐnsióng","哈啾,hāhcniù","哈氣,hākuì","哼呻,hnāicān","唉,hāih","喀,knéh","喃,lnāoh","喓,yāolnn","喔,oōh","喝令,huāhlîng","喢,snāh","嗙,pggn̄h","嗾,zák","嘈嘈唸,cáohcáohliâm","嘐潲,hāosiáo","噎,ūh","噯,āih","噷,hbbńh","嚇驚,hēhginā","嚓,ciák","嚷,zziǎng/liǒng","嚾,wāng","囤糴,dǔndiáh","困局,kùngiók","圓參,nísōm","在,zâi","坉塗,tûntoó","坑谷,knēgōk/knīgōk","坱埃,yīngyā","垃圾,lāhsāp","基金,gīgīm","堯韭,ggiáogǔ","塌替,tāptè/tāptuè","壁畫,biāhwê","壓模,āpbboó","外甥,gguêsīng","大山,Duâsunā","天光,tnīgn̄g","天后,tiānhiô","太魯閣,Tàiloǒgōh","央及,yānggíp","奇雙,kiāsiāng","奔喪,pūnsōng","好客,hnoòkēh","妙,bbniâo","妝娗,zn̄gtnâ","妾,ciāp","姓,snè/snì","媽媽,bbnābbnā","孵,bû","學園,hákhńg","學歹,óhpnǎi","孽,ggiát","宅,téh","安眠,ānbbín","寄來,giàlái","密實,bbátzát","專員,zuānwán","尿鈷,zziôgoǒ/liôgoǒ","屁,puì","屆時,gàisí","屈橋,kūtgió","屏遮那,Hèsēnlnǎ","屐,giáh","岩鹽,ggámyám","岳父,ggákhû","年表,lníbiǒ","店租,diàmzoō","庵廟,āmbbiô","廿,zziáp/liáp","彪,biū","彼樣,hītniû","徼,kiò","忍心,zzǐmsīm/lǐmsīm","快活,kunìwáh","忽然,hūtzzián/hūtlián","怦,pnê","怯膽,kiāpdnǎ","恐畏,kiǒngwì","惜略,siōhlióh","愕,ggók","愣,ggâng","慼心,cēhsīm/cuēhsīm","憚,dân","懦,lnoô","懷念,huáiliâm","戇,ggông","扒飯,bēbn̂g","扭尻川,ggniǔkācn̄g","抓癢,zziàozniû/liàozniû","披埕,pīdiná","抹粉,bbuāhhǔn","抾拾,kiōhsíp","拆壇,tiāhduná","拋出,pāocūt","拋捎,pāsā","拍插,pāhcāp","拖直,tuādít","招倚,ziōwǎ","括流,guāhláo","指,znǎi","挓,tà","挕捒,hnìsāk","挨餓,āiggô","掀冊,hiāncēh","掃蕩,sàodông","掇,duāh","掙,zinâ","掩目雞,ōmbbákgē/ōmbbákguē","插春,cāhcūn","揬,dúh","搐,diūh","搭嚇,dāhhināh","搭里霧,Dâlǐbbūh","摳,káolnlnh","撇清,piātcīng","撓,ggniǎo","撤職,tiātzīt","擉,diák","擔當,dāmdn̄g","擗,piák","攀登,pāndīng","攔閘,lnuázáh","敱,knǎi","斟酒,tínziǔ","方興未艾,hōnghīngbbîggnâi","昨,zóh","晚會,bbuǎnhuê","晴,zné","晾,lné","曲線,kiōksunà","朗讀,lǒngtók","木業,bbókggiáp","末路,bbuátloô","杵,tǔ","枴,guǎi","染,zziǎm/liǎm","校閱,gàowát","核可,híkkǒ","桌屜,dōhtuāh","榆,zziú/liú","標本,biāobǔn","樸實,pōhsít","橫扴,hunáigéh/hunígéh","檨,sunâi","欶,sūh","歇影,hiōhyinǎ","歌譜,guāpoǒ","歡度,hunādoô","歪斜,wāicuáh","每擺,bbnuǐbǎi","沃雨,ākhoô","沉著,dímdiók","沒藥,bbútyóh","沓,dáoh","沓滴,dápdīh","沖水,ciángzuǐ","沫,puéh/péh","海蟹,hǎihê","涼腔,liángkiāng","添設,tiāmsiāt","渺茫,bbiǎobbóng","湠叢,tunàzáng","滅無,bbiátbbó","漂浮,piāopú","漉屎,lōksǎi","漚肥,āobuí","漳,ziāng","潑扇,puāhsnì","潑賤,puātziân","潤餅,zzûnbinǎ/lûnbinǎ","澩,háolnlnh","激力,gīklát","濺,zunâ","煏,biāk","煠,sáh","煤,bbnué","熁,hnāh","熊,hím","熱烈,zziátliát/liátliát","爁,lnāh","爹,diā","牚,tnè","牛膝,ggiúcīk","物,bbníh/ḿggnh","物代,bbnīhdâi","牽強,kiāngióng","牽磕,kānkáp","猛勇,bbǐngyǒng","玉環,ggíkkuán","玉蘭,ggióklán","玩具,gguǎnkû","甘苦,gāmkoǒ","甪毛,lūtmńg","番薯,hānzí/hānzú","疊尖,tiápziām","疏散,soōsàn","癮甲,ggiàngāh","百般,bāhbunā","益蟲,yīktióng","益閣,yāhgōh","監牢,gnāló","相閃,siōsiǎm","眉額,bbáihiáh","看,kunà","眩痧,hínsuā","眵,cūh","眼福,ggǎnhōk","睚,gnái","督察,dōkcāt","瞌,kēh/kuēh","砌,gīh","研缽,ggǐngbuāh","破缺,puàkīh","硩,dēh","碗頭箸尾,wnǎtáodîbbuě/wnǎtáodûbbě","碧潭,pīktám","確保,kākbǒ","磨坩,bbuáknā","礁石,dāzióh","礎,coǒ","礙著,ggâidióh","票箱,piòsniū","禿,tūt","空空,kāngkāng","突,dút","笠,léh","筆算,bītsuàn","簇,cōk","簸,buà","籤王,ciāmóng","粒,liáp","糠瘡,kn̄gcn̄g","糶,tiò","紂,diû","納采,lápcǎi","索梯,sōhtuī","累積,luǐzīk","紺,kǒng","結疤,giātbā","絕對,zuátduì","絨布,zzióngboò/lióngboò","經繭,gnēgiǎn/gnīgiǎn","綠色,líksīk","緝捕,cīpboǒ","緟,tông","編篡,biāncuàn","缺糧,kuātlniú","美味,bbǐbbî","翕熱,hīpzzuáh/hīpluáh","聘請,pìngcinǎ","聽錯,tinācò","肉目,bbāhbbák","脈搏,bbnéhpōk","脫節,tuātziāt","腔調,kniūdiâo","腰骨,yōgūt","腳錢,giōhzní","船運,zúnwn̂","色牙,sīkggá","茅草,bbnáocǎo","草笠仔,cǎoléhǎ/cǎoluéhǎ","莢,ggnēh","落落,lāklóh","蓆,cióh","蔥藕,cāngggnâo","蕨貓,guēhlniāo","薄待,bóktâi","薄膜,bóhbbnoóh","薑,gniū","藃,hiāoh","藩屏,puānbín","虹,kîng","蚻,zuáh","蛤蜊,gāplá","蜀七,siókcīt","蜈蚣,ggiágāng","蜜月,bbítgguát","蝕秤,síhcìn","蝛,bbuī","蝨,sāt","蟯桮,ggióbuē","蟯蟯動,ggniáohggniáohdâng","蟳,zím","蟶坪,tānpiná","蠓罩,bbǎngdào","蠘,cíh","蠻皮病,bbánpuébnê/bbánpébnî","血油,huēhyú/huīhyú","血緣,hiātyán","裂縫,líhpâng","裂隙,liāhkiāh","褪,tǹg","褫奪,tǐduát","襟章,kīmziōng","襪束,bbuéhsōk","規暝,guībbné/guībbní","覕喙,bbīhcuì","觸纏,dākdní","訣說,guātsuāt","詰舌,kiātzíh","誇張,kuādiōng","諜,diáp","謔削,ggióhsiāh","謗大,bòngduâ","謙遜,kiāmsùn","謬誤,bbiûggoô","謼,hoōh","豐沛,pōngpài","買囑,bbnǎiziōk","賴,luâ","赤疹,ciāhzǐn","超市,ciāocî","趖,só","跋涉,buátsiáp","跡,zziāh/liāh","跤曲,kākiāo","跩,zunâi","跳躂,tiàotāt","躄倒,pīhdǒ","躡,lnēh/lnīh","輕聲細說,kīnsināsèsuēh/kīnsināsuèsēh","轄境,hātgǐng","辟走,piāhzǎo","迎神,ggniásín","迒,hnâ","迫切,bīkciāt","迭,diát","迸,biàng","送達,sàngdát","逝,zuâ","遮勘,zziākàm/liākàm","邀約,yāoyōk","邑,yīp","那通,lnǎtāng","郁,hiōk","鄭,dnê","酷人,kōkláng","重青,dângcnē/dângcnī","釣艚,diòzó","銀髮,ggínhuāt/ggúnhuāt","銳減,zzuêgiǎm/luêgiǎm","錚,cnâ","錦繡,ggǐmsiù","鎮煞,dìnsuāh","鏨,zâm","鐵塔,tīhtāh","鑠,siāk","鑱,cím","鑿,cák","閂,cunà","閱覽,yátlǎm","闊腹,kuāhbāk","闖,cuàng","關車,gunāiciā/gunīciā","闡,ciǎn","阿沙不魯,āsābūhlūh","陷,hâm","雜柴,zápcá","雞齊根,gēzégīn/guēzuégūn","靴管,hiāgǒng","項,hâng","領班,lniǎbān","額外,ggiáhgguâ","風吹日曝,hōngcuēzzítpák/hōngcēlítpák","香,hniū","香茅,hiānghḿ","香華,hiōnghuā","騙,piàn","驕傲,giāoggnoô","鬧房,lnâobáng","鬱卒,ūt-zūt","魠,tōh","鱉,bīh","鴆,tīm","鶴,hóh","麥牙,bbéhggé","麻衫,bbnuásnā","默契,bbíkkè/bbíkkuè","黜,tūh","齴,ggiàng","龐,piâng","𠢕,ggáo","𠯗,zíp","𣁳,kāt","𤆬,cuâ","𧮙,cōh","𧿳,pút","𨂿,wnǎi","𩚨,kiû","𩛩,gāoh"]
    checker(additional, c, c_north)