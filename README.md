[台語](README-oan.md) | [國語](README-cmn.md)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/andreihar/taibun">
    <img src="readme/logo.png" alt="Logo" width="90" height="80">
  </a>
  
# Taibun



<!-- PROJECT SHIELDS -->
[![Tests][tests-badge]][tests]
[![Contributors][contributors-badge]][contributors]
[![Release][release-badge]][release]
[![Licence][licence-badge]][licence]
[![LinkedIn][linkedin-badge]][linkedin]

**Taiwanese Hokkien Transliterator and Tokeniser**

It has methods that allow to customise transliteration and retrieve any necessary information about Taiwanese Hokkien pronunciation.<br />
Includes word tokeniser for Taiwanese Hokkien.

[Report Bug][bug] •
[PyPI][pypi]

</div>



---



<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#install">Install</a></li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li>
          <a href="#converter">Converter</a>
          <ul>
            <li><a href="#system">System</a></li>
            <li><a href="#dialect">Dialect</a></li>
            <li><a href="#format">Format</a></li>
            <li><a href="#delimiter">Delimiter</a></li>
            <li><a href="#sandhi">Sandhi</a></li>
            <li><a href="#punctuation">Punctuation</a></li>
          </ul>
        </li>
        <li><a href="#tokeniser">Tokeniser</a></li>
      </ul>
    </li>
    <li><a href="#example">Example</a></li>
    <li><a href="#data">Data</a></li>
    <li><a href="#licence">Licence</a></li>
  </ol>
</details>



<!-- INSTALL -->
## Install

Taibun can be installed from [pypi][pypi]

```bash
$ pip install taibun
```



<!-- USAGE -->
## Usage

### Converter

`Converter` class transliterates the Chinese characters to the chosen transliteration system with parameters specified by the developer. Works for both Traditional and Simplified characters.

```python
# constructor
c = Converter(system, dialect, format, delimiter, sandhi, punctuation)

# transliterate Chinese characters
c.get(input)

# convert Simplified Chinese characters to Traditional Chinese Characters
c.to_traditional(input)
```

#### System

`system` String - system of transliteration.

