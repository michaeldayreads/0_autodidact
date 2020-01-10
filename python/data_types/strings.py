"""
This module is used to experiment and document the use of strings in python.
"""

# Preserving formatting in strings.

def trim(text):
    """Remove leading and trailing new line character from a paragraph."""
    return(text.lstrip('\n').rstrip('\n'))

formatted_paragraph = '''
    The advantages of the tripple quotes before and after the text itself are
numerous. First, the paragraph looks in the code precisely as it will look when
printed by the program, at least between the quotes. The presence of the line
break before and after are likely to be useful in the way that the content 
should be displayed; namely a line before and after it.
'''

however = """
    However, there are cases where you may prefer to combine two such paragraphs
without any space between them. Or perhaps you wish to have that space in some
cases but not in others to aid in the grouping of thoughts by the reader. In 
such instances, we want to remove the line breaks, yet preserve the indentation:
foo makes this possible.
"""


print('--- tripple quotes above and below, simple printing ---')
print(formatted_paragraph)
print(however)

print('--- tripple quotes above and below, *clever* printing ---\n')
print(trim(formatted_paragraph))
print(trim(however))

