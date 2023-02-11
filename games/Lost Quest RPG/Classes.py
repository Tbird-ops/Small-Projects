# ---------------------------------------
# | Class Structures for Lost Quest RPG |
# ---------------------------------------

### Main Player Class ###

class Hero:
  # Initiate the character
  def __init__(self, health, damage, defence, luck, experience, level, items, name):
    self.health = health
    self.damage = damage
    self.defence = defence
    self.luck = luck
    self.experience = experience
    self.level = level
    self.items = []
    self.name = name

  # Helpful return methods
  def getHealth(self):
    return self.health
  def getDamage(self):
    return self.damage
  def getDefence(self):
    return self.defence
  def getLuck(self):
    return self.luck
  def getExperience(self):
    return self.experience
  def getLevel(self):
    return self.level
  def getItems(self):
    for item in self.items:
      print("-->", item)
  def getName(self):
    return self.name

  # Setting New Value methods
  def setHealth(self, newHealth):
    self.health =+ newHealth
  def setDamage(self, newDamage):
    self.damage += newDamage
  def setDefence(self, newDefence):
    self.defence += newDefence
  def setLuck(self, newLuck):
    self.luck += newLuck
  def setExperience(self, newExperience):
    self.experience += newExperience
  def setLevel(self, newLevel):
    self.level += newLevel

  # Item Controls
  def addItem(self, item):
    print("You have collected an item! --> " + item)
    self.items.append(item)
  def useItem(self, item):
    pass
  def dropItem(self, item):
    print("You have dropped an item! --> " + item)
    self.items.remove(item)
      

### Generic Enemy Class ###
class Enemy:
  def __init__(self, health, damage, defence, luck, experience, name):
    self.health = health
    self.damage = damage
    self.defence = defence
    self.luck = luck
    self.experience = experience
    self.name = name

  # Return Methods
  def getHealth(self):
    return self.health
  def getDamage(self):
    return self.damage
  def getDefence(self):
    return self.defence
  def getLuck(self):
    return self.luck
  def getXP(self):
    return self.experience
  def getName(self):
    return self.experience

  # Set Methods
  def setHealth(self, newHealth):
    self.health += newHealth
  def setDamage(self, newDamage):
    self.damage += newDamage
  def setdefence(self, newDefence):
    self.defence += newDefence
  def setLuck(self, newLuck):
    self.luck += Luck
  def setXP(self, newXP):
    self.experience += newXP



### Character Roles (Children of Hero) ###
'''
class Warrior(Hero):
  def __init__(self, health, stamina, recoveryRate, damage, defence, luck, experience, level, items, skills, name):
    super().__init__(health, damage, defence, luck, recoveryRate, experience, level, items, name)
    self.stamina = stamina
    self.skills = skills

  # Skill Controls
  def addSkill(self, skill):
    if skill not in self.skills:
      self.skills.append(skill)
  def getSkills(self):
    for skill in self.skills:
      print("-->", skill)

  #Stamina Functions
  def getStamina(self):
    return self.stamina
  def setStamina(self, newStamina):
    self.stamina += newStamina
  def refundStamina(self, recoveryRate):
    self.stamina += recoveryRate
  def useStamina(self, spentStamina):
    self.stamina -= spentStamina

  # Cleave: hit multiple enemies

  # Fired Up: temp boost of Luck and Damage

  # Focused Strike: chance to deal double damage to an enemy

class Archer(Hero):
  def __init__(self, health, focus, recoveryRate, damage, defence, luck, experience, level, items, skills, name):
    super().__init__(health, damage, defence, luck, recoveryRate, experience, level, items, name)
    self.focus = focus
    self.skills = skills

  # Skill Controls
  def addSkill(self, skill):
    if skill not in self.skills:
      self.skills.append(skill)
  def getSkills(self):
    for skill in self.skills:
      print("-->", skill)    

  # Focus Functions
  def getFocus(self):
    return self.focus
  def setFocus(self, newFocus):
    self.focus += newFocus
  def refundFocus(self, recoveryRate):
    self.focus += recoveryRate
  def useFocus(self, spentFocus):
    self.focus -= spentFocus

  # Dead shot: critical hit move "snipe"

  # Rapid Fire

  # Way of the Woods: temporarily boost luck and defence

class Wizard(Hero):
  def __init__(self, health, magic, recoveryRate, damage, defence, luck, experience, level, items, spells, name):
    super().__init__(health, damage, defence, luck, recoveryRate, experience, level, items, name)
    self.magic = magic
    self.spells = spells

  # Spell Control
  def addSpell(self, spell):
    if spell not in self.spells:
      self.spells.append(spell)
  def getSpells(self):
    for spell in self.spells:
      print("-->",spell)

  # Magic Functions
  def getMagic(self):
    return self.magic
  def setMagic(self, newMagic):
    self.magic += newMagic
  def refundMagic(self, recoveryRate):
    self.magic += recoveryRate
  def useFocus(self, spentMagic):
    self.magic -= spentMagic

  # Fireball

  # Lightning Bolt

  # Healing Spell

  # Iron FLesh

class Rogue(Hero):
  def __init__(self, health, stealth, recoveryRate, damage, defence, luck, experience, level, items, skills, name):
    super().__init__(health, damage, defence, luck, recoveryRate, experience, level, items, name)
    self.stealth = stealth
    self.skills = skills

  # Skill Controls
  def addSkill(self, skill):
    if skill not in self.skills:
      self.skills.append(skill)
  def getSkills(self):
    for skill in self.skills:
      print("-->", skill)

  #Stamina Functions
  def getStealth(self):
    return self.stealth
  def setStealth(self, newStealth):
    self.stealth += newStealth
  def refundStealth(self, recoveryRate):
    self.stealth += recoveryRate
  def useStealth(self, spentStealth):
    self.stealth -= spentStealth

  # Assassin's blade: Chance to immediately kill enemy

  # Stealth Strike: deal damage with a chance of lowering enemy defence temporarily

  # Pickpocket: chance to steal loot from enemy
'''
