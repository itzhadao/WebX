def run(input_dir):
  try:
    with open(input_dir, "r") as file:
      content = file.read()
      
  except FileNotFoundError:
    print("Error: File not found")
  except Exception as e:
    print(f"An error occurred: {e}")
