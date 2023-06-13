import datetime

from flask import Flask, request, jsonify

app = Flask(__name__)
app.debug = True


class Channel:
    def __init__(self, id, description):
        self.id = id
        self.description = description

    @classmethod
    def id_to_description(cls, channels, id):
        response = ""
        for channel in channels:
            if channel.id == id:
                response = channel.description

        return response


class Category:
    def __init__(self, id, description):
        self.id = id
        self.description = description

    @classmethod
    def id_to_description(cls, channels, id):
        response = ""
        for channel in channels:
            if channel.id == id:
                response = channel.description

        return response


class Message:
    def __init__(self, content, category):
        self.content = content
        self.category = category

    def send_later(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("messages.log", "a") as file:
            for user in users:
                if self.category in user.subscribed:
                    for channel in user.channels:
                        log_entry = f"{timestamp} - User: {user.email}, Channel: {Channel.id_to_description(channels,channel)}, Category: {Category.id_to_description(categories, self.category)}, Content: {self.content}\n"
                        file.write(log_entry)


class User:
    def __init__(self, id, name, email, phone_number, subscribed, channels):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.subscribed = subscribed
        self.channels = channels


channels = []
categories = []
users = []


@app.route("/message", methods=["POST"])
def message():
    Message(request.json.get("content"), request.json.get("category")).send_later()
    return jsonify(message="Your message will be send as soon as possible.")


if __name__ == "__main__":
    sports = Category(1, "Sports")
    finance = Category(2, "Finance")
    movies = Category(3, "Movies")

    categories.append(sports)
    categories.append(finance)
    categories.append(movies)

    sms = Channel(1, "SMS")
    email = Channel(2, "E-mail")
    push = Channel(3, "Push Notification")

    channels.append(sms)
    channels.append(email)
    channels.append(push)

    user1 = User(
        1,
        "Mozart Doe",
        "mozart.doe@gmail.com",
        "5563345435",
        [categories[0].id, categories[1].id],
        [channels[1].id, channels[2].id],
    )

    user2 = User(
        2,
        "Rafael Doe",
        "rafael.doe@gmail.com",
        "3453453456",
        [categories[0].id, categories[2].id],
        [channels[1].id],
    )

    user3 = User(
        3,
        "Mario Doe",
        "mario.doe@gmail.com",
        "45675467",
        [categories[0].id],
        [channels[0].id, channels[1].id, channels[2].id],
    )

    users.append(user1)
    users.append(user2)
    users.append(user3)

    app.run()
