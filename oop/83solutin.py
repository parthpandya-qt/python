import win32com.client

# List of names
names = ["Parth", "Krishna", "Shivam", "Sahil", "Aman", "Anshul", "Ankush", "Ankit", "Ashish", "Aayush"]

# Initialize the Windows speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Speak each name
for name in names:
    speaker.Speak(f"Shoutout to {name}")
