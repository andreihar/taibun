import json
import re
import csv
import unicodedata

"""
Description: Converts Chinese characters to phonetic transcription of any
	 		 of two main pronunciations of Taiwanese Hokkien. Supports both
             Traditional and Simplified characters.
Invariant: Phonetic transcription depends on the dialect passed into the method.
	 	   南 or 漳 for Zhangzhou (漳州)-leaning pronunciation (set by default).
		   北 or 泉 for Quanzhou (泉州)-leaning pronunciation.

		   Transcription depends on the system passed into the method.
           Tai-lo for 臺灣閩南語羅馬字拼音方案 (set by default).
           POJ for Pe̍h-ōe-jī.

           format = mark for diacritical representation
					number for numeric representation
                    strip for no representation of tones
"""

### invariant calls
# dialect
zhangzhou = ['南', 'south', '漳', 'zhangzhou', 'zhang']
quanzhou = ['北', 'north', '泉', 'quanzhou', 'quan']

# system
poj = ['poj', 'peh-oe-ji']
tl = ['tl', 'tai-lo']
zhuyin = ['zhuyin', 'bpmf', 'bomopofo']

poj_tones = 	["", "", "́", "̀", "", "̂", "", "̄", "̍", ""]
tl_tones = 		["", "", "́", "̀", "", "̂", "̌", "̄", "̍", "̋"]
zhuyin_tones = 	["", "", "ˋ", "˪", "", "ˊ", "", "˫", ""]

# system, format, delimiter, dialect
def converter(input, system="Tai-lo", format="mark", delimiter='-', dialect="南", punctuation="format"):
    word_dict = json.load(open("data/words.json", encoding="utf-8"))
    system = system.lower()

    input = simplifiedToTraditional(input)
    converted = ""
    while input != "":
        for j in reversed(range(1, 5)):
            if len(input) >= j:
                word = input[0:j]
                if word in word_dict:
                    word = word_dict[word]
                    if "/" in word:
                        if dialect.lower() in quanzhou: word = word.split("/")[1]
                        else: word = word.split("/")[0]
                    word = __system_conversion(system, word)
                    if format == 'number': word = markToNumber(word)
                    if format == 'strip': word = "".join(c for c in unicodedata.normalize("NFD", word) if unicodedata.category(c) != "Mn")
                    word = word.replace('--', 'SPECIAL_CHAR_SUFFIX').replace('-', delimiter).replace('SPECIAL_CHAR_SUFFIX', '--')
                    converted += word + " "
                    break
                elif j == 1:
                    if re.search("[\u4e00-\u9FFF]", input[0:j]):
                        converted += " " + input[0:j]
                    else:
                        converted += input[0:j]
        if len(input) == 1: input = ""
        else: input = input[j:]
    converted = converted[0].upper() + converted[1:]
    if punctuation == "format": return format_punctuation(converted.strip())
    return converted.strip()


def simplifiedToTraditional(input):
    reader = csv.reader(open("data/simplified.csv", encoding="utf-8"))
    simp = {}
    for k, v in reader:
        simp[k] = v
    for c in simp:
        input = input.replace(c, simp[c])
    return input


def markToNumber(input):
    input = input.replace('--', '-+')
    words = input.split('-')
    input = ""
    for w in words:
        if len(w) > 0: input += '-' + getNumberTone(w)
    return input[1:].replace('+', '--')


def markConvert(input, placement, dictionary):
    input = input.replace('--', '-+')
    words = input.split('-')
    input = ""
    for w in words:
        if len(w) > 0: input += '-' + getMarkTone(__replacement_tool(dictionary, getNumberTone(w)), placement)
    return input[1:].replace('+', '--')


def tailo_to_poj(input):
    placement_poj = [
        'oa*h', 'oa*n', 'oa*ng', 'oa*ⁿ', 'oa*t',
        'ia*u', 'oe*h', 'o*e', 'oa*i', 'u*i', 'o*a',
        'a*i', 'a*u', 'ia*', 'iu*', 'io*', 'a*',
        'o*', 'o͘*', 'e*', 'i*', 'u*', 'n*g', 'm*'
    ]
    poj = {
        'nn':'ⁿ', 'ts':'ch',
        'ing':'eng', 'uai':'oai', 'uan':'oan',
        'ik':'ek', 'ua':'oa', 'ue':'oe', 'oo':'o͘',
    }
    return markConvert(input, placement_poj, poj)


