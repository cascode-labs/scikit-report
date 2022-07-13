from types import MappingProxyType


class DefaultTemplate:
   MASTER_INDICES = MappingProxyType({
      "Title": 0, # presentation title slide
      "Title and Content": 1,
      "Section Header": 2, # sometimes called Segue
      "Two Content": 3, # side by side bullet textboxes
      "Comparison": 4, # same but additional title for both content boxes
      "Title Only": 5,
      "Blank": 6,
      "Content with Caption": 7,
      "Picture with Caption": 8,
   })


