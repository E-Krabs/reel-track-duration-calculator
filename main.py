from mutagen.flac import FLAC
from mutagen.mp3 import MP3
import os
import math

cwd = os.getcwd()
m3u8 = 'C:\\Users\\Tyler\\Music\\everything.m3u8' #input('Path (ex. C:\\usr\\Music\\.m3u8): ')


def flac_length():
	lengths = []
	with open(m3u8, 'r', encoding='utf-8-sig') as playlist:
		paths = playlist.readlines()
		for path in paths[1:]:
			path = path.replace("\n", "")
			try:
				length = FLAC(path).info.length
			except:
				length = MP3(path).info.length

			lengths.append(length)

	with open(f'{cwd}\\durations.txt', 'w', encoding='utf-8-sig') as output:
		for x in lengths:
			output.write(f'{x}\n')

	return (sum(lengths), len(lengths))


def flac_size():
	size_bytes = 0
	count = 0
	with open(m3u8, 'r', encoding='utf-8-sig') as playlist:
		paths = playlist.readlines()
		for path in paths[1:]:
			path = path.replace("\n", "")
			size_bytes += os.path.getsize(path)
			count += 1

	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return (f'{s} {size_name[i]}', count)

#total_length = flac_length()
total_size = flac_size()
#print(total_length)
print(total_size)