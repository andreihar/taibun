import os
import json
import re
import unicodedata

"""
Description: Converts Chinese characters to phonetic transcription of any
	 		 of two main pronunciations of Taiwanese Hokkien. Supports both
             Traditional and Simplified characters.
Invariant: dialect = `south` for Zhangzhou (漳州)-leaning pronunciation (set by default)
		             `north` for Quanzhou (泉州)-leaning pronunciation
           system = Tai-lo for Tâi-uân Lô-má-jī Phing-im Hong-àn (set by default)
                    POJ for Pe̍h-ōe-jī.
                    Zhuyin for Taiwanese Phonetic Symbols
                    TLPA for Taiwanese Language Phonetic Alphabet
                    Pingyim for Bbánlám Uē Pìngyīm Hōng'àn
                    Tongiong for Daī-ghî Tōng-iōng Pīng-im
           format = mark for diacritical representation
					number for numeric representation
                    strip for no representation of tones
           sandhi = True for word-local sandhi
                    False for no sandhi
           delimiter = String that replaces the default delimiter
           punctuation = 'format' for Latin-style punctuation (set by default)
                         'none' to preserve original Chinese-style punctuation
"""


word_dict = json.load(open(os.path.join(os.path.dirname(__file__), "data/words.json"),'r', encoding="utf-8"))

