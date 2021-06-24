from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
import time

def update():
	
	options = webdriver.ChromeOptions()
	options.add_argument("user-data-dir=C:Path")#your chrome profile path 
	
	url = 'https://www.reddit.com/r/subreddit/post_title'#link to your post

	driver = webdriver.Chrome(executable_path=binary_path,options=options)
	driver.get(url)

	edit = 'XPath'#XPath to the edit button
	save = 'XPath'#XPath to the save button
	upvote = 'XPath'#XPath to upvotes
	comment = 'XPath'#XPath to the comments
	edit_box = 'XPath'#XPath to the edit box

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
