from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.chromium('./chromiumdriver')

driver.get("https://img3.gelbooru.com//samples/63/0a/sample_630a062d709fc831741f4b70d309c98a.jpg")

img = document.getElementById("shrinkToFit")

print(img)
canvas = document.createElement('canvas')
canvas.width = img.width
canvas.height = img.height
ctx = canvas.getContext("2d")
