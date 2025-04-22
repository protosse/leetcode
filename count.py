import os

current_path = os.getcwd()
folders = [
    name
    for name in os.listdir(current_path)
    if not name.startswith(".") and os.path.isdir(os.path.join(current_path, name))
]
folders.sort(
    key=lambda x: int(x.split(".")[0]) if x.split(".")[0].isdigit() else float("inf")
)
