# coding=utf8
import reports_from_PDF
import xlsxwriter

class FinReportsFile():
    def __init__(self, file_name='fin_report'):
        print(' Не забудьте добавить в папку data годовые отчеты в формате pdf')
        self.acc_reports_data = []
        self.fin_report_data = []
        self.fin_report_formatted = []
        self.acc_data_formatted = []
        self.file_name = f'{file_name}.xlsx'

    def PrepareFinReport(self):
        self.acc_reports_data = reports_from_PDF.GetInfoFromAllPDF()
        print(self.acc_reports_data)
        self.fin_report_formatted = self.FormattingFinReport()
        self.acc_data_formatted = self.FormattingAccData()
    def FormattingFinReport(self):
        report = []
        my_data = self.acc_reports_data
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
            crp = round(my_data[year]['2200'][0]/my_data[year]['2110'][0], 3)
            line.append(crp)
        report.append(line)

        line = ["Коэффициент валовой прибыли"]
        for year in years:
            coef = round(my_data[year]['2100'][0] / my_data[year]['2110'][0], 3)
            line.append(coef)
        report.append(line)

        line = ["Коэффициент рентабельности операционной прибыли"]
        for year in years:
            coef = round(my_data[year]['2300'][0] / my_data[year]['2110'][0], 3)
            line.append(coef)
        report.append(line)

        line = ["Коэффициент рентабельности активов"]
        for year in years:
            coef = round((my_data[year]['2400'][0] / (my_data[year]['1600'][0] + my_data[year]['1600'][1])) / 2, 3)
            line.append(coef)
        report.append(line)

        line = ["Показатели платежеспособности"]
        for year in years:
            line.append(year)
        line.append("Норматив")
        report.append(line)

        line = ["Коэффициент текущей ликвидности"]
        for year in years:
            coef = round(my_data[year]['1200'][0] / my_data[year]['1500'][0], 3)
            line.append(coef)
        line.append(2)
        report.append(line)

        line = ["Коэффициент срочной ликвидности"]
        for year in years:
            coef = round((my_data[year]['1200'][0] - my_data[year]['1210'][0]) / my_data[year]['1500'][0], 3)
            line.append(coef)
        line.append(1)
        report.append(line)

        line = ["Коэффициент абсолютной ликвидности"]
        for year in years:
            coef = round((my_data[year]['1250'][0] - my_data[year]['1240'][0]) / my_data[year]['1500'][0], 3)
            line.append(coef)
        line.append(0.5)
        report.append(line)

        line = ["Коэффициенты финансовой устойчивости"]
        for year in years:
            line.append(year)
        line.append("Норматив")
        report.append(line)

        line = ["Коэффициент задолженности"]
        for year in years:
            coef = round((my_data[year]['1400'][0] + my_data[year]['1500'][0]) / my_data[year]['1600'][0], 3)
            line.append(coef)
        line.append("<0.5")
        report.append(line)

        line = ["Коэффициент Финансового левереджа"]
        for year in years:
            coef = round((my_data[year]['1400'][0] + my_data[year]['1500'][0]) / my_data[year]['1300'][0], 3)
            line.append(coef)
        line.append("<1.3")
        report.append(line)

        line = ["Коэффициент финансовой устойчивости"]
        for year in years:
            coef = round((my_data[year]['1400'][0] + my_data[year]['1300'][0]) / my_data[year]['1600'][0], 3)
            line.append(coef)
        line.append(">0.6")
        report.append(line)

        line = ["Коэффициенты деловой активности"]
        for year in years:
            line.append(year)
        line.append("Норматив")
        report.append(line)

        line = ["Коэффициент оборачиваемости активов"]
        for year in years:
            coa = round((my_data[year]['2110'][0] / (my_data[year]['1600'][0] + my_data[year]['1600'][1])) / 2, 3)
            line.append(coa)
        report.append(line)

        line = ["Период сбора дебиторской задолженности"]
        for year in years:
            coef_x = round(365 * my_data[year]['1230'][0] / my_data[year]['2110'][0], 3)
            line.append(coef_x)
        report.append(line)

        line = ["Период хранения запасов"]
        for year in years:
            coef_y = round(365 * my_data[year]['1210'][0] / my_data[year]['2120'][0], 3)
            line.append(coef_y)
        report.append(line)

        line = ["Период погашения кредиторской задолженности"]
        for year in years:
            coef_z = round(365 * my_data[year]['1520'][0] / my_data[year]['2120'][0], 3)
            line.append(coef_z)
        report.append(line)

        line = ["Финансовый цикл"]
        for year in years:
            coef = round(coef_x + coef_y - coef_z, 3)
            line.append(coef)
        report.append(line)

        line = ["Коэффициенты рыночных показателей"]
        for year in years:
            line.append(year)
        line.append("Норматив")
        report.append(line)

        line = ["Рентабельность собственного капитала"]
        for year in years:
            coef = round(my_data[year]['2400'][0] / my_data[year]['1300'][0], 3)
            line.append(coef)
        report.append(line)

        line = ["Мультипликатор собственного капитала"]
        for year in years:
            coefsk = round(my_data[year]['1600'][0] / my_data[year]['1300'][0], 3)
            line.append(coefsk)
        report.append(line)

        line = ["Рентабельность собственного капитала"]
        for year in years:
            coef = round(coa*crp*coefsk, 3)
            line.append(coef)
        report.append(line)
        return report


    def FormattingAccData(self):
        report = []
        codes = set()
        my_data = self.acc_reports_data
        years = my_data.keys()

        line = ["код показателя"]
        for year in years:
            line.append(year)
            for code in my_data[year].keys():
                int_code = int(code)
                codes.add(int_code)
        report.append(line)

        sorted_codes = list(codes)
        sorted_codes.sort()
        # print(f"{type(sorted_codes)}:{sorted_codes=}")
        for cod in sorted_codes:
            line = [cod]
            for year in years:
                value = my_data[year].get(str(cod), [None])
                line.append(value[0])
            report.append(line)

        return report

    def WriteFile(self):
        self.PrepareFinReport()
        try:
            with xlsxwriter.Workbook(f'data/{self.file_name}') as workbook:
                worksheet = workbook.add_worksheet('Report')
                for row_num, data in enumerate(self.fin_report_formatted):
                    worksheet.write_row(row_num, 0, data)
                worksheet = workbook.add_worksheet('DataReport')
                for row_num, data in enumerate(self.acc_data_formatted):
                    worksheet.write_row(row_num, 0, data)

            print(f"Файл data/{self.file_name} записан успешно")
        except Exception as e:
            print(e)


def DataReport():
    pass

if __name__ == '__main__':
    new_file = FinReportsFile('7')
    new_file.WriteFile()

