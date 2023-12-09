import os, sys



def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
        
        result = 0
        for line in lines:
            room_name, checksum = line.split("[",1)
            room_name, sector_id = room_name.rsplit("-",1)
            sector_id = int(sector_id)
            checksum = checksum[:-1]
            
            letters = {}
            for letter in room_name:
                if letter == "-":
                    continue
                if letter not in letters:
                    letters[letter] = 1
                letters[letter] += 1
            
            letters = sorted(letters.items(), key=lambda x: (-x[1], x[0]))
            letters = [x[0] for x in letters]
            letters = letters[:5]
            letters = "".join(letters)
            
            if letters == checksum:
                result += sector_id
        print(result)

if __name__ == "__main__":
    main()
    
