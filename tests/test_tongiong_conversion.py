from taibun.taibun import Converter

def test_hanji_to_tongiong():
    hanji = "先生講、學生恬恬聽。"
    expected = "Siān-sinn gòng, hāk-sing diâm-diām tiann."
    c = Converter(system="Tongiong")
    result = c.get(hanji)
    assert result == expected