import os

def execute_sc3tools(file_path):
    sc3tools_path = "\"./tools/sc3tools/sc3tools.exe\""
    arguments = f"extract-text {file_path}"
    os.system(f'"{sc3tools_path}" {arguments} sghd')

def main():
    script_dir = "../extracted/script"
    scx_files = [f for f in os.listdir(script_dir) if f.endswith('.SCX')]

    for file_name in scx_files:
        file_path = os.path.join(script_dir, file_name)
        execute_sc3tools(file_path)

if __name__ == "__main__":
    main()