import taibun

trad = "請買粿，用臺語講生日快樂，用箸食魚"
simp = "请买粿，用台语讲生日快乐，用箸食鱼"

print("\n 漢字")
print(trad)

print("\n Tâi-lô")
print(taibun.converter(trad, system="Tai-lo", dialect="south"))
print(taibun.converter(simp, system="Tai-lo", dialect="north"))

print("\n POJ")
print(taibun.converter(simp, system="POJ", dialect="south"))
print(taibun.converter(trad, system="POJ", dialect="north"))

print("\n Zhuyin")
print(taibun.converter(trad, system="zhuyin", dialect="south"))
print(taibun.converter(simp, system="zhuyin", dialect="north"))

trad = "白話字（POJ）是一款用拉丁（羅馬）拼音系統來寫臺灣的語言的書面文字。因為當初是傳教士引入來的，所以也有人共POJ叫做教會羅馬字，或者是簡稱教羅。不而過現代的使用者袂少毋是教徒，教徒嘛真濟袂曉POJ。"
#trad = "請買粿"
print("\n Zhuyin")
print(taibun.converter(trad, system="POJ"))
ting = 'Pe̍h-ōe-jī (POJ) sī chi̍t khoán iōng La-teng (lô bé) pheng-im hē-thóng lâi siá tâi oân--ê gí-giân--ê su-bīn bûn-jī. In-uī tong-chho͘ sī thoân-kàu sū ín-ji̍p lâi--ê, só͘-í iā iú lâng kā POJkiò-chò kàu-hōe Lô-má-jī, he̍k-chiá sī kán-chheng kà lô. Put-jî-kò hiān-tāi--ê sú-iōng chiá bē chió m̄ sī kà tô͘, kà tô͘ mā chin chē bē-hiáu POJ.'
if ting != taibun.converter(trad, system="POJ"):
    print("Error")
    print(ting)
print()
print(taibun.converter(trad, system="Tai-lo", delimiter=" "))
#print(taibun.converter(trad, system="zhuyin"))
