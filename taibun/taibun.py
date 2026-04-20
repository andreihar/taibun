import os
import re
import unicodedata

import msgpack

data_dir = os.path.join(os.path.dirname(__file__), "data")
with open(os.path.join(data_dir, "words.msgpack"), 'rb') as f:
    word_dict = msgpack.unpackb(f.read(), raw=False)
with open(os.path.join(data_dir, "traditional.msgpack"), 'rb') as f:
    trad_dict = msgpack.unpackb(f.read(), raw=False)
with open(os.path.join(data_dir, "simplified.msgpack"), 'rb') as f:
    simp_dict = {**{v: k for k, v in trad_dict.items() if len(k) == 1}, **msgpack.unpackb(f.read(), raw=False)}
with open(os.path.join(data_dir, "vars.msgpack"), 'rb') as f:
    vars_dict = msgpack.unpackb(f.read(), raw=False)
with open(os.path.join(data_dir, "prons.msgpack"), 'rb') as f:
    prons_dict = msgpack.unpackb(f.read(), raw=False)

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

# Convert Traditional to Simplified characters
def to_simplified(input):
    return ''.join(simp_dict.get(c, c) for c in input)

# Convert Simplified to Traditional characters
def to_traditional(input):
    input = ''.join(vars_dict.get(c, c) for c in input)
    traditional = []
    while input:
        for j in range(4, 0, -1):
            if len(input) < j:
                continue
            word = input[:j]
            if word in trad_dict or j == 1:
                traditional.append(trad_dict.get(word, word))
                input = input[j:]
                break
    return "".join(traditional)


