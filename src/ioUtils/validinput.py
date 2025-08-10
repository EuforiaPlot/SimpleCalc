def valid_input_float(prompt: str):
    try:
        var = float(input(f"{prompt}"))
        return var
    except ValueError:
        print("FLOAT NUMBER ERRROR")
