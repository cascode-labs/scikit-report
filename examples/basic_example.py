from pathlib import Path
from skreport import export_pptx, ReportModel, SlidePanelModel
from skreport.models.PictureContentModel import PictureContentModel

if __name__ == "__main__":
   report = ReportModel(**{
      'title': "Test Report",
      'panels': [
         SlidePanelModel(**{
            'title': "Test Text Content",
            'content':"Test some text",
         }),
         SlidePanelModel(**{
            'title': "Bulleted List Content",
            'content': [
               ["Level 0 bullet", "Level 1 bullet", "Level 2 bullet"],
               "2nd Level 0 bullet",
               ["some important info", "important sub-bullet"],
            ]
         }),
         SlidePanelModel(**{
            'title': "Picture Content",
            'content': PictureContentModel(path=Path("/home/curtisma3/prj/scikit-report/examples/monty_python.jpeg"))
         }),
      ]
   })

   export_pptx(report,"/mnt/chromeos/GoogleDrive/MyDrive/scikit-report/basic_example.pptx")
