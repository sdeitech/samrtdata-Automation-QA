import os
import json

# Path to Chrome's user data directory
user_data_dir = r"C:\Users\yashgaikwad\AppData\Local\Google\Chrome\User Data"


# Known Chrome profile folders
def is_chrome_profile(name):
    return name == "Default" or name.startswith("Profile")


# List profile folders
profiles = [name for name in os.listdir(user_data_dir) if
            os.path.isdir(os.path.join(user_data_dir, name)) and is_chrome_profile(name)]

print("Chrome Profiles Found:\n")

for profile in profiles:
    pref_path = os.path.join(user_data_dir, profile, "Preferences")

    if os.path.exists(pref_path):
        try:
            with open(pref_path, 'r', encoding='utf-8') as f:
                prefs = json.load(f)
                profile_name = prefs.get("profile", {}).get("name", "Unknown")
                print(f"{profile} → {profile_name}")
        except Exception as e:
            print(f"{profile} → Error reading Preferences: {e}")
    else:
        print(f"{profile} → Preferences file not found.")
