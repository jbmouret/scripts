#!/bin/sh
# usage: gs.sh input.pdf output.pdf
# goal: make the pdf smaller by putting all the images at 600dpi
echo $1
echo $2
gs \
  -sOutputFile=$2 \
   -sDEVICE=pdfwrite \
   -sNOPAUSE  \
  -dBATCH \
  -dCompatibilityLevel=1.4 \
  -dEmbedAllFonts=true \
  -dSubsetFonts=true \
  -dConvertCMYKImagesToRGB=true \
  -dCompressFonts=true \
  -dDownsampleColorImages=true \
  -dDownsampleGrayImages=true \
  -dDownsampleMonoImages=true \
  -dColorImageResolution=600 \
  -dGrayImageResolution=600 \
  -dMonoImageResolution=600 \
  -dCompatibilityLevel=1.4 \
  -f $1

