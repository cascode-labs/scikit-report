from typing import Union, Optional
from pydantic import BaseModel
from skreport.models.PictureContentModel import PictureContentModel


class SlidePanelModel(BaseModel):
   title: str
   subtitle: Optional[str] = None
   content: Optional[Union[str, list, PictureContentModel]] = None
   takeaway: Optional[str] = None
