from src.clear import clear
from src.start import run
import sys

def main():
  argv = sys.argv()
  argc = len(argv)
  the_input = argv[1]
  
  if argc != 2:
    print("Usage: https://github.com/itzhadao/WebX/blob/main/README.md")
    sys.exit()
  else:
    if the_input[-5:] != ".webx":
      print("Needs to be .webx file")
      sys.exit()
    else:
      run(the_input)

if __name__ == "__main__":
  clear()
  main()
