from os import mkdir
from pathlib import Path
from importlib import resources
from skreport import export_pptx, ReportModel, SlidePanelModel
from skreport.models.PictureContentModel import PictureContentModel
from skreport import examples

if __name__ == "__main__":

   title_slide = SlidePanelModel(**{
      'title': "Test Text Content",
      'content':"Test some text",
   })

   bulleted_list_slide = SlidePanelModel(**{
      'title': "Bulleted List Content",
      'content': [
         ["Level 0 bullet", "Level 1 bullet", "Level 2 bullet"],
         "2nd Level 0 bullet",
         ["some important info", "important sub-bullet"],
      ]
   })

   with resources.path(examples, "monty_python.jpeg") as picture_path:
      picture_slide = SlidePanelModel(**{
         'title': "Picture Content",
         'content': PictureContentModel(
            path=picture_path)
      })

      report = ReportModel(**{
         'title': "Test Report",
         'panels': [
            title_slide,
            bulleted_list_slide,
            picture_slide,
         ]
      })
      example_dir = Path("/workspaces/scikit-report/example_outputs")
      mkdir(example_dir)
      export_pptx(report, example_dir / "basic_example.pptx")
