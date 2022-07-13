from typing import Union, List, Optional
import pandas as pd
from pydantic import BaseModel
from skreport.models.PictureContentModel import PictureContentModel

class SlidePanelModel(BaseModel):
   title: str
   subtitle: Optional[str] = None
   content: Optional[Union[str, list, PictureContentModel]] = None
   takeaway: Optional[str] = None
