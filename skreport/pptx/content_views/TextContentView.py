from pptx.slide import Slide
from skreport.models.PictureContentModel import PictureContentModel
from skreport.pptx.ContentViewABC import ContentViewABC


class TextContentView(ContentViewABC):
   def __init__(self, model: str) -> None:
      self.model = model
   
   @staticmethod
   def is_view_model(content) -> bool:
      return isinstance(content, str)

   def create_content(self, slide: Slide) -> None:
      shapes = slide.shapes
      content_shape = shapes.placeholders[1]
      text_frame = content_shape.text_frame
      text_frame.text = self.model
