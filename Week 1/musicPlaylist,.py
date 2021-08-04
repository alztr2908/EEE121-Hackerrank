class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Playlist:
    def __init__(self):
        self.tracks = []

    def enqueue(self, track):
        """Adds a track to the playlist."""

        # --- YOUR CODE HERE ---
        self.tracks.append(track)

    def remove(self, trackNumber):
        """Removes the track at the given position from the playlist."""

        # --- YOUR CODE HERE ---
        self.tracks.pop(trackNumber-1)

    def view(self):
        """Displays all tracks in the playlist."""

        # --- YOUR CODE HERE ---
        for i,track in enumerate(self.tracks):
            print(i+1,track[1],track[0],sep=' - ')

    def duration(self):
        """Displays the total duration of the playlist."""

        # --- YOUR CODE HERE ---
        total = 0
        for time in self.tracks:
            total += int(time[2])
            
        hour = total//3600
        mins = (total%3600)//60 
        sec = ((total%3600)%60)%60
        print(f'Total duration: {str(hour).zfill(2)}:{str(mins).zfill(2)}:{str(sec).zfill(2)}')


if __name__ == '__main__':
    myTunes = Playlist()

    # Parse each line of input and add each track to the playlist.
    n = int(input())
    for _ in range(n):
        inputLine = input().split(',')

        # --- YOUR CODE HERE ---
        myTrack = Track(inputLine[0],inputLine[1],inputLine[2])
        myList = list((myTrack.title, myTrack.artist, myTrack.duration))
        myTunes.enqueue(myList)
    
    # If your methods are defined correctly, the following lines
    # should produce the desired output in the test cases.
    myTunes.remove(2)
    myTunes.remove(5)
    myTunes.view()
    myTunes.duration()