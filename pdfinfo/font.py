class TextStats:
  sizes = []
  fonts = set()

  def __init__(self, sizes = [], fonts = []):
    self.sizes = sizes
    self.fonts = self.fonts.union(fonts)

  def combine(self, stats):
    self.sizes += stats.sizes
    self.fonts = self.fonts.union(stats.fonts)

  def get_average_size(self):
    return sum(self.sizes) / len(self.sizes)

def iterate_spans(doc, cb, skip_refs=False):
  for page in doc.pages():
    blocks = page.get_text('dict')
    for block in blocks['blocks']:
      if block.get('type') == 0:
        for line in block.get('lines', []):
          for span in line.get('spans', []):
            if span['text'].lower() == 'references' and skip_refs:
              return
            cb(span)


def get_stats(doc, skip_refs=False):
  sizes = []
  fonts = set()

  def get_text_stats(span):
    sizes.append(span['size'])
    fonts.add(span['font'])
  iterate_spans(doc, get_text_stats, skip_refs=skip_refs)

  return TextStats(sizes, fonts)


def find_offenders(doc, size, skip_refs=False, tolerance=0.1):
  offenders = []
  def add_offender(span):
    if abs(span['size'] - size) > tolerance:
      offenders.append((span['text'], span['size']))
  iterate_spans(doc, add_offender, skip_refs=skip_refs)

  return offenders
