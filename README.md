# Magic Packet helper thingy

## Description

Checks if the public IP address of the computer has changed, and sends me an email if so.

## Instructions

I'm sorry I didn't put much effort into making the instructions easy to follow, I only spent like an hour doing this from start to finish so it's not the kind of thing I wanted to put a lot of time/effort in.

1. Download `script.py` and `addresses.txt`
2. Go to the your google account and generate an `app password` (not the same thing as the normal password)
3. Copy and paste the generated `app password` into a file in the same folder as the script and call it `password.txt`
4. Replace all the email addresses in the file `script.py` with your gmail address
5. If you're on Windows, use `Task Scheduler` to make the script run every hour (or however often you want it to run)
6. If you're on Linux or MacOS, use `cron` or something
7. (Optional) Replace the IP in `addresses.txt` with your current one to prevent the script sending you an email right away needlessly
8. Yay, you're done! Now you'll get an email if your IP ever changes (check your spam folder though lol)

## Author

> [Youssef Guindi](https://www.github.com/YoussefWindy "GitHub")
