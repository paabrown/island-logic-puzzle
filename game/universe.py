import meeple

Meeple = meeple.Meeple


class Universe:
    def __init__(self, num_blue_eyed):
        self.day = 0
        # ignore meeple with brown eyes for now
        self.num_blue_eyed = num_blue_eyed
        self.blue_eyed_meeple = []

        for i in range(num_blue_eyed):
            self.meeple.append(Meeple(
                containing_universe=self,
            ))

    def invalidate_imagined_universes(self, validator):
        for m in self.blue_eyed_meeple:
            m.invalidate_imagined_universes(validator)

    def leave_phase(self):
        initial_meeple = len(self.blue_eyed_meeple)

        self.blue_eyed_meeple = [
            m for m in self.blue_eyed_meeple
            if m.should_self_stay()
        ]

        for m in self.blue_eyed_meeple:
            m.imagine_meeple_leaving()

        return initial_meeple - len(self.blue_eyed_meeple)

    def everyone_sees_eachother_phase(self):
        for m in self.blue_eyed_meeple:
            m.check_imagined_universes_against_containing()
