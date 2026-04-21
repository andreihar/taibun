import json

from taibun.taibun import Converter

system = ['Tailo', 'POJ', 'Zhuyin', 'TLPA', 'Pingyim', 'Tongiong', 'IPA']
hanji_data = ["廟尪仔","翁某仔","肉幼仔","花搭仔","微微仔","慢慢仔","尾蝶仔"]

format = 'mark'
delimiter = '-'
apostrophe = True
sandhi = 'auto'
punctuation = 'format'
convert_non_cjk = True
output_tokens = True

with open('output.txt', 'w', encoding='utf-8') as f:
    for i, s in enumerate(system):
        c_south = Converter(system=s, format=format, delimiter=delimiter, apostrophe=apostrophe, sandhi=sandhi, punctuation=punctuation, convert_non_cjk=convert_non_cjk, output_tokens=output_tokens)
        c_north = Converter(system=s, dialect="north", format=format, delimiter=delimiter, apostrophe=apostrophe, sandhi=sandhi, punctuation=punctuation, convert_non_cjk=convert_non_cjk, output_tokens=output_tokens)
        transl = []
        for hanji in hanji_data:
            south = c_south.get(hanji)
            north = c_north.get(hanji)
            if south == north:
                transl.append(south)
            else:
                transl.append(f"{south}/{north}")
        line = f'({json.dumps(transl, ensure_ascii=False, separators=(",", ":"))}, "{s}")'
        if i != len(system) - 1:
            line += ','
        f.write(line + '\n')