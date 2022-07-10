from typing import Union, List, Optional
import pandas as pd
from pydantic import BaseModel

class SlidePanelModel(BaseModel):
   title: str
   subtitle: Optional[str] = None
   content: Optional[Union[str, List[str]]] = None
   takeaway: Optional[str] = None
