# Name: Andrew Blevins
# Email: andrewdblevins@gmail.com
#
# little mad-libber program the spits out a random shell for a random mission for the Antediluvian War 
#
#

import random
import re

d = {}

d['mission_type'] = ['defend <weak_ally>',
                     'escort <weak_ally> through <dangerous_location>',
                     'rescue <weak_ally> from <dangerous_location> where they are held by <enemy> ',
                     'investigate an anomoly',
                     'recover <magic_item>']

d['weak_ally'] = ['a small caravan', 'a group of merchants','a <size> village of settlers', 'a squad of green recruits', 'a tour of dandies and courtesans']

d['dangerous_location'] = ['<mission_place> held by an <enemy>']
d['enemy'] = ['<enemy> and <boss>','<boss>','the twins: <boss> and <boss>','squad of baby-eaters', 'cabal of wizards', 'uiger outriders', 'assassins and dervishes']

d['boss'] = ['<sylable><sylable><sylable> the wizard with a mastery of <wizard_mastery>', '<sylable><sylable> the dervish <dervish_attribute>', '<sylable> the warrior <warrior_attribute>']
d['wizard_mastery'] = ['<material>','<animal>s','<element>']
d['dervish_attribute'] = ['with the aspect of a <bird>', 'that flows like <liquid>','that flows like <gas>']
d['warrior_attribute'] = ['with the aspect of a <mammal>']

d['number'] = ['one','two','three','four']
# TODO better orthography
d['sylable'] = ['<sylable><sylable>', 'gir', 'lash', 'dam', 'mash', 'gum', 'gik', 'maas', 'gig', 'pir', 'sun', 'lag', 'saar', 'kin', 'mam', 'siir', 'din', 'miis', 'dir', 'lun', 'guk', 'gir', 'ger', 'giir', 'kuk', 'kek', 'diim', 'kiim', 'bir', 'kak', 'gar', 'lim', 'kar', 'mur', 'nak', 'mis', 'khir', 'pek', 'shuur', 'nim', 'shim', 'mim', 'pik', 'gar', 'lash', 'lar', 'mug', 'shur', 'sim', 'gur', 'lem', 'luum', 'khak', 'shar', 'buk', 'gim', 'lan', 'zer', 'kir', 'deg', 'khir', 'kur', 'gug', 'ler', 'daak', 'lam', 'kiig', 'kun', 'dir', 'kun', 'mam', 'khus', 'kar', 'zan', 'riis', 'gir', 'gar', 'lun', 'khiir', 'kar', 'mush', 'lag', 'zir', 'giir', 'lus', 'riim', 'lar', 'miik', 'kur', 'saash', 'gush', 'dan', 'sag', 'dem', 'sur', 'kuum', 'nur', 'shush', 'sher', 'zish', 'mik']

d['animal'] = ['<reptile>','<mammal>','<bird>']
d['reptile'] = ['snake','crocadile','lizard']
d['mammal'] = ['buck', 'bull', 'bear', 'wolf', 'lion', 'tiger', 'ram', 'gorrila']
d['bird'] = ['eagle','sparrow', 'raven']

d['ruthenian_mythical_creatures'] = ['leshi','rusalka','kikimora','vodyanoy','ala','bagiennik','bannik', 'boginki', 'dola', 'domavoi', 'drekavak', 'likho', 'polevik', 'rarog', 'shishiga', 'skrzak', 'stuhak', 'vampir', 'vila', 'vucari','were<animal>']
d['uiger_mythical_creatures'] = ['jinn','bahamut','dandan','roc','marid']

d['element'] = ['fire','water','wind','stone' ]
d['flowable'] = ['<gas>','<liquid>']
d['liquid'] = ['quicksilver', 'water','blood']
d['gas'] = ['smoke','wind','steam','fog']

d['stat'] = ['strength', 'intellect', 'dexterity', 'wisdom', 'charisma', 'beauty']

d['color'] = ['the color of <material>','blue','indigo','purple','red','crimson','burnt umber','orange','yellow','green','teal']

d['material'] = ['metal','wood','stone','leather']
d['metal'] = ['bronze','copper','iron', 'steel', 'gold', 'silver', 'mithril', 'solidified quicksilver']
d['wood'] = ['<tree> wood']
d['tree'] = ['elm','oak','pine', 'ash', 'rowan', 'cedar', 'beech']
d['stone'] = ['limestone','obsidian','basalt']
d['leather'] = ['<animal> hide', 'soft suede']

d['boltable'] = ['fire','lightning','<stone>','<metal>']

d['magic_item'] = ['a magical <item> which <magic_effect>']
d['magic_effect'] = ['turns your hair <color>',
                      'makes you invisible',
                      'throws <projectile>s of <boltable>',
                      'transforms you into a <animal>', 
                      'increases your <stat>']

d['item'] = ['<metal> <weapon>', '<stone> <weapon>','<leather> <armor>','<metal> <armor>','<leather> <clothing>','<material> <tool>','<material> <misc_item>']
d['weapon'] = ['sword', 'mace', 'dagger', 'spear', 'bow', 'trident', 'glaive', 'war hammer','crossbow']
d['armor'] = ['breast plate', 'chainmail','shield','skull cap']
d['clothing'] = ['hat', 'shirt', 'pants']
d['tool'] = ['hammer', 'scissors', 'chisel', 'anvil', 'tongs']
d['misc_item'] = ['mirror','comb']
d['projectile'] = ['sphere','bolt','arrow','javelin','net','bolo']

d['size'] = ['small', 'mid-sized', 'large']
d['castle_type'] = ['fortress', 'outpost', 'garrison', 'guard tower', '<stone> tower']
d['castle_location'] = ['on a hill', 'guarding a pass', 'bridging a river', 'perching on a cliff']

d['castle'] =['<size> <castle_type> <castle_location>']
d['bridge'] = ['<stone> arched bridge over a <land_obstacle>']
d['wall'] = ['<stone> wall']

d['land_feature'] = ['<ruins>','<land_obstacle>','<body_of_water>','<group_of_tree>','<rock_formations>']

d['land_obstacle'] = ['river', 'chasm', 'canyon' , 'a valley filled with spikey stones','lake', 'resevoir']
d['body_of_water'] = ['stream','creek','river','lake','sea', 'resevoir', 'spring']
d['group_of_tree'] = ['a copse of <tree> trees','a grove of <tree> trees']
d['rock_formations'] = ['a standing stone of <stone>','geyser of <flowable>']
d['ruins'] = ['collapsed <bridge>', 'fallen <wall>', 'crumbling <castle>', 'ruins of a old city', 'abandoned mine']

d['mission_place'] = ['<castle>','<bridge>', 'a valley containing <land_obstacle>, <land_feature> and <land_feature>']

mission = 'to  <mission_type> on <mission_place>.\n '

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
    generate(100)
