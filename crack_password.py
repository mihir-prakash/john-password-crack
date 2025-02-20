
import os
import subprocess
import time
from shutil import which


ZIP2JOHN_PATH = which("zip2john") or "/opt/homebrew/Cellar/john-jumbo/1.9.0_1/share/john/zip2john"
JOHN_PATH = which("john") or "/opt/homebrew/bin/john"


ZIP_FILE = "protected.zip"
HASH_FILE = "zip_hash.txt"
WORDLIST_FILE = "custom_wordlist.txt"

def reset_john_session():
    """Ensures John runs fresh by resetting any existing session."""
    potfile_path = os.path.expanduser("~/.john/john.pot")

    if os.path.exists(potfile_path):
        os.remove(potfile_path)
        print(" Resetting John's session (Deleted previous records)\n")
    else:
        print("✅ No existing session found. Proceeding fresh.\n")

def extract_hash():
    
    print("\n🔹 [STEP 1] Extracting password hash...\n")
    command = f"{ZIP2JOHN_PATH} {ZIP_FILE} > {HASH_FILE}"
    os.system(command)
    print(f"✅ Hash extracted and saved in: {HASH_FILE}\n")

def bruteforce_attack():
    
    print("\n [STEP 2] Beginning brute-force attack\n")
    time.sleep(10)  

def run_john_cracker():
   
   
    command = f"{JOHN_PATH} --format=pkzip --wordlist={WORDLIST_FILE} {HASH_FILE}"
    os.system(command)
    print("\n✅ Password cracking simulation completed!\n")

def retrieve_cracked_password():
    
    print("\n [STEP 4] Retrieving cracked password...\n")

    potfile_path = os.path.expanduser("~/.john/john.pot")

    if os.path.exists(potfile_path):
        with open(potfile_path, "r") as potfile:
            lines = potfile.readlines()

        for line in lines:
            parts = line.strip().split(":")
            if len(parts) > 1: 
                cracked_password = parts[-1].strip()  
                print(f" **Cracked Password:** \"{cracked_password}\" \n")
                return

    print("❌ No password found.\n")

if __name__ == "__main__":
    print("\n **Starting ZIP Password Cracking**\n")
    
    reset_john_session()         
    extract_hash()               
    bruteforce_attack() 
    run_john_cracker()           
    retrieve_cracked_password()  
