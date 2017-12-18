import xlwt


def write(file_name, lines, sheet="sheet1"):
    file = xlwt.Workbook(encoding="utf-8")
    table = file.add_sheet(sheet, cell_overwrite_ok=True)

    pass