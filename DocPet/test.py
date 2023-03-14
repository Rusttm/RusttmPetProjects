import xlsxwriter

my_data = [['Расчет показателей', '2020', '2021', '2022', 'Норматив'], ['Показатели эффективности'], ['Коэффициент рентабельности продаж', 0.017, 0.032, 0.054], ['Коэффициент валовой прибыли', 0.02, 0.032, 0.054]]

with xlsxwriter.Workbook('data/test.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(my_data):
        worksheet.write_row(row_num, 0, data)