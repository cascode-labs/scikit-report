from typing import List, Optional, Union
from pydantic import BaseModel
from skreport.models.SlidePanelModel import SlidePanelModel


class ReportModel(BaseModel):
   title: str
   subtitle: Optional[str]
   panels: List[SlidePanelModel]
