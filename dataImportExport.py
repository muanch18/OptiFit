import pandas as pd

class DataImportExport:
    def __init__(self, filepath):
        self.filepath = filepath

    def import_data(self):
        try:
            if self.filepath.endswith('.csv'):
                data = pd.read_csv(self.filepath)
            elif self.filepath.endswith('.json'):
                data = pd.read_json(self.filepath)
            elif self.filepath.endswith('.xlsx'):
                data = pd.read_excel(self.filepath)
            else:
                print(f"Unsupported file format: {self.filepath}")
                return None
            return data
        except FileNotFoundError:
            print(f"No file found at {self.filepath}")
            return None

    def export_data(self, data, filename):
        try:
            if filename.endswith('.csv'):
                data.to_csv(filename, index=False)
            elif filename.endswith('.json'):
                data.to_json(filename)
            elif filename.endswith('.xlsx'):
                data.to_excel(filename, index=False)
            else:
                print(f"Unsupported file format: {filename}")
                return None
            print(f"Data successfully exported to {filename}")
        except Exception as e:
            print(f"An error occurred while exporting data: {e}")
