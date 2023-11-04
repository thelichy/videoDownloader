import re
from pytube import YouTube, Playlist


def download_playlist(url: str, extension: str, only_audio: bool, path: str) :
	playlist = Playlist(url).video_urls

	for url in playlist:
		download_single(url, extension, only_audio, path)


def download_single(url: str, extension: str, only_audio: bool, path: str) :
	video = YouTube(url)
	print(f'Baixando {video.title}...')
	stream = video.bypass_age_gate

	if only_audio:
		stream = video.streams.get_audio_only()
	else:
		stream = video.streams.get_highest_resolution()

	if stream == None:
		raise Exception(f'Erro: não foi possível baixar {video.title}')

	return stream.download(path, f'{sanitize_filename(video.title)}.{extension}')


def sanitize_filename(input_str):
	input_str = re.sub(r'\([^)]*\)', '', input_str)
	input_str = re.sub(r'\{[^}]*\}', '', input_str)

	input_str = re.sub(r'[^\w\-. ]', '', input_str)

	input_str = input_str[:100]

	return input_str
