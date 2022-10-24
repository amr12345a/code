from os import path
from telethon import utils
from telethon.sync import TelegramClient as TC2
from telethon import TelegramClient, events
from telethon.tl.types import PeerUser
import threading
import datetime
import time
if __name__ == '__main__':

    client2 = TelegramClient("asdsad", 6284107, "376f444df0fcadd27458653b3f92ed6a")
    client = TC2("asdsad2", 6284107, "376f444df0fcadd27458653b3f92ed6a")
    # 1852941497:AAFrMp3NEqrCc2Ke-4vA4o3mVb5IhWU_L10
    print("Start")

    channelId = abs(int(input("The Channel id: ")))
    if not path.exists("Messages.csv"):
        messages = open("Messages.csv", "w+")
        messages.close()

    if not path.exists("Time.csv"):
        daysafter = datetime.date.today() + datetime.timedelta(days=5)
        f = daysafter.strftime("%m/%d/%Y")
        print(f)
        timere = open("Time.csv", "w+")
        timere.write(f)
        timere.close()

    else:
        timere = open("Time.csv", "r+").read()
        f = datetime.datetime.strptime(timere, "%m/%d/%Y")

    def sender():
        while True:
            if datetime.datetime.now() > f:
                winner = open("Messages.csv", "r+").read().split("\n")
                scores = []
                ids = []
                names = []
                for i in winner:
                    try:
                        scores.append(int(i.split(", ")[1]))
                        ids.append(i.split(", ")[0])
                        names.append(i.split(", ")[2])
                    except:
                        pass

                winner_user = names[scores.index(max(scores))]

                client.send_message(entity=PeerUser(user_id=1185034291), message=str("Congratulations "+str(winner_user)+"! You have won this month for being the most active member in the Rebel Society Chat Group! Please enter your wallet address in field below."))
                daysafterrr = datetime.date.today() + datetime.timedelta(days=5)
                fff = daysafterrr.strftime("%m/%d/%Y")
                print(fff)
                timeree = open("Time.csv", "w+")
                timeree.write(fff)
                timeree.close()
            time.sleep(300)


    fffff = threading.Thread(target=sender)
    fffff.start()

    @client2.on(events.NewMessage(chats=[channelId]))
    async def handler(event):

        sender = await event.get_sender()
        name = utils.get_display_name(sender)
        messagess = open("Messages_sent.txt", "a+")
        messagess.write(str(event).split("message='")[1].split("',")[0] + " " + name + " " + "\n")
        print(name, 'said', event.text, '!')

        if datetime.datetime.now() > f:
            winner = open("Messages.csv", "r+").read().split("\n")
            scores = []
            ids = []
            names = []
            for i in winner:
                try:
                    scores.append(int(i.split(", ")[1]))
                    ids.append(i.split(", ")[0])
                    names.append(i.split(", ")[2])
                except:
                    pass

            winner_user = names[scores.index(max(scores))]

            await client2.send_message(entity=PeerUser(user_id=1185034291), message=str("Congratulations "+str(winner_user)+"! You have won this month for being the most active member in the Rebel Society Chat Group! Please enter your wallet address in field below."))
            daysafterrr = datetime.date.today() + datetime.timedelta(days=5)
            fff = daysafterrr.strftime("%m/%d/%Y")
            print(fff)
            timeree = open("Time.csv", "w+")
            timeree.write(fff)
            timeree.close()
        print(event)
        user = str(event).split("user_id=")[1].split(",")[0].replace(")", "")
        messages_users = open("Messages.csv", "r+").read()
        print(messages_users)
        message_score = messages_users.split("\n")
        done = False
        for me in message_score:
            try:
                user_id = me.split(", ")[0]
                score = int(me.split(", ")[1])
                if user_id == user:
                    done = True
                    score += 1
                    messages_users = messages_users.replace(user_id + ", " + str(score - 1)  + ", " + name, user_id + ", " + str(score)  + ", " + name)
                    print(user_id + ", " + str(score))
                    new_message = open("Messages.csv", "w+")
                    new_message.write(messages_users)
                    new_message.close()
            except:
                pass
        if not done:
            new_message = open("Messages.csv", "a+")
            new_message.write("\n" + user + ", " + str(1)  + ", " + name)
            print(user + " " + str(1))
            new_message.close()


    client2.start()
    client2.run_until_disconnected()
