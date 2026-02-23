print("Vision Chatbot started")
print("--------------------------------")
print("This chatbot gives educational guidance only.")
print("It is NOT a medical diagnosis.")
print("Do you want to continue? (yes/no)")

consent = input("> ")

if consent.lower() != "yes":
    print("Okay — exiting. Stay safe.")
    exit()


while True:
    user = input("Describe your vision problem: ")

    if user.lower() == "quit":
        print("Goodbye")
        break

    msg = user.lower()

    # --- safety red flags ---
    if "pain" in msg or "flash" in msg or "floater" in msg or "sudden" in msg:
        print("- ⚠️ Warning signs detected.")
        print("- Sudden vision change, flashes, floaters, or pain can be serious.")
        print("- Recommended next step: seek urgent eye care.")
        continue

    # --- distance / near detection ---
    if "distance" in msg or "far" in msg:
        eye = input("Is it in one eye or both eyes? ")
        onset = input("Did it start suddenly or gradually? ")

        print("- You mentioned blurry distance vision.")
        print(f"- Affected: {eye}")
        print(f"- Onset: {onset}")
        print("- This often happens when prescription needs updating.")
        print("- Next step: consider a routine eye exam.")

    elif "near" in msg or "reading" in msg or "close" in msg:
        eye = input("Is it in one eye or both eyes? ")
        onset = input("Did it start suddenly or gradually? ")

        print("- You mentioned blurry near vision.")
        print(f"- Affected: {eye}")
        print(f"- Onset: {onset}")
        print("- This can be due to focusing changes or eye strain.")
        print("- Next step: consider a routine eye exam.")

    else:
        print("- I can currently help with near blur or distance blur.")
        print("- Please tell me if the blur is at NEAR or DISTANCE.")
