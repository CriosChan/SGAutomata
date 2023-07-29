from operator import index
import os
import time
import asyncio
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def translate_text(text, driver):
    driver.get(f"https://www.deepl.com/translator#en/fr/{text}")
    
    while True:
        try:
            # Attendre jusqu'à 10 secondes que l'élément contenant la traduction soit chargé
            translation_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-labelledby=translation-results-heading] > p > span"))
            )
            translation = translation_element.text.strip()
            if translation:
                return translation
        except TimeoutException:
            print("Temps d'attente dépassé pour trouver l'élément. Rafraîchissement de la page...")
            driver.get(f"https://www.deepl.com/translator#en/fr/{text}")
        
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

async def read_fr_lines(backup_file_path, file_path):
    
    if os.path.exists(backup_file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            fr_lines = file.readlines()
        with open(backup_file_path, 'r', encoding='utf-8') as backup_file:
            lines = backup_file.readlines()
    else:
        fr_lines = []
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(backup_file_path, 'w', encoding='utf-8') as backup_file:
            for line in lines:
                backup_file.write(line)
    return lines, fr_lines

def process_sg_files(directory, driver):
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory, file_name)
            backup_file_path = f"{file_path}.backup"
            loop = asyncio.get_event_loop()
            lines, fr_lines = loop.run_until_complete(read_fr_lines(backup_file_path, file_path))
            line_start = len(fr_lines)
            with open(file_path, 'w', encoding='utf-8') as file:
                line_index = 0
                for line in lines:
                    line_index = line_index + 1
                    if(line_index <= line_start):
                        print(line_start)
                        print(fr_lines)
                        print(line_index)
                        file.write(fr_lines[line_index-1])
                        continue
                    line = line.strip()
                    if line.startswith("[name]"):
                        name_line = line
                    if "[line]" in line and "[%p]" in line and name_line:
                        start_index = line.find("[line]") + len("[line]")
                        end_index = line.find("[%p]")
                        content = line[start_index+1:end_index-1].strip()
                        translation = translate_text(content, driver)
                        translation = translation.replace("œ", "oe").replace("'", "’").replace("é", "ぁ").replace("è", "ぃ").replace("â", "ぅ").replace("ù", "ぇ").replace("à", "ぉ").replace("ç", "c").replace("ê", "っ")
                        translation = replace_quotes(translation)
                        file.write(f'{line.replace(content, translation)}\n')

                        time.sleep(0.5)
                    else:
                        content_without_p = line.replace("[%p]", "")
                        print(content_without_p)
                        if(len(content_without_p) <= 1):
                            file.write(f'{line}\n')
                        translation = translate_text(content_without_p, driver)
                        translation = translation.replace("œ", "oe").replace("'", "’").replace("é", "ぁ").replace("è", "ぃ").replace("â", "ぅ").replace("ù", "ぇ").replace("à", "ぉ").replace("ç", "c").replace("ê", "っ")
                        translation = replace_quotes(translation)
                        file.write(f'{line.replace(content_without_p, translation)}\n')

                        time.sleep(0.5)
            os.remove(backup_file_path)

def main():
    parser = argparse.ArgumentParser(description="Script de traduction de fichiers SG.")
    parser.add_argument("-d", "--script_dir", default="../extracted/To Translate", help="Chemin du répertoire contenant les fichiers SG à traduire.")
    args = parser.parse_args()

    # Définir le chemin vers le pilote du navigateur (par exemple, ChromeDriver)
    driver_path = "C:/Users/CriosChan/Downloads/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)

    process_sg_files(args.script_dir, driver)

    driver.quit()

if __name__ == "__main__":
    main()
