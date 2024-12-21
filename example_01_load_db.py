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

import PolLettDB as pld
import matplotlib.pyplot as plt

loaded_data, loaded_labels, labels_count = pld.load_pol_lett_db_from_files(
                                                'pol_lett_db.bin', 
                                                'pol_lett_db_labels.bin')

d=1405
block_size=64*64
a=64*64 * d
iaa = loaded_data[a:a+block_size].reshape(64,64)

plt.matshow(iaa,  cmap='gray', vmin=0, vmax=255)

