from pytube import YouTube, Playlist


def download_playlist(url: str, extension: str, only_audio: bool, path: str) :
    playlist = Playlist(url)

    for video in playlist.videos:
        print(f'Baixando {video.title}...')

        try: 
            stream = video.streams.filter(only_audio=only_audio).first()
            stream.download(path, f'{video.title}.{extension}')

        except:
            print(f'Não foi possível baixar {video.title}')


def download_video(url: str, extension: str, only_audio: bool, path: str) :
    video = YouTube(url)
    print(f'Baixando {video.title}...')

    try:
        stream = video.streams.filter(only_audio=only_audio).first()
        stream.download(path, f'{video.title}.{extension}')

    except:
        print(f'Não foi possível baixar {video.title}')
