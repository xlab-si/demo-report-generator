import argparse
import getpass
import sys

import openpyxl

from report.db import Database
from report.pdf import Pdf

"""
Main module (command-line program).
"""


class ArgParser(argparse.ArgumentParser):
    """
    Argument parser that displays help on error
    """
    def error(self, message):
        self.print_help()
        sys.stderr.write("error: {}\n".format(message))
        sys.exit(2)


def _parse_arguments():
    parser = ArgParser(
        description="Demo report generator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("host", help="Database host IP address")
    parser.add_argument("port", help="Database host port")
    parser.add_argument("user", help="Database user")
    parser.add_argument("dbname", help="Database name")
    args = parser.parse_args()
    args.password = getpass.getpass()
    return args


def main():
    args = _parse_arguments()

    # Database access
    db = Database(args.host, args.port, args.user, args.password, args.dbname)
    result = db.execute("select * from store")
    print(result)

    # Excel writing
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Data"
    titles = "store_id", "manager_staff_id", "address_id", "last_update"
    for i, t in enumerate(titles, 1):
        ws.cell(1, i, t)
    for i, row in enumerate(result, 2):
        for j, val in enumerate(row, 1):
            ws.cell(i, j, val)
    wb.save("sample.xlsx")

    # PDF generation
    pdf = Pdf("test.pdf")
    pdf.set_store_address(("Store A", "My road 3", "another line", "City"))

    rows = (
        ("c1", "c2", "c3"),
        ("v1", "v2", "v3"),
    )
    sizes = 20, 30, 10
    pdf.add_table(rows, sizes)
    pdf.add_paragraph("Long text should this be but there is just no time.")

    labels = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug")
    data = [
        (   13,     5,    20,    22,    37,    45,    19,     4),
        (    5,    20,    46,    38,    23,    21,     6,    14),
    ]
    pdf.add_line_chart(140, 70, labels, data)
    pdf.add_paragraph("Long text should this be but there is just no time.")

    pdf.add_pie_chart(80, 80, labels, data[0])
    pdf.add_pie_chart(80, 80, labels, data[1], side_labels=True)
    pdf.add_paragraph("Long text should this be but there is just no time.")

    pdf.save()
    return 0
