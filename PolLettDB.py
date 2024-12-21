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

import os
import numpy as np


#
# file name: PolLettDB.py
#
# polish alphabet data set
# 

#
# load data
#   

def load_pol_lett_db_from_files( fname_db, fname_db_labels):
    labels_count = os.path.getsize( fname_db_labels )
    
    f_data = open( fname_db, 'rb')
    f_labels = open( fname_db_labels, 'rb')
    
    block_size  = 64 * 64
    data_size   = 64 * 64 * ( labels_count )
    
    loaded_data   = np.zeros( data_size,   dtype=np.uint8 )
    loaded_labels = np.zeros( labels_count, dtype=np.uint8 )
    
    for d in range( labels_count ):
        
        iaa_loaded = np.fromfile(f_data, dtype=np.uint8, count=block_size)
        label_loaded = np.fromfile(f_labels, dtype=np.uint8, count=1)
        a= block_size * d
        loaded_data[a:a+block_size]=iaa_loaded
        loaded_labels[d]=label_loaded
        
    f_data.close()
    f_labels.close()

    return loaded_data, loaded_labels, labels_count


