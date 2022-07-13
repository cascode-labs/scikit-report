# scikit-report

Scikit-report is a Python library that generates well formatted technical
reports and exports them to a variety of formats.  It has a model-view
structure.  The client builds a model to provide the contents of the report.  
The contents accept standard Python and scientific Python datastructures as
content such as Pandas dataframes and matplotlib plots.   Then either the
default export view for each export format can be used or the client can
select a specific view.

Export Formats under development:

- Power Point (.pptx)
- Excel (.xlsx)
- Qt for Python (GUI)

Content types supported for Power Point export:
- strings: Displayed in a paragraph
- Nested lists of strings: Displayed as a bulleted list with the level being
controlled by the nesting level
