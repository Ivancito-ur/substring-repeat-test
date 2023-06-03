def main(string: str):
    result = {}
    check_substring = []
    for i in range(0, len(string)):
        substring_base = string[i:i+4]
        if len(substring_base) == 4:
            for j in range(0, len(string)):
                aux = string[j:j+4]
                if substring_base == aux and not substring_base in check_substring:
                    result[substring_base] = 1 if result.get(substring_base, None) == None else result[substring_base] + 1        
            check_substring.append(substring_base)
            if result[substring_base] <= 1:
                result.pop(substring_base)
    return result
                
            
if __name__ == "__main__":
    string = input()
    print(main(string))
    