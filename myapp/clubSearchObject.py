class clubSearchObject:
    def __init__(self, image, id, name, nationality, marketValue):
        self.name = name
        self.id = id
        self.image = image
        self.nationality = nationality
        self.marketValue = marketValue
        self.type = "(Club)"
    def to_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'image': self.image,
            'nationality': self.nationality,
            'marketValue': self.marketValue,
        }
    def __str__(self):
        return f"{self.type}({self.name})({self.id})({self.image})({self.nationality})({self.marketValue})"
