import universe

Universe = universe.Universe


class Meeple:
    def __init__(self, containing_universe):
        self.containing_universe = containing_universe
        self.imagined_safe_universes = []

        self.imagined_safe_universes.append(
            Universe(num_blue_eyed=containing_universe.num_blue_eyed - 1)
        )

    def check_imagined_universes_against_containing(self):
        return self.invalidate_imagined_universes(
            lambda u, m: is_imagined_universe_valid(u, m.containing_u)
        )

    def invalidate_imagined_universes(self, validator):
        initial_num_universes = len(self.imagined_safe_universes)

        self.imagined_safe_universes = [
            u for u in self.imagined_safe_universes
            if validator(
                imagined_u=u,
                meeple=self,
            )
        ]

        for u in self.imagined_safe_universes:
            u.invalidate_imagined_universes(validator)

        return initial_num_universes - len(self.imagined_safe_universes)

    def imagine_meeple_leaving(self):
        for u in self.imagined_safe_universes:
            u.have_meeple_leave()

    def should_self_stay(self):
        return bool(self.imagined_safe_universes)


def is_imagined_universe_valid(self, imagined_u, containing_u):
    return abs(imagined_u - containing_u) <= 1
