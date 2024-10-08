[台語](README-oan.md) | [English](../README.md)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/andreihar/taibun">
    <img src="https://github.com/andreihar/taibun/raw/main/readme/logo.png" alt="Logo" width="90" height="80">
  </a>
  
# Taibun



<!-- PROJECT SHIELDS -->
[![Contributions][contributions-badge]][contributions]
[![Live Demo][demo-badge]][demo]
[![Tests][tests-badge]][tests]
[![Release][release-badge]][release]
[![Licence][licence-badge]][licence]
[![LinkedIn][linkedin-badge]][linkedin]
[![Downloads][downloads-badge]][pypi]

**臺灣話音譯器和標記器**

它具有允許自定義音譯，和檢索有關臺灣話發音的任何必要信息的方法<br />
包括臺灣話的單詞標記器

[報告軟件缺陷][bug] •
[PyPI][pypi]

</div>



---



<!-- TABLE OF CONTENTS -->
<details open>
  <summary>目錄</summary>
  <ol>
    <li><a href="#版本">版本</a></li>
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
        <li>
          <a href="#tokeniser">Tokeniser</a>
          <ul>
            <li><a href="#keep-original">Keep original</a></li>
          </ul>
        </li>
        <li><a href="#其他函式">其他函式</a></li>
      </ul>
    </li>
    <li><a href="#例子">例子</a></li>
    <li><a href="#數據">數據</a></li>
    <li><a href="#致謝">致謝</a></li>
    <li><a href="#執照">執照</a></li>
  </ol>
</details>



<!-- OTHER VERSIONS -->
## 版本

[![JavaScript Version][js-badge]][js-link]



<!-- INSTALL -->
## 安裝

Taibun 可以通過 [pypi][pypi] 安裝

```bash
$ pip install taibun
```



<!-- USAGE -->
## 用法

### Converter

`Converter` 類別使用開發人員指定的參數將中文字音譯為所選的音譯系統。適用於繁體和簡體字符。

```python
# 建構子
c = Converter(system, dialect, format, delimiter, sandhi, punctuation, convert_non_cjk)

# 音譯中文字
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

`dialect` String - 首選發音。

* `south` (預設) - 發音更接近[漳州話][zhangzhou-wiki]
* `north` - 發音更接近[泉州話][quanzhou-wiki]
* `singapore` - 帶有[新加坡特色][singapore-wiki]的泉州話發音

| 文本           | south                       | north                       | singapore                  |
| -------------- | --------------------------- | --------------------------- | -------------------------- |
| 五月節我啉咖啡 | Gōo-gue̍h-tseh guá lim ka-pi | Gōo-ge̍h-tsueh guá lim ka-pi | Gōo-ge̍h-tsueh uá lim ko-pi |

#### Format

`format` String - 轉換後的句子中表示聲調的格式。

* `mark` (預設) - 每個音節都使用變音符號。不支持拼音
* `number` - 添加一個代表音節末尾聲調的數字
* `strip` - 刪除任何音調標記

| 文本 | mark    | number    | strip   |
| ---- | ------- | --------- | ------- |
| 台灣 | Tâi-uân | Tai5-uan5 | Tai-uan |

#### Delimiter

`delimiter` String - 設定放置在單詞音節之間的分隔符。

預設值取決於所選的 `system`:

* `'-'` - 對於 `Tailo`, `POJ`, `Tongiong`
* `''` - 對於 `Pingyim`
* `' '` - 對於 `Zhuyin`, `TLPA`, `IPA`

| 文本 | '-'     | ''     | ' '     |
| ---- | ------- | ------ | ------- |
| 台灣 | Tâi-uân | Tâiuân | Tâi uân |

#### Sandhi

`sandhi` String - 應用[臺灣話變調規則][sandhi-wiki]。

由於編碼所有變調規則困難，Taibun 提供多種模式變調轉換以支援自訂變調處理。

* `none` - 不執行任何變調
* `auto` - 最接近臺灣話的正確音調變音，包括代詞、後綴和帶有「仔」詞的音調變音
* `exc_last` - 除了最後一個音節之外，每個音節都變調
* `incl_last` - 包括最後一個音節在內，每個音節都變調

預設值取決於所選的 `system`:

* `auto` - 對於 `Tongiong`
* `none` - 對於 `Tailo`, `POJ`, `Zhuyin`, `TLPA`, `Pingyim`, `IPA`

| 文本             | none                    | auto                   | exc_last               | incl_last              |
| ---------------- | ----------------------- | ---------------------- | ---------------------- | ---------------------- |
| 這是你的茶桌仔無 | Tse sī lí ê tê-toh-á bô | Tse sì li ē tē-to-á bô | Tsē sì li ē tē-tó-a bô | Tsē sì li ē tē-tó-a bō |

變調規則也會根據所選擇的方言而變化。

| 文本 | 沒有變調 | south   | north / singapore |
| ---- | -------- | ------- | ----------------- |
| 台灣 | Tâi-uân  | Tāi-uân | Tài-uân           |

#### Punctuation

`punctuation` String

* `format` (預設) - 將中文標點符號轉換為英文標點符號，並將每個句子開頭的單詞大寫
* `none` - 保留中文風格的標點符號，並且新句子開頭的單詞不大寫

| 文本                                                                           | format                                                                                            | none                                                                                                 |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。 | Tse sī Tâi-lâm, kán-tshing "lâm" (Pe̍h-uē-jī: Tâi-lâm; tsù-im hû-hō: ㄊㄞˊ ㄋㄢˊ, kok-gí: Táinán). | tse sī Tâi-lâm，kán-tshing「lâm」（Pe̍h-uē-jī：Tâi-lâm；tsù-im hû-hō：ㄊㄞˊ ㄋㄢˊ，kok-gí：Táinán）。 |

#### Convert non-CJK

`convert_non_cjk` Boolean - 定義是否轉換非中文單詞。可用於將臺羅拼音轉換為其他羅馬拼音系統。

* `True` - 轉換非中文字詞
* `False` (預設) - 僅轉換中文字詞

| 文本      | False                   | True                    |
| --------- | ----------------------- | ----------------------- |
| 我食pháng | ㆣㄨㄚˋ ㄐㄧㄚㆷ˙ pháng | ㆣㄨㄚˋ ㄐㄧㄚㆷ˙ ㄆㄤˋ |

### Tokeniser

`Tokeniser` 類別對臺灣話句子執行類似 [NLTK wordpunct_tokenize][nltk-tokenize] 的標記化。

```python
# 建構子
t = Tokeniser(keep_original)

