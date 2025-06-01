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

import PolLettDS as pld
import matplotlib.pyplot as plt

loaded_data, loaded_labels, labels_count = pld.load_pol_lett_ds_from_files(
                                                'pol_lett_ds_mf.bin',
                                                'pol_lett_ds_mf_labels.bin' )

n_set = labels_count // 80
print(f"Number of set: {n_set}")

# Ą
i=0
d=46 + i*80
block_size=64*64
a=64*64 * d
iaa = loaded_data[a:a+block_size].reshape(64,64)
fig, ax = plt.subplots() 
ax.set_axis_off()
ax.matshow(iaa,  cmap='gray', vmin=0, vmax=255)
#plt.savefig("image-1.png")
print("Label as char or digit:", pld.get_char_for_label(loaded_labels[d]))


# k
i=0
d=23 + i*80
block_size=64*64
a=64*64 * d
iaa = loaded_data[a:a+block_size].reshape(64,64)
fig, ax = plt.subplots() 
ax.set_axis_off()
ax.matshow(iaa,  cmap='gray', vmin=0, vmax=255)
#plt.savefig("image-2.png")
print("Label as char or digit:", pld.get_char_for_label(loaded_labels[d]))

# Ż
i=0
d=79 + i*80
block_size=64*64
a=64*64 * d
iaa = loaded_data[a:a+block_size].reshape(64,64)
fig, ax = plt.subplots( ) 
ax.set_axis_off()
ax.matshow(iaa,  cmap='gray', vmin=0, vmax=255)
#plt.savefig("image-3.png")
print("Label as char or digit:", pld.get_char_for_label(loaded_labels[d]))

# 4
i=0
d=4 + i*80
block_size=64*64
a=64*64 * d
iaa = loaded_data[a:a+block_size].reshape(64,64)
fig, ax = plt.subplots( ) 
ax.set_axis_off()
ax.matshow(iaa,  cmap='gray', vmin=0, vmax=255)
#plt.savefig("image-4.png")
print("Label as char or digit:", pld.get_char_for_label(loaded_labels[d]))

# 4
i=1
d=4 + i*80
block_size=64*64
a=64*64 * d
iaa = loaded_data[a:a+block_size].reshape(64,64)
fig, ax = plt.subplots( ) 
ax.set_axis_off()
ax.matshow(iaa,  cmap='gray', vmin=0, vmax=255)
#plt.savefig("image-4.png")
print("Label as char or digit:", pld.get_char_for_label(loaded_labels[d]))

# b
for i in range(n_set):
    d=46 + i*80
    block_size=64*64
    a=64*64 * d
    iaa = loaded_data[a:a+block_size].reshape(64,64)
    fig, ax = plt.subplots( ) 
    ax.set_axis_off()
    ax.matshow(iaa,  cmap='gray', vmin=0, vmax=255)
    #plt.savefig("image-5.png")
    print("Label as char or digit:", pld.get_char_for_label(loaded_labels[d]))


