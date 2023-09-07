class transferObject:
    def __init__(self, playerId, name, age, position, image, clubLeftName, clubLeftId, clubLeftImage, clubJoinedName, clubJoinedId, clubJoinedImage, leagueLeftName, leagueLeftId, leagueLeftImage, leagueJoinedName, leagueJoinedId, leagueJoinedImage, fee,):
        self.playerId = playerId
        self.name = name
        self.age = age
        self.position = position
        #continue
        self.image = image
        self.clubLeftName = clubLeftName
        self.clubLeftId = clubLeftId
        self.clubLeftImage = clubLeftImage
        self.clubJoinedName = clubJoinedName
        self.clubJoinedId = clubJoinedId
        self.clubJoinedImage = clubJoinedImage
        self.leagueLeftName = leagueLeftName
        self.leagueLeftId = leagueLeftId
        self.leagueLeftImage = leagueLeftImage
        self.leagueJoinedName = leagueJoinedName
        self.leagueJoinedId = leagueJoinedId
        self.leagueJoinedImage = leagueJoinedImage
        self.fee = fee
    def to_dict(self):
        return {
            'playerId': self.playerId,
            'name': self.name,
            'age': self.age,
            'position': self.position,
            'image': self.image,
            'clubLeftName': self.clubLeftName,
            'clubLeftId': self.clubLeftId,
            'clubLeftImage': self.clubLeftImage,
            'clubJoinedName': self.clubJoinedName,
            'clubJoinedId': self.clubJoinedId,
            'clubJoinedImage': self.clubJoinedImage,
            'leagueLeftName': self.leagueLeftName,
            'leagueLeftId': self.leagueLeftId,
            'leagueLeftImage': self.leagueLeftImage,
            'leagueJoinedName': self.leagueJoinedName,
            'leagueJoinedId': self.leagueJoinedId,
            'leagueJoinedImage': self.leagueJoinedImage,
            'fee': self.fee,
        }
        #id, name, age, position, image, clubLeftName, clubLeftId, clubJoinedName, clubJoinedId, leagueLeftName, leagueLeftId, leagueJoinedName, leagueJoinedId, market value, fee, nationality
    def __str__(self):
        return f"({self.name})({self.image})({self.age})({self.position})({self.clubLeftName})({self.clubLeftImage})({self.leagueLeftName})({self.leagueLeftImage})({self.clubJoinedName})({self.clubJoinedImage})({self.leagueJoinedName})({self.leagueJoinedImage})({self.fee})"
