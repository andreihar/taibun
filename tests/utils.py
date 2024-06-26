def checker(array, general_converter, north_converter):
    for word in array:
        hanji, transl = word
        transl = transl.strip().split('/')
        assert transl[0] == general_converter.get(hanji)
        if len(transl) > 1:
            assert transl[1] == north_converter.get(hanji)

bilabial_c = ['啡','波','毛','麻']
alveolar_c = ['地','唾','早','厝','思','耐','如','柳']
alveolo_palatal_c = ['遮','手','寫','而']
velar_c = ['求','去','雅','語','喜']
front_c = ['衣','會','圓','楹']
central_c = ['阿','亞','餡']
back_c = ['禹','烏','張','唔']
nasal_c = ['音','寅','紅']
stop_c = ['葉','楬','惡','曷']
syllabic_c = ['姆','黃']
additional_c = ['㨻','一概','三層','不屑','丑','丼','乎','乞食','亂鐘','交落','人間','仰角','休克','侮辱','停電','偝','傳接','僥倖','儼硬','兄哥','充作','免費','入口','八仙','八月節','冇浡','冰雹','刐','判斷','別莊','刮','剔斥','割禮','劃','加快','劣','劫棺','匆促','匹敵','半遂','協和','卡片','卯名','卯落去','危險','卵包','參照','合歡','含蓄','吭','吸汗','吻笑','呃酸','呿','品嘗','哈啾','哈氣','哼呻','唉','喀','喃','喓','喔','喝令','喢','嗙','嗾','嘈嘈唸','嘐潲','噎','噯','噷','嚇驚','嚓','嚷','嚾','囤糴','困局','圓參','在','坉塗','坑谷','坱埃','垃圾','基金','堯韭','塌替','壁畫','壓模','外甥','大山','天光','天后','太魯閣','央及','奇雙','奔喪','好客','妙','妝娗','妾','姓','媽媽','孵','學園','學歹','孽','宅','安眠','寄來','密實','專員','尿鈷','屁','屆時','屈橋','屏遮那','屐','岩鹽','岳父','年表','店租','庵廟','廿','彪','彼樣','徼','忍心','快活','忽然','怦','怯膽','恐畏','惜略','愕','愣','慼心','憚','懦','懷念','戇','扒飯','扭尻川','抓癢','披埕','抹粉','抾拾','拆壇','拋出','拋捎','拍插','拖直','招倚','括流','指','挓','挕捒','挨餓','掀冊','掃蕩','掇','掙','掩目雞','插春','揬','搐','搭嚇','搭里霧','摳','撇清','撓','撤職','擉','擔當','擗','攀登','攔閘','敱','斟酒','方興未艾','昨','晚會','晴','晾','曲線','朗讀','木業','末路','杵','枴','染','校閱','核可','桌屜','榆','標本','樸實','橫扴','檨','欶','歇影','歌譜','歡度','歪斜','每擺','沃雨','沉著','沒藥','沓','沓滴','沖水','沫','海蟹','涼腔','添設','渺茫','湠叢','滅無','漂浮','漉屎','漚肥','漳','潑扇','潑賤','潤餅','澩','激力','濺','煏','煠','煤','熁','熊','熱烈','爁','爹','牚','牛膝','物','物代','牽強','牽磕','猛勇','玉環','玉蘭','玩具','甘苦','甪毛','番薯','疊尖','疏散','癮甲','百般','益蟲','益閣','監牢','相閃','眉額','看','眩痧','眵','眼福','睚','督察','瞌','砌','研缽','破缺','硩','碗頭箸尾','碧潭','確保','磨坩','礁石','礎','礙著','票箱','禿','空空','突','笠','筆算','簇','簸','籤王','粒','糠瘡','糶','紂','納采','索梯','累積','紺','結疤','絕對','絨布','經繭','綠色','緝捕','緟','編篡','缺糧','美味','翕熱','聘請','聽錯','肉目','脈搏','脫節','腔調','腰骨','腳錢','船運','色牙','茅草','草笠仔','莢','落落','蓆','蔥藕','蕨貓','薄待','薄膜','薑','藃','藩屏','虹','蚻','蛤蜊','蜀七','蜈蚣','蜜月','蝕秤','蝛','蝨','蟯桮','蟯蟯動','蟳','蟶坪','蠓罩','蠘','蠻皮病','血油','血緣','裂縫','裂隙','褪','褫奪','襟章','襪束','規暝','覕喙','觸纏','訣說','詰舌','誇張','諜','謔削','謗大','謙遜','謬誤','謼','豐沛','買囑','賴','赤疹','超市','趖','跋涉','跡','跤曲','跩','跳躂','躄倒','躡','輕聲細說','轄境','辟走','迎神','迒','迫切','迭','迸','送達','逝','遮勘','邀約','邑','那通','郁','鄭','酷人','重青','釣艚','銀髮','銳減','錚','錦繡','鎮煞','鏨','鐵塔','鑠','鑱','鑿','閂','閱覽','闊腹','闖','關車','闡','阿沙不魯','陷','雜柴','雞齊根','靴管','項','領班','額外','風吹日曝','香','香茅','香華','騙','驕傲','鬧房','鬱卒','魠','鱉','鴆','鶴','麥牙','麻衫','默契','黜','齴','龐','𠢕','𠯗','𣁳','𤆬','𧮙','𧿳','𨂿','𩚨','𩛩']