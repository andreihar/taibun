import json
import re
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
__zhangzhou = ['南', 'south', '漳', 'zhangzhou', 'zhang']
__quanzhou = ['北', 'north', '泉', 'quanzhou', 'quan']

# system
__poj = ['poj', 'peh-oe-ji']
__tl = ['tl', 'tai-lo']
__zhuyin = ['zhuyin', 'bpmf', 'bomopofo']
__tlpa = ['tlpa']
__bp = ['bp']

word_dict = json.load(open("data/words.json", encoding="utf-8"))


# Tokenise the text into separate words
def tokenise(input):
    tokenised = []
    while input != "":
        for j in reversed(range(1, 5)):
            if len(input) >= j:
                word = input[0:j]
                if word in word_dict:
                    tokenised.append(word)
                    break
                elif j == 1:
                    if not re.search("[\u4e00-\u9FFF]", tokenised[-1]) and \
                       not re.search("[\u4e00-\u9FFF]", input[0:j]):
                        tokenised[-1] += input[0:j]
                    else:
                        tokenised.append(input[0:j])
        if len(input) == 1: input = ""
        else: input = input[j:]
    return tokenised

### Input formatting, interface with conversion methods

# Convert tokenised text into specified transliteration system
DEFAULT_DELIMITER = object()
def get(input, system='Tai-lo', format='mark', delimiter=DEFAULT_DELIMITER, dialect='南', punctuation='format'):
    system = system.lower()
    #if system in __tlpa and format == 'number': format = 'mark'
    if delimiter == DEFAULT_DELIMITER: delimiter = __set_default_delimiter(system)

    converted = tokenise(__simp_to_trad(input))
    converted = [__convert_tokenised(i, system, format, delimiter, dialect).strip() for i in converted]
    converted = ' '.join(converted).strip()
    if punctuation == 'format':
        converted = converted[0].upper() + converted[1:]
        return __format_text(__format_punctuation(converted.strip()))
    return converted.strip()


# Helper to convert separate words
def __convert_tokenised(word, system, format, delimiter, dialect):
    if word in word_dict:
        word = word_dict[word]
        if "/" in word:
            if dialect.lower() in __quanzhou: word = word.split("/")[1]
            else: word = word.split("/")[0]
        word = __system_conversion(system, word)
        if format == 'number': word = __mark_to_number(word)
        if format == 'strip': word = "".join(c for c in unicodedata.normalize("NFD", word) if unicodedata.category(c) != "Mn")
        word = word.replace('--', '[SUFFIX_TOKEN]').replace('-', delimiter).replace('[SUFFIX_TOKEN]', '--')
        return word
    return word


# Helper to format text to match dictionary keys
def __simp_to_trad(input):
    simp = json.load(open("data/simplified.json", encoding="utf-8"))
    for c in simp:
        input = input.replace(c, simp[c])
    return input


# Switch for converting 漢字 based on defined transliteration system
def __system_conversion(system, word):
    if system in __poj: return __tailo_to_poj(word)
    if system in __zhuyin: return __tailo_to_zhuyin(word)
    if system in __tlpa: return __tailo_to_tlpa(word)
    if system in __bp: return __tailo_to_bp(word)
    else: return word


# Set delimiter according to system if wasn't defined by user
def __set_default_delimiter(system):
    if system in __poj or system in __tl: return '-'
    if system in __bp: return ''
    return ' '


### Conversion methods

# Helper to convert between transliteration systems
def __replacement_tool(dictionary, input):
    pattern = re.compile('|'.join(dictionary.keys()))
    return pattern.sub(lambda m: dictionary[re.escape(m.group(0))], input)


# Helper to convert word from Tai-lo to number
def __mark_to_number(input):
    input = input.replace('--', '-[SUFFIX_TOKEN]')
    words = input.split('-')
    input = ""
    for w in words:
        if len(w) > 0: input += '-' + __get_number_tone(w)
    return input[1:].replace('[SUFFIX_TOKEN]', '--')