"""
Description: Converts Chinese characters to Taiwanese Hokkien phonetic transcriptions.
             Supports both Traditional and Simplified characters.
Invariant: system = `Tailo` (default), `POJ`, `Zhuyin`, `TLPA`, `Pingyim`, `Tongiong`, `IPA`
           dialect = `south` (Zhangzhou-leaning, default), `north` (Quanzhou-leaning), `singapore` (Quanzhou-leaning with Singaporean characteristics)
           format = `mark` (diacritical), `number` (numeric), `strip` (no tones)
           delimiter = String that replaces the default delimiter
           apostrophe = True (default for Pingyim), False
           sandhi = `auto`, `none`, `exc_last`, `incl_last`
           punctuation = `format` (Latin-style, default), `none` (preserve original)
           convert_non_cjk = True, False (default)
"""
class Converter(object):

    suffix_token = '[ЅFFX_ТКŊ]'
    tt = '[ТŊ_ТКŊ]'
    DEFAULT_DELIMITER = object()
    DEFAULT_APOSTROPHE = object()
    DEFAULT_SANDHI = object()
    SYSTEM_CONFIGS = {
        'tailo': {
            'placement': [f'ia{tt}u',f'ua{tt}i',f'ua{tt}',f'ue{tt}',f'ui{tt}',f'a{tt}i',f'a{tt}u',f'o{tt}o',f'ia{tt}',f'iu{tt}',f'io{tt}',f'o{tt}o',f'a{tt}',f'o{tt}',f'e{tt}',f'i{tt}',f'u{tt}',f'mn{tt}g',f'n{tt}g',f'm{tt}'],
            'tones': ['','','́','̀','','̂','̌','̄','̍','̋']
        },
        'poj': {
            'convert': {'nng':'nng','nnh':'hⁿ','nn':'ⁿ','ts':'ch','ing':'eng','uai':'oai','ik':'ek','ua':'oa','ue':'oe','oo':'o͘'},
            'placement': [f'oa{tt}h',f'oa{tt}n',f'oa{tt}ng',f'oa{tt}ⁿ',f'oa{tt}t',f'ia{tt}u',f'oe{tt}h',f'o{tt}e',f'oa{tt}i',f'u{tt}i',f'o{tt}a',f'a{tt}i',f'a{tt}u',f'ia{tt}',f'iu{tt}',f'io{tt}',f'a{tt}',f'o{tt}',f'o͘{tt}',f'e{tt}',f'i{tt}',f'u{tt}',f'mn{tt}g',f'n{tt}g',f'm{tt}'],
            'tones': ['','','́','̀','','̂','','̄','̍','']
        },
        'zhuyin': {
            'convert': {'p4':'ㆴ4','p8':'ㆴ8','k4':'ㆶ4','k8':'ㆶ8','t4':'ㆵ4','t8':'ㆵ8','h4':'ㆷ4','h8':'ㆷ8','h0': '0','tshing':'ㄑㄧㄥ','tshinn':'ㄑㆪ','phing':'ㄆㄧㄥ','phinn':'ㄆㆪ','tsing':'ㄐㄧㄥ','tsinn':'ㄐㆪ','ainn':'ㆮ','aunn':'ㆯ','giok':'ㆣㄧㄜㆶ','ngai':'ㄫㄞ','ngau':'ㄫㄠ','ngoo':'ㄫㆦ','ping':'ㄅㄧㄥ','pinn':'ㄅㆪ','senn':'ㄙㆥ','sing':'ㄒㄧㄥ','sinn':'ㄒㆪ','tshi':'ㄑㄧ','ang':'ㄤ','ann':'ㆩ','enn':'ㆥ','ing':'ㄧㄥ','eng':'ㆤㄥ','inn':'ㆪ','mai':'ㄇㄞ','mau':'ㄇㄠ','mng':'ㄇㆭ','moo':'ㄇㆦ','mua':'ㄇㄨㄚ','mue':'ㄇㄨㆤ','mui':'ㄇㄨㄧ','nga':'ㄫㄚ','nge':'ㄫㆤ','ngi':'ㄫㄧ','ong':'ㆲ','onn':'ㆧ','tsh':'ㄘ','tsi':'ㄐㄧ','unn':'ㆫ','ai':'ㄞ','am':'ㆰ','an':'ㄢ','au':'ㄠ','ji':'ㆢㄧ','kh':'ㄎ','ma':'ㄇㄚ','me':'ㄇㆤ','mi':'ㄇㄧ','ng':'ㆭ','ok':'ㆦㆶ','om':'ㆱ','oo':'ㆦ','ph':'ㄆ','si':'ㄒㄧ','th':'ㄊ','ts':'ㄗ','a':'ㄚ','b':'ㆠ','e':'ㆤ','g':'ㆣ','h':'ㄏ','i':'ㄧ','j':'ㆡ','k':'ㄍ','l':'ㄌ','m':'ㆬ','n':'ㄋ','o':'ㄜ','p':'ㄅ','s':'ㄙ','t':'ㄉ','u':'ㄨ'},
            'tones': ['','','ˋ','˪','','ˊ','','˫','˙']
        },
        'tlpa': {
            'convert': {'tsh':'ch','ts':'c'}
        },
        'pingyim': {
            'convert': {'p4':'p4','t4':'t4','k4':'k4','h4':'h4','p8':'p8','t8':'t8','k8':'k8','h8':'h8','au':'ao','ph':'p','nng':'lng','tsh':'c','ng':'ggn','ts':'z','th':'t','kh':'k','ir':'i','p':'b','b':'bb','t':'d','k':'g','g':'gg','j':'zz'},
            'placement': [f'ua{tt}i',f'ia{tt}o',f'a{tt}i',f'a{tt}o',f'oo{tt}',f'ia{tt}',f'iu{tt}',f'io{tt}',f'ua{tt}',f'ue{tt}',f'ui{tt}',f'a{tt}',f'o{tt}',f'e{tt}',f'i{tt}',f'u{tt}',f'm{tt}ggn',f'ggn{tt}',f'bbn{tt}',f'n{tt}g',f'm{tt}'],
            'tones': ['','̄','̌','̀','̄','́','','̂','́','']
        },
        'tongiong': {
            'convert': {'p4':'p4','t4':'t4','k4':'k4','h4':'h4','p8':'p8','t8':'t8','k8':'k8','h8':'h8','oo':'o','om':'om','ong':'ong','ir':'i','tsh':'c','ts':'z','nng':'nng','ng':'ng','g':'gh','kh':'k','k':'g','ph':'p','p':'b','b':'bh','th':'t','t':'d','j':'r'},
            'placement': [f'ua{tt}i',f'ia{tt}o',f'a{tt}i',f'a{tt}o',f'oo{tt}',f'ia{tt}',f'iu{tt}',f'io{tt}',f'ua{tt}',f'ue{tt}',f'ui{tt}',f'a{tt}',f'o{tt}',f'e{tt}',f'i{tt}',f'u{tt}',f'mn{tt}g',f'n{tt}g',f'm{tt}'],
            'tones': ['̊','','̀','̂','̄','̆','','̄','','́']
        },
        'ipa': {
            'convert': {'tsing':'tɕiɪŋ','jiang':'dʑiaŋ','tshing':'tɕʰiɪŋ','tsik':'tɕiɪk','tshik':'tɕʰiɪk','jian':'dʑiɛn','jiat':'dʑiɛt','tshi':'tɕʰi','iann':'iã','ainn':'ãi','iang':'iaŋ','nng':'nŋ','mia':'miã','mui':'muĩ','mue':'muẽ','mua':'muã','ma':'mã','me':'mẽ','mi':'mĩ','moo':'mɔ̃','nia':'niã','nua':'nuã','na':'nã','ne':'nẽ','ni':'nĩ','noo':'nɔ̃','ngia':'ŋiã','ngiu':'ŋiũ','nga':'ŋã','nge':'ŋẽ','ngi':'ŋĩ','ngoo':'ŋɔ̃','ing':'iɪŋ','eng':'eŋ','tsh':'tsʰ','tsi':'tɕi','ian':'iɛn','iat':'iɛt','onn':'ɔ̃','ong':'ɔŋ','ik':'iɪk','ji':'dʑi','kh':'kʰ','ng':'ŋ','oo':'ɔ','nn':'̃','hm':'hm̩','ph':'pʰ','th':'tʰ','ok':'ɔk','om':'ɔm','j':'dz','o':'ə'},
            'convert2': {'p4':'p̚4','p8':'p̚8','k4':'k̚4','k8':'k̚8','t4':'t̚4','t8':'t̚8','h4':'ʔ4','h8':'ʔ8','si':'ɕi','h0':'0'},
            'tones': ['','⁴⁴','⁵³','¹¹','²¹','²⁵','','²²','⁵']
        }
    }
    __suffixes = ['啊','矣','喂','欸','唅','嘿','諾','乎','唷','啦','喔','嘖']
    __no_sandhi = ['這','彼','遮','遐']
    __location = ['頂','跤','外','內']
    __singapore_prons = { '你':['lí/lú'], '我':["guá/uá","ngóo"], '物':["bu̍t","mi̍h","mih"] }
    __singapore_words = {
        '咖啡': { '咖': { 'ka':'ko' } }
    }

    def __init__(self, system='Tailo', dialect='south', format='mark', delimiter=DEFAULT_DELIMITER, apostrophe=DEFAULT_APOSTROPHE, sandhi=DEFAULT_SANDHI, punctuation='format', convert_non_cjk=False):
        self.system = system.lower()
        self.dialect = dialect.lower()
        self.format = format
        self.delimiter = delimiter if delimiter != self.DEFAULT_DELIMITER else self.__set_default_delimiter()
        self.apostrophe = apostrophe if apostrophe != self.DEFAULT_APOSTROPHE else self.__set_default_apostrophe()
        self.sandhi = sandhi if sandhi != self.DEFAULT_SANDHI else self.__set_default_sandhi()
        self.punctuation = punctuation
        self.convert_non_cjk = convert_non_cjk
        self.__declarations(dialect.lower())


    # Helper to declare system-specific conversion information
    def __declarations(self, dialect):
        # Conversion
        self.conversion_func = {
            'poj': self.__tailo_to_poj,
            'zhuyin': self.__tailo_to_zhuyin,
            'tlpa': self.__tailo_to_tlpa,
            'pingyim': self.__tailo_to_pingyim,
            'tongiong': self.__tailo_to_ti,
            'ipa': self.__tailo_to_ipa,
            'tailo': self.__tailo_to_tailo
        }.get(self.system, lambda word: word[0])

        config = self.SYSTEM_CONFIGS.get(self.system)
        if 'tones' in config: self.tones = config['tones']
        if 'placement' in config: 
            first_part = config['placement'][:-2]
            last_part = config['placement'][-2:]
            self.placement = [s[0].upper() + s[1:] for s in first_part] + first_part + [s[0].upper() + s[1:] for s in last_part] + last_part
        if 'convert' in config: self.convert = {**{k[0].upper() + k[1:]: v[0].upper() + v[1:] for k, v in config['convert'].items()}, **config['convert']}
        if 'convert2' in config: self.convert2 = {**{k[0].upper() + k[1:]: v[0].upper() + v[1:] for k, v in config['convert2'].items()}, **config['convert2']}

        # Dialect
        self.sandhi_conversion = {'1':'7','7':'3','3':'2','2':'1','5':'7','p4':'p8','t4':'t8','k4':'k8','h4':'2','p8':'p4','t8':'t4','k8':'k4','h8':'3'}
        self.a_sandhi = {'1':'7','2':'1','3':'1','5':'7','p4':'p8','t4':'t8','k4':'k8','h4':'1','p8':'p4','t8':'t4','k8':'k4','h8':'7'}

        # Apostrophe
        if self.apostrophe:
            syllables = ['a','ah','ai','aih','ainn','ak','am','an','ang','ann','ap','at','au','ba','bah','bai','bak','ban','bang','bat','bau','be','beh','bi','bian','biat','biau','bih','bik','bin','bing','bio','bit','biu','bo','bok','bong','boo','bu','bua','buah','buan','buat','bue','bueh','bui','bun','but','e','eh','enn','ga','gai','gak','gam','gan','gang','gau','ge','geh','gi','gia','giah','giak','giam','gian','giang','giap','giat','giau','gik','gim','gin','ging','gio','gioh','giok','giong','giu','go','gok','gong','goo','gu','gua','guan','guat','gue','gueh','gui','gun','ha','hah','hai','haih','hainn','hak','ham','han','hang','hann','hannh','hap','hat','hau','haunnh','he','heh','hi','hia','hiah','hiam','hian','hiang','hiann','hiannh','hiap','hiat','hiau','hiauh','hik','him','hin','hing','hinn','hio','hioh','hiok','hiong','hip','hit','hiu','hiunn','hm','hmh','hng','hngh','ho','hoh','hok','hong','honn','honnh','hoo','hooh','hu','hua','huah','huai','huainn','huan','huann','huat','hue','hueh','hui','huih','huinn','hun','hut','i','ia','iah','iam','ian','iang','iann','iap','iat','iau','iaunn','ik','im','in','ing','inn','io','ioh','iok','iong','ip','it','iu','iunn','ji','jia','jiah','jiam','jian','jiang','jiap','jiat','jiau','jim','jin','jio','jiok','jiong','jip','jit','jiu','ju','juah','jue','jun','ka','kah','kai','kainn','kak','kam','kan','kang','kann','kap','kat','kau','kauh','ke','keh','kenn','kha','khah','khai','khainn','khak','kham','khan','khang','khann','khap','khat','khau','khaunnh','khe','kheh','khenn','khennh','khi','khia','khiah','khiak','khiam','khian','khiang','khiap','khiat','khiau','khih','khik','khim','khin','khing','khinn','khio','khioh','khiok','khiong','khip','khit','khiu','khiunn','khng','khngh','kho','khok','khong','khoo','khu','khua','khuah','khuai','khuan','khuann','khuat','khue','khueh','khuh','khui','khuinn','khun','khut','ki','kia','kiah','kiam','kian','kiann','kiap','kiat','kiau','kih','kik','kim','kin','king','kinn','kio','kioh','kiok','kiong','kip','kiu','kiunn','kng','ko','koh','kok','kong','konn','koo','ku','kua','kuah','kuai','kuainn','kuan','kuann','kuat','kue','kueh','kui','kuih','kuinn','kun','kut','la','lah','lai','lak','lam','lan','lang','lap','lat','lau','lauh','le','leh','li','lia','liah','liam','lian','liang','liap','liat','liau','lih','lik','lim','lin','ling','lio','lioh','liok','liong','lip','lit','liu','lo','loh','lok','long','loo','looh','lop','lu','lua','luah','luan','luat','lue','lueh','luh','lui','lun','lut','m','ma','mah','mai','mau','mauh','me','meh','mi','mia','mian','miau','mih','mng','mngh','moo','mooh','mua','mue','mui','na','nah','nai','nau','nauh','ne','neh','ng','nga','ngai','ngau','nge','ngeh','ngi','ngia','ngiau','ngiauh','ngiu','ngoo','ni','nia','niau','nih','niu','nng','noo','nua','o','oh','ok','om','ong','onn','oo','ooh','pa','pah','pai','pak','pan','pang','pat','pau','pe','peh','penn','pha','phah','phai','phainn','phak','phan','phang','phann','phau','phauh','phe','pheh','phenn','phi','phiah','phiak','phian','phiang','phiann','phiat','phiau','phih','phik','phin','phing','phinn','phio','phit','phngh','pho','phoh','phok','phong','phoo','phu','phua','phuah','phuan','phuann','phuat','phue','phueh','phuh','phui','phun','phut','pi','piah','piak','pian','piang','piann','piat','piau','pih','pik','pin','ping','pinn','pio','pit','piu','png','po','poh','pok','pong','poo','pu','pua','puah','puan','puann','puat','pue','pueh','puh','pui','puinn','pun','put','sa','sah','sai','sak','sam','san','sang','sann','sannh','sap','sat','sau','se','seh','senn','si','sia','siah','siak','siam','sian','siang','siann','siap','siat','siau','sih','sik','sim','sin','sing','sinn','sio','sioh','siok','siong','sip','sit','siu','siunn','sng','so','soh','sok','som','song','soo','su','sua','suah','suainn','suan','suann','suat','sue','sueh','suh','sui','sun','sut','ta','tah','tai','tainn','tak','tam','tan','tang','tann','tap','tat','tau','tauh','te','teh','tenn','tha','thah','thai','thak','tham','than','thang','thann','thap','that','thau','the','theh','thenn','thi','thiah','thiam','thian','thiann','thiap','thiat','thiau','thih','thik','thim','thin','thing','thinn','thio','thiok','thiong','thiu','thng','tho','thoh','thok','thong','thoo','thu','thua','thuah','thuan','thuann','thuat','thue','thuh','thui','thun','thut','ti','tia','tiah','tiak','tiam','tian','tiann','tiap','tiat','tiau','tih','tik','tim','tin','ting','tinn','tio','tioh','tiok','tiong','tit','tiu','tiuh','tiunn','tng','to','toh','tok','tom','tong','too','tsa','tsah','tsai','tsainn','tsak','tsam','tsan','tsang','tsann','tsap','tsat','tsau','tse','tseh','tsenn','tsha','tshah','tshai','tshak','tsham','tshan','tshang','tshann','tshap','tshat','tshau','tshauh','tshe','tsheh','tshenn','tshi','tshia','tshiah','tshiak','tshiam','tshian','tshiang','tshiann','tshiap','tshiat','tshiau','tshih','tshik','tshim','tshin','tshing','tshinn','tshio','tshioh','tshiok','tshiong','tship','tshit','tshiu','tshiunn','tshng','tshngh','tsho','tshoh','tshok','tshong','tshoo','tshu','tshua','tshuah','tshuan','tshuang','tshuann','tshue','tshueh','tshuh','tshui','tshun','tshut','tsi','tsia','tsiah','tsiam','tsian','tsiang','tsiann','tsiap','tsiat','tsiau','tsih','tsik','tsim','tsin','tsing','tsinn','tsio','tsioh','tsiok','tsiong','tsip','tsit','tsiu','tsiuh','tsiunn','tsng','tso','tsoh','tsok','tsong','tsoo','tsu','tsua','tsuah','tsuainn','tsuan','tsuann','tsuat','tsue','tsueh','tsuh','tsui','tsun','tsut','tu','tua','tuah','tuan','tuann','tuat','tue','tuh','tui','tuinn','tun','tut','u','ua','uah','uai','uainn','uan','uang','uann','uat','ue','ueh','uh','ui','uih','uinn','un','ut']
            self.syllables = set([self.__strip_mark(self.conversion_func((s, False))) for s in syllables])

        class PronsDictProxy:
            def __init__(self, prons_dict, dialect, singapore_prons):
                self.prons_dict = prons_dict
                self.dialect = dialect
                self.singapore_prons = singapore_prons

            def __getitem__(self, key):
                if key in self.singapore_prons and self.dialect == 'singapore':
                    return self.singapore_prons[key]
                return self.prons_dict[key]

            def get(self, key, default=None):
                if key in self.singapore_prons and self.dialect == 'singapore':
                    return self.singapore_prons.get(key, default)
                return self.prons_dict.get(key, default)

        class WordDict:
            def __init__(self, word_dict, prons_dict, dialect, singapore_words):
                self.word_dict = word_dict
                self.prons_dict = prons_dict
                self.dialect = dialect
                self.singapore_words = singapore_words

            def __getitem__(self, key):
                value = self.word_dict.get(key)
                if not value or self.dialect == 'south': return value
                parts = [s for s in re.split('(--|-)', value.lower()) if s]
                variations = {char: {variation.split('/')[0]: variation.split('/')[1] if len(variation.split('/')) > 1 else variation.split('/')[0] for variation in self.prons_dict.get(char, [])} for char in key}

                if self.dialect == 'singapore':
                    substrings = set(
                        key[i:j+1]
                        for i in range(len(key))
                        for j in range(i, len(key))
                    )
                    for substring in substrings:
                        if substring in self.singapore_words:
                            for char, mappings in self.singapore_words[substring].items():
                                variations.setdefault(char, {}).update(mappings)
                    value = ''.join(variations.get(char, {}).get(char, char) for char in value)

                new_parts = []
                char_index = 0
                for part in parts:
                    if part in ['--','-']:
                        new_parts.append(part)
                    else:
                        char = key[char_index]
                        new_parts.append(variations.get(char, {}).get(part, part))
                        char_index += 1
                result = ''.join(new_parts)
                return result.capitalize() if value[0].isupper() else result

            def __contains__(self, key):
                return key in self.word_dict

        self.word_dict = WordDict(word_dict, PronsDictProxy(prons_dict, dialect, self.__singapore_prons), dialect, self.__singapore_words)

        if dialect == 'north' or dialect == 'singapore':
            self.sandhi_conversion.update({'5':'3'})
            if self.system == 'ipa':
                self.convert.update({'o':'o'})
                if dialect == 'north':
                    self.tones = ['','⁵⁵','⁵¹','²¹','³²','²⁴','','³³','⁴']
                else:
                    self.tones = ['','⁴⁴','⁴²','²¹','³²','²⁴','','²²','⁴']


    ### Interface functions

    # Convert tokenised text into specified transliteration system
    def get(self, input):
        converted = Tokeniser(False).tokenise(input)
        converted = ' '.join(self.__convert_tokenised(i).strip() for i in self.__tone_sandhi_position(converted)).strip()
        if self.punctuation == 'format':
            return self.__format_text(self.__format_punctuation_western(converted[0].upper() + converted[1:]))
        return self.__format_punctuation_cjk(converted)


    ### Input formatting

    # Helper to convert separate words
    def __convert_tokenised(self, word):
        if word[0] in self.word_dict:
            word = (self.word_dict[word[0]],) + word[1:]
        elif not self.convert_non_cjk or word[0] in ".,!?\"#$%&()*+/:;<=>@[\\]^`{|}~\t。．，、！？；：（）［］【】「」“”":
            return word[0]
        word = self.conversion_func(word).replace('---','--')
        if self.format == 'number' and self.system in ['tailo','poj']:
            word = self.__mark_to_number(word)
        if self.format == 'strip':
            word = self.__strip_mark(word)
        if self.delimiter == '' and self.apostrophe:
            return self.__add_apostrophes(word)
        return word.replace('--', self.suffix_token).replace('-', self.delimiter).replace(self.suffix_token, '--')


    # Helper functions to set delimiter according to transliteration system if wasn't explicitly defined by user
    def __set_default_delimiter(self):
        if self.system == 'tlpa' or self.system == 'zhuyin' or self.system == 'ipa': return ' '
        if self.system == 'pingyim': return ''
        return '-'
    

    # Helper functions to set disambiguating apostrophe according to transliteration system if wasn't explicitly defined by user
    def __set_default_apostrophe(self):
        if self.system == 'pingyim': return True
        return False


    # Helper functions to set sandhi according to transliteration system if wasn't explicitly defined by user
    def __set_default_sandhi(self):
        if self.system == 'tongiong': return 'auto'
        return 'none'


    ### Conversion functions

    # Helper to get number tones
    def __get_number_tones(self, input):
        words = self.__preprocess_word(input[0])
        number_tones = [self.__get_number_tone(w) for w in words if len(w) > 0]
        if self.sandhi in ['auto','exc_last','incl_last'] or self.format == 'number':
            replace_with_zero = False
            number_tones = [s[:-1] + '0' if replace_with_zero or (replace_with_zero := s[-1] == '0') else s for s in number_tones]
        if self.sandhi in ['auto','exc_last','incl_last']:
            index = next((i for i, s in enumerate(number_tones) if s.startswith(self.suffix_token)), len(number_tones))
            if len(number_tones) != index and len(number_tones) > 1:
                number_tones = self.__tone_sandhi(number_tones[:index], False) + number_tones[index:]
            else:
                number_tones = self.__tone_sandhi(number_tones, input[1])
        return number_tones


    # Helper to convert between transliteration systems
    def __replacement_tool(self, dictionary, input):
        pattern = re.compile('|'.join(dictionary.keys()))
        return pattern.sub(lambda m: dictionary[re.escape(m.group(0))], input)


    # Helper to convert word from Tai-lo to number
    def __mark_to_number(self, input):
        input = input.replace('--','-'+self.suffix_token)
        words = input.split('-')
        input = '-'.join(self.__get_number_tone(w) for w in words if len(w) > 0)
        return input.replace(self.suffix_token, '--')


    # Helper to convert syllable from Tai-lo diacritic tones to number tones
    def __get_number_tone(self, input):
        finals = ['p','t','k','h']
        lower_input = input.lower()
        if re.search("á|é|í|ó|ú|ḿ|ńg|́", lower_input): input += '2'
        elif re.search("à|è|ì|ò|ù|m̀|ǹg|̀", lower_input): input += '3'
        elif re.search("â|ê|î|ô|û|m̂|n̂g|̂", lower_input): input += '5'
        elif re.search("ā|ē|ī|ō|ū|m̄|n̄g|̄", lower_input): input += '7'
        elif re.search('̍', lower_input): input += '8'
        elif lower_input[-1] in finals: input += '4'
        else: input += '1'
        if input.startswith(self.suffix_token) and (input[-2:] == 'h4' or self.sandhi in ['auto','exc_last','incl_last'] or self.format == 'number'):
            input = input[:-1] + '0'
        input = "".join(c for c in unicodedata.normalize("NFD", input) if unicodedata.category(c) != "Mn")
        return input


    # Helper to break down a word into syllables for conversion
    def __preprocess_word(self, word):
        return word.replace('--','-'+self.suffix_token).split('-')


    # Helper to convert syllable from Tai-lo number tones to diacritic tones
    def __get_mark_tone(self, input, placement, tones):
        for s in placement:
            if s.replace(self.tt, '') in input:
                input = input.replace(s.replace(self.tt, ''), s.replace(self.tt, tones[int(input[-1])]))
                break
        return unicodedata.normalize('NFC', input[:-1])


    # Helper to apply tone sandhi to a word
    def __tone_sandhi(self, words, last):
        indices = (
            list(range(len(words) - 2)) if last == 'a suff' and len(words) > 1 
            else list(range(len(words) - 1)) if not last 
            else list(range(len(words)))
        )
        sandhi_words = [self.__replacement_tool(self.sandhi_conversion, words[i]) for i in indices]
        if last == 'a suff' and len(words) > 1:
            sandhi_words.append(self.__replacement_tool(self.a_sandhi, words[-2]))
        if not last or last == 'a suff':
            sandhi_words.append(words[-1])
        return sandhi_words
    

    # Helper to define which words should be sandhi'd fully
    def __tone_sandhi_position(self, input):
        sandhi_logic = {
            'exc_last': [(char, False if i == len(input) - 1 else True) for i, char in enumerate(input)],
            'incl_last': [(char, True) for char in input],
        }
        result_list = []
        for i, word in enumerate(input):
            if (i < len(input) - 1 and input[i+1] in self.__location) or word in self.__location or word in self.__no_sandhi:
                result = False
            elif len(word) > 1 and word[-1] == "仔":
                result = "a suff"
            else:
                result = (i < len(input) - 1) if self.convert_non_cjk else (i < len(input) - 1 and is_cjk(input[i+1]))
            result_list.append((word, result))
        result_list = sandhi_logic.get(self.sandhi, result_list)
        for i in range(len(result_list) - 2, -1, -1):
            if self.convert_non_cjk and result_list[i+1][0].startswith('--') or result_list[i+1][0] in self.__suffixes:
                result_list[i] = (result_list[i][0], False)
        return result_list


    # Helper function to remove tone markings
    def __strip_mark(self, input):
        if self.system == 'tlpa':
            input = input.translate(str.maketrans('','',''.join(['1','2','3','4','5','7','8'])))
        if self.system == 'zhuyin':
            input = input.translate(str.maketrans('','',''.join(['ˋ','˪','ˊ','˫','˙'])))
        if self.system == 'ipa':
            input = input.translate(str.maketrans('','',''.join(['¹','²','³','⁴','⁵'])))
        else: input = "".join(c for c in unicodedata.normalize("NFD", input) if unicodedata.category(c) != "Mn")
        return input


    # Helper function to determine if an apostrophe is needed between two syllables
    def __needs_apostrophe(self, s1, s2):
        def normalise(s):
            return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
        s1n = normalise(s1)
        s2n = normalise(s2)

        combined = s1n + s2n

        # Case 1: merges into a valid syllable
        if combined in self.syllables:
            return True

        # Case 2: alternative segmentation exists
        for i in range(1, len(combined)):
            alt1 = combined[:i]
            alt2 = combined[i:]

            if (alt1, alt2) != (s1n, s2n):
                if alt1 in self.syllables and alt2 in self.syllables:
                    return True

        return False


    # Helper function to add apostrophes between syllables where needed to prevent ambiguity
    def __add_apostrophes(self, syllables):
        def split_syllables(s):
            return [
                ('--' + sp if i and j == 0 else sp)
                for i, part in enumerate(s.split('--'))
                for j, sp in enumerate(part.split('-'))
                if sp
            ]
        syllables = split_syllables(syllables)
        result = syllables[0]

        for i in range(len(syllables) - 1):
            s1 = syllables[i]
            s2 = syllables[i+1]

            if self.__needs_apostrophe(s1, s2):
                result += "'" + s2
            else:
                result += s2

        return result
    

    # Helper to convert Taiwanese pronunciation to Singaporean
    def __convert_variant(self, input):
        return input.replace('ing','eng') if self.dialect == 'singapore' else input


    ### Tai-lo to other transliteration systems converting

    # Helper to convert syllable from Tai-lo to Tai-lo
    def __tailo_to_tailo(self, input):
        input = '-'.join(self.__get_mark_tone(self.__convert_variant(nt), self.placement, self.tones) for nt in self.__get_number_tones(input))
        return input.replace(self.suffix_token, '--')


    # Helper to convert syllable from Tai-lo to POJ
    def __tailo_to_poj(self, input):
        number_tones = self.__get_number_tones(input)
        input = '-'.join(
            self.__get_mark_tone(self.__replacement_tool(self.convert, self.__convert_variant(nt)), self.placement, self.tones) 
            for nt in number_tones
        )
        return input.replace(self.suffix_token, '--')


    # Helper to convert syllable from Tai-lo to 方音符號 (zhuyin)
    def __tailo_to_zhuyin(self, input):
        output = []
        for nt in self.__get_number_tones((input[0].lower(), input[1])):
            nt = self.__replacement_tool(self.convert, self.__convert_variant(nt)).replace(self.suffix_token, '')
            if len(nt) > 2 and nt[-2] == 'ㄋ':
                nt = nt[:-2] + 'ㄣ' + nt[-1]
            if self.format != 'number':
                nt = ''.join(self.tones[int(t)] if t.isnumeric() else t for t in nt)
            output.append(nt)
        return '-'.join(output).replace(self.suffix_token, '')


    # Helper to convert syllable from Tai-lo to TLPA
    def __tailo_to_tlpa(self, input):
        input = '-'.join(self.__replacement_tool(self.convert, self.__convert_variant(nt)) for nt in self.__get_number_tones(input))
        return input.replace(self.suffix_token, '')


    # Helper to convert syllable from Tai-lo to Bbanlam pingyim
    def __tailo_to_pingyim(self, input):
        output = []
        for nt in self.__get_number_tones(input):
            replaced = self.__replacement_tool(self.convert, self.__convert_variant(nt))
            if replaced[0] in ['i','I']: # Initial i
                replaced = ('Y' if replaced[0] == 'I' else 'y') + (replaced[1:] if replaced[1] in ['a','u','o'] else replaced.lower())
            if replaced[0] in ['u','U']: # Initial u
                replaced = ('W' if replaced[0] == 'U' else 'w') + (replaced[1:] if len(nt) > 2 and replaced[1] in ['a','i','e','o'] else replaced.lower())
            if replaced[0] in ['n','N']: # Initial n
                replaced = ('Ln' if replaced[0] == 'N' else 'ln') + replaced[1:]
            if replaced[0] in ['m','M'] and replaced[1] in 'aeiou': # Initial m
                replaced = ('Bbn' if replaced[0] == 'M' else 'bbn') + replaced[1:]
            if 'nn' in replaced.lower(): # Nasalisation
                idx = replaced.lower().find('nn')

                # handle onn
                if (
                    idx > 0 and
                    replaced[idx - 1] in ['o', 'O'] and
                    (idx - 2 < 0 or replaced[idx - 2].lower() not in 'aeiou')
                ):
                    o_char = replaced[idx - 1]
                    replaced = replaced[:idx - 1] + (o_char * 2) + replaced[idx:]
                    idx += 1

                replaced = replaced[:idx] + replaced[idx + 2:]
                insert_pos = 0
                for i in range(idx - 1, -1, -1):
                    if replaced[i].lower() not in 'aeiou':
                        insert_pos = i + 1
                        break
                replaced = replaced[:insert_pos] + 'n' + replaced[insert_pos:]
            if nt[-3:-1] in ['ng','Ng']: # Coda ng
                replaced = replaced[:-4] + nt[-3:-1] + nt[-1]
            if self.format != 'number':
                output.append(self.__get_mark_tone(replaced, self.placement, self.tones))
            else:
                output.append(replaced)
        return '-'.join(output).replace(self.suffix_token, '')


    # Helper to convert syllable from Tai-lo to Tong-iong ping-im
    def __tailo_to_ti(self, input):
        number_tones = [nt[:-2] + 'or' + nt[-1] if nt[-2] == 'o' else nt for nt in self.__get_number_tones(input)]
        input = '-'.join(
            self.__get_mark_tone(self.__replacement_tool(self.convert, self.__convert_variant(nt)), self.placement, self.tones) 
            if self.format != 'number' 
            else self.__replacement_tool(self.convert, self.__convert_variant(nt)) 
            for nt in number_tones
        )
        return input.replace(self.suffix_token, '--')
    

    # Helper to convert syllable from Tai-lo to International Phonetic Alphabet
    def __tailo_to_ipa(self, input):
        output = []
        for nt in self.__get_number_tones((input[0], input[1])):
            nt = self.__replacement_tool(self.convert, self.__convert_variant(nt)).replace(self.suffix_token, '')
            if 'ŋ' in nt:
                if len(nt) > 2:
                    if all(c.lower() not in 'aeioɔu' for c in nt[:nt.index('ŋ')]) and nt.index('ŋ') != 0:
                        nt = nt.replace('ŋ','ŋ̍')
                elif len(nt) == 2:
                    nt = nt.replace('ŋ','ŋ̍')
            if len(nt) == 2 and nt[0] == 'm':
                nt = 'm̩' + nt[-1]
            nt = self.__replacement_tool(self.convert2, self.__convert_variant(nt))
            if self.format != 'number':
                nt = ''.join(self.tones[int(t)] if t.isnumeric() else t for t in nt)
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
        punc_filter = re.compile(r"([.!?]\s*)")
        split_with_punc = punc_filter.split(input)
        split_with_punc = [i[0].upper() + i[1:] if len(i) > 1 else i for i in split_with_punc]
        return "".join(split_with_punc)


