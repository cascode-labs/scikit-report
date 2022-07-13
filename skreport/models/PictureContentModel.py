import os
from typing import Union
from pathlib import Path
from pydantic import BaseModel, FilePath


class PictureContentModel(BaseModel):
   path: FilePath
