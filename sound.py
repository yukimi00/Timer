import pygame


class Sound:
    @staticmethod
    def play_sound(path, volume=1.0):
        """
        サウンドを再生する

        :param path: 再生する音声ファイルのパス
        :type path: str
        :param volume: 再生するサウンドの音量:
        :type volume: float
        """
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()
