import json

with open ("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)

# # Create
# username = input("masukkan username baru: ")
# password = input("masukkan Password baru: ")
# data_baru = {
#     "username":username,
#     "password":password,
#     "role":"user"
# }

# # Update
# username = input("Masukkan username yang ingin diupdate: ")
# for akun in data:
#     if akun["username"] == username:
#         akun["username"] = input("Masukkan username baru: ")
#         akun["password"] = input("Masukkan password baru: ")

# Delete
# username = input("Masukkan username yang ingin dihapus: ")
# for akun in data:
#     if akun["username"] == username:
#         data.remove(akun)

# with open (r"data.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4)

