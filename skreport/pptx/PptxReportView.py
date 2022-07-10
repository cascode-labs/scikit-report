import os
from typing import List, Optional, Union
from pptx import Presentation
from skreport.models.ReportModel import ReportModel
from skreport.models.SlidePanelModel import SlidePanelModel

class PptxReportView:
   def __init__(self):
      pass

   def export(self, report_model:ReportModel, path: Union[str, os.PathLike]):
      self.presentation = Presentation()
      self._add_title_slide(report_model.title)
      self.presentation.save(str(path))

   def _add_title_slide(self,title: str, subtitle: Optional[str] = None):
      title_slide_layout = self.presentation.slide_layouts[0]
      slide = self.presentation.slides.add_slide(title_slide_layout)
      title_shape = slide.shapes.title
      title_shape.text = title
      if subtitle is not None:
         subtitle_shape = slide.placeholders[1]
         subtitle_shape.text = subtitle

   def _add_panels(self, panels: List[SlidePanelModel]):
      for panel in panels:
         self._add_panel(panel)

   def _add_panel(self, panel: SlidePanelModel):
      layout = self.presentation.slide.layouts[1]
      slide = self.presentation.slides.add_slide(layout)
      shapes = slide.shapes
      title_shape = shapes.title
      title_shape.text = panel.title
      content_shape = shapes.placeholders[1]
      if panel.content is str:
         text_frame = content_shape.text_frame
         text_frame.text = panel.content
