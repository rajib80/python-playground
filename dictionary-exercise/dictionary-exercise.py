# Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's
# mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through
# the dictionary using a maximum loop to find the most prolific committer.

file_handler = open("mbox-short.txt")

mail_count = dict()

for line in file_handler:
    if not line.startswith("From:") and line.startswith("From"):
        words = line.split()
        mail_count[words[1]] = mail_count.get(words[1], 0) + 1

max_mail_count = None
max_mail_sender = None

for mail_sender, number_of_mail in mail_count.items():
    if max_mail_count is None or max_mail_count < number_of_mail:
        max_mail_count = number_of_mail
        max_mail_sender = mail_sender

print(max_mail_sender, max_mail_count)
