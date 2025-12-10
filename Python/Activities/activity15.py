try:
    # This will cause a NameError because 'x' is not defined
    print(x)
except NameError as e:
    print("A NameError occurred:", e)
