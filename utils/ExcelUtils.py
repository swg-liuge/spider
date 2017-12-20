import xlwt


def write_lines(file_name, lines=list(), sheet="sheet1"):
    """
    写Excel文件 lines类二维数组
    :param file_name:
    :param lines:
    :param sheet:
    :return:
    """
    file = xlwt.Workbook(encoding="utf-8")
    table = file.add_sheet(sheet, cell_overwrite_ok=True)
    for line in lines:
        i = 0
        cols = len(line)
        for j in range(0, cols):
            table.write(i, j, line[j])
        i += 1
    file.save(file_name + ".xls")