* `Tailo` (default) - [Tâi-uân Lô-má-jī Phing-im Hong-àn][tailo-wiki]
* `POJ` - [Pe̍h-ōe-jī][poj-wiki]
* `Zhuyin` - [Taiwanese Phonetic Symbols][zhuyin-wiki]
* `TLPA` - [Taiwanese Language Phonetic Alphabet][tlpa-wiki]
* `Pingyim` - [Bbánlám Uē Pìngyīm Hōng'àn][pingyim-wiki]
* `Tongiong` - [Daī-ghî Tōng-iōng Pīng-im][tongiong-wiki]

| text | Tailo   | POJ     | Zhuyin      | TLPA      | Pingyim | Tongiong |
|------|---------|---------|-------------|-----------|---------|----------|
| 臺灣 | Tâi-uân | Tâi-oân | ㄉㄞˊ ㄨㄢˊ | Tai5 uan5 | Dáiwán  | Tāi-uǎn  |

#### Dialect

`dialect` String - preferred pronunciation.

* `south` (default) - [Zhangzhou][zhangzhou-wiki]-leaning pronunciation
* `north` - [Quanzhou][quanzhou-wiki]-leaning pronunciation

| text   | south         | north         |
|--------|---------------|---------------|
| 五月節 | Gōo-gue̍h-tseh | Gōo-ge̍h-tsueh |

#### Format

`format` String - format in which tones will be represented in the converted sentence.

* `mark` (default) - uses diacritics for each syllable. Not available for TLPA.
* `number` - add a number which represents the tone at the end of the syllable
* `strip` - removes any tone marking

| text | mark    | number    | strip   |
|------|---------|-----------|---------|
| 臺灣 | Tâi-uân | Tai5-uan5 | Tai-uan |

#### Delimiter

`delimiter` String - sets the delimiter character that will be placed in between syllables of a word.

Default value depends on the chosen `system`:

* `'-'` - for `Tailo`, `POJ`, `Tongiong`
* `''` - for `Pingyim`
* `' '` - for `Zhuyin`, `TLPA`

| text | '-'     | ''     | ' '     |
|------|---------|--------|---------|
| 臺灣 | Tâi-uân | Tâiuân | Tâi uân |

#### Sandhi

`sandhi` Boolean - applies the [sandhi rules of Taiwanese Hokkien][sandhi-wiki] to syllables of a single word.

Default value depends on the chosen `system`:

* `True` - for `Tongiong`
* `False` - for `Tailo`, `POJ`, `Zhuyin`, `TLPA`, `Pingyim`

| text     | False        | True         |
|----------|--------------|--------------|
| 馬來西亞 | Má-lâi-se-a  | Ma-lāi-sē-a  |

Sandhi rules also change depending on the dialect chosen.

| text | no sandhi | south   | north   |
|------|-----------|---------|---------|
| 臺灣 | Tâi-uân   | Tāi-uân | Tài-uân |

Note that the function is different from real sandhi rules, where changes are applied to every single syllable of the sentence, not just single words.

- **Taibun's sandhi rules**: Thái-khong pīng-iú, lin-hó! Lín tsià-pá buē?
- **Actual sandhi rules**: Thái-khōng pīng-iú, lin-hó! Lin tsià-pa buē?

#### Punctuation

`punctuation` String

* `format` (default) - converts Chinese-style punctuation to Latin-style punctuation and capitalises words at the beginning of each sentence.
* `none` - preserves Chinese-style punctuation and doesn't capitalise words at the beginning of new sentences.

| text | format | none |
|-|-|-|
| 這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。 | Tse sī Tâi-lâm, kán-tshing "lâm" (Pe̍h-uē-jī: Tâi-lâm; tsù-im hû-hō: ㄊㄞˊ ㄋㄢˊ, kok-gí: Táinán). | tse sī Tâi-lâm，kán-tshing「lâm」（Pe̍h-uē-jī：Tâi-lâm；tsù-im hû-hō：ㄊㄞˊ ㄋㄢˊ，kok-gí：Táinán）。 |

### Tokeniser

`Tokeniser` class performs [NLTK wordpunct_tokenize][nltk-tokenize]-like tokenisation of a Taiwanese Hokkien sentence.

```python
# constructor
t = Tokeniser()

# tokenise Taiwanese Hokkien sentence
t.tokenise(input)
```



<!-- EXAMPLE -->
## Example

```python
from taibun import Converter, Tokeniser

# System
c = Converter() # Tailo system default
c.get('先生講，學生恬恬聽。')
>> Sian-sinn kóng, ha̍k-sing tiām-tiām thiann.

c = Converter(system='Zhuyin')
c.get('先生講，學生恬恬聽。')
>> ㄒㄧㄢ ㄒㆪ ㄍㆲˋ, ㄏㄚㆶ˙ ㄒㄧㄥ ㄉㄧㆰ˫ ㄉㄧㆰ˫ ㄊㄧㆩ.

# Dialect
c = Converter() # south dialect default
c.get("我欲用箸食魚")
>> Guá beh īng tī tsia̍h hî

c = Converter(dialect='north')
c.get("我欲用箸食魚")
>> Guá bueh īng tū tsia̍h hû

# Format
c = Converter() # for Tailo, mark by default
c.get("生日快樂")
>> Senn-ji̍t khuài-lo̍k

c = Converter(format='number')
c.get("生日快樂")
>> Senn1-jit8 khuai3-lok8

c = Converter(format='strip')
c.get("生日快樂")
>> Senn-jit khuai-lok

# Delimiter
c = Converter(delimiter='')
c.get("先生講，學生恬恬聽。")
>> Siansinn kóng, ha̍ksing tiāmtiām thiann.

c = Converter(system='Pingyim', delimiter='-')
c.get("先生講，學生恬恬聽。")
>> Siān-snī gǒng, hág-sīng diâm-diâm tinā.

# Sandhi
c = Converter() # for Tailo, sandhi False by default
c.get("南迴鐵路")
>> Lâm-huê-thih-lōo

c = Converter(sandhi=True)
c.get("南迴鐵路")
>> Lām-huē-thí-lōo

# Punctuation
c = Converter() # format punctuation default
c.get("太空朋友，恁好！恁食飽未？")
>> Thài-khong pîng-iú, lín-hó! Lín tsia̍h-pá buē?

c = Converter(punctuation='none')
c.get("太空朋友，恁好！恁食飽未？")
>> thài-khong pîng-iú，lín-hó！lín tsia̍h-pá buē？


# Tokeniser
t = Tokeniser()
t.tokenise("太空朋友，恁好！恁食飽未？")
>> ['太空', '朋友', '，', '恁好', '！', '恁', '食飽', '未', '？']
```



<!-- DATA -->
## Data

- [Taiwanese-Chinese Online Dictionary][online-dictionary] (via [ChhoeTaigi][data-via])
- [iTaigi Chinese-Taiwanese Comparison Dictionary][itaigi-dictionary] (via [ChhoeTaigi][data-via])



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

- Samuel Jen ([Github][samuel-github] · [LinkedIn][samuel-linkedin]) - Taiwanese and Mandarin translation



<!-- LICENCE -->
## Licence

Because Taibun is MIT-licensed, any developer can essentially do whatever they want with it as long as they include the original copyright and licence notice in any copies of the source code. Note, that the data used by the package is licensed under a different copyright.

The data is licensed under [CC BY-SA 4.0][data-cc]



<!-- MARKDOWN LINKS -->
[tests]: https://github.com/andreihar/taibun/actions
[tests-badge]: https://img.shields.io/github/actions/workflow/status/andreihar/taibun/ci.yaml?style=for-the-badge&logo=github
[contributors-badge]: https://img.shields.io/github/contributors/andreihar/taibun?style=for-the-badge
[contributors]: #usage
[release-badge]: https://img.shields.io/github/v/release/andreihar/taibun?color=38618c&style=for-the-badge
[release]: https://github.com/andreihar/taibun/releases
[licence-badge]: https://img.shields.io/github/license/andreihar/taibun?color=000000&style=for-the-badge
[licence]: LICENSE
[linkedin-badge]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin]: https://www.linkedin.com/in/andrei-harbachov/

