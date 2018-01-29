from os.path import join, abspath, dirname
import sys

ROOT = join(dirname(dirname(abspath(__file__))))
sys.path.insert(0, ROOT)

print(ROOT)
