"To get the full path of the destination folders when needed"
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)
