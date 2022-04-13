#set -x
FONT="/Applications/GarageBand.app/Contents/Frameworks/MAWorkspace.framework/Versions/A/Resources/Fonts/BradleyHand-Bold.ttf"
mkdir stamped

total=$(expr `ls *.jpg|wc -l`)
i=0
for img in *.jpg; do
    img_height=$(identify -format "%h" $img)
    FONT_SIZE=$(echo "$img_height * 0.1 / 4 "|bc -l)
    img_date=$(identify -format "%[EXIF:DateTime]" $img)
    my_date=$(date -j -u -f "%Y:%m:%d %H:%M:%S" "$img_date" +"%Y/%m/%d")
    convert "$img"  -font "$FONT" -gravity SouthEast -pointsize $FONT_SIZE \
        -fill white -annotate +30+30 \
        $my_date "stamped/""$img";
    i=$(expr $i + 1)
    echo "processed [$i/$total]\r\c"
done