# Helper to convert syllable from Tai-lo diacritic tones to number tones
def __get_number_tone(input):
    finals = ['p', 't', 'k', 'h']
    if re.search("á|é|í|ó|ú|́", input):
        input += '2'
    elif re.search("à|è|ì|ò|ù|̀", input):
        input += '3'
    elif re.search("â|ê|î|ô|û|̂", input):
        input += '5'
    elif re.search("ā|ē|ī|ō|ū|̄", input):
        input += '7'
    elif re.search('̍', input):
        input += '8'
    elif input[-1] in finals:
        input += '4'
    else:
        input += '1'
    if input[0] == '+' and input[-1] == '4':
        input = input[:-1] + '0'
    input = "".join(c for c in unicodedata.normalize("NFD", input) if unicodedata.category(c) != "Mn")
    return input


# Helper to convert word to specified system
def __mark_to_mark(input, placement, dictionary, tones):
    input = input.replace('--', '-[SUFFIX_TOKEN]')
    words = input.split('-')
    input = ""
    for w in words:
        if len(w) > 0: input += '-' + __get_mark_tone(__replacement_tool(dictionary, __get_number_tone(w)), placement, tones)
    return input[1:].replace('[SUFFIX_TOKEN]', '--')

# Helper to convert syllable from Tai-lo number tones to diacritic tones
def __get_mark_tone(input, placement, tones):
    for s in placement:
        if s.replace('[TONE_TOKEN]', '') in input:
            part = s
            break
    return unicodedata.normalize('NFC', input.replace(part.replace('[TONE_TOKEN]',''), part.replace('[TONE_TOKEN]', tones[int(input[-1])]))[:-1])


### Tai-lo to other transliteration systems converting

# Helper to convert syllable from Tai-lo to POJ
def __tailo_to_poj(input):
    placement_poj = [
        'oa[TONE_TOKEN]h', 'oa[TONE_TOKEN]n', 'oa[TONE_TOKEN]ng', 'oa[TONE_TOKEN]ⁿ', 'oa[TONE_TOKEN]t',
        'ia[TONE_TOKEN]u', 'oe[TONE_TOKEN]h', 'o[TONE_TOKEN]e', 'oa[TONE_TOKEN]i', 'u[TONE_TOKEN]i', 'o[TONE_TOKEN]a',
        'a[TONE_TOKEN]i', 'a[TONE_TOKEN]u', 'ia[TONE_TOKEN]', 'iu[TONE_TOKEN]', 'io[TONE_TOKEN]', 'a[TONE_TOKEN]',
        'o[TONE_TOKEN]', 'o͘[TONE_TOKEN]', 'e[TONE_TOKEN]', 'i[TONE_TOKEN]', 'u[TONE_TOKEN]', 'n[TONE_TOKEN]g', 'm[TONE_TOKEN]'
    ]
    convert_poj = {
        'nn':'ⁿ', 'ts':'ch',
        'ing':'eng', 'uai':'oai', 'uan':'oan',
        'ik':'ek', 'ua':'oa', 'ue':'oe', 'oo':'o͘',
    }
    tones_poj = ['', '', '́', '̀', '', '̂', '', '̄', '̍', '']
    return __mark_to_mark(input, placement_poj, convert_poj, tones_poj)


# Helper to convert syllable from Tai-lo to 方音符號 (zhuyin)
def __tailo_to_zhuyin(input):
    input = __mark_to_number(input)
    zhuyin = {
        'p4': 'ㆴ', 't4': 'ㆵ', 'k4': 'ㆶ', 'h4': 'ㆷ', 'p8': 'ㆴ˙', 't8': 'ㆵ˙', 'k8': 'ㆶ˙', 'h8': 'ㆷ˙',
        'tshi': 'ㄑ', 'iunn': 'ㆫ', 'ainn': 'ㆮ', 'unn': 'ㆫ', 'inn': 'ㆪ', 'enn': 'ㆥ', 'ann': 'ㆩ', 'onn': 'ㆧ',
        'tsi': 'ㄐ', 'nng': 'ㄋㆭ', 'ong': 'ㆲ', 'ang': 'ㆭ', 'uan': 'ㄨㄢ', 'uai': 'ㄨㄞ',
        'tsh': 'ㄘ', 'ing': 'ㄧㄥ',
        'ji': 'ㆢ', 'si': 'ㄒ', 'ts': 'ㄗ',
        'ai': 'ㄞ', 'an': 'ㄢ', 'au': 'ㄠ', 'am': 'ㆰ', 'om': 'ㆱ', 'ua': 'ㄨㄚ', 'ue': 'ㄨㆤ', 'ng': 'ㆭ', 'oo': 'ㆦ',
        'ir': 'ㆨ', 'ph': 'ㄆ', 'th': 'ㄊ', 'kh': 'ㄎ', 'p': 'ㄅ', 'b': 'ㆠ', 'm': 'ㄇ', 't': 'ㄉ', 'n': 'ㄋ',
        'l': 'ㄌ', 'k': 'ㄍ', 'g': 'ㆣ', 'h': 'ㄏ', 'j': 'ㆡ', 's': 'ㄙ', 'i': 'ㄧ', 'm': 'ㄇ', 'u': 'ㄨ',
        'a': 'ㄚ', 'o': 'ㄜ', 'e': 'ㆤ'
    }
    zhuyin_tones = 	['', '', 'ˋ', '˪', '', 'ˊ', '', '˫', '']
    """
    if len(input) > 3:
        if input[0] == 's' and input[1] == 'i':
            input = input.replace('si', 'ㄒㄧ')
    if input[-2] == 'm' and len(input) > 3:
        l = list(input)
        l[-2] = 'ㆬ'
        input = "".join(l)
    if input[-2] == 'n' and len(input) > 3:
        l = list(input)
        l[-2] = 'ㄣ'
        input = "".join(l)
    """
    input = __replacement_tool(zhuyin, input)
    for t in input:
        if t.isnumeric():
            input = input.replace(t, zhuyin_tones[int(t)])
    return input


