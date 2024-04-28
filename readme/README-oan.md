[國語](README-cmn.md) | [English](../README.md)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/andreihar/taibun">
    <img src="logo.png" alt="Logo" width="90" height="80">
  </a>
  
# Taibun



<!-- PROJECT SHIELDS -->
[![Tests][tests-badge]][tests]
[![Contributors][contributors-badge]][contributors]
[![Release][release-badge]][release]
[![Licence][licence-badge]][licence]
[![LinkedIn][linkedin-badge]][linkedin]

**台語音譯器佮標記器**

伊有允許自己設定音譯，佮揣出關於台語發音所需要的資料的方法<br />
包括台語的單詞標記器

[回報程式缺點][bug] •
[PyPI][pypi]

</div>



---



<!-- TABLE OF CONTENTS -->
<details open>
  <summary>目錄</summary>
  <ol>
    <li><a href="#安裝">安裝</a></li>
    <li>
      <a href="#用法">用法</a>
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
            <li><a href="#convert-non-cjk">Convert non-CJK</a></li>
          </ul>
        </li>
        <li><a href="#tokeniser">Tokeniser</a></li>
        <li><a href="#其他的功能">其他的功能</a></li>
      </ul>
    </li>
    <li><a href="#例">例</a></li>
    <li><a href="#數據">數據</a></li>
    <li><a href="#牌照">牌照</a></li>
  </ol>
</details>



<!-- INSTALL -->
## 安裝

Taibun 會曉通過 [pypi][pypi] 安裝

```bash
$ pip install taibun
```



<!-- USAGE -->
## 用法

### Converter

`Converter` 類別使用開發人員指定的參數將漢文音譯為所選的音譯系統。繁體佮簡體攏合用。

```python
# 建構仔
c = Converter(system, dialect, format, delimiter, sandhi, punctuation, convert_non_cjk)

# 音譯漢文
c.get(input)
```

#### System

`system` String - 音譯系統。

* `Tailo` (預設) - [臺灣羅馬字拼音方案][tailo-wiki]
* `POJ` - [白話字][poj-wiki]
* `Zhuyin` - [臺語方音符號][zhuyin-wiki]
* `TLPA` - [臺灣語言音標方案][tlpa-wiki]
* `Pingyim` - [閩南話拼音方案][pingyim-wiki]
* `Tongiong` - [臺語通用拼音][tongiong-wiki]
* `IPA` - [國際音標][ipa-wiki]

| 文本 | Tailo   | POJ     | Zhuyin      | TLPA      | Pingyim | Tongiong | IPA         |
| ---- | ------- | ------- | ----------- | --------- | ------- | -------- | ----------- |
| 台灣 | Tâi-uân | Tâi-oân | ㄉㄞˊ ㄨㄢˊ | Tai5 uan5 | Dáiwán  | Tāi-uǎn  | Tai²⁵ uan²⁵ |

#### Dialect

`dialect` String - 頭一範的發音。

* `south` (預設) - 發音較像[漳州話][zhangzhou-wiki]
* `north` - 發音較像[泉州話][quanzhou-wiki]

| 文本   | south         | north         |
| ------ | ------------- | ------------- |
| 五月節 | Gōo-gue̍h-tseh | Gōo-ge̍h-tsueh |

#### Format

`format` String - 轉換後的句子中表示聲調的格式。

* `mark` (預設) - 每个音節攏用變音符號。毋支援拼音
* `number` - 加入一个代表音節尾端聲調的數字
* `strip` - 刪除任何音調標記

| 文本 | mark    | number    | strip   |
| ---- | ------- | --------- | ------- |
| 台灣 | Tâi-uân | Tai5-uan5 | Tai-uan |

#### Delimiter

`delimiter` String - 設定欲放佇詞音節中間的分隔符。

預設值看所選的 `system` 決定：

* `'-'` - 對著 `Tailo`, `POJ`, `Tongiong`
* `''` - 對著 `Pingyim`
* `' '` - 對著 `Zhuyin`, `TLPA`

| 文本 | '-'     | ''     | ' '     |
| ---- | ------- | ------ | ------- |
| 台灣 | Tâi-uân | Tâiuân | Tâi uân |

#### Sandhi

`sandhi` String - 將[台語變調規則][sandhi-wiki]做用佇單詞音節內。

因為編碼所有變調法度困難，Taibun 提供濟種模式變調改換以支援自訂變調處理。

* `none` - 無執行任何變調
* `auto` - 上接近台語的正確音調變音，包括代詞、後娗佮帶有「仔」詞的音調變音
* `exc_last` - 除了最後一个音節以外，每一个音節攏變調
* `incl_last` - 包括上尾一个音節在內，每一个音節攏變調

預設值看所選的 `system` 決定:

* `True` - 對著 `Tongiong`
* `False` - 對著 `Tailo`, `POJ`, `Zhuyin`, `TLPA`, `Pingyim`, `IPA`

