#!/usr/bin/env python
from cv2 import imshow, waitKey
import image_conversion
import rosbag
import rospy

# Read the bagfile
bag = rosbag.Bag('hiwi_test.bag')

# Extract topics
topics = bag.get_type_and_topic_info().topics
topic_name_list = topics.keys()
for i in range(len(topic_name_list)):
  topic = topic_name_list[i]
  info = topics[topic]
  print("Topic: {} Type: {}".format(topic, info.msg_type))

# If you want to output just the first image, please set this parameter to False.
more_image_output = True

# Load and show first image
if not more_image_output:
  bag_messages = bag.read_messages(topics='/camera/color/record/image_raw')
  single_image_data = bag_messages.next()
  msg = single_image_data.message
  width = msg.width
  height = msg.height
  img = image_conversion.data_to_image(msg.data, width, height)
  imshow("bag image", img) # Output the first image.
  waitKey()

# More images with 0.5 seconds between timestamps
else:
  bag_messages = bag.read_messages(topics='/camera/color/record/image_raw')
  single_image_data = bag_messages.next()
  msg = single_image_data.message
  width = msg.width
  height = msg.height
  img = image_conversion.data_to_image(msg.data, width, height)
  time_last = msg.header.stamp.to_sec() 	# Initialize time.
  imshow("bag image", img) 	# Output the first image.
  waitKey()
  
  # To find next image.
  while True:
    single_image_data = bag_messages.next()
    msg = single_image_data.message
    time = msg.header.stamp.to_sec()

    # Once the time between an image and the last image is more than 0.5 seconds, this image will be outputted. Otherwise it will enter the next loop to find the right image.
    if time - time_last >= 0.5: 		# To adjust the time interval between two images, you may set this parameter to another value (e.g. time - time_last >= 0.2).
      time_last = time
      width = msg.width
      height = msg.height
      img = image_conversion.data_to_image(msg.data, width, height)
      imshow("bag image", img)  	# Output the image. 
      waitKey()
    else:
      pass


