from mutagen.flac import FLAC
from mutagen.mp3 import MP3
import os

cwd = os.getcwd()
m3u8 = input('Path (ex. C:\\music\\.m3u8): ')

lengths = []
with open(m3u8, 'r', encoding='utf-8-sig') as playlist:
	paths = playlist.readlines()
	for path in paths[1:]:
		path = path.replace("\n", "")

		try:
			length = FLAC(path).info.length
		except:
			length = MP3(path).info.length

		print(length)
		lengths.append(length)

with open(f'{cwd}\\durations.txt', 'w', encoding='utf-8-sig') as output:
	for x in lengths:
		output.write(f'{x}\n')