import sys
from underscore import Underscore
import traceback

try:
    root_path = sys.argv[1]
    under_score = Underscore(root_path, '-', [' ', '_'])
    under_score.start()
    print('Success!!')
except Exception as e:
    traceback.print_exc()
    sys.exit(0)