import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import discord
cred = credentials.Certificate('Vanguardrp-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://vanguarddatabase-b1058-default-rtdb.firebaseio.com"
})


class Register:

    def __init__(self, name, premwinstat, vpremwinstat, standardwinstat):
        self.name = name
        self.premwinstat = premwinstat
        self.vpremwinstat = vpremwinstat
        self.standardwinstat = standardwinstat

    def registration_check(self):
        ref = db.reference("/")
        child_ref = ref.child("Users")
        val = child_ref.get()
        if self.name in val:
            return True

    def registration_embed(self):
        ref = db.reference("Users")
        user_ref = ref.child(self.name)
        user_ref.set({
            "Premium Wins": self.premwinstat,
            "V Premium Wins": self.vpremwinstat,
            "Standard Wins": self.standardwinstat
        })


class Trophy:

    def __init__(self, name):
        self.name = name

    def last_premium_trophy(self):
        ref = db.reference("Users")
        user_ref = ref.child(self.name).child("Premium Wins").get()
        return user_ref
    
    def last_vpremium_trophy(self):
        ref = db.reference("Users")
        user_ref = ref.child(self.name).child("V Premium Wins").get()
        return user_ref
    
    def last_standard_trophy(self):
        ref = db.reference("Users")
        user_ref = ref.child(self.name).child("Standard Wins").get()
        return user_ref
    
class Wins:
    
    def __init__(self, name):
        self.name = name
        
    def premium_list(self):
        ref = db.reference("Users")
        user_ref = ref.child(self.name)
        user_ref2 = ref.child(self.name).child("Premium Wins").get()
        user_ref2 += 10
        user_ref.update({
            "Premium Wins": user_ref2
        })
        
    def vpremium_list(self):
        ref = db.reference("Users")
        user_ref = ref.child(self.name)
        user_ref2 = ref.child(self.name).child("V Premium Wins").get()
        user_ref2 += 10
        user_ref.update({
            "V Premium Wins": user_ref2
        })
        
        
                
    def standard_list(self):
        ref = db.reference("Users")
        user_ref = ref.child(self.name)
        user_ref2 = ref.child(self.name).child("Standard Wins").get()
        user_ref2 += 10
        user_ref.update({
            "Standard Wins": user_ref2
        })
        
        
    def premium_lose(self):
        ref = db.reference("Users")
        user_ref = ref.child(self.name)
        user_ref2 = ref.child(self.name).child("Premium Wins").get()
        user_ref2 -= 5
        user_ref.update({
            "Premium Wins": user_ref2
        })
        
    def vpremium_lose(self):    
        ref = db.reference("Users")
        user_ref = ref.child(self.name)
        user_ref2 = ref.child(self.name).child("V Premium Wins").get()
        user_ref2 -= 5
        user_ref.update({
            "V Premium Wins": user_ref2
        })
        
        
    def standard_lose(self):
        ref = db.reference("Users")
        user_ref = ref.child(self.name)
        user_ref2 = ref.child(self.name).child("Standard Wins").get()
        user_ref2 -= 5
        user_ref.update({
            "Standard Wins": user_ref2
        })
        

def leaderboards(format):
    dict_people = {}
    sorted_dict = {}
    ref = db.reference("/")
    child_ref = ref.child("Users")
    val = child_ref.get()
    if format==1:
        format = "Premium Wins"
    elif format==2:
        format = "V Premium Wins"
    elif format==3:
        format = "Standard Wins"
    for name,ranking in val.items():
        dict_people[name] = ranking[format]
    sorted_people = sorted(dict_people.keys())
    for i in sorted_people:
        sorted_dict[i] = dict_people[i]
    embed_sorted = discord.Embed(
        title=format,
        colour=discord.Colour.orange()
    )
    count = 0
    for name in sorted_people:
        if name=="Master":
            continue
        else:
            count += 1
            embed_sorted.add_field(
                name = str(count) + ". " + name[:-4],
                value = "🏆"+str(sorted_dict[name]),
                inline = False
            )
    
    return embed_sorted
        
        