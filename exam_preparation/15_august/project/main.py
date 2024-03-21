from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.outdoor_team import OutdoorTeam
from project.tournament import Tournament

# ot = OutdoorTeam("Shadow", "Bulgaria", 200)
# pads = KneePad()
# pads1 = KneePad()
# pads2 = ElbowPad()
# pads3 = ElbowPad()
# ot.win()
# print(ot.advantage)
# ot.equipment.append(pads)
# ot.equipment.append(pads1)
# ot.equipment.append(pads2)
# ot.equipment.append(pads3)
# print(ot.get_statistics())
t = Tournament("Tournament", 2)
t.add_equipment("KneePad")
print(t.add_team("OutdoorTeam", "some", "country", 100))
print(t.add_team("OutdoorTeam", "other", "country", 100))
print(t.add_team("OutdoorTeam", "otr", "country", 100))
