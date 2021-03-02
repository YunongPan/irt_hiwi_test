# irt_ws
Workshop for IRT HiWi test.

## Installation
1. Open a terminal and clone this repository.  
  
	`cd ~`  
  
	`git clone https://github.com/YunongPan/irt_ws.git`  
  
2. Install dependencies.  
  
	`cd ~/irt_ws`  
  
	`rosdep install --from-paths src --ignore-src -r -y`  
  
3. Build the workspace.  
  
	`catkin_make`  
  
	
## Testing
1. Start roscore.
  
	`roscore`  
  
2. Start another terminal and source the environment.
  
	`source ~/irt_ws/devel/setup.bash`  
  
3. Start `image_creator.py`.
  
	`cd ~/irt_ws/src/image_output/bagfile`  
  
  	`rosrun image_output image_creator.py`  
  
  	*Before start the py.file please don't forget to set* `image_creator.py` *as an executable file:*  
  
	*Right click on* `image_creator.py` --> *Properties* --> *Permissions* --> *Allow executing file as program*
  
4. Change output model.  
  
	*If you want to output just the first image, please open* `image_creator.py`, *then set the parameter* `more_images_output`  *to* `False`.  
  
	*If you want to adjust the time interval between two output images, you may set* `time - time_last >= 0.5` *to another value (e.g.* `time - time_last >= 0.2`*).* 
  
## Result
1. Output first image.
  
  	![image](https://raw.githubusercontent.com/YunongPan/readme_add_pic/main/IRT_first_image.png)
	![image](https://raw.githubusercontent.com/YunongPan/readme_add_pic/main/IRT_topic.png)
  
2. Output more images.
  
  	![image](https://raw.githubusercontent.com/YunongPan/readme_add_pic/main/IRT_first_image.png)
	![image](https://raw.githubusercontent.com/YunongPan/readme_add_pic/main/IRT_2_image.png)
  	![image](https://raw.githubusercontent.com/YunongPan/readme_add_pic/main/IRT_3_image.png)
	![image](https://raw.githubusercontent.com/YunongPan/readme_add_pic/main/IRT_4_image.png)
	![image](https://raw.githubusercontent.com/YunongPan/readme_add_pic/main/IRT_5_image.png)
