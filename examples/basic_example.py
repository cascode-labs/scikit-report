from skreport import export_pptx, ReportModel, SlidePanelModel

if __name__ == "__main__":
   report = ReportModel(**{
      'title': "Test Report",
      'panels': [SlidePanelModel(**{
         'title': "Test Text",
         'content':"Test some text"
      })]
   })

   export_pptx(report,"/mnt/chromeos/GoogleDrive/MyDrive/scikit-report/basic_example.pptx")
