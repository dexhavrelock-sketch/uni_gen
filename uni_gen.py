# uni_gen.py
import itertools
import os

def uni(needed_returns, type_code, file_name):
    # This ensures the file is created in the SAME folder as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, f"{file_name}.txt")
    
    if type_code == 1:
        chars = "01"
    else:
        chars = "0123456789"

    digits = 0
    while len(chars) ** digits < needed_returns:
        digits += 1

    try:
        with open(full_path, "w") as f:
            combos = itertools.product(chars, repeat=digits)
            for i, combo in enumerate(combos):
                if i >= needed_returns:
                    break
                f.write("".join(combo) + "\n")
            f.flush() # Force Windows to write the data now
            
        print(f"✅ Created: {full_path}")
    except Exception as e:
        print(f"❌ Error: {e}")