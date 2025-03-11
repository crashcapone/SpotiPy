from dj_equipment import Artist,Album,Track
from hubs import BaseSonicHub
from player import menu

#TODO implement FileBasedSonicHub
class FileBasedSonicHub(BaseSonicHub):
    """ file based sonic hub class"""
    def __init__(self,name):
        """file based sonic hub constructor"""
        super().__init__(name)
        self.name = name
    def populate_maps(self):
        """ adds songs to FileBasedSonicHub"""

        with open("encoded/artists.txt","r") as artist:
            for line in artist:
                artist = Artist.deserialize(line.strip())
                self._artist_map[artist.get_id()] = artist

        with open("encoded/albums.txt","r") as album:
            for line in album:
                album = Album.deserialize(line.strip())
                self._album_map[album.get_id()] = album
        
        with open("encoded/tracks.txt","r") as track:
            for line in track:
                track = Track.deserialize(line.strip())
                self._track_map[track.get_id()] = track
        


if __name__ == "__main__":

    try:
        sonic_hub = FileBasedSonicHub("File Based Sonic Hub")
        print(sonic_hub)
        sonic_hub.populate_maps()
        print(sonic_hub)
        sonic_hub.cross_pollinate()

        menu(sonic_hub)

    except Exception as e:
        print("Could not run our program due to error",e)
