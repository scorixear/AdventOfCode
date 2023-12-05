row = 3010
col = 3019

def get_next_code(code):
    return (code * 252533) % 33554393

def get_code(row, col):
    code = 20151125
    current_row = 1
    current_col = 1
    while True:
        if current_row == row and current_col == col:
            break
        if current_row == 1:
            current_row = current_col + 1
            current_col = 1
        else:
            current_row -= 1
            current_col += 1
        code = get_next_code(code)
    return code

print(get_code(row, col))
    
