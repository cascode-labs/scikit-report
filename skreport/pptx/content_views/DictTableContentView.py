from pptx.slide import Slide
from skreport.pptx.ContentViewABC import ContentViewABC


class DictTableContentView(ContentViewABC):
   def __init__(self, model:dict) -> None:
      self.model: dict = model

   @staticmethod
   def is_view_model(content_model) -> bool:
      return isinstance(content_model, dict)

   def create_content(self, slide: Slide) -> None:
      pass

