from pyrogram import Client

api_id = input("Enter your API ID: ")
api_hash = input("Enter your API hash: ")

with Client("my_account", api_id, api_hash) as app:
    print("Please enter your phone number when prompted, and then enter the verification code you receive via Telegram.")
    try:
        session_string = app.export_session_string()
        if session_string:
            print("Session string generated successfully:")
            print(session_string)
        else:
            print("Failed to generate session string. Please try again.")
    except Exception as e:
        print("An error occurred:", e)
