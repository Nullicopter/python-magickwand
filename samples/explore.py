#!/usr/bin/env python

from magickwand.image import Image
import sys

if __name__=='__main__':
    img = Image(sys.argv[1])
    
    props = ['format', 'units', 'size', 'compression', 'background_color', 'colorspace']
    for p in props:
        print p, getattr(img, p)
    
    img.trim()
    print 'new size', img.size
    
    del img
