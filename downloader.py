from pytube import YouTube, Playlist


def download_playlist(url: str, extension: str, only_audio: bool, path: str) :
    playlist = Playlist(url)

    for video in playlist.videos:
        print(f'Baixando {video.title}...')

        stream = video.streams.filter(only_audio=only_audio)
        stream.download(path, f'{video.title}.{extension}')


def download_video(url: str, extension: str, only_audio: bool, path: str) :
    video = YouTube(url)
    print(f'Baixando {video.title}...')

    stream = video.streams.filter(only_audio=only_audio).first()
    stream.download(path, f'{video.title}.{extension}')
