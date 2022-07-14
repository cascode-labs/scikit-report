import os
from typing import Union
from skreport.models.ReportModel import ReportModel
from skreport.pptx.PptxReportView import PptxReportView
from skreport.pptx.content_views.TextContentView import TextContentView
from skreport.pptx.content_views.BulletedListContentView import BulletedListContentView
from skreport.pptx.content_views.PictureContentView import PictureContentView
from skreport.pptx.content_views.DictTableContentView import DictTableContentView

def export_pptx(report_model: ReportModel, path: Union[str, os.PathLike]):
   report_view = PptxReportView()
   report_view.export(report_model, path)

PptxReportView.register_content_view(TextContentView)
PptxReportView.register_content_view(BulletedListContentView)
PptxReportView.register_content_view(PictureContentView)
PptxReportView.register_content_view(DictTableContentView)