# 標記臺灣語句
t.tokenise(input)
```

#### Keep original

`keep_original` Boolean - 定義是否保留輸入的原始字符。

* `True` (預設) - 保留原始字符
* `False` - 使用資料集中定義的字符替換原始字符

| 文本         | True                 | False                |
| ------------ | -------------------- | -------------------- |
| 臺灣火鸡肉饭 | ['臺灣', '火鸡肉饭'] | ['台灣', '火雞肉飯'] |

### 其他函式

實用的臺灣話 NLP 助手函式。

`to_traditional` 函式將輸入轉換為繁體字元以便於資料集使用。也可應對繁體字符變體。

`to_simplified` 函式將輸入轉換為簡體字元。

`is_cjk` 函式檢查輸入字串是否完全由中文字符組成。

```python
to_traditional(input)

to_simplified(input)

is_cjk(input)
```



<!-- EXAMPLE -->
## 例子

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

c = new Converter({ dialect: 'singapore' });
c.get("我欲用箸食魚");
>> Uá bueh ēng tū tsia̍h hû

## Format
c = Converter() # 在 Tailo 中，format 預設值: mark
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
c = Converter() # 在 Tailo 中，sandhi 預設值: none
c.get("這是你的茶桌仔無")
>> Tse sī lí ê tê-toh-á bô

c = Converter(sandhi='auto')
c.get("這是你的茶桌仔無")
>> Tse sì li ē tē-to-á bô

c = Converter(sandhi='exc_last')
c.get("這是你的茶桌仔無")
>> Tsē sì li ē tē-tó-a bô

c = Converter(sandhi='incl_last')
c.get("這是你的茶桌仔無")
>> Tsē sì li ē tē-tó-a bō

## Punctuation
c = Converter() # punctuation 預設值: format
c.get("太空朋友，恁好！恁食飽未？")
>> Thài-khong pîng-iú, lín-hó! Lín tsia̍h-pá buē?

c = Converter(punctuation='none')
c.get("太空朋友，恁好！恁食飽未？")
>> thài-khong pîng-iú，lín-hó！lín tsia̍h-pá buē？

## Convert non-CJK
c = Converter(system='Zhuyin') # convert_non_cjk 預設值: False
c.get("我食pháng")
>> ㆣㄨㄚˋ ㄐㄧㄚㆷ˙ pháng

c = Converter(system='Zhuyin', convert_non_cjk=True)
c.get("我食pháng")
>> ㆣㄨㄚˋ ㄐㄧㄚㆷ˙ ㄆㄤˋ


# Tokeniser
from taibun import Tokeniser

t = Tokeniser()
t.tokenise("太空朋友，恁好！恁食飽未？")
>> ['太空', '朋友', '，', '恁好', '！', '恁', '食飽', '未', '？']

## Keep Original
t = Tokeniser() # keep_original 預設值: True
t.tokenise("爲啥物臺灣遮爾好？")
>> ['爲啥物', '臺灣', '遮爾', '好', '？']

t.tokenise("为啥物台湾遮尔好？")
>> ['为啥物', '台湾', '遮尔', '好', '？']

t = Tokeniser(False)
t.tokenise("爲啥物臺灣遮爾好？")
>> ['為啥物', '台灣', '遮爾', '好', '？']

t.tokenise("为啥物台湾遮尔好？")
>> ['為啥物', '台灣', '遮爾', '好', '？']


# 其他函式
from taibun import to_traditional, to_simplified, is_cjk

## to_traditional
to_traditional("我听无台语")
>> 我聽無台語

to_traditional("我爱这个个人台面")
>> 我愛這个個人檯面

to_traditional("爲啥物")
>> 為啥物

## to_simplified
to_simplified("我聽無台語")
>> 我听无台语

## is_cjk
is_cjk('我食麭')
>> True

is_cjk('我食pháng')
>> False
```



