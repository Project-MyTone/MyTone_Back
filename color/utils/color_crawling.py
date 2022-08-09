from selenium import webdriver
from selenium.webdriver.common.by import By
import pymysql


# search_color_cos = input('단어 검색 : ')
# url = f'https://www.google.com/search?q={quote_plus(search_color_cos)}&tbm=isch&ved=2ahUKEwjX_Yr8zaL5AhWeSfUHHSGFB68Q2-cCegQIABAA&oq={quote_plus(search_color_cos)}&gs_lcp=CgNpbWcQAzIFCAAQgAQ6BAgjECc6BAgAEBg6BggAEB4QB1C5BViJDGCKDmgBcAB4AYABowGIAZcJkgEDMC44mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=1y_mYpe2IZ6T1e8PoYqe-Ao&bih=691&biw=1440'
url = 'https://m.blog.naver.com/blanco926/222622673213'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# 여름 쿨톤 상품 이미지 크롤링
images_src = driver.find_elements(By.CSS_SELECTOR, "div[class='se-module se-module-oglink']")
img_scr = []
for src in images_src:
    # img_scr.append(src.get_attribute("src"))

    # 상품 이름
    name = src.find_element(By.CSS_SELECTOR, "a[class='se-oglink-info'] > div > strong")
    # print(name.text)
    name_product = name.text

    # 상품 사진
    img = src.find_element(By.CSS_SELECTOR, "a[class='se-oglink-thumbnail'] > img")
    # print(img.get_attribute("src"))
    img_product = img.get_attribute("src")

    # 상품 구매 링크
    ur = src.find_element(By.CSS_SELECTOR, "a[class='se-oglink-thumbnail']")
    # print(ur.get_attribute("href"))
    ur_product = ur.get_attribute("href")

    list_product = [name_product, img_product, ur_product, 4]

    img_scr.append(list_product)

img_scr.pop()
img_scr.pop()
print(img_scr)

connect = pymysql.connect(host='localhost', user='root', password='1234', db='MyTone', charset='utf8mb4')
cursor = connect.cursor()

for r in img_scr:
    name = str(r[0])
    image = str(r[1])
    url = str(r[2])
    color = int(r[3])

    sql = """insert into cosmetic
    (name, image, url, color_id) values ('%s', '%s', '%s', '%d')
    """ % (name, image, url, color)

    cursor.execute(sql)
    connect.commit()

connect.close()


# 상품 텍스트 크롤링
# images_name = driver.find_element(By.XPATH, '//*[@id="SE-ab63f17a-32ef-47d2-adc4-09ab6283f007"]/div/div/div/a[2]/div/strong')
#
# img_name = []
# print(images_name.text)


# search_color_cos = input('단어 검색 : ')
#
# url = f'https://www.google.com/search?q={quote_plus(search_color_cos)}&tbm=isch&ved=2ahUKEwjX_Yr8zaL5AhWeSfUHHSGFB68Q2-cCegQIABAA&oq={quote_plus(search_color_cos)}&gs_lcp=CgNpbWcQAzIFCAAQgAQ6BAgjECc6BAgAEBg6BggAEB4QB1C5BViJDGCKDmgBcAB4AYABowGIAZcJkgEDMC44mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=1y_mYpe2IZ6T1e8PoYqe-Ao&bih=691&biw=1440'
#
# options = webdriver.ChromeOptions()
# options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
# options.add_argument('disable-gpu')    # GPU 사용 안함
# options.add_argument('lang=ko_KR')    # 언어 설정
# driver = webdriver.Chrome('/Users/iseungmin/PycharmProjects/4th_project/chromedriver', options=options)
# driver.get(url)
#
# links = []
# images = driver.find_elements_by_css_selector('s0Fsx eKtPwd')
# for image in images:
#     if image.get_attribute('src') != None:
#         links.append(image.get_attribute('src'))
#
#
# theater_df = pd.DataFrame(links, columns=['사진'])
# theater_df.index = theater_df.index + 1
#
# theater_df.to_csv(f'color_cos_df.csv', mode='w', encoding='utf-8-sig',
#                    header=True, index=True)