import requests
import dhooks


counter = 0
pool = []
auth = 'https://discordapp.com/oauth2/authorize?client_id='
permcode = '&scope=bot&permissions=66321471'
#hook = dhooks.Webhook('DISCORD_WEBHOOK_HERE')

def removeduplicate():
    lines_seen = set()
    outfile = open('botlinksNodupes.txt', "w")
    for line in open('botlinks.txt', "r"):
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)


while True:
    counter += 1
    src = requests.get('https://divinediscordbots.com/list/top?page='+str(counter)).text
    links = src.split('<a href="/bots/')
    for link in links:
        if 'https://discordapp.com/' in link:
            boturl = requests.get(auth+link)
            url = boturl.url[18:]
            url = url[:82]
            url = url[32:]
            url = url[:18]
            url = (auth)+(url)+(permcode)
            #print (counter)
            print(url)
            #hook.send (url) #enable if you want to send links through webhook
            with open('botlinks.txt','a') as handle:
                handle.write(url+'\n')
                #removeduplicate() #enable if you are getting a lot of duplicate links.

