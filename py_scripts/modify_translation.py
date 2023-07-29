import os

def replace_quotes(text):
    result = ""
    first = True
    index = 0
    for char in text:
        if char == '"':
            if(index-1 >= 0) and (index+1 < len(text)):
                if(text[index-1] == "="):
                    result += char
                elif(text[index+1] == "]"):
                    result += char
                else:
                    if(first):
                        result += "“"  # Remplace les guillemets ouvrants
                        first = False
                    else:
                        result += "”"
                        first = True
            elif(index+1 > len(text)):
                result += "”"
            elif(index < 0):
                result += "“"
                first = True
        else:
            result += char
        index = index + 1

    return result

def change_line(directory, english_dir, code):
    file_name = "SG" + code.split(":")[0] + ".SCX.txt"
    line_num = int(code.split(":")[1]) - 1
    with open(os.path.join(directory, file_name), 'r', encoding='utf-8') as file:
        fr_lines = file.readlines()
        searched_line_fr = fr_lines[line_num]
    with open(os.path.join(english_dir, file_name), 'r', encoding='utf-8') as file:
        en_lines = file.readlines()
        searched_line_en = en_lines[line_num]
    
    if searched_line_fr.startswith("[name]"):
        name_line_fr = searched_line_fr
        name_line_en = searched_line_en
    if "[line]" in searched_line_fr and "[%p]" in searched_line_fr and name_line_fr:
        start_index = searched_line_fr.find("[line]") + len("[line]")
        end_index = searched_line_fr.find("[%p]")
        content_fr = searched_line_fr[start_index+1:end_index-1].strip()
        content_fr = content_fr.replace("ぁ", "é").replace("ぃ", "è").replace("ぅ", "â").replace("ぇ", "ù").replace("ぉ", "à").replace("っ", "ê").replace(code, "")
    else:
        content_fr = searched_line_fr.replace("[%p]", "")
        content_fr = content_fr.replace("ぁ", "é").replace("ぃ", "è").replace("ぅ", "â").replace("ぇ", "ù").replace("ぉ", "à").replace("っ", "ê").replace(code, "")

    if "[line]" in searched_line_en and "[%p]" in searched_line_en and name_line_en:
        start_index = searched_line_en.find("[line]") + len("[line]")
        end_index = searched_line_en.find("[%p]")
        content_en = searched_line_en[start_index+1:end_index-1].strip()
        content_en = content_en.replace("ぁ", "é").replace("ぃ", "è").replace("ぅ", "â").replace("ぇ", "ù").replace("ぉ", "à").replace("っ", "ê")
    else:
        content_en = searched_line_en.replace("[%p]", "")
        content_en = content_en.replace("ぁ", "é").replace("ぃ", "è").replace("ぅ", "â").replace("ぇ", "ù").replace("ぉ", "à").replace("っ", "ê")

    print("English : " + content_en)
    print("French : " + content_fr)

    new_content_fr = input("Veuillez remplire la nouvelle traduction : ")
    content_fr = content_fr.replace("œ", "oe").replace("'", "’").replace("é", "ぁ").replace("è", "ぃ").replace("â", "ぅ").replace("ù", "ぇ").replace("à", "ぉ").replace("ç", "c").replace("ê", "っ").replace("\n", "")
    new_content_fr = new_content_fr.replace("œ", "oe").replace("'", "’").replace("é", "ぁ").replace("è", "ぃ").replace("â", "ぅ").replace("ù", "ぇ").replace("à", "ぉ").replace("ç", "c").replace("ê", "っ")
    new_content_fr = replace_quotes(new_content_fr)
    fr_lines[line_num] = fr_lines[line_num].replace(content_fr, new_content_fr)

    with open(os.path.join(directory, file_name), 'w', encoding='utf-8') as file:
        for i, line in enumerate(fr_lines, 1):
            line = line.strip()
            file.write(line + "\n")

def main():
    script_dir = "../extracted/debug"
    english_dir = "../extracted/en_backup"
    code = input("Game line code : ")
    change_line(script_dir, english_dir, code)

if __name__ == "__main__":
    main()