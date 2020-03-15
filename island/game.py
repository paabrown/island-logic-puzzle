import island.universe

Universe = island.universe.Universe


class Game:
    def __init__(self, num_blue_eyed):
        self.day = 0
        self.base_universe = Universe(num_blue_eyed=num_blue_eyed)

    def run_guru(self):
        self.base_universe.invalidate_imagined_universes(
            lambda u, m: len(u.blue_eyed_meeple) != 0
        )

    def advance_one_day(self):
        num_left = self.base_universe.leave_phase()
        self.base_universe.everyone_sees_eachother_phase()

        self.day += 1

        return num_left
