# coding:utf-8
__author__ = 'Helen'
'''
description:UI页面公共类
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage():

      def __init__(self,driver):
          self.driver = driver

      def find_element(self,*loc):
          try:
              WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
              return self.driver.find_element(*loc)
          except Exception as err:
              raise err

      def send_keys(self,value,*loc):
          try:
              self.find_element(*loc).clear()
              self.find_element(*loc).send_keys(value)
          except AttributeError as err:
              raise err

      def scroll_to(self, start, stop, duration):
          "scroll"
          try:
              self.driver.scroll(self.find_element(*start), self.find_element(*stop), duration)
          except Exception as err:
              raise err




























