import pandas as pd
import os
import ctypes
import ipywidgets as widgets
from IPython.display import display, HTML
from ipyfilechooser import FileChooser


class ScaleDataExtractor:
    def __init__(self):
        self.folder_chooser = FileChooser()
        self.together = []
        self.file_type = '.out'

        # Set up folder chooser widget
        self.folder_chooser.show_only_dirs = True
        self.folder_chooser.use_dir_icons = True
        self.folder_chooser.title = 'Select Folder'
        self.folder_chooser.default_path = os.getcwd()

        # Add a header for the VBox
        header_label = widgets.Label(value='Data Extractor from String')
        header_label.add_class('header-label')

        # Add input fields for search_string_1 and search_string_2
        self.search_string_1_input = widgets.Text(description='Search String 1:', value= 'space_group Pnma',layout=widgets.Layout(width='75%'),style = {'description_width': 'initial'})
        self.search_string_2_input = widgets.Text(description='Search String 2:', value= 'scale @', layout=widgets.Layout(width='75%'),style = {'description_width': 'initial'})

        # Add a button to trigger data extraction
        self.extract_button = widgets.Button(description='Extract Data', button_style='success')
        self.extract_button.on_click(self.extract_data)
        
        # Add a progress bar        
        self.progress_bar = widgets.FloatProgress(min=0, max=1, bar_style='success', style={'bar_width': '20000px', 'description_width': '100px'})

        # Create a container for the widgets
        container = widgets.VBox([header_label, self.folder_chooser, self.search_string_1_input, self.search_string_2_input, self.extract_button, self.progress_bar])
        container.layout.width = '600px'
        container.layout.margin = '20px auto'
        container.layout.padding = '20px'
        container.layout.border = '5px solid #AAA'
        container.layout.border_radius = '10px'
        container.layout.background = '#F9F9F9'

        # Wrap the container in another VBox
        outer_container = widgets.VBox([container])

        # Center align the outer container
        outer_container.layout.align_items = 'center'

        # Apply CSS styling for the header label
        style = """
        .header-label {
            font-weight: bold;
            font-size: 22px;
            margin-bottom: 10px;
            color: Green;
        }
        """
        display(HTML('<style>{}</style>'.format(style)))


        # Create an Output widget to preserve interactivity
        output = widgets.Output(layout={'border': '1px solid #AAA', 'padding': '20px'})

        # Display the outer container
        display(output)
        with output:
            display(outer_container)

    def collect_files(self):
        folder_path = self.folder_chooser.selected_path
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                if name.endswith(self.file_type):
                    self.together.append(name)

    def read_line_with_string(self, file_path, search_string_1, search_string_2):
        with open(file_path, 'r') as file:
            found_search_string_1 = False
            for line_number, line in enumerate(file, 1):
                if search_string_1 in line:
                    found_search_string_1 = True
                if found_search_string_1 and search_string_2 in line:
                    return line.strip(), line_number
        return None, None

    def push_message(self):
        ctypes.windll.user32.MessageBoxW(0, "Data extraction is complete.", "Notification", 0x40)

    def extract_data(self, button):
        self.collect_files()
        self.progress_bar.max = len(self.together)
        search_string_1 = self.search_string_1_input.value
        search_string_2 = self.search_string_2_input.value

        dictionary_data = {}
        for file in self.together:
            self.progress_bar.value += 1
            self.progress_bar.description = 'Progress: {}%'.format(int((self.progress_bar.value / self.progress_bar.max) * 100))
            file_path = os.path.join(self.folder_chooser.selected_path, file)
            line, line_number = self.read_line_with_string(file_path, search_string_1, search_string_2)
            print(line, line_number)
            dictionary_data[file] = line[7:]

        df = pd.DataFrame.from_dict(dictionary_data, orient="index", columns=['scale @'])
        output_file_path = os.path.join(self.folder_chooser.selected_path, "scale_data_from_out_file.csv")
        df.to_csv(output_file_path)
        self.push_message()


