from reportlab import platypus
from reportlab.lib import styles
from reportlab.lib.units import mm

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie

"""
Module with PDF generator code.
"""


class Pdf(object):
    PARAGRAPH_STYLE = styles.ParagraphStyle(
        "default", fontSize=12, leading=13
    )

    def __init__(self, filename):
        frame = platypus.Frame(
            20 * mm,  20 * mm,  170 * mm, 227 * mm, showBoundary=0,
            topPadding=0, bottomPadding=0, leftPadding=0, rightPadding=0
        )
        page = platypus.PageTemplate("main", frames=[frame],
                                     onPage=self._decorate_page)
        self.doc = platypus.BaseDocTemplate(filename, pageTemplates=[page])
        self.story = []
        self.address = None

    def _decorate_page(self, canvas, document):
        text = canvas.beginText(20 * mm, 277 * mm)
        for line in self.address:
            text.textLine(line)
        canvas.drawText(text)

    def set_store_address(self, address_lines):
        self.address = address_lines

    def add_table(self, rows, column_sizes, style=[]):
        real_style = platypus.TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.8, (0, 0, 0)),
            ("BACKGROUND", (0, 0), (-1, 0), (0.8471, 0.8941, 0.7373)),
        ] + style)
        sizes = [s * mm for s in column_sizes]
        self.story.extend([
            platypus.Spacer(1, 3 * mm),
            platypus.Table(rows, colWidths=sizes, style=real_style),
            platypus.Spacer(1, 3 * mm),
        ])

    @staticmethod
    def _find_min_max(data):
        _min, _max = data[0][0], data[0][0]
        for d in data:
            tmp_min = min(d)
            tmp_max = max(d)
            _min = _min if _min < tmp_min else tmp_min
            _max = _max if _max > tmp_max else tmp_max
        return _min, _max

    def add_line_chart(self, width, height, labels, data, minv=None, maxv=None):
        pad = 10

        _min, _max = self._find_min_max(data)
        minv = _min if minv is None else minv
        maxv = _max if maxv is None else maxv

        lc = HorizontalLineChart()
        lc.x = pad * mm
        lc.y = pad * mm
        lc.width = (width - 2 * pad) * mm
        lc.height = (height - 2 * pad) * mm

        lc.categoryAxis.categoryNames = labels
        lc.data = data
        lc.valueAxis.valueMin = minv
        lc.valueAxis.valueMax = maxv

        lc.joinedLines = 1
        lc.categoryAxis.labels.boxAnchor = "n"
        lc.lines.strokeWidth = 2

        drawing = Drawing(width * mm, height * mm)
        drawing.hAlign = "CENTER"
        drawing.add(lc)
        self.story.append(drawing)

    def add_pie_chart(self, width, height, labels, data, side_labels=False):
        pad = 15

        pc = Pie()
        pc.x = pad * mm
        pc.y = pad * mm
        pc.width = (width - 2 * pad) * mm
        pc.height = (height - 2 * pad) * mm

        pc.labels = labels
        pc.data = data
        pc.sideLabels = side_labels

        drawing = Drawing(width * mm, height * mm)
        drawing.hAlign = "CENTER"
        drawing.add(pc)
        self.story.append(drawing)

    def add_bar_chart(self, width, height, labels, data, minv=None, maxv=None):
        pad = 10

        _min, _max = self._find_min_max(data)
        minv = _min if minv is None else minv
        maxv = _max if maxv is None else maxv

        bc = VerticalBarChart()
        bc.x = pad * mm
        bc.y = pad * mm
        bc.width = (width - 2 * pad) * mm
        bc.height = (height - 2 * pad) * mm

        bc.categoryAxis.categoryNames = labels
        bc.data = data
        bc.valueAxis.valueMin = minv
        bc.valueAxis.valueMax = maxv

        drawing = Drawing(width * mm, height * mm)
        drawing.hAlign = "CENTER"
        drawing.add(bc)
        self.story.append(drawing)

    def add_paragraph(self, text):
        self.story.append(platypus.Paragraph(text, self.PARAGRAPH_STYLE))

    def new_page(self):
        self.story.append(platypus.PageBreak())

    def save(self):
        assert self.address is not None, \
            "Use #set_store_address to set address"
        self.doc.build(self.story)
