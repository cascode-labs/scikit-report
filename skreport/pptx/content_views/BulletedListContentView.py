from pptx.slide import Slide
from skreport.pptx.ContentViewABC import ContentViewABC


class BulletedListContentView(ContentViewABC):
   
   def __init__(self, model: list) -> None:
      self.model: list = model

   @staticmethod
   def is_view_model(content) -> bool:
      return BulletedListContentView._is_nested_str_list(content)

   def create_content(self, slide: Slide) -> None:
      shapes = slide.shapes
      content_shape = shapes.placeholders[1]
      text_frame = content_shape.text_frame
      self._add_bulleted_list_content(text_frame, self.model)
      
   @staticmethod      
   def _is_nested_str_list(input):
      if not isinstance(input, list):
         return False
      for item in input:
         if isinstance(item, list):
            if not BulletedListContentView._is_nested_str_list(item):
               return False
         elif not isinstance(item, str):
            return False
      return True

   @staticmethod
   def _add_bulleted_list_content(text_frame, bullets: list):
      BulletedListContentView._add_bulleted_list_content_internal(text_frame, bullets, 
                                                         level=0)
   
   @staticmethod
   def _add_bulleted_list_content_internal(text_frame, bullets: list,
                                           level: int = 0) -> None:
      first_str = True
      for bullet in bullets:
         if isinstance(bullet, str) and first_str:
            text_frame.text = bullet
            first_str = False
         elif isinstance(bullet, str) and not first_str:
            p = text_frame.add_paragraph()
            p.text = bullet
            p.level = level
         elif isinstance(bullet, list):
            BulletedListContentView._add_bulleted_list_content_internal(
               text_frame, bullet, level+1)
         else:
            raise Exception("Error with bulleted list format")
