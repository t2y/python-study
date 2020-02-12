from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side, Font

wb = Workbook()
ws = wb.active

navy_colored_font = Font(name='ＭＳ Ｐ明朝', size=20, color='000080')

a1 = ws['A1']
a1.value = 'フォントを変える'
a1.font = navy_colored_font

salmon_colored_fill = PatternFill('solid', fgColor='FA8072')

a2 = ws['A2']
a2.value = '背景色を変える'
a2.fill = salmon_colored_fill

red_colored_thin = Side(style='thin', color='ff0000')
blue_colored_double = Side(style='double', color='0000ff')
border = Border(
    left=red_colored_thin, right=red_colored_thin,        #←左右は赤の罫線を使う
    top=blue_colored_double, bottom=blue_colored_double,        #←上下は青の二重罫線を使う
)

b4 = ws['B4']
b4.value = '罫線で囲む'
b4.border = border

ws.title = 'セルとスタイル'
wb.save('write_cell_with_style.xlsx')
