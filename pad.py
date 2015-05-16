import sys
import json
import requests

from pprint import pprint as pp

from dataset import get_all_raw_data
from models import Pad

if __name__ == "__main__":
    pad = Pad(verbose=False)

    monster_id = int(sys.argv[1])
    m1 = pad.get_monster(monster_id)

    monsters = pad.get_all_monsters()

    pp(pad.get_evolution_tree(m1))