class Converter(object):

    suffix_token = '[ЅFFX_ТКŊ]'
    tone_token = '[ТŊ_ТКŊ]'
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
        with open(os.path.join(os.path.dirname(__file__), "data/simplified.json"),'r', encoding="utf-8") as file:
            trad = json.load(file)
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
            word = self.__system_conversion(word).replace('---', '--')
            if self.format == 'number' and (self.system == 'tailo' or self.system == 'poj'): word = self.__mark_to_number(word)
            if self.format == 'strip':
                if self.system == 'tlpa':
                    for tone in ['1', '2', '3', '4', '5', '7', '8']: word = word.replace(tone, '')
                if self.system == 'zhuyin':
                    for tone in ['ˋ', '˪', 'ˊ', '˫', '˙']: word = word.replace(tone, '')
                else: word = "".join(c for c in unicodedata.normalize("NFD", word) if unicodedata.category(c) != "Mn")
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
        if re.search("á|é|í|ó|ú|ḿ|ńg|́", input): input += '2'
        elif re.search("à|è|ì|ò|ù|m̀|ǹg|̀", input): input += '3'
        elif re.search("â|ê|î|ô|û|m̂|n̂g|̂", input): input += '5'
        elif re.search("ā|ē|ī|ō|ū|m̄|n̄g|̄", input): input += '7'
        elif re.search('̍', input): input += '8'
        elif input[-1] in finals: input += '4'
        else: input += '1'
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
    # TODO: Make a better ruleset for Zhuyin
    def __tailo_to_zhuyin(self, input):
        """
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
            if 'ㄐ' in nt:
                if len(nt) > 1 and ('ㆴ' in nt or 'ㆵ' in nt or 'ㆶ' in nt or 'ㆷ' in nt):
                    nt = nt.replace('ㄐ', 'ㄐㄧ')
                if len(nt) == 1:
                    nt = nt.replace('ㄐ', 'ㄐㄧ')
            if 'ㄑ' in nt:
                if len(nt) > 1 and ('ㆴ' in nt or 'ㆵ' in nt or 'ㆶ' in nt or 'ㆷ' in nt):
                    nt = nt.replace('ㄑ', 'ㄑㄧ')
                if len(nt) == 1:
                    nt = nt.replace('ㄑ', 'ㄑㄧ')
            if 'ㄋ' in nt:
                for tone in zhuyin_tones:
                    if 'ㄋ'+tone in nt:
                        nt = nt.replace('ㄋ'+tone, 'ㄣ'+tone)
                for tone in stop_tones:
                    if 'ㄋ'+tone in nt:
                        nt = nt.replace('ㄋ'+tone, 'ㄣ'+tone)
        """
        input = input.lower()
        zhuyin = {
            'tshiunn':'ㄑㄧㆫ','tshiann':'ㄑㄧㆩ','tshuann':'ㄘㄨㆩ','tsuainn':'ㄗㄨㆮ','khaunnh':'ㄎㆯㆷ','tshuang':'ㄘㄨㄤ','tshiang':'ㄑㄧㄤ','tshiong':'ㄑㄧㆲ','khiang':'ㄎㄧㄤ','khennh':'ㄎㆥㆷ','khuann':'ㄎㄨㆩ','haunnh':'ㄏㆯㆷ','thuann':'ㄊㄨㆩ','tshioh':'ㄑㄧㄜㆷ','tshueh':'ㄘㄨㆤㆷ','tshang':'ㄘㄤ','huainn':'ㄏㄨㆮ','suainn':'ㄙㄨㆮ','phiang':'ㄆㄧㄤ','thiann':'ㄊㄧㆩ','tsiang':'ㄐㄧㄤ','tshiam':'ㄑㄧㆰ','khainn':'ㄎㆮ','phainn':'ㄆㆮ','tshinn':'ㄑㆪ','tshian':'ㄑㄧㄢ','tsiong':'ㄐㄧㆲ','tsuann':'ㄗㄨㆩ','tsainn':'ㄗㆮ','khiong':'ㄎㄧㆲ','tshiap':'ㄑㄧㄚㆴ','tshiau':'ㄑㄧㄠ','tshuan':'ㄘㄨㄢ','tsiunn':'ㄐㄧㆫ','tshiah':'ㄑㄧㄚㆷ','tshann':'ㄘㆩ','tshiok':'ㄑㄧㆦㆶ','tshong':'ㄘㆲ','kuainn':'ㄍㄨㆮ','tshuah':'ㄘㄨㄚㆷ','hiannh':'ㄏㄧㆩㆷ','tshiat':'ㄑㄧㄚㆵ','khiunn':'ㄎㄧㆫ','thiong':'ㄊㄧㆲ','phiann':'ㄆㄧㆩ','tshing':'ㄑㄧㄥ','tsiann':'ㄐㄧㆩ','ngiauh':'ㄫㄧㄠㆷ','tshenn':'ㄘㆥ','phuann':'ㄆㄨㆩ','tshauh':'ㄘㄠㆷ','khuinn':'ㄎㄨㆪ','tshiak':'ㄑㄧㄚㆶ','liong':'ㄌㄧㆲ','khuat':'ㄎㄨㄚㆵ','tsiat':'ㄐㄧㄚㆵ','puann':'ㄅㄨㆩ','tshap':'ㄘㄚㆴ','tshah':'ㄘㄚㆷ','kainn':'ㄍㆮ','tshau':'ㄘㄠ','khiat':'ㄎㄧㄚㆵ','thiok':'ㄊㄧㆦㆶ','tship':'ㄑㄧㆴ','piann':'ㄅㄧㆩ','tshuh':'ㄘㄨㆷ','hainn':'ㄏㆮ','thuah':'ㄊㄨㄚㆷ','tshoh':'ㄘㄜㆷ','phann':'ㄆㆩ','tshih':'ㄑㄧㆷ','tshan':'ㄘㄢ','tsenn':'ㄗㆥ','tsuat':'ㄗㄨㄚㆵ','thuan':'ㄊㄨㄢ','tshin':'ㄑㄧㄣ','phing':'ㄆㄧㄥ','thiap':'ㄊㄧㄚㆴ','tiong':'ㄉㄧㆲ','thiah':'ㄊㄧㄚㆷ','jiong':'ㆢㄧㆲ','khinn':'ㄎㆪ','tuann':'ㄉㄨㆩ','hiong':'ㄏㄧㆲ','thenn':'ㄊㆥ','tshak':'ㄘㄚㆶ','thuat':'ㄊㄨㄚㆵ','sannh':'ㄙㆩㆷ','tsiam':'ㄐㄧㆰ','thong':'ㄊㆲ','khuan':'ㄎㄨㄢ','tshoo':'ㄘㆦ','khiah':'ㄎㄧㄚㆷ','tsham':'ㄘㆰ','phiah':'ㄆㄧㄚㆷ','tiunn':'ㄉㄧㆫ','khann':'ㄎㆩ','phuah':'ㄆㄨㄚㆷ','thing':'ㄊㄧㄥ','phian':'ㄆㄧㄢ','tsing':'ㄐㄧㄥ','siong':'ㄒㄧㆲ','tsinn':'ㄐㆪ','tsong':'ㄗㆲ','tsiap':'ㄐㄧㄚㆴ','hannh':'ㄏㆩㆷ','thiat':'ㄊㄧㄚㆵ','tsioh':'ㄐㄧㄜㆷ','tshai':'ㄘㄞ','tsiah':'ㄐㄧㄚㆷ','khuah':'ㄎㄨㄚㆷ','tsiok':'ㄐㄧㆦㆶ','tshia':'ㄑㄧㄚ','khiap':'ㄎㄧㄚㆴ','phngh':'ㄆㆭㆷ','khioh':'ㄎㄧㄜㆷ','liang':'ㄌㄧㄤ','suann':'ㄙㄨㆩ','khang':'ㄎㄤ','siang':'ㄒㄧㄤ','thann':'ㄊㆩ','phong':'ㄆㆲ','khiam':'ㄎㄧㆰ','phiat':'ㄆㄧㄚㆵ','khuai':'ㄎㄨㄞ','hiauh':'ㄏㄧㄠㆷ','khngh':'ㄎㆭㆷ','thian':'ㄊㄧㄢ','khing':'ㄎㄧㄥ','phauh':'ㄆㄠㆷ','thang':'ㄊㄤ','piang':'ㄅㄧㄤ','phiak':'ㄆㄧㄚㆶ','tsuah':'ㄗㄨㄚㆷ','tshui':'ㄘㄨㄧ','phueh':'ㄆㄨㆤㆷ','honnh':'ㄏㆧㆷ','tshng':'ㄘㆭ','iaunn':'ㄧㆯ','phenn':'ㄆㆥ','tsang':'ㄗㄤ','thinn':'ㄊㆪ','khong':'ㄎㆲ','thiau':'ㄊㄧㄠ','khiok':'ㄎㄧㆦㆶ','tsian':'ㄐㄧㄢ','tainn':'ㄉㆮ','phuat':'ㄆㄨㄚㆵ','tsann':'ㄗㆩ','tiann':'ㄉㄧㆩ','kiong':'ㄍㄧㆲ','thiam':'ㄊㄧㆰ','tshim':'ㄑㄧㆬ','tsueh':'ㄗㄨㆤㆷ','khian':'ㄎㄧㄢ','tshik':'ㄑㄧㆶ','khueh':'ㄎㄨㆤㆷ','hiann':'ㄏㄧㆩ','khiau':'ㄎㄧㄠ','phinn':'ㄆㆪ','tsuan':'ㄗㄨㄢ','tshua':'ㄘㄨㄚ','giang':'ㆣㄧㄤ','kuinn':'ㄍㄨㆪ','tshio':'ㄑㄧㄜ','tshue':'ㄘㄨㆤ','tshut':'ㄘㄨㆵ','tsheh':'ㄘㆤㆷ','siunn':'ㄒㄧㆫ','tshiu':'ㄑㄧㄨ','phiau':'ㄆㄧㄠ','tshok':'ㄘㆦㆶ','phuan':'ㄆㄨㄢ','giong':'ㆣㄧㆲ','jiang':'ㆢㄧㄤ','huinn':'ㄏㄨㆪ','tsiau':'ㄐㄧㄠ','tshit':'ㄑㄧㆵ','hiunn':'ㄏㄧㆫ','hiang':'ㄏㄧㄤ','khenn':'ㄎㆥ','phang':'ㄆㄤ','huann':'ㄏㄨㆩ','tshun':'ㄘㄨㄣ','kuann':'ㄍㄨㆩ','kiunn':'ㄍㄧㆫ','uainn':'ㄨㆮ','ngiau':'ㄫㄧㄠ','kiann':'ㄍㄧㆩ','siann':'ㄒㄧㆩ','tshat':'ㄘㄚㆵ','piau':'ㄅㄧㄠ','phah':'ㄆㄚㆷ','khiu':'ㄎㄧㄨ','tsim':'ㄐㄧㆬ','tsam':'ㄗㆰ','tshi':'ㄑㄧ','khio':'ㄎㄧㄜ','phau':'ㄆㄠ','tong':'ㄉㆲ','tsau':'ㄗㄠ','tsia':'ㄐㄧㄚ','hinn':'ㄏㆪ','tsoo':'ㄗㆦ','iong':'ㄧㆲ','phue':'ㄆㄨㆤ','tsok':'ㄗㆦㆶ','tian':'ㄉㄧㄢ','sing':'ㄒㄧㄥ','bian':'ㆠㄧㄢ','iunn':'ㄧㆫ','khip':'ㄎㄧㆴ','khik':'ㄎㄧㆶ','thin':'ㄊㄧㄣ','thok':'ㄊㆦㆶ','honn':'ㄏㆧ','tsng':'ㄗㆭ','tsiu':'ㄐㄧㄨ','tsun':'ㄗㄨㄣ','tsha':'ㄘㄚ','tsik':'ㄐㄧㆶ','penn':'ㄅㆥ','kian':'ㄍㄧㄢ','kuan':'ㄍㄨㄢ','senn':'ㄙㆥ','khap':'ㄎㄚㆴ','tenn':'ㄉㆥ','kuai':'ㄍㄨㄞ','kinn':'ㄍㆪ','gian':'ㆣㄧㄢ','thua':'ㄊㄨㄚ','khng':'ㄎㆭ','bing':'ㆠㄧㄥ','long':'ㄌㆲ','phoo':'ㄆㆦ','pian':'ㄅㄧㄢ','song':'ㄙㆲ','khun':'ㄎㄨㄣ','hann':'ㄏㆩ','kham':'ㄎㆰ','lang':'ㄌㄤ','ging':'ㆣㄧㄥ','gueh':'ㆣㄨㆤㆷ','buat':'ㆠㄨㄚㆵ','guat':'ㆣㄨㄚㆵ','biat':'ㆠㄧㄚㆵ','bueh':'ㆠㄨㆤㆷ','kiah':'ㄍㄧㄚㆷ','liat':'ㄌㄧㄚㆵ','mngh':'ㄇㆭㆷ','thue':'ㄊㄨㆤ','thim':'ㄊㄧㆬ','tiok':'ㄉㄧㆦㆶ','hiok':'ㄏㄧㆦㆶ','khat':'ㄎㄚㆵ','tsak':'ㄗㄚㆶ','biau':'ㆠㄧㄠ','tioh':'ㄉㄧㄜㆷ','phik':'ㄆㄧㆶ','giau':'ㆣㄧㄠ','iann':'ㄧㆩ','khok':'ㄎㆦㆶ','tuan':'ㄉㄨㄢ','buan':'ㆠㄨㄢ','siak':'ㄒㄧㄚㆶ','kioh':'ㄍㄧㄜㆷ','huih':'ㄏㄨㄧㆷ','luah':'ㄌㄨㄚㆷ','tsho':'ㄘㄜ','hiap':'ㄏㄧㄚㆴ','jiah':'ㆢㄧㄚㆷ','jiam':'ㆢㄧㆰ','jiap':'ㆢㄧㄚㆴ','jiat':'ㆢㄧㄚㆵ','gioh':'ㆣㄧㄜㆷ','liok':'ㄌㄧㆦㆶ','lioh':'ㄌㄧㄜㆷ','tsap':'ㄗㄚㆴ','kooh':'ㄍㆦㆷ','lueh':'ㄌㄨㆤㆷ','tiak':'ㄉㄧㄚㆶ','tauh':'ㄉㄠㆷ','pheh':'ㄆㆤㆷ','luat':'ㄌㄨㄚㆵ','pueh':'ㄅㄨㆤㆷ','kuih':'ㄍㄨㄧㆷ','tuat':'ㄉㄨㄚㆵ','lauh':'ㄌㄠㆷ','puat':'ㄅㄨㄚㆵ','phuh':'ㄆㄨㆷ','piat':'ㄅㄧㄚㆵ','tiap':'ㄉㄧㄚㆴ','juah':'ㆡㄨㄚㆷ','tsat':'ㄗㄚㆵ','pong':'ㄅㆲ','hioh':'ㄏㄧㄜㆷ','gong':'ㆣㆲ','sioh':'ㄒㄧㄜㆷ','siok':'ㄒㄧㆦㆶ','tsip':'ㄐㄧㆴ','ainn':'ㆮ','thau':'ㄊㄠ','siam':'ㄒㄧㆰ','sang':'ㄙㄤ','tsua':'ㄗㄨㄚ','phua':'ㄆㄨㄚ','tsin':'ㄐㄧㄣ','thik':'ㄊㄧㆶ','uann':'ㄨㆩ','sinn':'ㄒㆪ','kenn':'ㄍㆥ','thak':'ㄊㄚㆶ','luan':'ㄌㄨㄢ','phai':'ㄆㄞ','thio':'ㄊㄧㄜ','khue':'ㄎㄨㆤ','pinn':'ㄅㆪ','suan':'ㄙㄨㄢ','phin':'ㄆㄧㄣ','siah':'ㄒㄧㄚㆷ','hian':'ㄏㄧㄢ','tham':'ㄊㆰ','puan':'ㄅㄨㄢ','tsue':'ㄗㄨㆤ','thap':'ㄊㄚㆴ','thah':'ㄊㄚㆷ','khin':'ㄎㄧㄣ','khai':'ㄎㄞ','kiok':'ㄍㄧㆦㆶ','kiau':'ㄍㄧㄠ','khim':'ㄎㄧㆬ','jian':'ㆢㄧㄢ','thng':'ㄊㆭ','khak':'ㄎㄚㆶ','kann':'ㄍㆩ','khua':'ㄎㄨㄚ','phok':'ㄆㆦㆶ','tsit':'ㄐㄧㆵ','lian':'ㄌㄧㄢ','siat':'ㄒㄧㄚㆵ','tsah':'ㄗㄚㆷ','that':'ㄊㄚㆵ','phio':'ㄆㄧㄜ','tinn':'ㄉㆪ','huai':'ㄏㄨㄞ','hiau':'ㄏㄧㄠ','khoo':'ㄎㆦ','tshu':'ㄘㄨ','iang':'ㄧㄤ','liap':'ㄌㄧㄚㆴ','giat':'ㆣㄧㄚㆵ','hooh':'ㄏㆦㆷ','kueh':'ㄍㄨㆤㆷ','piah':'ㄅㄧㄚㆷ','giap':'ㆣㄧㄚㆴ','giah':'ㆣㄧㄚㆷ','suat':'ㄙㄨㄚㆵ','sueh':'ㄙㄨㆤㆷ','tiah':'ㄉㄧㄚㆷ','hiah':'ㄏㄧㄚㆷ','suah':'ㄙㄨㄚㆷ','piak':'ㄅㄧㄚㆶ','tiuh':'ㄉㄧㄨㆷ','liah':'ㄌㄧㄚㆷ','nauh':'ㄋㄠㆷ','kuah':'ㄍㄨㄚㆷ','puah':'ㄅㄨㄚㆷ','tsih':'ㄐㄧㆷ','khih':'ㄎㄧㆷ','haih':'ㄏㄞㆷ','huah':'ㄏㄨㄚㆷ','phih':'ㄆㄧㆷ','thih':'ㄊㄧㆷ','kong':'ㄍㆲ','mooh':'ㄇㆦㆷ','tann':'ㄉㆩ','phak':'ㄆㄚㆶ','thiu':'ㄊㄧㄨ','sann':'ㄙㆩ','siau':'ㄒㄧㄠ','tsai':'ㄗㄞ','king':'ㄍㄧㄥ','thoo':'ㄊㆦ','khau':'ㄎㄠ','tshe':'ㄘㆤ','huan':'ㄏㄨㄢ','bong':'ㆠㆲ','khit':'ㄎㄧㆵ','tiau':'ㄉㄧㄠ','liau':'ㄌㄧㄠ','ting':'ㄉㄧㄥ','thoh':'ㄊㄜㆷ','theh':'ㄊㆤㆷ','tuah':'ㄉㄨㄚㆷ','tiat':'ㄉㄧㄚㆵ','hiat':'ㄏㄧㄚㆵ','kheh':'ㄎㆤㆷ','kauh':'ㄍㄠㆷ','huat':'ㄏㄨㄚㆵ','buah':'ㆠㄨㄚㆷ','bang':'ㆠㄤ','khui':'ㄎㄨㄧ','kiam':'ㄍㄧㆰ','phan':'ㄆㄢ','phun':'ㄆㄨㄣ','ngia':'ㄫㄧㄚ','pang':'ㄅㄤ','liam':'ㄌㄧㆰ','tiam':'ㄉㄧㆰ','khia':'ㄎㄧㄚ','than':'ㄊㄢ','ngiu':'ㄫㄧㄨ','phui':'ㄆㄨㄧ','miau':'ㄇㄧㄠ','thun':'ㄊㄨㄣ','hang':'ㄏㄤ','khan':'ㄎㄢ','tang':'ㄉㄤ','tsui':'ㄗㄨㄧ','ngoo':'ㄫㆦ','kang':'ㄍㄤ','thui':'ㄊㄨㄧ','niau':'ㄋㄧㄠ','gang':'ㆣㄤ','tsoh':'ㄗㄜㆷ','khut':'ㄎㄨㆵ','khuh':'ㄎㄨㆷ','tsut':'ㄗㄨㆵ','thuh':'ㄊㄨㆷ','thut':'ㄊㄨㆵ','kuat':'ㄍㄨㄚㆵ','ngeh':'ㄫㆤㆷ','kiap':'ㄍㄧㄚㆴ','phut':'ㄆㄨㆵ','hueh':'ㄏㄨㆤㆷ','tsan':'ㄗㄢ','phoh':'ㄆㄜㆷ','kiat':'ㄍㄧㄚㆵ','mauh':'ㄇㄠㆷ','tseh':'ㄗㆤㆷ','ngai':'ㄫㄞ','ngau':'ㄫㄠ','uang':'ㄨㄤ','giam':'ㆣㄧㆰ','hiam':'ㄏㄧㆰ','ling':'ㄌㄧㄥ','jiok':'ㆢㄧㆦㆶ','phit':'ㄆㄧㆵ','siap':'ㄒㄧㄚㆴ','tsio':'ㄐㄧㄜ','thai':'ㄊㄞ','jiau':'ㆢㄧㄠ','sian':'ㄒㄧㄢ','hing':'ㄏㄧㄥ','guan':'ㆣㄨㄢ','hong':'ㄏㆲ','ping':'ㄅㄧㄥ','khah':'ㄎㄚㆷ','nua':'ㄋㄨㄚ','pio':'ㄅㄧㄜ','lio':'ㄌㄧㄜ','peh':'ㄅㆤㆷ','put':'ㄅㄨㆵ','sut':'ㄙㄨㆵ','hok':'ㄏㆦㆶ','koh':'ㄍㄜㆷ','phi':'ㄆㄧ','hak':'ㄏㄚㆶ','sen':'ㄙㆤㄣ','pau':'ㄅㄠ','tiu':'ㄉㄧㄨ','hue':'ㄏㄨㆤ','gam':'ㆣㆰ','pak':'ㄅㄚㆶ','hai':'ㄏㄞ','nga':'ㄫㄚ','kah':'ㄍㄚㆷ','sin':'ㄒㄧㄣ','gau':'ㆣㄠ','tak':'ㄉㄚㆶ','pua':'ㄅㄨㄚ','gai':'ㆣㄞ','bui':'ㆠㄨㄧ','gio':'ㆣㄧㄜ','lia':'ㄌㄧㄚ','ioh':'ㄧㄜㆷ','sip':'ㄒㄧㆴ','gun':'ㆣㄨㄣ','ngi':'ㄫㄧ','lua':'ㄌㄨㄚ','bua':'ㆠㄨㄚ','lok':'ㄌㆦㆶ','mau':'ㄇㄠ','hiu':'ㄏㄧㄨ','lak':'ㄌㄚㆶ','nau':'ㄋㄠ','soh':'ㄙㄜㆷ','bok':'ㆠㆦㆶ','kut':'ㄍㄨㆵ','suh':'ㄙㄨㆷ','png':'ㄅㆭ','mua':'ㄇㄨㄚ','beh':'ㆠㆤㆷ','sap':'ㄙㄚㆴ','tio':'ㄉㄧㄜ','pin':'ㄅㄧㄣ','tho':'ㄊㄜ','seh':'ㄙㆤㆷ','mai':'ㄇㄞ','iap':'ㄧㄚㆴ','puh':'ㄅㄨㆷ','ong':'ㆲ','bih':'ㆠㄧㆷ','toh':'ㄉㄜㆷ','tuh':'ㄉㄨㆷ','keh':'ㄍㆤㆷ','kok':'ㄍㆦㆶ','nah':'ㄋㄚㆷ','thu':'ㄊㄨ','enn':'ㆥ','hut':'ㄏㄨㆵ','jia':'ㆢㄧㄚ','lap':'ㄌㄚㆴ','kng':'ㄍㆭ','gin':'ㆣㄧㄣ','ann':'ㆩ','hip':'ㄏㄧㆴ','tah':'ㄉㄚㆷ','tap':'ㄉㄚㆴ','tom':'ㄉㆱ','kat':'ㄍㄚㆵ','meh':'ㄇㆤㆷ','teh':'ㄉㆤㆷ','jun':'ㆡㄨㄣ','piu':'ㄅㄧㄨ','nge':'ㄫㆤ','tui':'ㄉㄨㄧ','kio':'ㄍㄧㄜ','pui':'ㄅㄨㄧ','tun':'ㄉㄨㄣ','poo':'ㄅㆦ','boo':'ㆠㆦ','sun':'ㄙㄨㄣ','lih':'ㄌㄧㆷ','pan':'ㄅㄢ','lun':'ㄌㄨㄣ','han':'ㄏㄢ','mui':'ㄇㄨㄧ','bin':'ㆠㄧㄣ','kui':'ㄍㄨㄧ','iat':'ㄧㄚㆵ','hoh':'ㄏㄜㆷ','koo':'ㄍㆦ','khi':'ㄎㄧ','kun':'ㄍㄨㄣ','uih':'ㄨㄧㆷ','geh':'ㆣㆤㆷ','tut':'ㄉㄨㆵ','gua':'ㆣㄨㄚ','san':'ㄙㄢ','tan':'ㄉㄢ','hun':'ㄏㄨㄣ','kho':'ㄎㄜ','pun':'ㄅㄨㄣ','bun':'ㆠㄨㄣ','gue':'ㆣㄨㆤ','sit':'ㄒㄧㆵ','loo':'ㄌㆦ','gia':'ㆣㄧㄚ','hia':'ㄏㄧㄚ','buh':'ㆠㄨㆷ','mia':'ㄇㄧㄚ','gui':'ㆣㄨㄧ','hui':'ㄏㄨㄧ','kha':'ㄎㄚ','iam':'ㄧㆰ','lan':'ㄌㄢ','noo':'ㄋㆦ˫','gik':'ㆣㄧㆶ','pit':'ㄅㄧㆵ','kia':'ㄍㄧㄚ','ooh':'ㆦㆷ','leh':'ㄌㆤㆷ','bue':'ㆠㄨㆤ','lui':'ㄌㄨㄧ','gan':'ㆣㄢ','ing':'ㄧㄥ','jue':'ㆡㄨㆤ','giu':'ㆣㄧㄨ','som':'ㄙㆱ','kue':'ㄍㄨㆤ','hat':'ㄏㄚㆵ','biu':'ㆠㄧㄨ','kam':'ㄍㆰ','hik':'ㄏㄧㆶ','iah':'ㄧㄚㆷ','tia':'ㄉㄧㄚ','sah':'ㄙㄚㆷ','ueh':'ㄨㆤㆷ','gok':'ㆣㆦㆶ','sui':'ㄙㄨㄧ','uah':'ㄨㄚㆷ','lit':'ㄌㄧㆵ','tso':'ㄗㄜ','bau':'ㆠㄠ','nia':'ㄋㄧㄚ','niu':'ㄋㄧㄨ','luh':'ㄌㄨㆷ','jip':'ㆢㄧㆴ','jit':'ㆢㄧㆵ','lip':'ㄌㄧㆴ','lat':'ㄌㄚㆵ','lik':'ㄌㄧㆶ','gak':'ㆣㄚㆶ','tat':'ㄉㄚㆵ','bit':'ㆠㄧㆵ','bik':'ㆠㄧㆶ','tsa':'ㄗㄚ','sak':'ㄙㄚㆶ','kip':'ㄍㄧㆴ','pai':'ㄅㄞ','gim':'ㆣㄧㆬ','kau':'ㄍㄠ','nng':'ㄋㆭ','sio':'ㄒㄧㄜ','tha':'ㄊㄚ','jiu':'ㆢㄧㄨ','tai':'ㄉㄞ','uai':'ㄨㄞ','tin':'ㄉㄧㄣ','kua':'ㄍㄨㄚ','hng':'ㄏㆭ','lin':'ㄌㄧㄣ','tok':'ㄉㆦㆶ','bai':'ㆠㄞ','bio':'ㆠㄧㄜ','iok':'ㄧㆦㆶ','sng':'ㄙㆭ','pue':'ㄅㄨㆤ','nai':'ㄋㄞ','kin':'ㄍㄧㄣ','pik':'ㄅㄧㆶ','kik':'ㄍㄧㆶ','tsu':'ㄗㄨ','kan':'ㄍㄢ','sia':'ㄒㄧㄚ','kih':'ㄍㄧㆷ','mih':'ㄇㄧㆷ','hio':'ㄏㄧㄜ','tau':'ㄉㄠ','nih':'ㄋㄧㆷ','khu':'ㄎㄨ','lim':'ㄌㄧㆬ','pha':'ㄆㄚ','him':'ㄏㄧㆬ','pho':'ㄆㄜ','ham':'ㄏㆰ','hau':'ㄏㄠ','sim':'ㄒㄧㆬ','soo':'ㄙㆦ','ian':'ㄧㄢ','sat':'ㄙㄚㆵ','uan':'ㄨㄢ','hit':'ㄏㄧㆵ','sam':'ㄙㆰ','phe':'ㄆㆤ','mue':'ㄇㄨㆤ','tng':'ㄉㆭ','lah':'ㄌㄚㆷ','thi':'ㄊㄧ','pok':'ㄅㆦㆶ','kiu':'ㄍㄧㄨ','pat':'ㄅㄚㆵ','jin':'ㆢㄧㄣ','tua':'ㄉㄨㄚ','tse':'ㄗㆤ','sue':'ㄙㄨㆤ','hah':'ㄏㄚㆷ','khe':'ㄎㆤ','tue':'ㄉㄨㆤ','hua':'ㄏㄨㄚ','tsi':'ㄐㄧ','kai':'ㄍㄞ','iau':'ㄧㄠ','bak':'ㆠㄚㆶ','the':'ㄊㆤ','sua':'ㄙㄨㄚ','jim':'ㆢㄧㆬ','sok':'ㄙㆦㆶ','too':'ㄉㆦ','uat':'ㄨㄚㆵ','siu':'ㄒㄧㄨ','aih':'ㄞㆷ','but':'ㆠㄨㆵ','inn':'ㆪ','heh':'ㄏㆤㆷ','liu':'ㄌㄧㄨ','tim':'ㄉㄧㆬ','tik':'ㄉㄧㆶ','lai':'ㄌㄞ','pah':'ㄅㄚㆷ','pih':'ㄅㄧㆷ','tam':'ㄉㆰ','poh':'ㄅㄜㆷ','ang':'ㄤ','moo':'ㄇㆦ','tih':'ㄉㄧㆷ','hmh':'ㄏㆬㆷ','lau':'ㄌㄠ','hin':'ㄏㄧㄣ','kim':'ㄍㄧㆬ','onn':'ㆧ','ban':'ㆠㄢ','neh':'ㄋㆤㆷ','hoo':'ㄏㆦ','loh':'ㄌㄜㆷ','mng':'ㄇㆭ','kak':'ㄍㄚㆶ','bat':'ㆠㄚㆵ','sau':'ㄙㄠ','sai':'ㄙㄞ','kap':'ㄍㄚㆴ','goo':'ㆣㆦ','lam':'ㄌㆰ','sik':'ㄒㄧㆶ','hap':'ㄏㄚㆴ','lue':'ㄌㄨㆤ','phu':'ㄆㄨ','jio':'ㆢㄧㄜ','bah':'ㆠㄚㆷ','lut':'ㄌㄨㆵ','sih':'ㄒㄧㆷ','tit':'ㄉㄧㆵ','bo':'ㆠㄜ','tu':'ㄉㄨ','ah':'ㄚㆷ','ni':'ㄋㄧ','un':'ㄨㄣ','in':'ㄧㄣ','lu':'ㄌㄨ','la':'ㄌㄚ','bu':'ㆠㄨ','ak':'ㄚㆶ','ta':'ㄉㄚ','bi':'ㆠㄧ','ui':'ㄨㄧ','he':'ㄏㆤ','sa':'ㄙㄚ','lo':'ㄌㄜ','oo':'ㆦ','le':'ㄌㆤ','pe':'ㄅㆤ','ha':'ㄏㄚ','hi':'ㄏㄧ','au':'ㄠ','im':'ㄧㆬ','ka':'ㄍㄚ','ua':'ㄨㄚ','li':'ㄌㄧ','gi':'ㆣㄧ','ik':'ㄧㆶ','at':'ㄚㆵ','ip':'ㄧㆴ','se':'ㄙㆤ','ko':'ㄍㄜ','ng':'ㆭ','be':'ㆠㆤ','ge':'ㆣㆤ','ue':'ㄨㆤ','ho':'ㄏㄜ','mi':'ㄇㄧ','ne':'ㄋㆤ','an':'ㄢ','ok':'ㆦㆶ','ma':'ㄇㄚ','ut':'ㄨㆵ','ti':'ㄉㄧ','te':'ㄉㆤ','ju':'ㆡㄨ','pa':'ㄅㄚ','so':'ㄙㄜ','oh':'ㄜㆷ','gu':'ㆣㄨ','me':'ㄇㆤ','si':'ㄒㄧ','eh':'ㆤㆷ','hm':'ㄏㆬ','ki':'ㄍㄧ','su':'ㄙㄨ','am':'ㆰ','hu':'ㄏㄨ','na':'ㄋㄚ','io':'ㄧㄜ','ku':'ㄍㄨ','om':'ㆱ','ga':'ㆣㄚ','ke':'ㄍㆤ','po':'ㄅㄜ','ai':'ㄞ','ji':'ㆢㄧ','iu':'ㄧㄨ','ba':'ㆠㄚ','ia':'ㄧㄚ','to':'ㄉㄜ','it':'ㄧㆵ','ap':'ㄚㆴ','uh':'ㄨㆷ','pu':'ㄅㄨ','go':'ㆣㄜ','pi':'ㄅㄧ','o':'ㄜ','a':'ㄚ','e':'ㆤ','i':'ㄧ','m':'ㆬ','u':'ㄨ'
        }
        zhuyin_tones = 	['', '', 'ˋ', '˪', '', 'ˊ', '', '˫', '˙']
        words = self.__preprocess_word(input)
        input = ""
        number_tones = [self.__get_number_tone(w) for w in words if len(w) > 0]
        if self.sandhi:
            for i in range(0, len(number_tones)-1):
                number_tones[i] = self.__tone_sandhi(number_tones[i])
        for nt in number_tones:
            nt = self.__replacement_tool(zhuyin, nt).replace(self.suffix_token, '')
            if self.format != 'number':
                for t in nt:
                    if t.isnumeric(): nt = nt.replace(t, zhuyin_tones[int(t)])
            input += '-' + nt
        return input[1:]


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
            if self.format != 'number': input += '-' + self.__get_mark_tone(replaced, placement_pingyim, tones_pingyim)
            else: input += '-' + replaced
        return input[1:].replace(self.suffix_token, '')


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
            if self.format != 'number': input += '-' + self.__get_mark_tone(self.__replacement_tool(convert_ti, nt), placement_ti, tones_ti)
            else: input += '-' + self.__replacement_tool(convert_ti, nt)
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
        for word in tokenised:
            if (word[-1] == '的' or word[-1] == '矣') and len(word) > 1:
                tokenised.insert(tokenised.index(word)+1, word[-1])
                tokenised[tokenised.index(word)] = word[:-1]
        return tokenised