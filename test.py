import taibun

trad = "請買粿，用臺語講生日快樂，用箸食魚。"
simp = "请买粿，用台语讲生日快乐，用箸食鱼。"

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

print("\n TLPA")
print(taibun.get(trad, system="tlpa", dialect="south"))
print(taibun.get(simp, system="tlpa", dialect="north"))

print("\n Bbanlam pingyim")
print(taibun.get(trad, system="bp", dialect="south"))
print(taibun.get(simp, system="bp", dialect="north"))