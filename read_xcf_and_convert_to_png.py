#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

#/***************************************************************************
# *   Copyright (C) 2024         by Marek Sawerwain                         *
# *                                  <M.Sawerwain@gmail.com>                *
# *                                  <M.Sawerwain@issi.uz.zgora.pl>         *
# *                                                                         *
# *                                                                         *
# *   Part of the PolLettDB:                                                *
# *         https://github.com/qMSUZ/PolLettDB                              *
# *                                                                         *
# * Permission is hereby granted, free of charge, to any person obtaining   *
# * a copy of this software and associated documentation files              *
# * (the “Software”), to deal in the Software without restriction,          *
# * including without limitation the rights to use, copy, modify, merge,    *
# * publish, distribute, sublicense, and/or sell copies of the Software,    *
# * and to permit persons to whom the Software is furnished to do so,       *
# * subject to the following conditions:                                    *
# *                                                                         *
# * The above copyright notice and this permission notice shall be included *
# * in all copies or substantial portions of the Software.                  *
# *                                                                         *
# * THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS *
# * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF              *
# * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  *
# * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY    *
# * CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,    *
# * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH           *
# * THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.              *
# ***************************************************************************/


#import os
import glob
#import numpy as np

#from PIL import Image #, ImageDraw, ImageFilter, ImageEnhance
#from PIL.ImageOps import crop as pil_image_crop


from gimpformats.gimpXcfDocument import GimpDocument


#import matplotlib.pyplot as plt
#import PolLettDB as pld


dir_path_in = "./raw_dataset/*.xcf"
dir_path_out = "./png_files/"

xcf_files = glob.glob( dir_path_in )
xcf_files.sort()

file_count = len(xcf_files)
file_idx=1

for fname in xcf_files:
    print("processing file", file_idx,"/", 
          file_count, ":", fname, "...", end=" ")
    doc = GimpDocument( fname )
    img = doc.layers[0].image
    fnamefile, ext = doc.fileName.split(".")
    img.save(dir_path_out+fnamefile+".png")
    print(" done", end="\n")
    file_idx=file_idx+1

