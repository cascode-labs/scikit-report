from skreport.pptx import PptxReportView as view

def test_is_nested_str_list_1item():
   assert view._is_nested_str_list(["single item"])

def test_is_nested_str_list_2items():
   assert view._is_nested_str_list(["item1", "item2"])

def test_is_nested_str_list_2_nested_items():
   assert view._is_nested_str_list([
      "item1",
      ["subitem1", "subitem2"]
   ])

def test_is_nested_str_list_multiple_nested_items():
   assert view._is_nested_str_list([
      ["Level 0 bullet", "Level 1 bullet", "Level 2 bullet"],
      "2nd Level 0 bullet",
      ["some important info", "important sub-bullet"],
      ])

def test_is_nested_str_list_false_string():
   assert not view._is_nested_str_list("string")

def test_is_nested_str_list_false_int_list():
   assert not view._is_nested_str_list([0, 1, 2])

def test_is_nested_str_list_false_mixed_list():
   assert not view._is_nested_str_list([0, "hi", 2])
