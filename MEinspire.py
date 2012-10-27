# Name: Andrew Blevins
# Email: andrewdblevins@gmail.com
#
# little mad-libber program the spits out a random shell for a Mass Effect mission
#
#

import random
import re

d = {}

d['race'] = ['Human','Asari','Drell','Elcore','Hanar','Salurian','Turian','Volus','Batarians','Geth','Krogan','Quarian','Raloi','Vorcha','Yahg', '<race> and <race>']

d['item'] = ['Prothean Artifact',"Competitor`s Research",'weapon Prototype',]

d['corporation']=['Seraphtech Industries', 'ExoGeni Corporation']
d['evil_corporation'] = ['The Cerberus Network']

d['occupation_peaceful'] = ['miners','scientists', 'colonists', 'orphans' ,'researchers', 'archeologists', 'whores']


d['good_faction'] = ['<race> <occupation_peaceful>','Citadel Council','<corporation>','<race> government', '<race> military','<bad_faction>']
d['bad_faction'] = ['the <race> military','the  <race> rebels','the <race> Mercenaries','The Rachni','The Geth','The Yahg','<evil_corporation>','<good_faction>']

d['mission_type'] = ['defend them','escort them','rescue thier compatriots','retrive thier property','investigate an anomoly','recover <item>']

d['number'] = ['I','II','III','IV']
# TODO better orthography
d['sylable'] = ['<sylable><sylable>', 'gir', 'lash', 'dam', 'mash', 'gum', 'gik', 'maas', 'gig', 'pir', 'sun', 'lag', 'saar', 'kin', 'mam', 'siir', 'din', 'miis', 'dir', 'lun', 'guk', 'gir', 'ger', 'giir', 'kuk', 'kek', 'diim', 'kiim', 'bir', 'kak', 'gar', 'lim', 'kar', 'mur', 'nak', 'mis', 'khir', 'pek', 'shuur', 'nim', 'shim', 'mim', 'pik', 'gar', 'lash', 'lar', 'mug', 'shur', 'sim', 'gur', 'lem', 'luum', 'khak', 'shar', 'buk', 'gim', 'lan', 'zer', 'kir', 'deg', 'khir', 'kur', 'gug', 'ler', 'daak', 'lam', 'kiig', 'kun', 'dir', 'kun', 'mam', 'khus', 'kar', 'zan', 'riis', 'gir', 'gar', 'lun', 'khiir', 'kar', 'mush', 'lag', 'zir', 'giir', 'lus', 'riim', 'lar', 'miik', 'kur', 'saash', 'gush', 'dan', 'sag', 'dem', 'sur', 'kuum', 'nur', 'shush', 'sher', 'zish', 'mik']



d['planet_type'] = ['Lava Planet', 'Eden World', 'Jungle Planet', 'Temperate Planet', 'Gas Giant', 'Ocean Planet', 'Ice Planet', 'Desert World']
d['planet_name'] = ['<sylable> <number>','<sylable>`<sylable> <number>']
d['planet_pre'] = ['Rachni infested ','Quarantined ','Wartorn ','Beautiful ']
d['planet_post'] = [' known for its strange flora']

d['station_type'] =['research station','intelligence outpost','mining operation','colony','city','tourist destination','space port']

d['mission_place'] = ['a <station_type> on <planet_name> a <planet_pre><planet_type><planet_post>',
              'an abandoned <race> space station',
              'a prothean derelict',
              'space station in an asteroid field',
              'a <race> derelict spaceship',
              'a <station_type> on <planet_name> a <planet_type><planet_post>',
              'a <station_type> on <planet_name> a <planet_pre><planet_type>',
              'a <station_type> on <planet_name> a <planet_type>',
              ]

d['response'] = ['may try to kill you','will be displeased','has an ambush ready','is extra vulnrible','have recently cleaned thier station, and thus cover will be lacking']



mission = 'The party has been hired by <good_faction> to  <mission_type> on <mission_place>. <bad_faction> <response>'

def generate(n):
    for i in range(n):
        _mission = mission
        while 1:
            try:
                 _mission = replace_tag(_mission)
            except NameError:
                break
        print _mission
                        
def replace_tag(s):
    tags =  re.findall('<(.*?)>',s)
    if not tags:
        raise NameError('nothing left to replace')
    for tag in tags:
        try:
            new = random.choice(d[tag])
            old = '<'+tag+'>'
            s = s.replace(old,new,1)
        except KeyError:
            print 'Idiot, you forgot to make a key for ' + tag
            raise NameError
    return s 


if __name__=='__main__':
    generate(10)
