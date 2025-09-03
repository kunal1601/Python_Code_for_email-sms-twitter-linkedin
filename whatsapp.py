import pywhatkit as kit

    # Take user input for phone number and message
phone_number = input("Enter the recipient's phone number (including country code): ")
message = input("Enter the message you want to send: ")
    
    # Take user input for time
hour = int(input("Enter the hour (in 24-hour format) to send the message: "))
minute = int(input("Enter the minute to send the message: "))

kit.sendwhatmsg(phone_number, message, hour, minute)
