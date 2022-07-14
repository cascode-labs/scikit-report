from pptx.slide import Slide
from skreport.models.PictureContentModel import PictureContentModel
from skreport.pptx.ContentViewABC import ContentViewABC


class PictureContentView(ContentViewABC):
   def __init__(self, model: PictureContentModel) -> None:
      self.model = model
   
   @staticmethod
   def is_view_model(content) -> bool:
      return isinstance(content, PictureContentModel)

   def create_content(self, slide: Slide) -> None:
      pass
