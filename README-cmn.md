[台語](README-oan.md) | [English](README.md)



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
          </ul>
        </li>
        <li><a href="#tokeniser">Tokeniser</a></li>
      </ul>
    </li>
    <li><a href="#例子">例子</a></li>
    <li><a href="#數據">數據</a></li>
    <li><a href="#執照">執照</a></li>
  </ol>
</details>



<!-- INSTALL -->
## 安裝

Taibun 可以通過 [pypi][pypi] 安裝

```bash
$ pip install taibun
```



<!-- USAGE -->
## 用法

### Converter

`Converter` 類別使用開發人員指定的參數將漢字音譯為所選的音譯系統。適用於繁體和簡體字符。

```python
# 建構子
c = Converter(system, dialect, format, delimiter, sandhi, punctuation)

# 音譯漢字
c.get(input)

# 將簡體中文字符轉換為繁體中文字符
c.to_traditional(input)
```

#### System

`system` String - 音譯系統。

* `Tailo` (預設) - [臺灣羅馬字拼音方案][tailo-wiki]
* `POJ` - [白話字][poj-wiki]
* `Zhuyin` - [臺語方音符號][zhuyin-wiki]
* `TLPA` - [臺灣語言音標方案][tlpa-wiki]
* `Pingyim` - [閩南話拼音方案][pingyim-wiki]
* `Tongiong` - [臺語通用拼音][tongiong-wiki]

| 文本 | Tailo   | POJ     | Zhuyin      | TLPA      | Pingyim | Tongiong |
|------|---------|---------|-------------|-----------|---------|----------|
| 臺灣 | Tâi-uân | Tâi-oân | ㄉㄞˊ ㄨㄢˊ | Tai5 uan5 | Dáiwán  | Tāi-uǎn  |

#### Dialect

`dialect` String - 首選發音。

* `south` (預設) - 發音更接近[漳州話][zhangzhou-wiki]
* `north` - 發音更接近[泉州話][quanzhou-wiki]

| 文本   | south         | north         |
|--------|---------------|---------------|
| 五月節 | Gōo-gue̍h-tseh | Gōo-ge̍h-tsueh |

#### Format

`format` String - 轉換後的句子中表示聲調的格式。

* `mark` (預設) - 每個音節都使用變音符號。不支持拼音
* `number` - 添加一個代表音節末尾聲調的數字
* `strip` - 刪除任何音調標記

| 文本 | mark    | number    | strip   |
|------|---------|-----------|---------|
| 臺灣 | Tâi-uân | Tai5-uan5 | Tai-uan |

#### Delimiter

`delimiter` String - 設定放置在單詞音節之間的分隔符。

預設值取決於所選的 `system`:

* `'-'` - 對於 `Tailo`, `POJ`, `Tongiong`
* `''` - 對於 `Pingyim`
* `' '` - 對於 `Zhuyin`, `TLPA`

| 文本 | '-'     | ''     | ' '     |
|------|---------|--------|---------|
| 臺灣 | Tâi-uân | Tâiuân | Tâi uân |

#### Sandhi

`sandhi` Boolean - 將[臺灣話變調規則][sandhi-wiki]應用於單個單詞的音節。

預設值取決於所選的 `system`:

* `True` - 對於 `Tongiong`
* `False` - 對於 `Tailo`, `POJ`, `Zhuyin`, `TLPA`, `Pingyim`

| 文本     | False        | True         |
|----------|--------------|--------------|
| 馬來西亞 | Má-lâi-se-a  | Ma-lāi-sē-a  |

變調規則也會根據所選擇的方言而變化。

| 文本 | 沒有變速 | south   | north   |
|------|---------|---------|---------|
| 臺灣 | Tâi-uân | Tāi-uân | Tài-uân |

請注意，該功能與真正的變調規則不同，真正的中文的變化適用於句子的每個音節，而不僅僅是單個單詞。

- **Taibun 的變調規則**: Thái-khong pīng-iú, lin-hó! Lín tsià-pá buē?
- **實際變調規則**: Thái-khōng pīng-iú, lin-hó! Lin tsià-pa buē?

