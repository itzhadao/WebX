import 

def run(input_dir):
  type = ''''''
  content = ""
  try:
    with open(input_dir, "r") as file:
      content = file.read()
    i = 0
    current = ""
    latest = ""
    list = ["#", "##", "###", "*bg="]
    for i in range(len(content)):
      if content[i] == ' ':
        if current == "\n":
          type += '\n'
        elif current == "#":
          type += "h1:"
        elif current == "##":
          type += "h2:"
        elif current == "###":
          type += "h3:"
        elif current == "*bg=":
          type += "bg:"
        else:
          if latest in list:
            type += current
          else:
            print("Error: Unknown token!")
            sys.exit()
        
        if current != "":
          latest = current
        current = ""
      else:
        current += content[i]
  except FileNotFoundError:
    print("Error: File not found")
  except Exception as e:
    print(f"An error occurred: {e}")
