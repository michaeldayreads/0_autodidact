import logging

LOG_FILENAME = "put_me_in_the_gitignore.log"

logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

logging.debug('This is the most basic logging.')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)