| 文本         | none                 | auto                 | exc_last             | incl_last            |
| ------------ | -------------------- | -------------------- | -------------------- | -------------------- |
| 這是台灣囡仔 | Tse sī Tâi-uân gín-á | Tse sì Tāi-uān gin-á | Tsē sì Tāi-uān gin-á | Tsē sì Tāi-uān gin-a |

變調規則也會隨著選的方言而有所改變。

| 文本 | 沒有變速 | south   | north   |
| ---- | -------- | ------- | ------- |
| 台灣 | Tâi-uân  | Tāi-uân | Tài-uân |

#### Punctuation

`punctuation` String

* `format` (預設) - 將中文標點符號轉做英文標點符號，佮將每句頭前的詞大寫
* `none` - 保留中文風格的標點符號，佮新句開頭的詞毋大寫

| 文本                                                                           | format                                                                                            | none                                                                                                 |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。 | Tse sī Tâi-lâm, kán-tshing "lâm" (Pe̍h-uē-jī: Tâi-lâm; tsù-im hû-hō: ㄊㄞˊ ㄋㄢˊ, kok-gí: Táinán). | tse sī Tâi-lâm，kán-tshing「lâm」（Pe̍h-uē-jī：Tâi-lâm；tsù-im hû-hō：ㄊㄞˊ ㄋㄢˊ，kok-gí：Táinán）。 |

#### Convert non-CJK

`convert_non_cjk` Boolean - 定義轉換非中文單詞。會當用台羅來做其他羅馬拼音系統。

* `True` - 轉換非中文字詞
* `False` (預設) - 干焦轉換中文字詞

| 文本      | False                   | True                    |
| --------- | ----------------------- | ----------------------- |
| 我食pháng | ㆣㄨㄚˋ ㄐㄧㄚㆷ˙ pháng | ㆣㄨㄚˋ ㄐㄧㄚㆷ˙ ㄆㄤˋ |

### Tokeniser

`Tokeniser` 類別佇台語句子做類似 [NLTK wordpunct_tokenize][nltk-tokenize] 的標記化。

```python
# 建構仔
t = Tokeniser()

# 標記台語句
t.tokenise(input)
```

### 其他的功能

```python
# 轉換做繁體
to_traditional(input)

# 轉換做簡體
to_simplified(input)

# 檢查字串是毋是完全由中文字符組成
is_cjk(input)
```



<!-- EXAMPLE -->
## 例

```python
# Converter
from taibun import Converter

## System
c = Converter() # system 預設值: Tailo
c.get('先生講，學生恬恬聽。')
>> Sian-sinn kóng, ha̍k-sing tiām-tiām thiann.

c = Converter(system='Zhuyin')
c.get('先生講，學生恬恬聽。')
>> ㄒㄧㄢ ㄒㆪ ㄍㆲˋ, ㄏㄚㆶ˙ ㄒㄧㄥ ㄉㄧㆰ˫ ㄉㄧㆰ˫ ㄊㄧㆩ.

## Dialect
c = Converter() # dialect 預設值: south
c.get("我欲用箸食魚")
>> Guá beh īng tī tsia̍h hî

c = Converter(dialect='north')
c.get("我欲用箸食魚")
>> Guá bueh īng tū tsia̍h hû

## Format
c = Converter() # 佇 Tailo 中，format 預設值: mark
c.get("生日快樂")
>> Senn-ji̍t khuài-lo̍k

c = Converter(format='number')
c.get("生日快樂")
>> Senn1-jit8 khuai3-lok8

c = Converter(format='strip')
c.get("生日快樂")
>> Senn-jit khuai-lok

## Delimiter
c = Converter(delimiter='')
c.get("先生講，學生恬恬聽。")
>> Siansinn kóng, ha̍ksing tiāmtiām thiann.

c = Converter(system='Pingyim', delimiter='-')
c.get("先生講，學生恬恬聽。")
>> Siān-snī gǒng, hág-sīng diâm-diâm tinā.

## Sandhi
c = Converter() # 佇 Tailo 中，sandhi 預設值: none
c.get("這是台灣囡仔")
>> Tse sī Tâi-uân gín-á

c = Converter(sandhi='auto')
c.get("這是台灣囡仔")
>> Tse sì Tāi-uān gin-á

c = Converter(sandhi='exc_last')
c.get("這是台灣囡仔")
>> Tsē sì Tāi-uān gin-á

c = Converter(sandhi='incl_last')
c.get("這是台灣囡仔")
>> Tsē sì Tāi-uān gin-a

## Punctuation
c = Converter() # punctuation 預設值: format
c.get("太空朋友，恁好！恁食飽未？")
>> Thài-khong pîng-iú, lín-hó! Lín tsia̍h-pá buē?

c = Converter(punctuation='none')
c.get("太空朋友，恁好！恁食飽未？")
>> thài-khong pîng-iú，lín-hó！lín tsia̍h-pá buē？

## Convert non-CJK
c = Convert(system='Zhuyin') # convert_non_cjk 預設值: False
c.get("我食pháng")
>> ㆣㄨㄚˋ ㄐㄧㄚㆷ˙ pháng

c = Convert(system='Zhuyin', convert_non_cjk=True)
c.get("我食pháng")
>> ㆣㄨㄚˋ ㄐㄧㄚㆷ˙ ㄆㄤˋ


# Tokeniser
from taibun import Tokeniser

t = Tokeniser()
t.tokenise("太空朋友，恁好！恁食飽未？")
>> ['太空', '朋友', '，', '恁好', '！', '恁', '食飽', '未', '？']


# 其他的功能
from taibun import to_traditional, to_simplified, is_cjk

to_traditional("我听无台湾话")
>> 我聽無台灣話

to_simplified("我聽無臺灣話")
>> 我听无台湾话

is_cjk('我食麭')
>> True

is_cjk('我食pháng')
>> False
```



