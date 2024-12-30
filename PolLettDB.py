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

from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

#
# file name: PolLettDB.py
#

labels = {
    '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, 
    '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
    
    'a' : 10, 'ą' : 11, 'b' : 12, 'c' : 13, 'ć' : 14,
    'd' : 15, 'e' : 16, 'ę' : 17, 'f' : 18, 'g' : 19,
    'h' : 20, 'i' : 21, 'j' : 22, 'k' : 23, 'l' : 24,
    'ł' : 25, 'm' : 26, 'n' : 27, 'ń' : 28, 'o' : 29,
    'ó' : 30, 'p' : 31, 'q' : 32, 'r' : 33, 's' : 34,
    'ś' : 35, 't' : 36, 'u' : 37, 'v' : 38, 'w' : 39,
    'x' : 40, 'y' : 41, 'z' : 42, 'ź' : 43, 'ż' : 44,

    'A' : 50, 'Ą' : 51, 'B' : 52, 'C' : 53, 'Ć' : 54,
    'D' : 55, 'E' : 56, 'Ę' : 57, 'F' : 58, 'G' : 59,
    'H' : 60, 'I' : 61, 'J' : 62, 'K' : 63, 'L' : 64,
    'Ł' : 65, 'M' : 66, 'N' : 67, 'Ń' : 68, 'O' : 69,
    'Ó' : 70, 'P' : 71, 'Q' : 72, 'R' : 73, 'S' : 74,
    'Ś' : 75, 'T' : 76, 'U' : 77, 'V' : 78, 'W' : 79,
    'X' : 80, 'Y' : 81, 'Z' : 82, 'Ź' : 83, 'Ż' : 84
    }

inverse_labels_dict = {value: key for key, value in labels.items()}

_letters_offset_dictionary = {
    
    'a' :  0, 'ą' :  1, 'b' :  2, 'c' :  3, 'ć' : 4,
    'd' :  5, 'e' :  6, 'ę' :  7, 'f' :  8, 'g' : 9,
    'h' : 10, 'i' : 11, 'j' : 12, 'k' : 13, 
    
    'l' :  0, 'ł' :  1, 'm' :  2, 'n' :  3, 'ń' : 4, 
    'o' :  5, 'ó' :  6, 'p' :  7, 'q' :  8, 'r' : 9,
    's' : 10, 'ś' : 11, 't' : 12, 'u' : 13, 
    
    'v' : 0, 'w' : 1, 'x' : 2, 'y' : 3, 'z' : 4, 'ź' : 5, 'ż' : 6,

    'A' :  0, 'Ą' :  1, 'B' :  2, 'C' : 3, 'Ć' : 4,
    'D' :  5, 'E' :  6, 'Ę' :  7, 'F' : 8, 'G' : 9,
    'H' : 10, 'I' : 11, 'J' : 12, 'K' : 13, 
    
    'L' :  0, 'Ł' :  1, 'M' :  2, 'N' :  3, 'Ń' : 4, 
    'O' :  5, 'Ó' :  6, 'P' :  7, 'Q' :  8, 'R' : 9,
    'S' : 10, 'Ś' : 11, 'T' : 12, 'U' : 13, 
    
    'V' : 0, 'W' : 1, 'X' : 2, 'Y' : 3, 'Z' : 4, 'Ź' : 5, 'Ż' : 6
    
    }



