from typing import Union
import pandas as pd
from pydantic import BaseModel

class SlidePanelModel(BaseModel):
   title: str
   subtitle: str
   content: Union[str,pd.DataFrame]
   takeaway: str
