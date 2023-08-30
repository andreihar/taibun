from taibun.taibun import Converter

def test_hanji_to_tlpa():
    hanji = "先生講、學生恬恬聽。"
    expected = "Sian1 sinn1 kong2, hak8 sing1 tiam7 tiam7 thiann1."
    c = Converter(system="TLPA")
    result = c.get(hanji)
    assert result == expected