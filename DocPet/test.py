# coding="utf-8"
import xlsxwriter

my_data = [['Расчет показателей', '2020', '2021', '2022', 'Норматив'], ['Показатели эффективности'], ['Коэффициент рентабельности продаж', 0.017, 0.032, 0.054], ['Коэффициент валовой прибыли', 0.02, 0.032, 0.054], ['Коэффициент рентабельности операционной прибыли', 0.0, 0.013, 0.034], ['Коэффициент рентабельности активов', 0.0, 0.004, 0.006], ['Показатели платежеспособности', '2020', '2021', '2022', 'Норматив'], ['Коэффициент текущей ликвидности', 1.039, 1.045, 1.069, 2], ['Коэффициент срочной ликвидности', 0.313, 0.302, 0.288, 1], ['Коэффициент абсолютной ликвидности', 0.041, 0.008, 0.005, 0.5], ['Коэффициенты финансовой устойчивости', '2020', '2021', '2022', 'Норматив'], ['Коэффициент задолженности', 0.959, 0.953, 0.935, '<0.5'], ['Коэффициент Финансового левереджа', 23.514, 20.495, 14.291, '<1.3'], ['Коэффициент финансовой устойчивости', 0.041, 0.047, 0.065, '>0.6'], ['Коэффициенты деловой активности', '2020', '2021', '2022', 'Норматив'], ['Коэффициент оборачиваемости активов', 0.267, 0.402, 0.226], ['Период сбора дебиторской задолженности', 83.631, 61.827, 108.302], ['Период хранения запасов', -239.178, -186.376, -328.089], ['Период погашения кредиторской задолженности', -0.014, -3.027, -3.126], ['Финансовый цикл', -216.661, -216.661, -216.661], ['Коэффициенты рыночных показателей', '2020', '2021', '2022', 'Норматив'], ['Рентабельность собственного капитала', 0.01, 0.313, 0.358], ['Мультипликатор собственного капитала', 24.514, 21.495, 15.291], ['Рентабельность собственного капитала', 0.012, 0.012, 0.012]]

with xlsxwriter.Workbook('data/test.xlsx', encoding="utf-8") as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(my_data):
        worksheet.write_row(row_num, 0, data)