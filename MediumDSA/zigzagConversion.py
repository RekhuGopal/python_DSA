def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    zigzag = ['' for _ in range(numRows)]
    row, direction = 0, 1
    for char in s: 
        print(row)
        zigzag[row] += char
        if row == 0:
            direction = 1
        elif row == numRows - 1:
            direction = -1
        row += direction
        print(row)

    return ''.join(zigzag)

# Test cases
#print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
#print(convert("A", 1))               # Output: "A"
