# misc
프로젝트 진행 중, 이런 저런 잡다한 것들 모아둔 곳...

* TEXT Encoding 변환
  + ICONV on terminal
  <pre>
  <code>
    iconv -f CP949 -t UTF-8 test.txt > out.txt
  </code>
  </pre>
  
  + Python Code
  <pre>
  <code>
  for entry in listOfFiles:
	if fnmatch.fnmatch(entry, pattern):
		_fileName = open(entry,"r",encoding='cp949')
		if _fileName.mode == "r":
			content = _fileName.read()
			# content = content.decode('cp949').encode('utf-8')
			# content = content.decode('euckr').encode('utf-8')
			print(content)
  </code>
  </pre>

* PCM to WAV
<pre><code>
for input_file in `find . -name "*.pcm"`
do
  output_file=`echo $input_file | sed 's/\//-/g' | sed 's/\.-//g' | sed 's/\.pcm/\.wav/g'`
  ffmpeg -v quiet -f s16le -ar 16k -ac 1 -i $input_file $output_file
done

</code></pre>
