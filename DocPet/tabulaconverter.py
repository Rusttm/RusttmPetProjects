# Import the required Module
import tabula
import xlsxwriter
# Read a PDF File
# print(tabula.environment_info())
df = tabula.read_pdf("data/2020.pdf", pages='all')[0]
# convert PDF into CSV
# tabula.convert_into("IPLmatch.pdf", "iplmatch.csv", output_format="csv", pages='all')
print(df)
