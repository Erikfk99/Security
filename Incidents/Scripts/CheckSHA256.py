import os
import hashlib

#put known hashes which you want to look for in this list:
check_hashes = [
    "2303b3a593b79ea570db7f69ae05bf3aa75377b3e79ad9c708998a4a4370ee29",
    "2303b3a593b79ea570db7f69ae05bf3aa75377b3e79ad9c708998a4a4370ee29",
    "A7F1248BA316824FF515896564AC41A4756416A335FE1D258B2610E7966F6B97",
    "76f860a0e238231c2ac262901ce447e83d840e16fca52018293c6cf611a6807e",
    "fd7cbadcfca84b38380cf57898d0de2adcdfb9c3d64d17f886e8c5903e416039",
]

def calc_sha256(file_path): # calculates sha256
    sha256 = hashlib.sha256()
    
    with open(file_path, "rb") as file: 
        while True: 
            data = file.read(65536) # read in 64kb chunks
            if not data:
                break
            sha256.update(data)
    
    return sha256.hexdigest()

# function to search file system and check hashes to list above
def search_files_by_sha256(directory, check_hashes):
    for root, _, files in os.walk(directory):
        for filename in files: 
            file_path = os.path.join(root, filename)
            file_hash = calc_sha256(file_path)
            if file_hash in check_hashes:
                print(f"File '{file_path}' has a matching SHA-256 hash: {file_hash}")


#Directory containing files to check 
start_directory = "/Users/erikfayekarla/Desktop" #change this to directory you want to check.

search_files_by_sha256(start_directory, check_hashes)