<!-- DATA -->
## 數據

- [台華線頂對照典][online-dictionary] (藉著 [ChhoeTaigi][data-via])
- [iTaigi華台對照典][itaigi-dictionary] (藉著 [ChhoeTaigi][data-via])



<!-- ACKNOWLEDGEMENTS -->
## 致謝

- 任全恩 ([Github][samuel-github] · [LinkedIn][samuel-linkedin]) - 台語佮國語通譯



<!-- LICENCE -->
## 牌照

因為 Taibun 合和 MIT 許可，所以任何開發人員基本上攏會當用伊做任何𪜶欲做的代誌，只欲𪜶佇源代碼的任何副本中含原始版權佮許可聲明。 請注意，彼包使用的資料已經拿著不同版權的許可。

數據已獲得 [CC BY-SA 4.0][data-cc] 許可



<!-- MARKDOWN LINKS -->
[tests]: https://github.com/andreihar/taibun/actions
[tests-badge]: https://img.shields.io/github/actions/workflow/status/andreihar/taibun/ci.yaml?style=for-the-badge&logo=github&label=構建
[contributors-badge]: https://img.shields.io/github/contributors/andreihar/taibun?style=for-the-badge&label=貢獻者
[contributors]: #usage
[release-badge]: https://img.shields.io/github/v/release/andreihar/taibun?color=38618c&style=for-the-badge&label=發布
[release]: https://github.com/andreihar/taibun/releases
[licence-badge]: https://img.shields.io/github/license/andreihar/taibun?color=000000&style=for-the-badge&label=牌照
[licence]: ../LICENSE
[linkedin-badge]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin]: https://www.linkedin.com/in/andrei-harbachov/

[pypi]: https://pypi.org/project/taibun
[bug]: https://github.com/andreihar/taibun/issues
[online-dictionary]: http://ip194097.ntcu.edu.tw/ungian/soannteng/chil/Taihoa.asp
[itaigi-dictionary]: https://itaigi.tw/
[data-via]: https://github.com/ChhoeTaigi/ChhoeTaigiDatabase
[data-cc]: https://creativecommons.org/licenses/by-sa/4.0/deed.zh_TW
[samuel-github]: https://github.com/SSSam
[samuel-linkedin]: https://www.linkedin.com/in/samuel-jen/

[tailo-wiki]: https://zh.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3%E9%96%A9%E5%8D%97%E8%AA%9E%E7%BE%85%E9%A6%AC%E5%AD%97%E6%8B%BC%E9%9F%B3%E6%96%B9%E6%A1%88
[poj-wiki]: https://zh.wikipedia.org/zh-tw/%E7%99%BD%E8%A9%B1%E5%AD%97
[zhuyin-wiki]: https://zh.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3%E6%96%B9%E9%9F%B3%E7%AC%A6%E8%99%9F
[tlpa-wiki]: https://zh.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3%E8%AA%9E%E8%A8%80%E9%9F%B3%E6%A8%99%E6%96%B9%E6%A1%88
[pingyim-wiki]: https://zh.wikipedia.org/zh-tw/%E9%96%A9%E5%8D%97%E8%A9%B1%E6%8B%BC%E9%9F%B3%E6%96%B9%E6%A1%88
[tongiong-wiki]: https://zh.wikipedia.org/zh-tw/%E8%87%BA%E8%AA%9E%E9%80%9A%E7%94%A8%E6%8B%BC%E9%9F%B3
[ipa-wiki]: https://zh.wikipedia.org/zh-tw/%E5%9C%8B%E9%9A%9B%E9%9F%B3%E6%A8%99
[zhangzhou-wiki]: https://zh.wikipedia.org/zh-tw/%E6%BC%B3%E5%B7%9E%E8%AF%9D
[quanzhou-wiki]: https://zh.wikipedia.org/zh-tw/%E6%B3%89%E5%B7%9E%E8%AF%9D
[nltk-tokenize]: https://nltk.org/api/nltk.tokenize.html
[sandhi-wiki]: https://zh.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3%E8%A9%B1#%E9%80%A3%E8%AE%80%E8%AE%8A%E8%AA%BF:~:text=%E3%80%82%5B144%5D-,%E9%80%A3%E8%AE%80%E8%AE%8A%E8%AA%BF,-%E9%80%A3%E8%AE%80%E8%AE%8A%E8%AA%BF