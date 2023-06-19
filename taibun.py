import json
import re
import unicodedata

"""
Description: Converts Chinese characters to phonetic transcription of any
	 		 of two main pronunciations of Taiwanese Hokkien. Supports both
             Traditional and Simplified characters.
Invariant: Phonetic transcription depends on the dialect passed into the function.
	 	   南 or 漳 for Zhangzhou (漳州)-leaning pronunciation (set by default).
		   北 or 泉 for Quanzhou (泉州)-leaning pronunciation.

		   Transcription depends on the system passed into the function.
           Tai-lo for 臺灣閩南語羅馬字拼音方案 (set by default).
           POJ for Pe̍h-ōe-jī.

           format = mark for diacritical representation
					number for numeric representation
                    strip for no representation of tones
"""

## TODO: strip doesn't work for zhuyin and TLPA
##       zhuyin conversion incorrect

### invariant calls
# dialect
__zhangzhou = ['南', 'south', '漳', 'zhangzhou', 'zhang']
__quanzhou = ['北', 'north', '泉', 'quanzhou', 'quan']

# system
__poj = ['poj', 'peh-oe-ji']
__tl = ['tl', 'tai-lo']
__zhuyin = ['zhuyin', 'bpmf', 'bomopofo']
__tlpa = ['tlpa']
__bp = ['bp', 'bbanlam pingyim']
__dt = ['dt', 'daighi tongiong pingim', 'daighi tongiong']

word_dict = json.load(open("data/words.json", encoding="utf-8"))

suffix_token = '[SUFFIX_TOKEN]'
tone_token = '[TONE_TOKEN]'

### Interface functions

# Convert tokenised text into specified transliteration system
DEFAULT_DELIMITER = object()
DEFAULT_SANDHI = object()
def get(input, system='Tai-lo', format='mark', delimiter=DEFAULT_DELIMITER, sandhi=DEFAULT_SANDHI, dialect='南', punctuation='format'):
    system = system.lower()
    if system in __tlpa and format == 'number' or system in __zhuyin and format == 'number': format = 'mark'
    if delimiter == DEFAULT_DELIMITER: delimiter = __set_default_delimiter(system)
    if sandhi == DEFAULT_SANDHI: sandhi = __set_default_sandhi(sandhi)

    converted = tokenise(to_traditional(input))
    converted = [__convert_tokenised(i, system, format, delimiter, sandhi, dialect).strip() for i in converted]
    converted = ' '.join(converted).strip()
    if punctuation == 'format':
        converted = converted[0].upper() + converted[1:]
        return __format_text(__format_punctuation(converted.strip()))
    return converted.strip()


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
                    if len(tokenised) > 0:
                        if not re.search("[\u4e00-\u9FFF]", tokenised[-1]) and \
                        not re.search("[\u4e00-\u9FFF]", input[0:j]):
                            tokenised[-1] += input[0:j]
                        else:
                            tokenised.append(input[0:j])
                    else:
                        tokenised.append(input[0:j])
        if len(input) == 1: input = ""
        else: input = input[j:]
    return tokenised


# Convert Simplified to Traditional characters
def to_traditional(input):
    trad = json.load(open("data/simplified.json", encoding="utf-8"))
    for c in trad:
        input = input.replace(c, trad[c])
    return input


# Convert Traditional to Simplified characters
def to_simplified(input):
    simp = json.load(open("data/simplified.json", encoding="utf-8"))
    simp = {v: k for k, v in simp.items()}
    for c in simp:
        input = input.replace(c, simp[c])
    return input


### Input formatting

# Helper to convert separate words
def __convert_tokenised(word, system, format, delimiter, sandhi, dialect):
    if word in word_dict:
        word = word_dict[word]
        if "/" in word:
            if dialect.lower() in __quanzhou: word = word.split("/")[1]
            else: word = word.split("/")[0]
        word = __system_conversion(word, system, sandhi, dialect)
        if format == 'number': word = __mark_to_number(word)
        if format == 'strip': word = "".join(c for c in unicodedata.normalize("NFD", word) if unicodedata.category(c) != "Mn")
        word = word.replace('--', suffix_token).replace('-', delimiter).replace(suffix_token, '--')
        return word
    return word


# Helper switch for converting 漢字 based on defined transliteration system
def __system_conversion(word, system, sandhi, dialect):
    if system in __poj: return __tailo_to_poj(word, sandhi, dialect)
    if system in __zhuyin: return __tailo_to_zhuyin(word, sandhi, dialect)
    if system in __tlpa: return __tailo_to_tlpa(word, sandhi, dialect)
    if system in __bp: return __tailo_to_bp(word, sandhi, dialect)
    if system in __dt: return __tailo_to_dt(word, sandhi, dialect)
    if sandhi: return __tailo_to_tailo(word, dialect)
    else: return word


# Helper functions to set delimiter according to transliteration system if wasn't explicitly defined by user
def __set_default_delimiter(system):
    if system in __poj or system in __tl or system in __dt: return '-'
    if system in __bp: return ''
    return ' '


