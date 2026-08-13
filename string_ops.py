VOWELS = "aeiouAEIOU"

def decribe_line(raw: str,line_no: int,out_handle) -> None:
    trimmed = raw.strip()
    upper_line = trimmed.upper()
    lower_line = trimmed.lower()
    reversed_line = trimmed[::-1]

    vowel_total = 0
    for ch in trimmed:
        if ch in VOWELS:
            vowel_total += 1
    
    header = f"\nLine {line_no}: {trimmed!r}"
    print(header)
    out_handle.write(header + "\n")

    line_out = f" Upper-case : {upper_line}"
    print(line_out)
    out_handle.write(line_out + "\n")

    line_out = f" Lower-case : {lower_line}"
    print(line_out)
    out_handle.write(line_out + "\n")

    line_out = f" Reversed : {reversed_line}"
    print(line_out)
    out_handle.write(line_out + "\n")

    line_out = f" Vowels : {vowel_total}"
    print(line_out)
    out_handle.write(line_out + "\n")

def main() -> None: #None is used when the function will return nothing
    try:
        with open("input.txt",encoding="utf-8") as infile, \
             open("output.txt",'w',encoding="utf-8") as outfile:

             line_no = 1
             for line in infile:
                decribe_line(line,line_no,outfile)
                line_no += 1
        
        print("\n✅ Result also save to 'output.txt'.")
    except:
        print("\n⚠️ File input.txt not found. Place it in the same folder as this script.")

if __name__ == "__main__":
    main()