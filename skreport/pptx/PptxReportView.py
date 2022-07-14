import os
from typing import List, Optional, Union, Type
from pptx import Presentation as create_presentation
from pptx.presentation import Presentation 
from skreport.models.ReportModel import ReportModel
from skreport.models.SlidePanelModel import SlidePanelModel
from skreport.pptx.ContentViewABC import ContentViewABC
from skreport.pptx.content_views import PPPTX_CONTENT_VIEWS


class PptxReportView:
   content_views: List[Type[ContentViewABC]] = []

   def __init__(self):
      self.presentation: Presentation

   def export(self, report_model:ReportModel, path: Union[str, os.PathLike]):
      self.presentation: Presentation = create_presentation()
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
      for content_view in self.content_views:
         if content_view.is_view_model(panel.content):
            view = content_view(panel.content)
            view.create_content(slide)
            break
      else:
         raise SlideContentError("Content not supported")

   @classmethod
   def register_content_view(cls, content_view_class: Type[ContentViewABC]) -> None:
      cls.content_views.append(content_view_class)

   @classmethod
   def register_content_views(cls, content_view_class_list: List[Type[ContentViewABC]]) -> None:
      for content_view in content_view_class_list:
         cls.register_content_view(content_view)

PptxReportView.register_content_views(PPPTX_CONTENT_VIEWS)

class SlideContentError(Exception):
   pass