<!-- DATA -->
## 數據

- [台華線上對照典][online-dictionary] (藉由 [ChhoeTaigi][data-via])
- [iTaigi華台對照典][itaigi-dictionary] (藉由 [ChhoeTaigi][data-via])



<!-- ACKNOWLEDGEMENTS -->
## 致謝

- 任全恩 ([Github][samuel-github] · [LinkedIn][samuel-linkedin]) - 臺灣話和國語翻譯



<!-- LICENCE -->
## 執照

因為 Taibun 是 MIT 許可的，所以任何開發人員基本上都可以用它做任何他們想做的事情，只要他們在源代碼的任何副本中包含原始版權和許可聲明。 請注意，該包使用的數據已獲得不同版權的許可。

數據已獲得 [CC BY-SA 4.0][data-cc] 許可



<!-- MARKDOWN LINKS -->
[contributions]: https://github.com/andreihar/taibun/issues
[contributions-badge]: https://img.shields.io/badge/歡迎-貢獻協助-be132d?style=for-the-badge&logo=github
[demo]: https://taibun.andreihar.com/
[demo-badge]: https://img.shields.io/badge/現場演示-222222?style=for-the-badge&logo=homeadvisor&logoColor=white
[tests]: https://github.com/andreihar/taibun/actions
[tests-badge]: https://img.shields.io/github/actions/workflow/status/andreihar/taibun/ci.yaml?style=for-the-badge&logo=github-actions&logoColor=ffffff&label=構建
[release-badge]: https://img.shields.io/github/v/release/andreihar/taibun?color=38618c&style=for-the-badge&label=發布
[release]: https://github.com/andreihar/taibun/releases
[licence-badge]: https://img.shields.io/github/license/andreihar/taibun?color=000000&style=for-the-badge&label=執照
[licence]: ../LICENSE
[linkedin-badge]: https://img.shields.io/badge/LinkedIn-0077b5?style=for-the-badge&logo=linkedin&logoColor=ffffff
[linkedin]: https://www.linkedin.com/in/andreihar/
[js-badge]: https://img.shields.io/badge/JS_版本-f7df1e?style=for-the-badge&logo=javascript&logoColor=000000
[js-link]: https://github.com/andreihar/taibun.js
[downloads-badge]: https://img.shields.io/pypi/dm/taibun.svg?style=for-the-badge&label=下載

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
[singapore-wiki]: https://zh.wikipedia.org/wiki/%E6%96%B0%E5%8A%A0%E5%9D%A1%E7%A6%8F%E5%BB%BA%E8%A9%B1
[nltk-tokenize]: https://nltk.org/api/nltk.tokenize.html
[sandhi-wiki]: https://zh.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3%E8%A9%B1#%E9%80%A3%E8%AE%80%E8%AE%8A%E8%AA%BF:~:text=%E3%80%82%5B144%5D-,%E9%80%A3%E8%AE%80%E8%AE%8A%E8%AA%BF,-%E9%80%A3%E8%AE%80%E8%AE%8A%E8%AA%BF