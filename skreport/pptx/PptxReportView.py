import os
from typing import List, Optional, Union
from pptx import Presentation
from skreport.models.ReportModel import ReportModel
from skreport.models.SlidePanelModel import SlidePanelModel
from skreport.models.PictureContentModel import PictureContentModel

class PptxReportView:
   def __init__(self):
      pass

   def export(self, report_model:ReportModel, path: Union[str, os.PathLike]):
      self.presentation = Presentation()
      self._add_title_slide(report_model.title)
      self._add_panels(report_model.panels)
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
      layout = self.presentation.slide_layouts[1]
      slide = self.presentation.slides.add_slide(layout)
      shapes = slide.shapes
      title_shape = shapes.title
      title_shape.text = panel.title
      content_shape = shapes.placeholders[1]
      if isinstance(panel.content, str):
         text_frame = content_shape.text_frame
         text_frame.text = panel.content
      # bulleted list content
      elif panel.content is not None and \
           self._is_nested_str_list(panel.content):
         text_frame = content_shape.text_frame
         self._add_bulleted_list_content(text_frame, panel.content)
      elif isinstance(panel.content, PictureContentModel):
         slide.shapes.add_picture(str(panel.content.path),
            content_shape.left, content_shape.top)
      elif panel.content is not None:
         raise SlideContentError("Content not supported")

   @staticmethod      
   def _is_nested_str_list(input):
      if not isinstance(input, list):
         return False
      for item in input:
         if isinstance(item, list):
            if not PptxReportView._is_nested_str_list(item):
               return False
         elif not isinstance(item, str):
            return False
      return True

   @staticmethod
   def _add_bulleted_list_content(text_frame, bullets: List[str]):
      PptxReportView._add_bulleted_list_content_internal(text_frame, bullets, 
                                                         level=0)
   
   @staticmethod
   def _add_bulleted_list_content_internal(text_frame, bullets: list, 
                                           level: int = 0):
      for bullet in bullets:
         if isinstance(bullet, str) and level == 0:
            text_frame.text = bullet
         elif isinstance(bullet, str) and level > 0:
            p = text_frame.add_paragraph()
            p.text = bullet
            p.level = level
         elif isinstance(bullet, list):
            PptxReportView._add_bulleted_list_content_internal(
               text_frame, bullet, level+1)
         else:
            raise Exception("Error with bulleted list format")

   def _choose_picture_height()

class SlideContentError(Exception):
   pass
