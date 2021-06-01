class Track:
    def __init__(self, name, artiste, timesplayed):
        self.name = name
        self.artiste = artiste
        self.timesplayed = timesplayed

    def __str__(self):
        return '%s, %s, Times played: %i' % (self.name, self.artiste, self.timesplayed)

    def get_name(self):
        return self.name

    def get_artiste(self):
        return self.artiste

    def play(self):
        if Track:
            self.timesplayed += 1
            return 'Playing: %s, %s, Times played: %i' % (self.name, self.artiste, self.timesplayed)
        else:
            return 'There is no currently selected track.'

class DLLNode:
    def __init__(self, item, prevnode, nextnode):
        self.item = item
        self.prevnode = prevnode
        self.nextnode = nextnode

class PyToonz:
    def __init__(self):
        self.head = None
        self.tail = None
        self.track_length = 0
        self.current = None

    def __str__(self):
        tracks = 'Playlist: \n'
        node = self.head
        for i in range(self.track_length):
            if self.current == node:
                tracks += '--> ' + str(node.item) + '\n'
            else:
                tracks += str(node.item) + '\n'
            node = node.nextnode
        return tracks

    def length(self):
        if self.track_length >= 0:
            return 'There are currently %i tracks in your library.' % self.track_length
        else:
            return 'There are no tracks in your library.'

    def add_track(self, track):
        newDLLNode = DLLNode(track, None, None)
        if self.head == None:
            self.head = newDLLNode
            self.current = newDLLNode
        else:
            self.tail.nextnode = newDLLNode
            newDLLNode.prevnode = self.tail
        self.tail = newDLLNode
        self.track_length += 1

    def get_current(self):
        if self.track_length <= 0:
            return None
        else:
            return 'Current Track: %s' % (self.current.item)

    def add_after(self, track):
        newDllNode = DLLNode(track, None, None)
        newDllNode.prevnode = self.current
        newDllNode.nextnode = self.current.nextnode
        self.current.nextnode = newDllNode
        self.tail.prevnode = newDllNode
        self.track_length += 1

    def next_track(self):
        if self.current == self.tail:
            self.current = self.head
        else:
            self.current = self.current.nextnode

    def prev_track(self):
        if self.current == self.head:
            self.current = self.tail
        else:
            self.current = self.current.prevnode

    def reset(self):
        self.current = self.head

    def play(self):
        return Track.play(self.current.item)

    def remove_current(self):
        if self.current == self.head:
            self.head = self.head.nextnode
            self.head.prevnode = self.tail.nextnode
            self.current = self.current.nextnode
        elif self.current == self.tail:
            self.tail = self.tail.prevnode
            self.tail.nextnode = self.head.prevnode
            self.current = self.current.prevnode
        else:
            self.current.prevnode.nextnode = self.current.nextnode
            self.current.nextnode.prevnode = self.current.prevnode
            self.current = self.current.nextnode
        self.track_length -= 1
