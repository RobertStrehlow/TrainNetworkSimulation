# Create Train stations
from src.stations import TrainStation

WIDTH, HEIGHT = 1600, 900

#s2 lines
blankenfelde = TrainStation("Blankenfelde", int(WIDTH * 0.5), int(HEIGHT * 0.95))
mahlow = TrainStation("Mahlow", int(WIDTH * 0.5), int(HEIGHT * 0.9))
lichtenrade = TrainStation("Lichtenrade", int(WIDTH * 0.5), int(HEIGHT * 0.85))
schichaueweg = TrainStation("Schichauweg", int(WIDTH * 0.5), int(HEIGHT * 0.8))
buckower_chaussee = TrainStation("Buckower Chaussee", int(WIDTH * 0.5), int(HEIGHT * 0.75))
marienfelde = TrainStation("Marienfelde", int(WIDTH * 0.5), int(HEIGHT * 0.7))
attilastrasse = TrainStation("Attilastraße", int(WIDTH * 0.45), int(HEIGHT * 0.65))
priesterweg = TrainStation("Priesterweg", int(WIDTH * 0.4), int(HEIGHT * 0.6))
suedkreuz = TrainStation("Südkreuz", int(WIDTH * 0.4), int(HEIGHT * 0.55))
yorckstr = TrainStation("Yorckstraße", int(WIDTH * 0.4), int(HEIGHT * 0.5))
anhalter_bahnhof = TrainStation("Anhalter Bahnhof", int(WIDTH * 0.4), int(HEIGHT * 0.45))
potsdamer_platz = TrainStation("Potsdamer Platz", int(WIDTH * 0.4), int(HEIGHT * 0.4))

suedende = TrainStation("Südende", int(WIDTH * 0.35), int(HEIGHT * 0.65))
lankwitz = TrainStation("Lankwitz", int(WIDTH * 0.3), int(HEIGHT * 0.7))
lichterfelde_ost = TrainStation("Lichterfelde Ost", int(WIDTH * 0.25), int(HEIGHT * 0.75))
osdorfer_str = TrainStation("Osdorfer Str.", int(WIDTH * 0.2), int(HEIGHT * 0.8))
lichterfelde_sued = TrainStation("Lichterfelde Süd", int(WIDTH * 0.15), int(HEIGHT * 0.85))
teltow_stadt = TrainStation("Teltow Stadt", int(WIDTH * 0.1), int(HEIGHT * 0.9))