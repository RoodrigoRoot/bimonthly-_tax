import csv
class Reports:
    @classmethod
    def generate_Report(cls):
        doc = open("archivoW.csv", "w")
        doc_csv_w=csv.writer(doc)
        lista = [["Pedro", 9999], ["Uno", 1000],["Dos", 2000],["Tres", 3000],["Cuatro", 4000]]
        doc_csv_w.writerows(lista)
        doc.close()

