# 0.750718518519

file_handle = open("mbox-short.txt")

line_count = 0
total_x_dspam_confidence = 0

for line in file_handle:
    if line.startswith("X-DSPAM-Confidence:"):
        # print(line)
        line_count += 1
        total_x_dspam_confidence += float(line[line.find(":")+1:])

# print(total_x_dspam_confidence)
# print(line_count)
print("Average spam confidence:", total_x_dspam_confidence / line_count)