def get_char_for_label( _label ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 

    if _label in labels.values():
        return inverse_labels_dict[_label]
    else:
        return None

def get_digit_for_label( _label ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 

    return get_char_for_label( _label )

def get_letter_for_label( _label ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 

    return get_char_for_label( _label )

def get_label_for_digit( _digit ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 

    if _digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return get_label_for_char( _digit )
    else:
        return None

def get_label_for_letter( _letter ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 

    if _letter in ['a', 'ą', 'b', 'c', 'ć',
                   'd', 'e', 'ę', 'f', 'g',
                   'h', 'i', 'j', 'k', 'l',
                   'ł', 'm', 'n', 'ń', 'o',
                   'ó', 'p', 'q', 'r', 's',
                   'ś', 't', 'u', 'v', 'w',
                   'x', 'y', 'z', 'ź', 'ż',
                   'A', 'Ą', 'B', 'C', 'Ć',
                   'D', 'E', 'Ę', 'F', 'G',
                   'H', 'I', 'J', 'K', 'L',
                   'Ł', 'M', 'N', 'Ń', 'O',
                   'Ó', 'P', 'Q', 'R', 'S',
                   'Ś', 'T', 'U', 'V', 'W',
                   'X', 'Y', 'Z', 'Ź', 'Ż']:
        return get_label_for_char( _letter )
    else:
        return None


def get_label_for_char( _char ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 
    
    lbl = -1
    
    try:
        lbl = labels[ _char ]
    except:
        lbl = None
        
    return lbl


# TODO: check the value of _digit (allow values: 0,1,2,3,...,8,9)
def coords_for_digit( _digit ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 
    
    _digit=int(_digit)
    xg=64
    yg=128

    xg = xg + (_digit*64)
    
    return (xg, yg)

# TODO: check the value of letter (allow values: a,ą,b,...,x,y,z,ź,ż,
# and A,Ą,B,...,X,Y,Z,Ź,Ż,
def coords_for_letter( _letter ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 
    
    xg = -1
    yg = -1
    
    if _letter in ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 
                   'g', 'h', 'i', 'j', 'k']:
        xg = 64  + (_letters_offset_dictionary[ _letter ] * 64) 
        yg = 256
        
        return (xg, yg)


    if _letter in ['l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'q',
                   'r', 's', 'ś', 't', 'u']:
        xg = 64  + (_letters_offset_dictionary[ _letter ] * 64) 
        yg = 384
        
        return (xg, yg)

    if _letter in ['v', 'w', 'x', 'y', 'z', 'ź', 'ż']:
        xg = 64  + (_letters_offset_dictionary[ _letter ] * 64) 
        yg = 512
        
        return (xg, yg)


    if _letter in ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 
                   'G', 'H', 'I', 'J', 'K']:
        xg = 64  + (_letters_offset_dictionary[ _letter ] * 64) 
        yg = 640
        
        return (xg, yg)


    if _letter in ['L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'Q',
                   'R', 'S', 'Ś', 'T', 'U']:
        xg = 64  + (_letters_offset_dictionary[ _letter ] * 64) 
        yg = 768
        
        return (xg, yg)

    if _letter in ['V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż']:
        xg = 64  + (_letters_offset_dictionary[ _letter ] * 64) 
        yg = 896
        
        return (xg, yg)

         

    return (xg, yg)

    
def get_digit_image_from_document( im, _digit ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 

    #xg=64
    #yg=128
    
    xg,yg = coords_for_digit( _digit )
    
    (box_left, box_upper, box_right, box_lower) = (xg, yg, xg+64, yg+64) 
    im_crop = im.crop((box_left, box_upper, box_right, box_lower))
    # draw black lines
    # to remove white box
    draw = ImageDraw.Draw(im_crop)
    draw.line( [ (0, 0), (63, 0) ], fill = (0, 0, 0, 0) )
    draw.line( [ (0, 0), (0, 63) ], fill = (0, 0, 0, 0) )
    
    return im_crop


def get_letter_from_document( im, _letter ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 
    
    xg,yg = coords_for_letter( _letter )
    
    (box_left, box_upper, box_right, box_lower) = (xg, yg, xg+64, yg+64) 
    im_crop = im.crop((box_left, box_upper, box_right, box_lower))
    # draw black lines
    # to remove white box
    draw = ImageDraw.Draw(im_crop)
    draw.line( [ (0, 0), (63, 0) ], fill = (0, 0, 0, 0) )
    draw.line( [ (0, 0), (0, 63) ], fill = (0, 0, 0, 0) )
    
    return im_crop
    

#convert_xcf_files_to_png( './raw_dataset/*.xcf' )

def get_digits( doc, with_blur=1 ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 

    output_array=None

    for digit in [0,1,2,3,4,5,6,7,8,9]:
        im = get_digit_image_from_document(doc, digit)
         
        bbox = im.getbbox()
        
        #
        # centering image
        im_crop = im.crop(bbox)
        
        (width, height) = im.size
        (sx, sy) = im_crop.size
        
        pad_x = (width // 2) - (sx // 2)
        pad_y = (height // 2) - (sy // 2)
        
        cropped_im = Image.new("RGBA", (width, height), (0,0,0))

        # Paste the cropped image onto the new image
        cropped_im.paste(im_crop, (pad_x, pad_y))
        # end of centering
        #

        
        # additional blur
        cropped_im_blur = cropped_im.filter(ImageFilter.GaussianBlur(radius = 0.75)) 

        cropped_im_blur = ImageEnhance.Contrast(cropped_im_blur).enhance(5)
        

        iaa = np.asarray( cropped_im_blur )

        if output_array is None:
            output_array=iaa.flatten()
        else:
            output_array=np.concatenate( (output_array, iaa.flatten()), axis=0 )
            
    return output_array


def get_small_letters( doc, with_blur=1 ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 
    
    output_array=None
    
    for letter in ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'ź', 'ż']:
        im = get_letter_from_document(doc, letter)
         
        #
        # centering image
        bbox = im.getbbox()
        
        im_crop = im.crop(bbox)
        
        (width, height) = im.size
        (sx, sy) = im_crop.size
        
        pad_x = (width // 2) - (sx // 2)
        pad_y = (height // 2) - (sy // 2)
        
        cropped_im = Image.new("RGBA", (width, height), (0,0,0))
    
        # Paste the cropped image onto the new image
        cropped_im.paste(im_crop, (pad_x, pad_y))
        # end of centering
        #

        # additional blur
        cropped_im_blur = cropped_im.filter(ImageFilter.GaussianBlur(radius = 0.75)) 

        cropped_im_blur = ImageEnhance.Contrast(cropped_im_blur).enhance(5)
        

        iaa = np.asarray( cropped_im_blur )

        if output_array is None:
            output_array=iaa.flatten()
        else:
            output_array=np.concatenate( (output_array, iaa.flatten()), axis=0 )
            
    return output_array


def get_big_letters( doc, with_blur=1 ):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 
    
    output_array=None
    
    for letter in ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż']:
        im = get_letter_from_document(doc, letter)
         
        #
        # centering image
        bbox = im.getbbox()
        
        im_crop = im.crop(bbox)
        
        (width, height) = im.size
        (sx, sy) = im_crop.size
        
        pad_x = (width // 2) - (sx // 2)
        pad_y = (height // 2) - (sy // 2)
        
        cropped_im = Image.new("RGBA", (width, height), (0,0,0))
    
        # Paste the cropped image onto the new image
        cropped_im.paste(im_crop, (pad_x, pad_y))
        # end of centering
        #

        # additional blur
        cropped_im_blur = cropped_im.filter(ImageFilter.GaussianBlur(radius = 0.75)) 

        cropped_im_blur = ImageEnhance.Contrast(cropped_im_blur).enhance(5)
        
        iaa = np.asarray( cropped_im_blur )
        
        if output_array is None:
            output_array=iaa.flatten()
        else:
            output_array=np.concatenate( (output_array, iaa.flatten()), axis=0 )
            
    return output_array


def convert_array_to_gray_values( iaa ):
    """
    TODO

    Parameters
    ----------
    iaa : numpy array contains pixel in gray scale (0 -- 255)
        

    Returns
    -------
        output_image

    """    
    
    xidx=0
    yidx=0
    
    output_image = np.zeros( (64, 64), dtype=np.uint8)
    
    for xidx in range(0, 64):
        for yidx in range(0, 64):
            pixel = iaa[xidx,yidx]
            
            _v_red = pixel[0]
            _v_green = pixel[1]
            _v_blue = pixel[2]
            
            _gray = 0.299 * _v_red + 0.587 * _v_green + 0.114 * _v_blue
            
            output_image[xidx, yidx] = np.uint8(_gray)

    return output_image



#
# load data
#   

def load_pol_lett_db_from_files( fname_db, fname_db_labels):
    """
    TODO

    Parameters
    ----------
    aaa : type  description
        

    Returns
    -------
        description

    """ 

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

def create_handles_for_db( leading_name ):
    fImages = open(leading_name + '.bin', 'wb')
    fLabels = open(leading_name + '_labels.bin', 'wb')
    
    return fImages, fLabels
    
def dump_data_to_file( fImages, fLabels, documentName):
    doc = Image.open( documentName )

    # extract digit and put it into file
    
    digits_data = get_digits( doc , with_blur=1)
    digits_output_label=np.zeros( 1, dtype=np.uint8 )
    
    small_letters_data = get_small_letters( doc , with_blur=1)
    small_letters_output_label=np.zeros( 1, dtype=np.uint8 )
    
    big_letters_data = get_big_letters( doc , with_blur=1)
    big_letters_output_label=np.zeros( 1, dtype=np.uint8 )
    
    
    for d in [0,1,2,3,4,5,6,7,8,9]:
        
        block=16384
        a=16384 * d
        iaa = digits_data[a:a+block].reshape(64,64,4)
        
        #plt.matshow(iaa)
        
        output_image = convert_array_to_gray_values( iaa )
        
        digits_output_label[0] = d
        
        output_image.tofile(fImages)
        digits_output_label.tofile(fLabels)
        
        
    for lpair in [ ( 0, 'a'), ( 1, 'ą'), ( 2, 'b'), ( 3, 'c'), ( 4, 'ć'), ( 5, 'd'),
                   ( 6, 'e'), ( 7, 'ę'), ( 8, 'f'), ( 9, 'g'), (10, 'h'), (11, 'i'),
                   (12, 'j'), (13, 'k'), (14, 'l'), (15, 'ł'), (16, 'm'), (17, 'n'),
                   (18, 'ń'), (19, 'o'), (20, 'ó'), (21, 'p'), (22, 'q'), (23, 'r'),
                   (24, 's'), (25, 'ś'), (26, 't'), (27, 'u'), (28, 'v'), (29, 'w'),
                   (30, 'x'), (31, 'y'), (32, 'z'), (33, 'ź'), (34, 'ż') ]: 
        
        block=16384
        a=16384 * lpair[0]
        iaa = small_letters_data[ a:a+block ].reshape(64,64,4)
        
        #plt.matshow(iaa)
        
        output_image = convert_array_to_gray_values( iaa )
        
        small_letters_output_label[0] = get_label_for_letter( lpair[1] )
        
        output_image.tofile(fImages)
        small_letters_output_label.tofile(fLabels)
        
        
    for lpair in [ ( 0, 'A'), ( 1, 'Ą'), ( 2, 'B'), ( 3, 'C'), ( 4, 'Ć'), ( 5, 'D'),
                   ( 6, 'E'), ( 7, 'Ę'), ( 8, 'F'), ( 9, 'G'), (10, 'H'), (11, 'I'),
                   (12, 'J'), (13, 'K'), (14, 'L'), (15, 'Ł'), (16, 'M'), (17, 'N'),
                   (18, 'Ń'), (19, 'O'), (20, 'Ó'), (21, 'P'), (22, 'Q'), (23, 'R'),
                   (24, 'S'), (25, 'Ś'), (26, 'T'), (27, 'U'), (28, 'V'), (29, 'W'),
                   (30, 'X'), (31, 'Y'), (32, 'Z'), (33, 'Ź'), (34, 'Ż') ]:
        
        block=16384
        a=16384 * lpair[0]
        iaa = big_letters_data[ a:a+block ].reshape(64,64,4)
        
        #plt.matshow(iaa)
        
        output_image = convert_array_to_gray_values( iaa )
        
        big_letters_output_label[0] = get_label_for_letter( lpair[1] )
        
        output_image.tofile(fImages)
        big_letters_output_label.tofile(fLabels)
        

def close_handles( fImages, fLabels):
    fImages.close()
    fLabels.close()


