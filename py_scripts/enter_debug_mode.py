import os

def add_code_to_lines(directory):
    for file_name in os.listdir(directory):
        if file_name.startswith("SG") and file_name.endswith(".txt"):
            file_path = os.path.join(directory, file_name)
            code = file_name.replace("SG", "").replace(".SCX.txt", "")
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            new_file_name = directory + "/../debug/" + file_name
            if os.path.exists(new_file_name):
                 os.remove(new_file_name)
            with open(new_file_name, 'w', encoding='utf-8') as new_file:
                for i, line in enumerate(lines, 1):
                    line = line.strip()
                    line_with_code = line[:-4] + code + f":{str(i).zfill(3)}" + line[-4:]
                    new_file.write(line_with_code + "\n")

def main():
    script_dir = "../extracted/release"  # Remplacez par le chemin de votre répertoire contenant les fichiers .txt à modifier

    add_code_to_lines(script_dir)

if __name__ == "__main__":
    main()