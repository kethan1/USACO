with open("billboard.in") as input_file:
    lawn_x1, lawn_y1, lawn_x2, lawn_y2 = map(int, input_file.readline().split())
    feed_x1, feed_y1, feed_x2, feed_y2 = map(int, input_file.readline().split())

tarp_size = (lawn_x2 - lawn_x1) * (lawn_y2 - lawn_y1)

if feed_x1 <= lawn_x1 and lawn_x2 <= feed_x2:
    if feed_y1 <= lawn_y1 and feed_y2 >= lawn_y2:
        tarp_size = 0
    elif lawn_y1 <= feed_y2 <= lawn_y2 and not lawn_y1 <= feed_y1 <= lawn_y2:
        tarp_size -= (feed_y2 - lawn_y1) * (lawn_x2 - lawn_x1)
    elif lawn_y1 <= feed_y1 <= lawn_y2 and not lawn_y1 <= feed_y2 <= lawn_y2:
        tarp_size -= (lawn_y2 - feed_y1) * (lawn_x2 - lawn_x1)

elif feed_y1 <= lawn_y1 and lawn_y2 <= feed_y2:
    if lawn_x1 <= feed_x2 <= lawn_x2 and not lawn_x1 <= feed_x1 <= lawn_x2:
        tarp_size -= (feed_x2 - lawn_x1) * (lawn_y2 - lawn_y1)
    elif lawn_x1 <= feed_x1 <= lawn_x2 and not lawn_x1 <= feed_x2 <= lawn_x2:
        tarp_size -= (lawn_x2 - feed_x1) * (lawn_y2 - lawn_y1)


with open("billboard.out", "w") as output_file:
    output_file.write(str(tarp_size))
