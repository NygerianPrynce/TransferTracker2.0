class playerSearchObject:
    def __init__(self, playerId, name, age, position, image, clubName, clubID, clubImage, nationality, marketValue):
        self.playerId = playerId
        self.name = name
        self.age = age
        self.position = position
        self.image = image
        self.clubName = clubName
        self.clubID = clubID
        self.clubImage = clubImage
        self.nationality = nationality
        self.marketValue = marketValue
        self.type = "(Player)"
    def to_dict(self):
        return {
            'playerId': self.playerId, #
            'name': self.name, #
            'age': self.age, #
            'position': self.position, #
            'image': self.image, #
            'clubName': self.clubName, #
            'clubID': self.clubID, #
            'clubImage': self.clubImage, #
            'nationality': self.nationality, #
            'marketValue': self.marketValue, #
        }
    def __str__(self):
        return f"{self.type}({self.name})({self.age})({self.position})({self.image})({self.clubName})({self.nationality})({self.marketValue})({self.playerId})({self.clubImage})"
#