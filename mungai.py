
def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as infile:
            original_content = infile.read()
            print("✅ File read successfully.")
    except FileNotFoundError:
        print("❌ Error: File not found.")
        return
    except IOError:
        print("❌ Error: Cannot read the file.")
        return

    modified_content = modify_content(original_content)

    output_filename = "modified_" + filename
    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"🎉 Modified content written to '{output_filename}'")
    except IOError:
        print("❌ Error: Could not write to the output file.")

if __name__ == "__main__":
    main()

