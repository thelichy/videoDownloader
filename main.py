from pytube import YouTube, Playlist


PLAYLIST_URL = input('Insira a url da playlist: ')
FILE_EXTENSION = input('Insira o tipo de extensão: ')


playlist = Playlist(PLAYLIST_URL)

for video in playlist.videos:
    print(f'Baixando {video.title}...')

    try: 
        video.streams.filter(only_audio=True).first().download('.', f'{video.title}.{FILE_EXTENSION}')

    except:
        print(f'Não foi possível baixar {video.title}')
