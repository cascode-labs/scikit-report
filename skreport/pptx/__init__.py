import os
from typing import Union
from skreport.models.ReportModel import ReportModel
from skreport.pptx.PptxReportView import PptxReportView

def export_pptx(report_model: ReportModel, path: Union[str, os.PathLike]):
   report_view = PptxReportView()
   report_view.export(report_model, path)
