import os

def get_patient_history_file(patient_id):
    file_name = f"{patient_id}.txt"
    file_path = os.path.join("data", "patient_history", file_name)
    return file_path

def get_patient_name(patient_id):
    file_path = get_patient_history_file(patient_id)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            patient_data = file.read()
        return patient_data.split("\n")[0]
    return None
# # Example usage
# patient_id = 123
# file_path = get_patient_history_file(patient_id)
# if os.path.exists(file_path):
#     print(f"File found: {file_path}")
# else:
#     print(f"File not found, but the path is: {file_path}")
