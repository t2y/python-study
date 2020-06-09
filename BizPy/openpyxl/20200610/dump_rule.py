import sys
from openpyxl import load_workbook
from pprint import pprint

rule_method = {        #←type属性とメソッド名の変換テーブル
    'cellIs': 'CellIsRule',
    'colorScale': 'ColorScaleRule',
    'dataBar': 'DataBarRule',
    'expression': 'FormulaRule',
    'iconSet': 'IconSetRule',
}

if len(sys.argv) < 2:
    print(f'{__file__}の後に条件付き書式設定をもつExcelファイルを指定してください')
    sys.exit(0)

filename = sys.argv[1]
wb = load_workbook(filename)
ws = wb.active
for cond in ws.conditional_formatting:        #←条件付き書式の設定を繰り返し処理
    for rule in cond.rules:
        rule_method_name = rule_method.get(rule.type)        #←ルールメソッド名を変換
        if rule_method_name is None:
            continue

        print(f'#' * 32)
        print(f'セルの範囲: {cond.cells}')
        print(f'ルールメソッド: {rule_method_name}')
        print(f'パラメーター:')
        pprint(vars(rule))        #←ruleオブジェクトの属性を表示