"""
Description: Tokenises Taiwanese Hokkien sentences.
             Supports both Traditional and Simplified characters.
Invariant: keep_original = True (default), False
"""
class Tokeniser(object):

    def __init__(self, keep_original=True):
        self.keep_original = keep_original

    # Tokenise the text into separate words
    def tokenise(self, input):
        traditional = to_traditional(input)
        n = len(traditional)
        dp = [{'score': float('inf'), 'last_word': None} for _ in range(n+1)]
        dp[0]['score'] = 0
        for i in range(1, n+1):
            for j in range(max(0, i-4), i):
                word = traditional[j:i]
                if word_dict.get(word) or len(word) == 1:
                    score = dp[j]['score'] + 1
                    if score < dp[i]['score']:
                        dp[i]['score'] = score
                        dp[i]['last_word'] = word
        tokenised = []
        i = n
        while i > 0:
            word = dp[i]['last_word']
            if tokenised and not (is_cjk(tokenised[-1]) or is_cjk(word)):
                tokenised[-1] = word + tokenised[-1]
            else:
                tokenised.append(word)
            i -= len(word)
        tokenised.reverse()
        punctuations = re.compile(r"([.,!?\"#$%&()*+/:;<=>@[\]^`{|}~\t。．，、！？；：（）［］【】「」“”]\s*)")
        if self.keep_original:
            indices = [0] + [len(item) for item in tokenised]
            tokenised = [input[sum(indices[:i+1]):sum(indices[:i+2])] for i in range(len(indices)-1)]
        tokenised = [
            item 
            for word in tokenised 
            for subword in re.split(punctuations, word) if subword 
            for item in subword.split(" ") if item
        ]
        return [
            subword 
            for word in tokenised 
            for subword in (
                (word[:-1], word[-1]) if (word[-1] == '矣') and len(word) > 1 
                else (word,)
            )
        ]