# Helper to convert syllable from Tai-lo to TLPA
def __tailo_to_tlpa(input):
    convert_tlpa = {
        'tsh':'ch', 'ts':'c'
    }
    return __replacement_tool(convert_tlpa, __mark_to_number(input))


# Helper to convert syllable from Tai-lo to Bbanlam pingyim
def __tailo_to_bp(input):
    placement_bp = [
        'ua[TONE_TOKEN]i', 'ia[TONE_TOKEN]o', 'a[TONE_TOKEN]i', 'a[TONE_TOKEN]o', 
        'oo[TONE_TOKEN]', 'ia[TONE_TOKEN]', 'iu[TONE_TOKEN]', 'io[TONE_TOKEN]', 'ua[TONE_TOKEN]', 'ue[TONE_TOKEN]', 'ui[TONE_TOKEN]',
        'a[TONE_TOKEN]', 'o[TONE_TOKEN]', 'e[TONE_TOKEN]', 'i[TONE_TOKEN]', 'u[TONE_TOKEN]', 'n[TONE_TOKEN]g', 'm[TONE_TOKEN]'
    ]
    input = input.lower()
    convert_bp = {
        'ainn':'nai', 'iunn':'niu', 'ann':'na', 'onn':'noo', 'enn':'ne',
        'inn':'ni', 'unn':'nu', 'au':'ao', 'ph':'p', 'nng':'lng', 'tsh':'c',
        'ng':'ng',
        'ts':'z', 'th':'t', 'kh':'k', 'ir':'i', 'p':'b', 'b':'bb',
        't':'d', 'k':'g', 'g':'gg', 'j':'l'
    } #'m':'bb',
    tones_bp = ['', '̄', '̌', '̀', '̄', '́', '', '̂', '́', '']
    return __mark_to_mark(input, placement_bp, convert_bp, tones_bp)


### Converted output formatting

# Helper to convert Chinese punctuation to Latin punctuation with appropriate spacing
def __format_punctuation(input):
    left_space = {'。':'.', '．':' ', '，':',', '、':',',
                  '！':'!', '？':'?', '；':';', '：':':',
                  '）':')', '］':']', '】':']', '」':'"',
                  '”':'"', '--':'--'}
    right_space = {'（':'(', '［':'[', '【':'[', '「':'"', '“':'"'}
    for left in left_space:
        input = input.replace(' ' + left, left_space[left])
        input = input.replace(left, left_space[left])
    for right in right_space:
        input = input.replace(right + ' ', right_space[right])
        input = input.replace(right, right_space[right])
    return input


# Helper to capitalise text in according to punctuation
def __format_text(input):
    punc_filter = re.compile("([.!?]\s*)")
    split_with_punc = punc_filter.split(input)
    formatted = "".join([i[0].upper() + i[1:] for i in split_with_punc if len(i) > 1]).strip()
    if len(input) != len(formatted):
        return formatted+input[-1]
    return formatted