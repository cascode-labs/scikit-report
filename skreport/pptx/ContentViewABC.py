from abc import ABCMeta, abstractmethod
from pptx.slide import Slide

class ContentViewABC(metaclass=ABCMeta):

   @abstractmethod
   def __init__(self, model) -> None:
      raise NotImplementedError

   @staticmethod
   @abstractmethod
   def is_view_model(content_model) -> bool:
      """Checks the model too see if this view can create content for it.

      Args:
          content_model (_type_): A model to check for compatibility with 
          this view.

      Raises:
          NotImplementedError: Subclasses must implement this method.

      Returns:
          bool: _description_
      """
      raise NotImplementedError

   @abstractmethod
   def create_content(self, slide: Slide) -> None:
      raise NotImplementedError