def tailo_to_zhuyin(input):
    zhuyin = {
        'p4': 'ㆴ', 't4': 'ㆵ', 'k4': 'ㆶ', 'h4': 'ㆷ', 'p8': 'ㆴ˙', 't8': 'ㆵ˙', 'k8': 'ㆶ˙', 'h8': 'ㆷ˙',
        'tshi': 'ㄑ', 'iunn': 'ㆫ', 'ainn': 'ㆮ', 'unn': 'ㆫ', 'inn': 'ㆪ', 'enn': 'ㆥ', 'ann': 'ㆩ', 'onn': 'ㆧ',
        'tsi': 'ㄐㄧ', 'nng': 'ㄋㆭ', 'ong': 'ㆲ', 'ang': 'ㆭ', 'uan': 'ㄨㄢ', 'uai': 'ㄨㄞ',
        'tsh': 'ㄘ', 'ing': 'ㄧㄥ',
        'ji': 'ㆢ', 'si': 'ㄒ', 'ts': 'ㄗ',
        'ai': 'ㄞ', 'an': 'ㄢ', 'au': 'ㆯ', 'am': 'ㆰ', 'om': 'ㆱ', 'ua': 'ㄨㄚ', 'ue': 'ㄨㆤ', 'ng': 'ㆭ', 'oo': 'ㆦ',
        'ir': 'ㆨ', 'ph': 'ㄆ', 'th': 'ㄊ', 'kh': 'ㄎ', 'p': 'ㄅ', 'b': 'ㆠ', 'm': 'ㄇ', 't': 'ㄉ', 'n': 'ㄋ',
        'l': 'ㄌ', 'k': 'ㄍ', 'g': 'ㆣ', 'h': 'ㄏ', 'j': 'ㆡ', 's': 'ㄙ', 'i': 'ㄧ', 'm': 'ㄇ', 'u': 'ㄨ',
        'a': 'ㄚ', 'o': 'ㄜ', 'e': 'ㆤ'
    }
    if len(input) > 3:
        if input[0] == "s" and input[1] == "i":
            input = input.replace("si", "ㄒㄧ")
    if input[-2] == "m" and len(input) > 3:
        l = list(input)
        l[-2] = "ㆬ"
        input = "".join(l)
    if input[-2] == "n" and len(input) > 3:
        l = list(input)
        l[-2] = "ㄣ"
        input = "".join(l)
    input = __replacement_tool(zhuyin, input)
    for t in input:
        if t.isnumeric():
            input = input.replace(t, zhuyin_tones[int(t)])
    return input


def getNumberTone(input):
    finals = ['p', 't', 'k', 'h']
    if re.search("á|é|í|ó|ú|́", input):
        input += '2'
    elif re.search("à|è|ì|ò|ù|̀", input):
        input += '3'
    elif re.search("â|ê|î|ô|û|̂", input):
        input += '5'
    elif re.search("ā|ē|ī|ō|ū|̄", input):
        input += '7'
    elif re.search("̍", input):
        input += '8'
    elif input[-1] in finals:
        input += '4'
    else: #re.search("a|e|i|o|u", input):
        input += '1'
    if input[0] == '+' and input[-1] == '4':
        input = input[:-1] + '0'
    input = "".join(c for c in unicodedata.normalize("NFD", input) if unicodedata.category(c) != "Mn")
    return input


def format_punctuation(input):
    input = input.replace("。", ". ")
    input = input.replace("，", ", ").replace("、", ", ")
    input = input.replace("！", "! ").replace("？", "? ")
    input = input.replace("；", "; ").replace("：", ": ")
    input = input.replace("（", " (").replace("）", ") ")
    input = input.replace("［", " [").replace("］", "] ")
    input = input.replace("【", " [").replace("】", "] ")
    input = input.replace("」", '"').replace("「", ' "')
    input = input.replace("．", " ")
    input = (
        input.replace(" . ", ". ")
        .replace('" ', '"')
        .replace(" ,", ",")
        .replace("( ", "(")
        .replace(" ;", "; ")
        .replace("  (", " (")
        .replace(" ) ", ") ")
        .replace(" --", "--")
    )
    punc_filter = re.compile("([.!?]\s*)")
    split_with_punc = punc_filter.split(input)
    input = "".join([i[0].upper() + i[1:] for i in split_with_punc if len(i) > 1]).strip()
    return input


def __replacement_tool(dictionary, input):
    pattern = re.compile("|".join(dictionary.keys()))
    return pattern.sub(lambda m: dictionary[re.escape(m.group(0))], input)


def __system_conversion(system, word):
    if system in poj: return tailo_to_poj(word)
    if system in zhuyin: return tailo_to_zhuyin(word)
    else: return word


def getMarkTone(input, placement):
    for s in placement:
        if s.replace("*", "") in input:
            part = s
            break
    return unicodedata.normalize('NFC', input.replace(part.replace('*',''), part.replace('*', poj_tones[int(input[-1])]))[:-1])