from taibun.taibun import Converter

def test_hanji_to_pingyim():
    hanji = "先生講、學生恬恬聽。"
    expected = "Siānsnī gǒng, hágsīng diâmdiâm tinā."
    c = Converter(system="Pingyim")
    result = c.get(hanji)
    assert result == expected