# Helper functions to set sandhi according to transliteration system if wasn't explicitly defined by user
def __set_default_sandhi(sandhi):
    if sandhi in __dt: return True
    return False


### Conversion functions

# Helper to convert between transliteration systems
def __replacement_tool(dictionary, input):
    pattern = re.compile('|'.join(dictionary.keys()))
    return pattern.sub(lambda m: dictionary[re.escape(m.group(0))], input)


# Helper to convert word from Tai-lo to number
def __mark_to_number(input):
    input = input.replace('--', '-'+suffix_token)
    words = input.split('-')
    input = ""
    for w in words:
        if len(w) > 0: input += '-' + __get_number_tone(w)
    return input[1:].replace(suffix_token, '--')

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


# Helper to break down a word into syllables for conversion
def __preprocess_word(word):
    return word.replace('--', '-'+suffix_token).split('-')


# Helper to convert syllable from Tai-lo number tones to diacritic tones
def __get_mark_tone(input, placement, tones):
    for s in placement:
        if s.replace(''+tone_token+'', '') in input:
            part = s
            break
    return unicodedata.normalize('NFC', input.replace(part.replace(''+tone_token+'',''), part.replace(''+tone_token+'', tones[int(input[-1])]))[:-1])


# Helper to apply tone sandhi to a word
def __tone_sandhi(word, dialect):
    sandhi = {'1':'7', '7':'3', '3':'2', '2':'1', '5':'7',
              'p4':'p8', 't4':'t8', 'k4':'k8', 'h4':'2',
              'p8':'p4', 't8':'t4', 'k8':'k4', 'h8':'3'}
    if dialect in __quanzhou:
        sandhi.update({'5':'3'})
    return __replacement_tool(sandhi, word)


### Tai-lo to other transliteration systems converting

# Helper to convert syllable from Tai-lo to Tai-lo
# (called only in cases when tone sandhi is applied)
def __tailo_to_tailo(input, dialect):
    placement_tl = [
        'ia'+tone_token+'u', 'ua'+tone_token+'i', 'ua'+tone_token+'', 'ue'+tone_token+'', 'ui'+tone_token+'', 'a'+tone_token+'i',
        'a'+tone_token+'u', 'o'+tone_token+'o','ia'+tone_token+'', 'iu'+tone_token+'', 'io'+tone_token+'', 'o'+tone_token+'o', 'a'+tone_token+'', 
        'o'+tone_token+'', 'e'+tone_token+'', 'i'+tone_token+'', 'u'+tone_token+'', 'n'+tone_token+'g', 'm'+tone_token+''
    ]
    tones_tl = ["", "", "́", "̀", "", "̂", "̌", "̄", "̍", "̋"]
    words = __preprocess_word(input)
    input = ""
    number_tones = [__get_number_tone(w) for w in words if len(w) > 0]
    for i in range(0, len(number_tones)-1):
        number_tones[i] = __tone_sandhi(number_tones[i], dialect)
    for nt in number_tones:
        input += '-' + __get_mark_tone(nt, placement_tl, tones_tl)
    return input[1:].replace(suffix_token, '--')


# Helper to convert syllable from Tai-lo to POJ
def __tailo_to_poj(input, sandhi, dialect):
    placement_poj = [
        'oa'+tone_token+'h', 'oa'+tone_token+'n', 'oa'+tone_token+'ng', 'oa'+tone_token+'ⁿ', 'oa'+tone_token+'t',
        'ia'+tone_token+'u', 'oe'+tone_token+'h', 'o'+tone_token+'e', 'oa'+tone_token+'i', 'u'+tone_token+'i', 'o'+tone_token+'a',
        'a'+tone_token+'i', 'a'+tone_token+'u', 'ia'+tone_token+'', 'iu'+tone_token+'', 'io'+tone_token+'', 'a'+tone_token+'',
        'o'+tone_token+'', 'o͘'+tone_token+'', 'e'+tone_token+'', 'i'+tone_token+'', 'u'+tone_token+'', 'n'+tone_token+'g', 'm'+tone_token+''
    ]
    convert_poj = {
        'nng':'nng', 'nn':'ⁿ', 'ts':'ch',
        'ing':'eng', 'uai':'oai', 'uan':'oan',
        'ik':'ek', 'ua':'oa', 'ue':'oe', 'oo':'o͘',
    }
    tones_poj = ['', '', '́', '̀', '', '̂', '', '̄', '̍', '']
    words = __preprocess_word(input)
    input = ""
    number_tones = [__get_number_tone(w) for w in words if len(w) > 0]
    if sandhi:
        for i in range(0, len(number_tones)-1):
            number_tones[i] = __tone_sandhi(number_tones[i], dialect)
    for nt in number_tones:
        input += '-' + __get_mark_tone(__replacement_tool(convert_poj, nt), placement_poj, tones_poj)
    return input[1:].replace(suffix_token, '--')


