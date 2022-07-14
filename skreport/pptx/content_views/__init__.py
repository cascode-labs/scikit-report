from typing import List, Type
from skreport.pptx.ContentViewABC import ContentViewABC
from skreport.pptx.content_views.TextContentView import TextContentView
from skreport.pptx.content_views.BulletedListContentView import BulletedListContentView
from skreport.pptx.content_views.PictureContentView import PictureContentView
from skreport.pptx.content_views.DictTableContentView import DictTableContentView


PPPTX_CONTENT_VIEWS: List[Type[ContentViewABC]] = [
   TextContentView,
   BulletedListContentView,
   PictureContentView,
   DictTableContentView,
   ]
