import taibun

trad = "請買粿，用臺語講生日快樂，用箸食魚"
simp = "请买粿，用台语讲生日快乐，用箸食鱼"

print("\n 漢字")
print(trad)

print("\n Tâi-lô")
print(taibun.get(trad, system="Tai-lo", dialect="south", format="number"))
print(taibun.get(simp, system="Tai-lo", dialect="north", format="strip"))

print("\n POJ")
print(taibun.get(simp, system="POJ", dialect="south"))
print(taibun.get(trad, system="POJ", dialect="north"))

print("\n Zhuyin")
print(taibun.get(trad, system="zhuyin", dialect="south"))
print(taibun.get(simp, system="zhuyin", dialect="north"))

trad = "白話字（POJ）是一款用拉丁（羅馬）拼音系統來寫臺灣的語言的書面文字。因為當初是傳教士引入來的，所以也有人共POJ叫做教會羅馬字，或者是簡稱教羅。不而過現代的使用者袂少毋是教徒，教徒嘛“真濟”袂曉POJ。"
print("\n Zhuyin")
print(taibun.get(trad, system="POJ"))