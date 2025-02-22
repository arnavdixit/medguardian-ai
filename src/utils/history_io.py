import os

def get_patient_history_file(patient_id):
    file_name = f"{patient_id}.txt"
    file_path = os.path.join("data", "patient_history", file_name)
    return file_path

def get_patient_name(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            while True:
                line = file.readline()
                if line.startswith("Name"):
                    name = line.split(":")[1].strip()
                    return name
                if not line:
                    break
    return None
# # Example usage
# patient_id = 123
# file_path = get_patient_history_file(patient_id)
# if os.path.exists(file_path):
#     print(f"File found: {file_path}")
# else:
#     print(f"File not found, but the path is: {file_path}")
