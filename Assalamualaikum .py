import requests
import time

# Get the user's Facebook login credentials
username = input("Enter your Facebook username: ")
password = input("Enter your Facebook password: ")

# Get the group ID
group_id = input("Enter the group ID: ")

# Get the link to the post that you want to share
post_link = input("Enter the link to the post that you want to share: ")

# Set the start, end, and sleep times
start_time = input("Enter the start time (in 24-hour format): ")
end_time = input("Enter the end time (in 24-hour format): ")
sleep_time = int(input("Enter the sleep time (in seconds): "))


# Start the loop
while True:
    # Check if it is within the start and end times
    if time.strftime("%H:%M") >= start_time and time.strftime("%H:%M") <= end_time:
        # Post the link to the group
        response = requests.post("https://graph.facebook.com/v2.12/groups/" + group_id + "/feed",
                                params={"access_token": username + "|" + password},
                                data={"link": post_link})

        # Display the timer
        print("Posting at " + time.strftime("%H:%M"))

        # Display whether the post was successful or failed
        if response.status_code == 200:
            print("Post successful!")
        else:
            print("Post failed!")
            print("Post Failed".center(50, "="))

    # Sleep for the specified amount of time
    time.sleep(sleep_time)
