# PDFInfo

Extract pdf font information.

# Usage
## Scan pdf
Return average font size and font families used in entire document.
```
Usage: main.py scan [OPTIONS] FILENAME

Options:
  --get-size
  --get-fonts
  --skip-refs
```

## Test pdf for min size
Test a pdf for paragraphs with text font size smaller than specified.
```
Usage: main.py test [OPTIONS] FILENAME

Options:
  --font-size INTEGER
  --tolerance FLOAT
  --skip-refs
```