[pypi]: https://pypi.org/project/taibun
[bug]: https://github.com/andreihar/taibun/issues
[online-dictionary]: http://ip194097.ntcu.edu.tw/ungian/soannteng/chil/Taihoa.asp
[itaigi-dictionary]: https://itaigi.tw/
[data-via]: https://github.com/ChhoeTaigi/ChhoeTaigiDatabase
[data-cc]: https://creativecommons.org/licenses/by-sa/4.0/deed.en
[samuel-github]: https://github.com/SSSam
[samuel-linkedin]: https://www.linkedin.com/in/samuel-jen/

[tailo-wiki]: https://en.wikipedia.org/wiki/T%C3%A2i-u%C3%A2n_L%C3%B4-m%C3%A1-j%C4%AB_Phing-im_Hong-%C3%A0n
[poj-wiki]: https://en.wikipedia.org/wiki/Pe%CC%8Dh-%C5%8De-j%C4%AB
[zhuyin-wiki]: https://en.wikipedia.org/wiki/Taiwanese_Phonetic_Symbols
[tlpa-wiki]: https://en.wikipedia.org/wiki/Taiwanese_Language_Phonetic_Alphabet
[pingyim-wiki]: https://en.wikipedia.org/wiki/Bb%C3%A1nl%C3%A1m_p%C3%ACngy%C4%ABm
[tongiong-wiki]: https://en.wikipedia.org/wiki/Da%C4%AB-gh%C3%AE_t%C5%8Dng-i%C5%8Dng_p%C4%ABng-im
[zhangzhou-wiki]: https://en.wikipedia.org/wiki/Zhangzhou_dialects
[quanzhou-wiki]: https://en.wikipedia.org/wiki/Quanzhou_dialects
[nltk-tokenize]: https://nltk.org/api/nltk.tokenize.html
[sandhi-wiki]: https://en.wikipedia.org/wiki/Taiwanese_Hokkien#Tone%20sandhi:~:text=thng%E2%9F%A9%20(%22soup%22).-,Tone%20sandhi,-%5Bedit%5D