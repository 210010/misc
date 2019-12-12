#!/bin/sh
## 받은 트레이닝 데이터가 모두 PCM format이라 FFMPEG를 이용해 Wav파일로 변환
for input_file in `find . -name "*.pcm"`
do
  output_file=`echo $input_file | sed 's/\//-/g' | sed 's/\.-//g' | sed 's/\.pcm/\.wav/g'`
  ffmpeg -v quiet -f s16le -ar 16k -ac 1 -i $input_file $output_file
done
