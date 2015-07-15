import sys
import traceback

from src.underscore import Underscore
from src.iosExtHandler import IOSExtentionHandler

# try:
#     root_path = sys.argv[1]
#     under_score = Underscore(root_path, '-', [' ', '_'])
#     under_score.start()
#     print('Success!!')
# except Exception as e:
#     traceback.print_exc()
#     sys.exit(0)



try:
    root_path = sys.argv[1]
    replacements = {
        '@0.5x':'',
        '@1x':'@2x',
        '@1.5x':'@3x'
    }

    ios_handler = IOSExtentionHandler(root_path, replacements)
    ios_handler.rename()
    print('Success!!')
except Exception as e:
    traceback.print_exc()
    sys.exit(0)