# Helper to convert syllable from Tai-lo to 方音符號 (zhuyin)
# TODO: incorrect conversions
def __tailo_to_zhuyin(input, sandhi, dialect):
    #input = __mark_to_number(input)
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
    words = __preprocess_word(input)
    input = ""
    number_tones = [__get_number_tone(w) for w in words if len(w) > 0]
    if sandhi:
        for i in range(0, len(number_tones)-1):
            number_tones[i] = __tone_sandhi(number_tones[i], dialect)
    for nt in number_tones:
        for t in nt:
            if t.isnumeric(): nt = nt.replace(t, zhuyin_tones[int(t)])
        input += '-' + __replacement_tool(zhuyin, nt)
    return input[1:].replace(suffix_token, '--')


# Helper to convert syllable from Tai-lo to TLPA
def __tailo_to_tlpa(input, sandhi, dialect):
    convert_tlpa = {
        'tsh':'ch', 'ts':'c'
    }
    words = __preprocess_word(input)
    input = ""
    number_tones = [__get_number_tone(w) for w in words if len(w) > 0]
    if sandhi:
        for i in range(0, len(number_tones)-1):
            number_tones[i] = __tone_sandhi(number_tones[i], dialect)
    for nt in number_tones:
        input += '-' + __replacement_tool(convert_tlpa, nt)
    return input[1:].replace(suffix_token, '--')


# Helper to convert syllable from Tai-lo to Bbanlam pingyim
# TODO: initial i to yi, probably solved
def __tailo_to_bp(input, sandhi, dialect):
    placement_bp = [
        'ua'+tone_token+'i', 'ia'+tone_token+'o', 'a'+tone_token+'i', 'a'+tone_token+'o', 
        'oo'+tone_token+'', 'ia'+tone_token+'', 'iu'+tone_token+'', 'io'+tone_token+'', 'ua'+tone_token+'', 'ue'+tone_token+'', 'ui'+tone_token+'',
        'a'+tone_token+'', 'o'+tone_token+'', 'e'+tone_token+'', 'i'+tone_token+'', 'u'+tone_token+'', 'n'+tone_token+'g', 'm'+tone_token+''
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
    words = __preprocess_word(input)
    input = ""
    number_tones = [__get_number_tone(w) for w in words if len(w) > 0]
    if sandhi:
        for i in range(0, len(number_tones)-1):
            number_tones[i] = __tone_sandhi(number_tones[i], dialect)
    for nt in number_tones:
        replaced = __replacement_tool(convert_bp, nt)
        if nt[0] == 'i': replaced = 'y' + replaced
        input += '-' + __get_mark_tone(replaced, placement_bp, tones_bp)
    return input[1:].replace(suffix_token, '--')


# Helper to convert syllable from Tai-lo to Tong-iong ping-im
#       Not enough information on tone mark placement
def __tailo_to_dt(input, sandhi, dialect):
    placement_dt = [
        'ua'+tone_token+'i', 'ia'+tone_token+'o', 'a'+tone_token+'i', 'a'+tone_token+'o', 
        'oo'+tone_token+'', 'ia'+tone_token+'', 'iu'+tone_token+'', 'io'+tone_token+'', 'ua'+tone_token+'', 'ue'+tone_token+'', 'ui'+tone_token+'',
        'a'+tone_token+'', 'o'+tone_token+'', 'e'+tone_token+'', 'i'+tone_token+'', 'u'+tone_token+'', 'n'+tone_token+'g', 'm'+tone_token+''
    ]
    # plosives don't change, ptkh 4/8 -> ptkh 4/8
    convert_dt = {'p4':'p4', 't4':'t4', 'k4':'k4', 'h4':'h4', 'p8':'p8', 't8':'t8', 'k8':'k8', 'h8':'h8',
                  'oo':'o', 'om':'om', 'ong':'ong', 'ir':'i', 'tsh':'c',
                  'ts':'z', 'nng':'nng', 'ng':'ng', 'g':'gh', 'kh':'k', 'k':'g',
                  'ph':'p', 'p':'b', 'b':'bh', 'th':'t', 't':'d',
                  'j':'r'}
    tones_dt = ["̊", "", "̀", "̂", "̄", "̌", "", "̄", "", "́"]
    words = __preprocess_word(input)
    input = ""
    number_tones = [__get_number_tone(w) for w in words if len(w) > 0]
    if sandhi:
        for i in range(0, len(number_tones)-1):
            number_tones[i] = __tone_sandhi(number_tones[i], dialect)
    for nt in number_tones:
        if nt[-2] == 'o': nt = (nt[:-2] + 'or' + nt[-1])
        input += '-' + __get_mark_tone(__replacement_tool(convert_dt, nt), placement_dt, tones_dt)
    return input[1:].replace(suffix_token, '--')


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
    for i in split_with_punc:
        if len(i) > 1:
            split_with_punc[split_with_punc.index(i)] = (i[0].upper() + i[1:])
    return "".join(split_with_punc)