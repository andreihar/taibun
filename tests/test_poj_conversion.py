from taibun.taibun import Converter
from utils import checker

def test_hanji_to_poj():
    hanji = "先生講、學生恬恬聽。"
    conversion = ["先生講,sian-siⁿ kóng","學生恬恬聽,ha̍k-seng tiām-tiām thiaⁿ","太空朋友,thài-khong pêng-iú","恁好,lín-hó","恁食飽未,lín chia̍h-pá bōe","有閒,ū-êng","就來阮遮坐喔,tō lâi goán chia chē--o͘h"]
    c = Converter(system="POJ", punctuation='none')
    c_north = Converter(system="POJ", dialect="north", punctuation='none')
    checker(conversion, c, c_north)