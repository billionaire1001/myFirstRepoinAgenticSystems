import os

def solve_everything():
    filename = 'number.txt'
    
    
    
    with open(filename, 'w') as f:
        f.write("10\n20\n30\n40\n50")
    print(f"Success: Created '{filename}' at {os.getcwd()}")

    # 2. RUN THE CALCULATION
    try:
        with open(filename, 'r') as file:
            print(" File opened successfully")
            total = 0
            count = 0
            for line in file:
                num = line.strip()
                if num: 
                    total += int(num)
                    count += 1
            
            print(f" Read {count} numbers")
            print(f" Sum: {total}")
            if count > 0:
                print(f" Average: {total / count}")
            print(" Processing completed")
            
    except FileNotFoundError:
        print(" Error: File still not found.")
    except ValueError:
        print(" Error: The file contains non-numeric data.")

if __name__ == "__main__":
    solve_everything()


  