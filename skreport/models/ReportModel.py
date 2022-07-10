from typing import List, Union
from pydantic import BaseModel
from skreport.models.SlidePanelModel import SlidePanelModel

class ReportModel(BaseModel):
   title: str
   subtitle: str
   authors: Union[str, List[str]]
   panels: List[SlidePanelModel]
