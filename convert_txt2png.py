#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 18-12-11
@Author  : leemiracle
"""
from PIL import Image,ImageFont,ImageDraw


fnt = ImageFont.truetype('/Lib/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-R.ttf', 15)


def render_by_pygame(s, path="image.jpg"):
    import pygame
    pygame.init()
    # 设置字体和字号
    font = pygame.font.SysFont('Microsoft YaHei', 64)
    # 渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
    ftext = font.render(s, True, (65, 83, 130), (255, 255, 255))
    pygame.image.save(ftext, path)  # 图片保存地址


def render_by_pil(s, path="image.jpg"):
    # todo 去掉行高
    sl = s.split("\n")
    height = len(sl)*20
    width = max([len(l) for l in sl])*10
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.multiline_text((5, 5), s, font=fnt, fill=(0, 0, 0), spacing=4)
    # d.text((10, 10), s, font=fnt, fill=(0, 0, 0))
    img.save(path)

def main():
    with open("/home/lwz/project/favorite/flask_tree.txt", "r+") as f:
        txt = f.readlines()
    s = "\n".join(txt)
    # render_by_pygame(s) # height too large
    render_by_pil(s)


if __name__ == '__main__':
    main()
