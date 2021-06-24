from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
import time
# import praw
# import config
# import requests


def update():
	# user = config.USERNAME
	# passw = config.PASSWORD

	# r = requests.get('https://www.reddit.com/r/teenagers/comments/lobyus/this_is_a_test_to_check_if_i_have_enough_karma/').text
	options = webdriver.ChromeOptions()
	options.add_argument("user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")
	
	url = 'https://www.reddit.com/r/teenagers/comments/o76q4y/uhh_i_might_be_wrong_but_okay/'

	driver = webdriver.Chrome(executable_path=binary_path,options=options)
	# driver.minimize()
	driver.get(url)

	edit = '//*[@id="t3_o76q4y"]/div/div[6]/div[1]/div[3]/button'
	save = '//*[@id="t3_o76q4y"]/div/div[5]/div[2]/button[2]'
	upvote = '//*[@id="vote-arrows-t3_o76q4y"]/div'
	comment = '//*[@id="t3_o76q4y"]/div/div[6]/div[1]/div[1]/span'
	edit_box = '//*[@id="t3_o76q4y"]/div/div[5]/div[1]/div/div[3]/div/div[1]/div/div/div'

	upvotes = driver.find_element_by_xpath(upvote).text
	comments = driver.find_element_by_xpath(comment).text

	edit_post = driver.find_element_by_xpath(edit)
	edit_post.click()

	post = driver.find_element_by_xpath(edit_box)
	post.send_keys(Keys.CONTROL,"a", Keys.DELETE)
	post.send_keys(f"I'm guessing this post has {upvotes} up arrows and {comments}.")
	driver.find_element_by_xpath(save).click()

	time.sleep(1)
	driver.close()
	update()
update()
