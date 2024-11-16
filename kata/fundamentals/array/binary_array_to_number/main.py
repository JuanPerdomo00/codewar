def binary_array_to_number(arr):
  # your code
  return int(''.join([str(i) for i in arr]), 2)



def main():
  print(binary_array_to_number([0,0,0,1]))


if __name__ == "__main__":
  main()