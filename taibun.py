import os
import json
import re
import unicodedata

"""
Description: Converts Chinese characters to phonetic transcription of any
	 		 of two main pronunciations of Taiwanese Hokkien. Supports both
             Traditional and Simplified characters.
Invariant: Phonetic transcription depends on the dialect passed into the function.
	 	   `south` for Zhangzhou (漳州)-leaning pronunciation (set by default).
		   `north` for Quanzhou (泉州)-leaning pronunciation.

		   Transcription depends on the system passed into the function.
           Tai-lo for 臺灣閩南語羅馬字拼音方案 (set by default).
           POJ for Pe̍h-ōe-jī.

           format = mark for diacritical representation
					number for numeric representation
                    strip for no representation of tones
"""

## TODO: strip doesn't work for zhuyin and TLPA
##       zhuyin conversion incorrect

word_dict = json.load(open(os.path.join(os.path.dirname(__file__), "data/words.json"), encoding="utf-8"))

class Converter(object):

    suffix_token = '[SFFX_TKN]'
    tone_token = '[TN_TKN]'
    DEFAULT_DELIMITER = object()
    DEFAULT_SANDHI = object()

    def __init__(self, system='Tailo', dialect='south', format='mark', delimiter=DEFAULT_DELIMITER, sandhi=DEFAULT_SANDHI, punctuation='format'):
        self.system = system.lower()
        self.dialect = dialect
        self.format = format
        self.delimiter = delimiter
        self.sandhi = sandhi
        self.punctuation = punctuation


    ### Interface functions

    # Convert tokenised text into specified transliteration system
    def get(self, input):
        if self.system == 'tlpa' and self.format == 'number' or self.system == 'zhuyin' and self.format == 'number': self.format = 'mark'
        if self.delimiter == self.DEFAULT_DELIMITER: self.delimiter = self.__set_default_delimiter()
        if self.sandhi == self.DEFAULT_SANDHI: self.sandhi = self.__set_default_sandhi()

        tokeniser = Tokeniser()
        converted = tokeniser.tokenise(self.to_traditional(input))
        converted = [self.__convert_tokenised(i).strip() for i in converted]
        converted = ' '.join(converted).strip()
        if self.punctuation == 'format':
            converted = converted[0].upper() + converted[1:]
            return self.__format_text(self.__format_punctuation_western(converted.strip()))
        return self.__format_punctuation_cjk(converted.strip())


    # Convert Simplified to Traditional characters
    def to_traditional(self, input):
        trad = json.load(open(os.path.join(os.path.dirname(__file__), "data/simplified.json"), encoding="utf-8"))
        for c in trad:
            input = input.replace(c, trad[c])
        return input


    ### Input formatting

    # Helper to convert separate words
    def __convert_tokenised(self, word):
        if word in word_dict:
            word = word_dict[word]
            if "/" in word:
                if self.dialect.lower() == 'north': word = word.split("/")[1]
                else: word = word.split("/")[0]
            word = self.__system_conversion(word)
            if self.format == 'number': word = self.__mark_to_number(word)
            if self.format == 'strip': word = "".join(c for c in unicodedata.normalize("NFD", word) if unicodedata.category(c) != "Mn")
            word = word.replace('--', self.suffix_token).replace('-', self.delimiter).replace(self.suffix_token, '--')
            return word
        return word


    # Helper switch for converting 漢字 based on defined transliteration system
    def __system_conversion(self, word):
        if self.system == 'poj': return self.__tailo_to_poj(word)
        if self.system == 'zhuyin': return self.__tailo_to_zhuyin(word)
        if self.system == 'tlpa': return self.__tailo_to_tlpa(word)
        if self.system == 'pingyim': return self.__tailo_to_pingyim(word)
        if self.system == 'tongiong': return self.__tailo_to_ti(word)
        if self.sandhi: return self.__tailo_to_tailo(word)
        else: return word


    # Helper functions to set delimiter according to transliteration system if wasn't explicitly defined by user
    def __set_default_delimiter(self):
        if self.system == 'tlpa' or self.system == 'zhuyin': return ' '
        if self.system == 'pingyim': return ''
        return '-'


    # Helper functions to set sandhi according to transliteration system if wasn't explicitly defined by user
    def __set_default_sandhi(self):
        if self.system == 'tongiong': return True
        return False


    ### Conversion functions

    # Helper to convert between transliteration systems
    def __replacement_tool(self, dictionary, input):
        pattern = re.compile('|'.join(dictionary.keys()))
        return pattern.sub(lambda m: dictionary[re.escape(m.group(0))], input)


    # Helper to convert word from Tai-lo to number
    def __mark_to_number(self, input):
        input = input.replace('--', '-'+self.suffix_token)
        words = input.split('-')
        input = ""
        for w in words:
            if len(w) > 0: input += '-' + self.__get_number_tone(w)
        return input[1:].replace(self.suffix_token, '--')

    # Helper to convert syllable from Tai-lo diacritic tones to number tones
    def __get_number_tone(self, input):
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
    def __preprocess_word(self, word):
        return word.replace('--', '-'+self.suffix_token).split('-')


    # Helper to convert syllable from Tai-lo number tones to diacritic tones
    def __get_mark_tone(self, input, placement, tones):
        for s in placement:
            if s.replace(''+self.tone_token+'', '') in input:
                part = s
                break
        return unicodedata.normalize('NFC', input.replace(part.replace(''+self.tone_token+'',''), part.replace(''+self.tone_token+'', tones[int(input[-1])]))[:-1])


    # Helper to apply tone sandhi to a word
    def __tone_sandhi(self, word):
        sandhi = {'1':'7', '7':'3', '3':'2', '2':'1', '5':'7',
                'p4':'p8', 't4':'t8', 'k4':'k8', 'h4':'2',
                'p8':'p4', 't8':'t4', 'k8':'k4', 'h8':'3'}
        if self.dialect == 'north':
            sandhi.update({'5':'3'})
        return self.__replacement_tool(sandhi, word)


    ### Tai-lo to other transliteration systems converting

    # Helper to convert syllable from Tai-lo to Tai-lo
    # (called only in cases when tone sandhi is applied)
    def __tailo_to_tailo(self, input):
        placement_tl = [
            'ia'+self.tone_token+'u', 'ua'+self.tone_token+'i', 'ua'+self.tone_token+'', 'ue'+self.tone_token+'', 'ui'+self.tone_token+'', 'a'+self.tone_token+'i',
            'a'+self.tone_token+'u', 'o'+self.tone_token+'o','ia'+self.tone_token+'', 'iu'+self.tone_token+'', 'io'+self.tone_token+'', 'o'+self.tone_token+'o', 'a'+self.tone_token+'', 
            'o'+self.tone_token+'', 'e'+self.tone_token+'', 'i'+self.tone_token+'', 'u'+self.tone_token+'', 'n'+self.tone_token+'g', 'm'+self.tone_token+'',
            'Ia'+self.tone_token+'u', 'Ua'+self.tone_token+'i', 'Ua'+self.tone_token+'', 'Ue'+self.tone_token+'', 'Ui'+self.tone_token+'', 'A'+self.tone_token+'i',
            'A'+self.tone_token+'u', 'O'+self.tone_token+'o','Ia'+self.tone_token+'', 'Iu'+self.tone_token+'', 'Io'+self.tone_token+'', 'O'+self.tone_token+'o', 'A'+self.tone_token+'', 
            'O'+self.tone_token+'', 'E'+self.tone_token+'', 'I'+self.tone_token+'', 'U'+self.tone_token+'', 'N'+self.tone_token+'g', 'M'+self.tone_token+''
        ]
        tones_tl = ["", "", "́", "̀", "", "̂", "̌", "̄", "̍", "̋"]
        words = self.__preprocess_word(input)
        input = ""
        number_tones = [self.__get_number_tone(w) for w in words if len(w) > 0]
        for i in range(0, len(number_tones)-1):
            number_tones[i] = self.__tone_sandhi(number_tones[i])
        for nt in number_tones:
            input += '-' + self.__get_mark_tone(nt, placement_tl, tones_tl)
        return input[1:].replace(self.suffix_token, '--')


    # Helper to convert syllable from Tai-lo to POJ
    def __tailo_to_poj(self, input):
        placement_poj = [
            'oa'+self.tone_token+'h', 'oa'+self.tone_token+'n', 'oa'+self.tone_token+'ng', 'oa'+self.tone_token+'ⁿ', 'oa'+self.tone_token+'t',
            'ia'+self.tone_token+'u', 'oe'+self.tone_token+'h', 'o'+self.tone_token+'e', 'oa'+self.tone_token+'i', 'u'+self.tone_token+'i', 'o'+self.tone_token+'a',
            'a'+self.tone_token+'i', 'a'+self.tone_token+'u', 'ia'+self.tone_token+'', 'iu'+self.tone_token+'', 'io'+self.tone_token+'', 'a'+self.tone_token+'',
            'o'+self.tone_token+'', 'o͘'+self.tone_token+'', 'e'+self.tone_token+'', 'i'+self.tone_token+'', 'u'+self.tone_token+'', 'n'+self.tone_token+'g', 'm'+self.tone_token+'',
            'Oa'+self.tone_token+'h', 'Oa'+self.tone_token+'n', 'Oa'+self.tone_token+'ng', 'Oa'+self.tone_token+'ⁿ', 'Oa'+self.tone_token+'t',
            'Ia'+self.tone_token+'u', 'Oe'+self.tone_token+'h', 'O'+self.tone_token+'e', 'Oa'+self.tone_token+'i', 'U'+self.tone_token+'i', 'O'+self.tone_token+'a',
            'A'+self.tone_token+'i', 'A'+self.tone_token+'u', 'Ia'+self.tone_token+'', 'Iu'+self.tone_token+'', 'Io'+self.tone_token+'', 'A'+self.tone_token+'',
            'O'+self.tone_token+'', 'O͘'+self.tone_token+'', 'E'+self.tone_token+'', 'I'+self.tone_token+'', 'U'+self.tone_token+'', 'N'+self.tone_token+'g', 'M'+self.tone_token+''
        ]
        convert_poj = {
            'nng':'nng', 'nnh':'hⁿ', 'nn':'ⁿ', 'ts':'ch',
            'ing':'eng', 'uai':'oai', 'uan':'oan',
            'ik':'ek', 'ua':'oa', 'ue':'oe', 'oo':'o͘',
            'Nng':'Nng', 'Nnh':'Hⁿ', 'Nn':'ⁿ', 'Ts':'Ch',
            'Ing':'Eng', 'Uai':'Oai', 'Uan':'Oan',
            'Ik':'Ek', 'Ua':'Oa', 'Ue':'Oe', 'Oo':'O͘',
        }
        tones_poj = ['', '', '́', '̀', '', '̂', '', '̄', '̍', '']
        words = self.__preprocess_word(input)
        input = ""
        number_tones = [self.__get_number_tone(w) for w in words if len(w) > 0]
        if self.sandhi:
            for i in range(0, len(number_tones)-1):
                number_tones[i] = self.__tone_sandhi(number_tones[i])
        for nt in number_tones:
            input += '-' + self.__get_mark_tone(self.__replacement_tool(convert_poj, nt), placement_poj, tones_poj)
        return input[1:].replace(self.suffix_token, '--')


    # Helper to convert syllable from Tai-lo to 方音符號 (zhuyin)
    # TODO: incorrect conversions
    def __tailo_to_zhuyin(self, input):
        input = input.lower()
        #input = self.__mark_to_number(input)
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
        words = self.__preprocess_word(input)
        input = ""
        number_tones = [self.__get_number_tone(w) for w in words if len(w) > 0]
        if self.sandhi:
            for i in range(0, len(number_tones)-1):
                number_tones[i] = self.__tone_sandhi(number_tones[i])
        for nt in number_tones:
            for t in nt:
                if t.isnumeric(): nt = nt.replace(t, zhuyin_tones[int(t)])
            input += '-' + self.__replacement_tool(zhuyin, nt)
        return input[1:].replace(self.suffix_token, '--')


    # Helper to convert syllable from Tai-lo to TLPA
    def __tailo_to_tlpa(self, input):
        convert_tlpa = {
            'tsh':'ch', 'ts':'c', 'Tsh':'Ch', 'Ts':'C'
        }
        words = self.__preprocess_word(input)
        input = ""
        number_tones = [self.__get_number_tone(w) for w in words if len(w) > 0]
        if self.sandhi:
            for i in range(0, len(number_tones)-1):
                number_tones[i] = self.__tone_sandhi(number_tones[i])
        for nt in number_tones:
            input += '-' + self.__replacement_tool(convert_tlpa, nt)
        return input[1:].replace(self.suffix_token, '--')


    # Helper to convert syllable from Tai-lo to Bbanlam pingyim
    # TODO: initial i to yi, probably solved
    def __tailo_to_pingyim(self, input):
        placement_pingyim = [
            'ua'+self.tone_token+'i', 'ia'+self.tone_token+'o', 'a'+self.tone_token+'i', 'a'+self.tone_token+'o', 
            'oo'+self.tone_token+'', 'ia'+self.tone_token+'', 'iu'+self.tone_token+'', 'io'+self.tone_token+'', 'ua'+self.tone_token+'', 'ue'+self.tone_token+'', 'ui'+self.tone_token+'',
            'a'+self.tone_token+'', 'o'+self.tone_token+'', 'e'+self.tone_token+'', 'i'+self.tone_token+'', 'u'+self.tone_token+'', 'n'+self.tone_token+'g', 'm'+self.tone_token+'',
            'Ua'+self.tone_token+'i', 'Ia'+self.tone_token+'o', 'A'+self.tone_token+'i', 'A'+self.tone_token+'o', 
            'Oo'+self.tone_token+'', 'Ia'+self.tone_token+'', 'Iu'+self.tone_token+'', 'Io'+self.tone_token+'', 'Ua'+self.tone_token+'', 'Ue'+self.tone_token+'', 'Ui'+self.tone_token+'',
            'A'+self.tone_token+'', 'O'+self.tone_token+'', 'E'+self.tone_token+'', 'I'+self.tone_token+'', 'U'+self.tone_token+'', 'N'+self.tone_token+'g', 'M'+self.tone_token+''
        ]
        input = input.lower()
        convert_pingyim = {
            'ainn':'nai', 'iunn':'niu', 'ann':'na', 'onn':'noo', 'enn':'ne',
            'inn':'ni', 'unn':'nu', 'au':'ao', 'ph':'p', 'nng':'lng', 'tsh':'c',
            'ng':'ng',
            'ts':'z', 'th':'t', 'kh':'k', 'ir':'i', 'p':'b', 'b':'bb',
            't':'d', 'k':'g', 'g':'gg', 'j':'l',
            'Ainn':'Nai', 'Iunn':'Niu', 'Ann':'Na', 'Onn':'Noo', 'Enn':'Ne',
            'Inn':'Ni', 'Unn':'Nu', 'Au':'Ao', 'Ph':'P', 'Nng':'Lng', 'Tsh':'C',
            'Ng':'Ng',
            'Ts':'Z', 'Th':'T', 'Kh':'K', 'Ir':'I', 'P':'B', 'B':'Bb',
            'T':'D', 'K':'G', 'G':'Gg', 'J':'L'
        }
        tones_pingyim = ['', '̄', '̌', '̀', '̄', '́', '', '̂', '́', '']
        words = self.__preprocess_word(input)
        input = ""
        number_tones = [self.__get_number_tone(w) for w in words if len(w) > 0]
        if self.sandhi:
            for i in range(0, len(number_tones)-1):
                number_tones[i] = self.__tone_sandhi(number_tones[i])
        for nt in number_tones:
            replaced = self.__replacement_tool(convert_pingyim, nt)
            if nt[0] == 'i': replaced = 'y' + replaced
            if nt[0] == 'u' and len(nt) > 2: replaced = 'w' + replaced[1:]
            elif nt[0] == 'u' and len(nt) == 2: replaced = 'w' + replaced
            if nt[0] == 'm': replaced = 'bbn' + replaced[1:]
            input += '-' + self.__get_mark_tone(replaced, placement_pingyim, tones_pingyim)
        return input[1:].replace(self.suffix_token, '--')


    # Helper to convert syllable from Tai-lo to Tong-iong ping-im
    #       Not enough information on tone mark placement
    def __tailo_to_ti(self, input):
        placement_ti = [
            'ua'+self.tone_token+'i', 'ia'+self.tone_token+'o', 'a'+self.tone_token+'i', 'a'+self.tone_token+'o', 
            'oo'+self.tone_token+'', 'ia'+self.tone_token+'', 'iu'+self.tone_token+'', 'io'+self.tone_token+'', 'ua'+self.tone_token+'', 'ue'+self.tone_token+'', 'ui'+self.tone_token+'',
            'a'+self.tone_token+'', 'o'+self.tone_token+'', 'e'+self.tone_token+'', 'i'+self.tone_token+'', 'u'+self.tone_token+'', 'n'+self.tone_token+'g', 'm'+self.tone_token+'',
            'Ua'+self.tone_token+'i', 'Ia'+self.tone_token+'o', 'A'+self.tone_token+'i', 'A'+self.tone_token+'o', 
            'Oo'+self.tone_token+'', 'Ia'+self.tone_token+'', 'Iu'+self.tone_token+'', 'Io'+self.tone_token+'', 'Ua'+self.tone_token+'', 'Ue'+self.tone_token+'', 'Ui'+self.tone_token+'',
            'A'+self.tone_token+'', 'O'+self.tone_token+'', 'E'+self.tone_token+'', 'I'+self.tone_token+'', 'U'+self.tone_token+'', 'N'+self.tone_token+'g', 'M'+self.tone_token+''
        ]
        # plosives don't change, ptkh 4/8 -> ptkh 4/8
        convert_ti = {'p4':'p4', 't4':'t4', 'k4':'k4', 'h4':'h4', 'p8':'p8', 't8':'t8', 'k8':'k8', 'h8':'h8',
                    'oo':'o', 'om':'om', 'ong':'ong', 'ir':'i', 'tsh':'c',
                    'ts':'z', 'nng':'nng', 'ng':'ng', 'g':'gh', 'kh':'k', 'k':'g',
                    'ph':'p', 'p':'b', 'b':'bh', 'th':'t', 't':'d',
                    'j':'r',
                    'Oo':'O', 'Om':'Om', 'Ong':'Ong', 'Ir':'I', 'Tsh':'C',
                    'Ts':'Z', 'Nng':'Nng', 'Ng':'Ng', 'G':'Gh', 'Kh':'K', 'K':'G',
                    'Ph':'P', 'P':'B', 'B':'Bh', 'Th':'T', 'T':'D',
                    'J':'R'}
        tones_ti = ["̊", "", "̀", "̂", "̄", "̌", "", "̄", "", "́"]
        words = self.__preprocess_word(input)
        input = ""
        number_tones = [self.__get_number_tone(w) for w in words if len(w) > 0]
        if self.sandhi:
            for i in range(0, len(number_tones)-1):
                number_tones[i] = self.__tone_sandhi(number_tones[i])
        for nt in number_tones:
            if nt[-2] == 'o': nt = (nt[:-2] + 'or' + nt[-1])
            input += '-' + self.__get_mark_tone(self.__replacement_tool(convert_ti, nt), placement_ti, tones_ti)
        return input[1:].replace(self.suffix_token, '--')


    ### Converted output formatting

    # Helper to convert Chinese punctuation to Latin punctuation with appropriate spacing
    # TODO: better punctuation spacing management
    def __format_punctuation_western(self, input):
        left_space = {'.':'.', ',':',',
                    '!':'!', '?':'?', ';':';', ':':':',
                    ')':')', ']':']', '」':'"',
                    '”':'"', '--':'--'}
        right_space = {'(':'(', '[':'[', '「':'"', '“':'"'}
        punctuation_converter = {'。':'.', '．':' ', '，':',', '、':',',
                                '！':'!', '？':'?', '；':';', '：':':',
                                '）':')', '］':']', '】':']', '（':'(',
                                '［':'[', '【':'['}
        for punctuation in punctuation_converter: input = input.replace(punctuation, punctuation_converter[punctuation])
        for left in left_space:
            input = input.replace(' ' + left, left_space[left])
            input = input.replace(left, left_space[left])
        for right in right_space:
            input = input.replace(right + ' ', right_space[right])
            input = input.replace(right, right_space[right])
        return input
    

    # Helper to restore original CJK punctuation with appropriate spacing
    def __format_punctuation_cjk(self, input):
        left_space = ['。', '．', '，', '、', '！', '？', '；', '：', '）', '］', '】', '」', '”', '--']
        right_space = ['（', '［', '【', '「', '“']
        for left in left_space:
            input = input.replace(' ' + left + ' ', left)
            input = input.replace(' ' + left, left)
        for right in right_space:
            input = input.replace(' ' + right + ' ', right)
            input = input.replace(right + ' ', right)
        return input


    # Helper to capitalise text in according to punctuation
    def __format_text(self, input):
        punc_filter = re.compile("([.!?]\s*)")
        split_with_punc = punc_filter.split(input)
        for i in split_with_punc:
            if len(i) > 1:
                split_with_punc[split_with_punc.index(i)] = (i[0].upper() + i[1:])
        return "".join(split_with_punc)
    

class Tokeniser(object):

    def __init__(self):
        pass

    # Tokenise the text into separate words
    def tokenise(self, input):
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
        for word in tokenised:
            punctuations = re.compile("([.,!?\"#$%&()*+/:;<=>@[\\]^`{|}~\t。．，、！？；：（）［］【】「」“”]\s*)")
            tokenised_word = punctuations.split(word)
            for subword in tokenised_word:
                tokenised_word[tokenised_word.index(subword)] = subword.split(" ")
            tokenised[tokenised.index(word)] = sum(tokenised_word, [])
        tokenised = sum(tokenised, [])
        while "" in tokenised: tokenised.remove("")
        return tokenised