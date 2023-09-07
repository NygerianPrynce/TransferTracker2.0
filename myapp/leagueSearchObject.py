class leagueSearchObject:
    def __init__(self, image, id, name, nationality, clubNums, playerNums,  marketValue, association):
        self.name = name
        self.id = id
        self.image = image
        self.nationality = nationality
        self.clubNums = clubNums
        self.playerNums = playerNums
        self.association = association
        self.marketValue = marketValue
        self.type = "(League)"
    def to_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'image': self.image,
            'nationality': self.nationality,
            'clubNums': self.clubNums,
            'playerNums': self.playerNums,
            'association': self.association,
            'marketValue': self.marketValue,
        }
    def __str__(self):
        return f"{self.type}({self.name})({self.id})({self.image})({self.clubNums})({self.playerNums})({self.marketValue})({self.nationality})({self.association})"
