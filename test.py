import taibun
"""
trad = "請買粿，用臺語講生日快樂，用箸食魚"
simp = "请买粿，用台语讲生日快乐，用箸食鱼"

print("\n 漢字")
print(trad)

print("\n Tâi-lô")
print(taibun.converter(trad, system="Tai-lo", dialect="south", format="number"))
print(taibun.converter(simp, system="Tai-lo", dialect="north", format="strip"))

print("\n POJ")
print(taibun.converter(simp, system="POJ", dialect="south"))
print(taibun.converter(trad, system="POJ", dialect="north"))

print("\n Zhuyin")
print(taibun.converter(trad, system="zhuyin", dialect="south"))
print(taibun.converter(simp, system="zhuyin", dialect="north"))
"""
trad = "白話字（POJ）是一款用拉丁（羅馬）拼音系統來寫臺灣的語言的書面文字。因為當初是傳教士引入來的，所以也有人共POJ叫做教會羅馬字，或者是簡稱教羅。不而過現代的使用者袂少毋是教徒，教徒嘛真濟袂曉POJ。"
#trad = "紅毛鬼"
print("\n Zhuyin")
#print(taibun.converter(trad, system="POJ"))
import time

start = time.time()
print(taibun.converter(trad, system="Tai-lo"))
end = time.time()
print(end - start)
#print(taibun.tokenise(trad))
#print(taibun.converter(trad, system="zhuyin"))
