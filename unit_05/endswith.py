#!/usr/bin/env/python
s = "Today is a good day"
s.startswith("Today")


s.startswith("is", 6, 15)


s = "Today is a good day"
suffix = "day"
s.endswith("day")


s.endswith("day", 2, 8)


filename = "photo_22052014.jpg"
if filename.lower().endswith((".jpg", ".jpeg")):
print(filename, "is a JPEG image")


def ContReader(infile):
    lines = []
    for line in infile:
        line = line.rstrip()
        if line.endswith("\\"):
            lines.append(line[:-1])
            continue
        lines.append(line)
        yield "".join(lines)
        lines = []
    if lines:
        yield "".join(lines)

for line in ContReader(datafile):
    pass # process full record in 'line' here
