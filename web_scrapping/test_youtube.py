from selenium import webdriver
import pandas as pd


url = 'https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=p&flow=grid'

driver = webdriver.Chrome()


driver.get(url)

videos = driver.find_elements_by_id('dismissible')

video_list = []
for a_video in videos:
    title = a_video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = a_video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    when = a_video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text

    vid_item = {
        'title': title,
        'views': views,
        'post_date': when,
    }

    video_list.append(vid_item)

df = pd.DataFrame(video_list)
df.to_csv('./test_youtube.csv')