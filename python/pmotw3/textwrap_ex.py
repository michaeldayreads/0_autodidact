"""
This file contains examples from and reactions to:
https://pymotw.com/3/textwrap/index.html
"""

import textwrap

def header(description):
    print("\n----- {} -----\n".format(description))

sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

header("fill, width of 50.")
print(textwrap.fill(sample_text, width=50))

header("dedented")
print(textwrap.dedent(sample_text))

dedented_text = textwrap.dedent(sample_text).strip()

for width in [45, 60]:
    header("{} Columns:".format(width))
    print(textwrap.fill(dedented_text, width=width))

header('Indented in the style of email quote block.')
wrapped = textwrap.fill(dedented_text, width=50)
print(textwrap.indent(wrapped, '> '))

header("As object - very limited...")
wrapper = textwrap.TextWrapper()
wrapper.width = 80
wrapper.initial_indent = "     "
wrapper.drop_whitespace = True
print(wrapper.fill(sample_text))
