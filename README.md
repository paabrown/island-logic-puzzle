WIP

See https://xkcd.com/blue_eyes.html

Run using play.sh - requires python3 to be installed and accessible by the command "python3".

I'm not actually 100% satisfied with the code - specifically the code for the "is_imagined_universe_valid" in the "everyone_sees_eachother" phase seems wrong to me - though coincidentally it happens to work properly as it is being used here. But I'm being lazy and can always work on this later.

--

Basically the way it works is - each person on the island is called a meeple. Each meeple imagines/simulates all the possible universes in which they do not have blue eyes. They then compare what happens in those simulations (eg how many people leave the island) compared to how many people they see leaving the island around them. If those differ, they invalidate the possible universes they are imagining (these imagined universes also recursively have imaginary meeple doing the same thing). If they have no remaining universes in which they don't have blue eyes, they leave the island.

The reason I only simulate universes in which they don't have blue eyes is to avoid infinite recursion.

I also don't simulate any meeple without blue eyes. I think it would be nicer and possible to include them, but I left them out for now to make it easier on myself to work on this.
