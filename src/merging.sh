#/bin/bash

duration=$(mp3info -p "%S" demo.mp3)
echo $duration
video_file=$1
audio_file=$2
merged_file=$3
MP4Box -add $video_file -splitx 0:$duration demo.mp4
MP4Box -add demo.mp4 -add $audio_file $merged_file
rm demo.mp4