#### Punctuation

`punctuation` String

* `format` (預設) - 將中文標點符號轉換為英文標點符號，並將每個句子開頭的單詞大寫
* `none` - 保留中文風格的標點符號，並且新句子開頭的單詞不大寫

| 文本 | format | none |
|-|-|-|
| 這是臺南，簡稱「南」（白話字：Tâi-lâm；注音符號：ㄊㄞˊ ㄋㄢˊ，國語：Táinán）。 | Tse sī Tâi-lâm, kán-tshing "lâm" (Pe̍h-uē-jī: Tâi-lâm; tsù-im hû-hō: ㄊㄞˊ ㄋㄢˊ, kok-gí: Táinán). | tse sī Tâi-lâm，kán-tshing「lâm」（Pe̍h-uē-jī：Tâi-lâm；tsù-im hû-hō：ㄊㄞˊ ㄋㄢˊ，kok-gí：Táinán）。 |

### Tokeniser

`Tokeniser` 類別對臺灣話句子執行類似 [NLTK wordpunct_tokenize][nltk-tokenize] 的標記化。

```python
# 建構子
t = Tokeniser()

# 標記臺灣語句
t.tokenise(input)
```



<!-- EXAMPLE -->
## 例子

```python
from taibun import Converter, Tokeniser

# System
c = Converter() # system 預設值: Tailo
c.get('先生講，學生恬恬聽。')
>> Sian-sinn kóng, ha̍k-sing tiām-tiām thiann.

c = Converter(system='Zhuyin')
c.get('先生講，學生恬恬聽。')
>> ㄒㄧㄢ ㄒㆪ ㄍㆲˋ, ㄏㄚㆶ˙ ㄒㄧㄥ ㄉㄧㆰ˫ ㄉㄧㆰ˫ ㄊㄧㆩ.

# Dialect
c = Converter() # dialect 預設值: south
c.get("我欲用箸食魚")
>> Guá beh īng tī tsia̍h hî

c = Converter(dialect='north')
c.get("我欲用箸食魚")
>> Guá bueh īng tū tsia̍h hû

# Format
c = Converter() # 在 Tailo 中，format 預設值: mark
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
c = Converter() # 在 Tailo 中，sandhi 預設值: False
c.get("南迴鐵路")
>> Lâm-huê-thih-lōo

c = Converter(sandhi=True)
c.get("南迴鐵路")
>> Lām-huē-thí-lōo

# Punctuation
c = Converter() # punctuation 預設值: foramt
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
[tests]: https://github.com/andreihar/taibun/actions
[tests-badge]: https://img.shields.io/github/actions/workflow/status/andreihar/taibun/ci.yaml?style=for-the-badge&logo=github&label=構建
[contributors-badge]: https://img.shields.io/github/contributors/andreihar/taibun?style=for-the-badge&label=貢獻者
[contributors]: #usage
[release-badge]: https://img.shields.io/github/v/release/andreihar/taibun?color=38618c&style=for-the-badge&label=發布
[release]: https://github.com/andreihar/taibun/releases
[licence-badge]: https://img.shields.io/github/license/andreihar/taibun?color=000000&style=for-the-badge&label=執照
[licence]: LICENSE
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
[zhangzhou-wiki]: https://zh.wikipedia.org/zh-tw/%E6%BC%B3%E5%B7%9E%E8%AF%9D
[quanzhou-wiki]: https://zh.wikipedia.org/zh-tw/%E6%B3%89%E5%B7%9E%E8%AF%9D
[nltk-tokenize]: https://nltk.org/api/nltk.tokenize.html
[sandhi-wiki]: https://zh.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3%E8%A9%B1#%E9%80%A3%E8%AE%80%E8%AE%8A%E8%AA%BF:~:text=%E3%80%82%5B144%5D-,%E9%80%A3%E8%AE%80%E8%AE%8A%E8%AA%BF,-%E9%80%A3%E8%AE%80%E8%AE%8A%E8%AA%BF