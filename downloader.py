from pytube import YouTube, Playlist


def download_playlist(url: str, extension: str, only_audio: bool, path: str) :
    playlist = Playlist(url).video_urls

    for url in playlist:
        download_single(url, extension, only_audio, path)


def download_single(url: str, extension: str, only_audio: bool, path: str) :
    video = YouTube(url)
    print(f'Baixando {video.title}...')

    if only_audio:
        stream = video.streams.get_audio_only()
    else:
        stream = video.streams.get_highest_resolution()

    stream.download(path, f'{video.title}.{extension}')
