import os
import argparse

def execute_sc3tools(script_dir, file_name, folder):
    sc3tools_path = "\"./tools/sc3tools/sc3tools.exe\""
    script = os.path.join(script_dir, file_name).replace(".txt", "")
    file_path = os.path.join(folder, file_name)
    arguments = f"replace-text {script} {file_path}"
    os.system(f'"{sc3tools_path}" {arguments} sghd')

def main():
    parser = argparse.ArgumentParser(description="Execute sc3tools and optionally move file to debug directory.")
    parser.add_argument("--debug", action="store_true", help="Get files from debug folder")
    args = parser.parse_args()

    script_dir = "../extracted/script"

    if args.debug == True:
        folder = "../extracted/debug"
    else:
        folder = "../extracted/release"
    txt_files = [f for f in os.listdir(folder) if f.endswith('.txt')]
    for file_name in txt_files:
        execute_sc3tools(script_dir, file_name, folder)

if __name__ == "__main__":
    main()