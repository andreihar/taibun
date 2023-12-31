import os
import json
import re
import unicodedata

"""
Description: Converts Chinese characters to Taiwanese Hokkien phonetic transcriptions.
             Supports both Traditional and Simplified characters.
Invariant: dialect = `south` (Zhangzhou-leaning, default), `north` (Quanzhou-leaning)
           system = `Tailo` (default), `POJ`, `Zhuyin`, `TLPA`, `Pingyim`, `Tongiong`, `IPA`
           format = `mark` (diacritical), `number` (numeric), `strip` (no tones)
           sandhi = True, False
           delimiter = String that replaces the default delimiter
           punctuation = `format` (Latin-style, default), `none` (preserve original)
"""


word_dict = json.load(open(os.path.join(os.path.dirname(__file__), "data/words.json"),'r', encoding="utf-8"))

# Helper to check if the character is a Chinese character
def is_cjk(input):
    return all(
        0x4E00 <= ord(char) <= 0x9FFF or  # BASIC
        0x3400 <= ord(char) <= 0x4DBF or  # Ext A
        0x20000 <= ord(char) <= 0x2A6DF or  # Ext B
        0x2A700 <= ord(char) <= 0x2EBEF or  # Ext C,D,E,F
        0x30000 <= ord(char) <= 0x323AF or  # Ext G,H
        0x2EBF0 <= ord(char) <= 0x2EE5F  # Ext I
        for char in input
    )

# Convert Simplified to Traditional characters
def to_traditional(input):
    with open(os.path.join(os.path.dirname(__file__), "data/simplified.json"),'r', encoding="utf-8") as file:
        trad = json.load(file)
    return ''.join(trad.get(c, c) for c in input)

