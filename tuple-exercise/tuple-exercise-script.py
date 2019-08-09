# Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and
# then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

file_handle = open("mbox-short.txt")

message_count_by_hour = dict()

for line in file_handle:
    if not line.startswith("From:") and line.startswith("From"):
        words = line.split()
        # print(words[5])
        hours = words[5].split(":")
        # print(hours)
        # print(int(hours[0]))
        # hour = int(hours[0])
        message_count_by_hour[hours[0]] = message_count_by_hour.get(hours[0], 0) + 1

# print(sorted(message_count_by_hour.items()))
for hour, count in sorted(message_count_by_hour.items()):
    print(hour, count)

