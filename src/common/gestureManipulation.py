# coding:utf-8
__author__ = 'jack'
'''
description: 手势操作
'''


class GestureManipulation:
    def __base_swipe(self, driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return x, y

    def swipe_right(self, driver, duration: int):
        '''右滑'''
        x, y = self.__base_swipe(driver)
        driver.swipe(x * 3 / 4, y / 4, x / 4, y / 4, duration)

    def swipe_left(self, driver, duration: int):
        '''左滑'''
        x, y = self.__base_swipe(driver)
        driver.swipe(x / 4, y / 4, x * 3 / 4, y / 4, duration)

    def swipe_up(self, driver, duration: int):
        '''上滑'''
        x, y = self.__base_swipe(driver)
        driver.swipe(x / 2, y * 3 / 4, x / 2, y / 4, duration)

    def swipe_down(self, driver, duration: int):
        '''下滑'''
        x, y = self.__base_swipe(driver)
        driver.swipe(x / 2, y / 4, x / 2, y * 3 / 4, duration)

    def swipe_value(self, driver, duration: int, x1, y1, x2, y2):

        '''自定义，底层代码A：int，代表时间的时长，需要用int这个格式'''
        x = driver.get_window_size()["width"]
        y = driver.get_window_size()["height"]
        driver.swipe(x * x1, y * y1, x * x2, y * y2, duration)