import pandas as pd
import ipywidgets as widgets
import os
import ctypes
import glob
from IPython.display import display


class ScaleDataExtractor:
    # Initialize ScaleDataExtractor with the specified folder path.
    def __init__(self, folder_path, batch=False):
        self.batch_or_na = not batch
        self.folder = folder_path
        self.together = []
        self.file_type = '.out'

    # Collect relevant files with '.out' extension from the specified folder.
    def collect_files(self):
        self.together = [name for name in os.listdir(self.folder) if name.endswith(self.file_type)]


    # Read a specific line from the file based on a search string.
    def read_line_with_string(self, file_path, search_string_1, search_string_2):
        with open(file_path, 'r') as file:
            found_search_string_1 = False
            for line_number, line in enumerate(file, 1):
                if search_string_1 in line:
                    found_search_string_1 = True
                if found_search_string_1 and search_string_2 in line:
                    return line.strip(), line_number
        return None, None


    # Sends push message to user
    def push_message(self):
        ctypes.windll.user32.MessageBoxW(0, "Data extraction is complete.", "Notification", 0x40)


    # Extract scale data from the files and save it to a CSV file.
    def extract_data(self):
        self.collect_files()
        self.max_count = len(self.together)
        f = widgets.FloatProgress(min=0, max=self.max_count, bar_style='success', style={'bar_width': '20000px', 'description_width': '100px'})
        display(f)

        dictionary_data = {}
        search_string_1 = 'space_group Pnma'
        search_string_2 = 'scale @'
        for file in self.together:
            f.value += 1
            f.description = 'Progress: {}%'.format(int((f.value / self.max_count) * 100))
            file_path = os.path.join(self.folder, file)
            line, line_number = self.read_line_with_string(file_path, search_string_1, search_string_2)
            if line is not None:
                dictionary_data[file] = line[7:]

        df = pd.DataFrame.from_dict(dictionary_data, orient="index", columns=['scale @'])
        output_file_path = os.path.join(self.folder, "scale_data_from_out_file.csv")
        df.to_csv(output_file_path)
        if self.batch_or_na:
            self.push_message()
