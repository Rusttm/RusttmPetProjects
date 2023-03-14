
import reports_from_PDF


def FinReport():
    report = []
    my_data = reports_from_PDF.GetInfoFromAllPDF()
    years = my_data.keys()

    line = ["Расчет показателей"]
    for year in years:
        line.append(year)
    line.append("Норматив")
    report.append(line)

    line = ["Показатели эффективности"]
    report.append(line)

    line = ["Коэффициент рентабельности продаж"]
    for year in years:
        coef = round(my_data[year]['2200'][0]/my_data[year]['2110'][0], 3)
        line.append(coef)
    report.append(line)

    line = ["Коэффициент валовой прибыли"]
    for year in years:
        coef = round(my_data[year]['2100'][0] / my_data[year]['2110'][0], 3)
        line.append(coef)
    report.append(line)

    return report


if __name__ == '__main__':
    print(FinReport())
