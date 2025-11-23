class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Initializes status, muted, volume, and channel variables to default values
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Method to change the power status
        Alternates between True(On) and False(Off)
        '''
        if self.__status:
            self.__status = False
        else:
            self.__status = True


    def mute(self) -> None:
        '''
        Method to mute the volume
        Alternates between True(Muted) and False(Unmuted)
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        '''
        Method to increase the channel
        Loops back to MIN_CHANNEL if at MAX_CHANNEL
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Method to decrease the channel
        Loops back to MAX_CHANNEL if at MIN_CHANNEL
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Method to increase the volume
        Unmutes if muted, caps at MAX_VOLUME
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method to decrease the volume
        Unmutes if muted, does not go below MIN_VOLUME
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method to show the current values for status, channel, and volume
        :return: status, channel, volume
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