class Converter(object):

    suffix_token = '[ЅFFX_ТКŊ]'
    tt = '[ТŊ_ТКŊ]'
    DEFAULT_DELIMITER = object()
    DEFAULT_SANDHI = object()

    def __init__(self, system='Tailo', dialect='south', format='mark', delimiter=DEFAULT_DELIMITER, sandhi=DEFAULT_SANDHI, punctuation='format'):
        self.system = system.lower()
        self.dialect = dialect.lower()
        self.format = format
        self.delimiter = delimiter
        self.sandhi = sandhi
        self.punctuation = punctuation


    ### Interface functions

    # Convert tokenised text into specified transliteration system
    def get(self, input):
        self.delimiter = self.delimiter if self.delimiter != self.DEFAULT_DELIMITER else self.__set_default_delimiter()
        self.sandhi = self.sandhi if self.sandhi != self.DEFAULT_SANDHI else self.__set_default_sandhi()

        converted = Tokeniser().tokenise(to_traditional(input))
        converted = ' '.join(self.__convert_tokenised(i).strip() for i in self.__tone_sandhi_position(converted)).strip()
        if self.punctuation == 'format':
            return self.__format_text(self.__format_punctuation_western(converted[0].upper() + converted[1:]))
        return self.__format_punctuation_cjk(converted)


    ### Input formatting

    # Helper to convert separate words
    def __convert_tokenised(self, word):
        if word[0] not in word_dict:
            return word[0]
        word = (word_dict[word[0]],) + word[1:]
        if "/" in word[0]:
            dialect_part = word[0].split("/")[1] if self.dialect == 'north' else word[0].split("/")[0]
            word = (dialect_part,) + word[1:]
        word = self.__system_conversion(word).replace('---', '--')
        if self.format == 'number' and self.system in ['tailo', 'poj']:
            word = self.__mark_to_number(word)
        if self.format == 'strip':
            if self.system == 'tlpa':
                word = word.translate(str.maketrans('', '', ''.join(['1', '2', '3', '4', '5', '7', '8'])))
            if self.system == 'zhuyin':
                word = word.translate(str.maketrans('', '', ''.join(['ˋ', '˪', 'ˊ', '˫', '˙'])))
            if self.system == 'ipa':
                word = word.translate(str.maketrans('', '', ''.join(['¹', '²', '³', '⁴', '⁵'])))
            else: word = "".join(c for c in unicodedata.normalize("NFD", word) if unicodedata.category(c) != "Mn")
        return word.replace('--', self.suffix_token).replace('-', self.delimiter).replace(self.suffix_token, '--')


    # Helper switch for converting 漢字 based on defined transliteration system
    def __system_conversion(self, word):
        if self.system == 'poj': return self.__tailo_to_poj(word)
        if self.system == 'zhuyin': return self.__tailo_to_zhuyin(word)
        if self.system == 'tlpa': return self.__tailo_to_tlpa(word)
        if self.system == 'pingyim': return self.__tailo_to_pingyim(word)
        if self.system == 'tongiong': return self.__tailo_to_ti(word)
        if self.system == 'ipa': return self.__tailo_to_ipa(word)
        if self.sandhi: return self.__tailo_to_tailo(word)
        else: return word[0]


    # Helper functions to set delimiter according to transliteration system if wasn't explicitly defined by user
    def __set_default_delimiter(self):
        if self.system == 'tlpa' or self.system == 'zhuyin' or self.system == 'ipa': return ' '
        if self.system == 'pingyim': return ''
        return '-'


    # Helper functions to set sandhi according to transliteration system if wasn't explicitly defined by user
    def __set_default_sandhi(self):
        if self.system == 'tongiong': return True
        return False


    ### Conversion functions

    # Helper to get number tones
    def __get_number_tones(self, input):
        words = self.__preprocess_word(input[0])
        number_tones = [self.__get_number_tone(w) for w in words if len(w) > 0]
        if self.sandhi:
            number_tones = self.__tone_sandhi(number_tones, input[1])
        return number_tones


    # Helper to convert between transliteration systems
    def __replacement_tool(self, dictionary, input):
        pattern = re.compile('|'.join(dictionary.keys()))
        return pattern.sub(lambda m: dictionary[re.escape(m.group(0))], input)


    # Helper to convert word from Tai-lo to number
    def __mark_to_number(self, input):
        input = input.replace('--', '-'+self.suffix_token)
        words = input.split('-')
        input = '-'.join(self.__get_number_tone(w) for w in words if len(w) > 0)
        return input.replace(self.suffix_token, '--')


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
            if s.replace(self.tt, '') in input:
                part = s
                break
        return unicodedata.normalize('NFC', input.replace(part.replace(self.tt, ''), part.replace(self.tt, tones[int(input[-1])]))[:-1])


    # Helper to apply tone sandhi to a word
    def __tone_sandhi(self, words, last):
        sandhi = {'1':'7', '7':'3', '3':'2', '2':'1', '5':'7', 'p4':'p8', 't4':'t8', 'k4':'k8', 'h4':'2', 'p8':'p4', 't8':'t4', 'k8':'k4', 'h8':'3'}
        if self.dialect == 'north':
            sandhi.update({'5':'3'})
        indices = range(len(words)-1) if not last else range(len(words))
        sandhi_words = [self.__replacement_tool(sandhi, words[i]) for i in indices]
        if not last:
            sandhi_words.append(words[-1])
        return sandhi_words
    

    # Helper to define which words should be sandhi'd fully
    def __tone_sandhi_position(self, input):
        result_list = []
        for i, char in enumerate(input):
            result_list.append((char, (i < len(input) - 1 and is_cjk(input[i+1]))))
        return result_list


    ### Tai-lo to other transliteration systems converting

    # Helper to convert syllable from Tai-lo to Tai-lo
    # (called only in cases when tone sandhi is applied)
    def __tailo_to_tailo(self, input):
        placement = [
            'ia'+self.tt+'u', 'ua'+self.tt+'i', 'ua'+self.tt, 'ue'+self.tt, 'ui'+self.tt, 'a'+self.tt+'i',
            'a'+self.tt+'u', 'o'+self.tt+'o','ia'+self.tt, 'iu'+self.tt, 'io'+self.tt, 'o'+self.tt+'o', 'a'+self.tt, 
            'o'+self.tt, 'e'+self.tt, 'i'+self.tt, 'u'+self.tt, 'n'+self.tt+'g', 'm'+self.tt
        ]
        tones = ["", "", "́", "̀", "", "̂", "̌", "̄", "̍", "̋"]
        placement += [s.capitalize() for s in placement]
        input = '-'.join(self.__get_mark_tone(nt, placement, tones) for nt in self.__get_number_tones(input))
        return input.replace(self.suffix_token, '--')


    # Helper to convert syllable from Tai-lo to POJ
    def __tailo_to_poj(self, input):
        placement = [
            'oa'+self.tt+'h', 'oa'+self.tt+'n', 'oa'+self.tt+'ng', 'oa'+self.tt+'ⁿ', 'oa'+self.tt+'t',
            'ia'+self.tt+'u', 'oe'+self.tt+'h', 'o'+self.tt+'e', 'oa'+self.tt+'i', 'u'+self.tt+'i', 'o'+self.tt+'a',
            'a'+self.tt+'i', 'a'+self.tt+'u', 'ia'+self.tt, 'iu'+self.tt, 'io'+self.tt, 'a'+self.tt,
            'o'+self.tt, 'o͘'+self.tt, 'e'+self.tt, 'i'+self.tt, 'u'+self.tt, 'n'+self.tt+'g', 'm'+self.tt
        ]
        convert = {'nng':'nng', 'nnh':'hⁿ', 'nn':'ⁿ', 'ts':'ch', 'ing':'eng', 'uai':'oai', 'uan':'oan', 'ik':'ek', 'ua':'oa', 'ue':'oe', 'oo':'o͘'}
        tones = ['', '', '́', '̀', '', '̂', '', '̄', '̍', '']
        placement += [s.capitalize() for s in placement]
        convert.update({k.capitalize(): v.capitalize() for k, v in convert.items()})
        input = '-'.join(self.__get_mark_tone(self.__replacement_tool(convert, nt), placement, tones) for nt in self.__get_number_tones(input))
        return input.replace(self.suffix_token, '--')


    # Helper to convert syllable from Tai-lo to 方音符號 (zhuyin)
    def __tailo_to_zhuyin(self, input):
        convert = {
            'p4':'ㆴ4', 'p8':'ㆴ8', 'k4':'ㆶ4', 'k8':'ㆶ8', 't4':'ㆵ4', 't8':'ㆵ8', 'h4':'ㆷ4', 'h8':'ㆷ8',
            'tshing':'ㄑㄧㄥ', 'tshinn':'ㄑㆪ', 'phing':'ㄆㄧㄥ', 'phinn':'ㄆㆪ', 'tsing':'ㄐㄧㄥ', 'tsinn':'ㄐㆪ',
            'ainn':'ㆮ', 'aunn':'ㆯ', 'giok':'ㆣㄧㄜㆶ', 'ngai':'ㄫㄞ', 'ngau':'ㄫㄠ', 'ngoo':'ㄫㆦ', 'ping':'ㄅㄧㄥ',
            'pinn':'ㄅㆪ', 'senn':'ㄙㆥ', 'sing':'ㄒㄧㄥ', 'sinn':'ㄒㆪ', 'tshi':'ㄑㄧ',
            'ang':'ㄤ', 'ann':'ㆩ', 'enn':'ㆥ', 'ing':'ㄧㄥ', 'inn':'ㆪ', 'mai':'ㄇㄞ', 'mau':'ㄇㄠ', 'mng':'ㄇㆭ',
            'moo':'ㄇㆦ', 'mua':'ㄇㄨㄚ', 'mue':'ㄇㄨㆤ', 'mui':'ㄇㄨㄧ', 'nga':'ㄫㄚ', 'nge':'ㄫㆤ', 'ngi':'ㄫㄧ',
            'ong':'ㆲ', 'onn':'ㆧ', 'tsh':'ㄘ', 'tsi':'ㄐㄧ', 'unn':'ㆫ',
            'ai':'ㄞ', 'am':'ㆰ', 'an':'ㄢ', 'au':'ㄠ', 'ji':'ㆢㄧ', 'kh':'ㄎ', 'ma':'ㄇㄚ', 'me':'ㄇㆤ', 'mi':'ㄇㄧ',
            'ng':'ㆭ', 'ok':'ㆦㆶ', 'om':'ㆱ', 'oo':'ㆦ', 'ph':'ㄆ', 'si':'ㄒㄧ', 'th':'ㄊ', 'ts':'ㄗ',
            'a':'ㄚ', 'b':'ㆠ', 'e':'ㆤ', 'g':'ㆣ', 'h':'ㄏ', 'i':'ㄧ', 'j':'ㆡ', 'k':'ㄍ', 'l':'ㄌ', 'm':'ㆬ',
            'n':'ㄋ', 'o':'ㄜ', 'p':'ㄅ', 's':'ㄙ', 't':'ㄉ', 'u':'ㄨ'}
        tones = ['', '', 'ˋ', '˪', '', 'ˊ', '', '˫', '˙']
        output = []
        for nt in self.__get_number_tones((input[0].lower(), input[1])):
            nt = self.__replacement_tool(convert, nt).replace(self.suffix_token, '')
            if len(nt) > 2 and nt[-2] == 'ㄋ':
                nt = nt[:-2] + 'ㄣ' + nt[-1]
            if self.format != 'number':
                nt = ''.join(tones[int(t)] if t.isnumeric() else t for t in nt)
            output.append(nt)
        return '-'.join(output).replace(self.suffix_token, '')


    # Helper to convert syllable from Tai-lo to TLPA
    def __tailo_to_tlpa(self, input):
        convert = {'tsh':'ch', 'ts':'c'}
        convert.update({k.capitalize(): v.capitalize() for k, v in convert.items()})
        input = '-'.join(self.__replacement_tool(convert, nt) for nt in self.__get_number_tones(input))
        return input.replace(self.suffix_token, '')


    # Helper to convert syllable from Tai-lo to Bbanlam pingyim
    def __tailo_to_pingyim(self, input):
        placement = [
            'ua'+self.tt+'i', 'ia'+self.tt+'o', 'a'+self.tt+'i', 'a'+self.tt+'o', 
            'oo'+self.tt, 'ia'+self.tt, 'iu'+self.tt, 'io'+self.tt, 'ua'+self.tt, 'ue'+self.tt, 'ui'+self.tt,
            'a'+self.tt, 'o'+self.tt, 'e'+self.tt, 'i'+self.tt, 'u'+self.tt, 'n'+self.tt+'g', 'm'+self.tt, 'n'+self.tt
        ]
        # plosives don't change, ptkh 4/8 -> ptkh 4/8
        convert = {
            'p4':'p4', 't4':'t4', 'k4':'k4', 'h4':'h4', 'p8':'p8', 't8':'t8', 'k8':'k8', 'h8':'h8',
            'ainn':'nai', 'iunn':'niu', 'ann':'na', 'onn':'noo', 'enn':'ne',
            'inn':'ni', 'unn':'nu', 'au':'ao', 'ph':'p', 'nng':'lng', 'tsh':'c',
            'ng':'ggn', 'ts':'z', 'th':'t', 'kh':'k', 'ir':'i', 'p':'b', 'b':'bb',
            't':'d', 'k':'g', 'g':'gg', 'j':'zz', 'n':'ln', 'm':'bbn'}
        tones = ['', '̄', '̌', '̀', '̄', '́', '', '̂', '́', '']
        placement += [s.capitalize() for s in placement]
        convert.update({k.capitalize(): v.capitalize() for k, v in convert.items()})
        output = []
        for nt in self.__get_number_tones(input):
            replaced = self.__replacement_tool(convert, nt)
            if replaced[0] in ['i', 'I']: # Initial i
                replaced = ('Y' if replaced[0] == 'I' else 'y') + (replaced[1:] if replaced[1] in ['a', 'u', 'o'] else replaced.lower())
            if replaced[0] in ['u', 'U']: # Initial u
                replaced = ('W' if replaced[0] == 'U' else 'w') + (replaced[1:] if len(nt) > 2 and replaced[1] in ['a', 'i', 'e', 'o'] else replaced.lower())
            if nt[0] in ['m', 'M']: # Syllabic consonant m
                if len(nt) == 2:
                    replaced = nt[0] + nt[-1]
                elif nt[1] == 'n':
                    replaced = nt[0] + replaced[3:]
            if nt[-3:-1] in ['ng', 'Ng']: # Coda ng
                replaced = replaced[:-4] + nt[-3:-1] + nt[-1]
            if 'bbn' in replaced[-4:-1]: # Final m
                replaced = replaced.replace('bbn', 'm', 1)
            if replaced[-3:-1] == 'ln': # Final n
                replaced = replaced[:-3] + 'n' + replaced[-1]
            if self.format != 'number':
                output.append(self.__get_mark_tone(replaced, placement, tones))
            else:
                output.append(replaced)
        return '-'.join(output).replace(self.suffix_token, '')


    # Helper to convert syllable from Tai-lo to Tong-iong ping-im
    #       Not enough information on tone mark placement
    def __tailo_to_ti(self, input):
        placement = [
            'ua'+self.tt+'i', 'ia'+self.tt+'o', 'a'+self.tt+'i', 'a'+self.tt+'o', 
            'oo'+self.tt, 'ia'+self.tt, 'iu'+self.tt, 'io'+self.tt, 'ua'+self.tt, 'ue'+self.tt, 'ui'+self.tt,
            'a'+self.tt, 'o'+self.tt, 'e'+self.tt, 'i'+self.tt, 'u'+self.tt, 'n'+self.tt+'g', 'm'+self.tt
        ]
        # plosives don't change, ptkh 4/8 -> ptkh 4/8
        convert = {
            'p4':'p4', 't4':'t4', 'k4':'k4', 'h4':'h4', 'p8':'p8', 't8':'t8', 'k8':'k8', 'h8':'h8',
            'oo':'o', 'om':'om', 'ong':'ong', 'ir':'i', 'tsh':'c',
            'ts':'z', 'nng':'nng', 'ng':'ng', 'g':'gh', 'kh':'k', 'k':'g',
            'ph':'p', 'p':'b', 'b':'bh', 'th':'t', 't':'d', 'j':'r'}
        tones = ["̊", "", "̀", "̂", "̄", "̆", "", "̄", "", "́"]
        placement += [s.capitalize() for s in placement]
        convert.update({k.capitalize(): v.capitalize() for k, v in convert.items()})
        number_tones = [nt[:-2] + 'or' + nt[-1] if nt[-2] == 'o' else nt for nt in self.__get_number_tones(input)]
        input = '-'.join(self.__get_mark_tone(self.__replacement_tool(convert, nt), placement, tones) if self.format != 'number' else self.__replacement_tool(convert, nt) for nt in number_tones)
        return input.replace(self.suffix_token, '--')
    

    # Helper to convert syllable from Tai-lo to International Phonetic Alphabet
    def __tailo_to_ipa(self, input):
        convert = {
            'tsing':'tɕiɪŋ','jiang':'dʑiaŋ','tshing':'tɕʰiɪŋ','tsik':'tɕiɪk','tshik':'tɕʰiɪk',
            'jian':'dʑiɛn','jiat':'dʑiɛt','tshi':'tɕʰi',
            'iann':'iã','ainn':'ãi','iang':'iaŋ','nng':'nŋ',
            'mia':'miã','mui':'muĩ','mue':'muẽ','mua':'muã','ma':'mã','me':'mẽ','mi':'mĩ','moo':'mɔ̃', # m nasalisation
            'nia':'niã','nua':'nuã','na':'nã','ne':'nẽ','ni':'nĩ','noo':'nɔ̃', # n nasalisation
            'ngia':'ŋiã','ngiu':'ŋiũ','nga':'ŋã','nge':'ŋẽ','ngi':'ŋĩ','ngoo':'ŋɔ̃', # ng nasalisation
            'ing':'iɪŋ','tsh':'tsʰ','tsi':'tɕi','ian':'iɛn','iat':'iɛt','onn':'ɔ̃',
            'ong':'ɔŋ','ik':'iɪk','ji':'dʑi','kh':'kʰ','ng':'ŋ','oo':'ɔ','nn':'̃',
            'hm':'hm̩','ph':'pʰ','th':'tʰ','ok':'ɔk','om':'ɔm','j':'dz','o':'ə'}
        if self.dialect == 'north':
            convert.update({'o':'o'})
        convert2 = {
            'p4':'p̚4','p8':'p̚8','k4':'k̚4','k8':'k̚8','t4':'t̚4','t8':'t̚8','h4':'ʔ4','h8':'ʔ8','si':'ɕi'}
        tones = ['', '⁴⁴', '⁵³', '¹¹', '²¹', '²⁵', '', '²²', '⁵'] if self.dialect != 'north' else ['', '⁵⁵', '⁵¹', '²¹', '³²', '²⁴', '', '³³', '⁴']
        convert.update({k.capitalize(): v.capitalize() for k, v in convert.items()})
        convert2.update({k.capitalize(): v.capitalize() for k, v in convert2.items()})
        output = []
        for nt in self.__get_number_tones((input[0], input[1])):
            nt = self.__replacement_tool(convert, nt).replace(self.suffix_token, '')
            if 'ŋ' in nt:
                if len(nt) > 2:
                    if all(c.lower() not in 'aeioɔu' for c in nt[:nt.index('ŋ')]) and nt.index('ŋ') != 0:
                        nt = nt.replace('ŋ', 'ŋ̍')
                elif len(nt) == 2:
                    nt = nt.replace('ŋ', 'ŋ̍')
            if len(nt) == 2 and nt[0] == 'm':
                nt = 'm̩' + nt[-1]
            nt = self.__replacement_tool(convert2, nt)
            if self.format != 'number':
                nt = ''.join(tones[int(t)] if t.isnumeric() else t for t in nt)
            output.append(unicodedata.normalize('NFC', nt))
        return '-'.join(output).replace(self.suffix_token, '')


    ### Converted output formatting

    # Helper to convert Chinese punctuation to Latin punctuation with appropriate spacing
    def __format_punctuation_western(self, input):
        punctiation_mapping = {'。':'.', '．':' ', '，':',', '、':',', '！':'!', '？':'?', '；':';', '：':':',
                               '）':')', '］':']', '】':']', '（':'(', '［':'[', '【':'['}
        left_space = {'.':'.', ',':',', '!':'!', '?':'?', ';':';', ':':':', ')':')', ']':']', '」':'"', '”':'"', '--':'--'}
        right_space = {'(':'(', '[':'[', '「':'"', '“':'"'}
        for punct_ch, punct_lat in punctiation_mapping.items():
            input = input.replace(punct_ch, punct_lat)
        for left, space in left_space.items():
            input = input.replace(' ' + left, space).replace(left, space)
        for right, space in right_space.items():
            input = input.replace(right + ' ', space).replace(right, space) 
        return input
    

    # Helper to restore original CJK punctuation with appropriate spacing
    def __format_punctuation_cjk(self, input):
        left_space = ['。', '．', '，', '、', '！', '？', '；', '：', '）', '］', '】', '」', '”', '--']
        right_space = ['（', '［', '【', '「', '“']
        for punct in left_space:
            input = input.replace(' ' + punct + ' ', punct).replace(' ' + punct, punct)
        for punct in right_space:
            input = input.replace(' ' + punct + ' ', punct).replace(punct + ' ', punct)
        return input


    # Helper to capitalise text in according to punctuation
    def __format_text(self, input):
        punc_filter = re.compile("([.!?]\s*)")
        split_with_punc = punc_filter.split(input)
        split_with_punc = [i[0].upper() + i[1:] if len(i) > 1 else i for i in split_with_punc]
        return "".join(split_with_punc)


class Tokeniser(object):

    def __init__(self):
        pass

    # Tokenise the text into separate words
    def tokenise(self, input):
        tokenised = []
        traditional = to_traditional(input)
        while traditional:
            for j in range(4, 0, -1):
                if len(traditional) < j:
                    continue
                word = traditional[:j]
                if word_dict.get(word) or j == 1:
                    if j == 1 and tokenised and not (is_cjk(tokenised[-1]) or is_cjk(word)):
                        tokenised[-1] += word
                    else:
                        tokenised.append(word)
                    traditional = traditional[j:]
                    break
            else:
                traditional = ""
        punctuations = re.compile("([.,!?\"#$%&()*+/:;<=>@[\\]^`{|}~\t。．，、！？；：（）［］【】「」“”]\s*)")
        indices = [0] + [len(item) for item in tokenised]
        tokenised = [input[sum(indices[:i+1]):sum(indices[:i+2])] for i in range(len(tokenised))]
        tokenised = [item for word in tokenised for subword in punctuations.split(word) if subword for item in subword.split(" ") if item]
        return [subword for word in tokenised for subword in ((word[:-1], word[-1]) if (word[-1] == '的' or word[-1] == '矣') and len(word) > 1 else (word,))]