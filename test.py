from taibun import Converter, Tokeniser

trad = "請買粿，用臺語講生日快樂，用箸食魚。"
simp = "请买粿，用台语讲生日快乐，用箸食鱼。"

print("\n 漢字")
print(trad)

print("\n Tâi-lô")
c = Converter(system="Tai-lo", dialect="south", format="number")
print(c.get(trad))
c = Converter(system="Tai-lo", dialect="north", format="strip")
print(c.get(simp))

systems = ['Tai-lo', 'POJ', 'Zhuyin', 'TLPA', 'Bbanlam Pingyim', 'Daighi Tongiong']
siansinn = "先生講，學生恬恬聽。"
kinajit = "今仔日彼个查某囡仔來阮兜看我。"
pengiu = "太空朋友，恁好！恁食飽未？有閒著來阮遮坐喔。"
langkai = "人皆生而自由；在尊嚴及權利上各平等。人各賦有理性良知，誠應和睦相處，情同手足。"

for s in systems:
    c = Converter(system=s)
    print("\n " + s)
    print(c.get(siansinn))
    print(c.get(kinajit))
    print(c.get(pengiu))
    print(c.get(langkai))

t = Tokeniser()
print(t.tokenise(langkai))