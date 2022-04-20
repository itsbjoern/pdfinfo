from unittest import skip
import fitz
import click

from pdfinfo import font

@click.group()
def cli():
  pass

@click.command()
@click.argument('filename')
@click.option('--get-size', is_flag=True, default=True)
@click.option('--get-fonts', is_flag=True, default=False)
@click.option('--skip-refs', is_flag=True, default=False)
def scan(filename, get_size=True, get_fonts=False, skip_refs=False):
  doc = fitz.open(filename)
  stats = font.get_stats(doc, skip_refs=skip_refs)

  print('Title:', doc.metadata.get('title'))
  print()
  if get_size:
    print('Average font size:', stats.get_average_size())
  if get_fonts:
    print('Used fonts:')
    for fontFam in stats.fonts:
      print(f'  {fontFam}')

@click.command()
@click.argument('filename')
@click.option('--font-size', default=11)
@click.option('--tolerance', default=0.1)
@click.option('--skip-refs', is_flag=True, default=False)
def test(filename, font_size=11, skip_refs=False, tolerance=0.1):
  doc = fitz.open(filename)
  offenders = font.find_offenders(doc, font_size, skip_refs=skip_refs, tolerance=tolerance)
  print("Offenders")
  for off in offenders:
    print(f'\t{off[0][:25]}')
    print(f'\tFound size: {off[1]}')

cli.add_command(scan)
cli.add_command(test)



if __name__ == '__main__':
  cli()