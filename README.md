# misc
프로젝트 진행 중, 이런 저런 잡다한 것들 모아둔 곳...

* TEXT Encoding 변환
<pre><code>iconv -f CP949 -t UTF-8 test.txt > out.txt</code></pre>

* PCM to WAV
<pre><code>
for input_file in `find . -name "*.pcm"`
do
  output_file=`echo $input_file | sed 's/\//-/g' | sed 's/\.-//g' | sed 's/\.pcm/\.wav/g'`
  ffmpeg -v quiet -f s16le -ar 16k -ac 1 -i $input_file $output_file
done
</code></pre>
