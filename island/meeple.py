class Meeple:
    def __init__(self, containing_universe):
        self.containing_universe = containing_universe
        self.imagined_safe_universes = []

        blue_eyed_for_imagined = len(containing_universe.blue_eyed_meeple) - 1
        if blue_eyed_for_imagined >= 0:
            self.imagined_safe_universes.append(
                island.universe.Universe(
                    num_blue_eyed=blue_eyed_for_imagined,
                )
            )

    def check_imagined_universes_against_containing(self):
        return self.invalidate_imagined_universes(
            lambda u, m: is_imagined_universe_valid(u, m.containing_universe)
        )

    def invalidate_imagined_universes(self, validator):
        initial_num_universes = len(self.imagined_safe_universes)

        self.imagined_safe_universes = [
            u for u in self.imagined_safe_universes
            if validator(
                u=u,
                m=self,
            )
        ]

        for u in self.imagined_safe_universes:
            u.invalidate_imagined_universes(validator)

        return initial_num_universes - len(self.imagined_safe_universes)

    def imagine_meeple_leaving(self):
        for u in self.imagined_safe_universes:
            u.leave_phase()

    def should_self_stay(self):
        return bool(self.imagined_safe_universes)


def is_imagined_universe_valid(imagined_u, containing_u):

    return abs(
        len(imagined_u.blue_eyed_meeple)
        - len(containing_u.blue_eyed_meeple)) <= 1


import island.universe
