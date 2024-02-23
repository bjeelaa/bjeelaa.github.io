import sys
import shutil
import os
import subprocess

def process_pdf(file_path, destination_folder):
    file_name = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, file_name)

    if os.path.exists(destination_path):
        os.remove(file_path)
        error_message = f'Error: A file with the same name already exists in the destination folder: {destination_path}'
        return error_message

    shutil.copy(file_path, destination_path)
    success_message = f'File saved to {destination_path}'
    os.remove(file_path)
    
    return success_message

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python process_file.py <file_path> <destination_folder>')
    else:
        destination_folder = sys.argv[2]
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        result_message = process_pdf(sys.argv[1], destination_folder)
        print(result_message)
