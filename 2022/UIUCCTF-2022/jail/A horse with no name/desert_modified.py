#!/usr/bin/python3
import re
import random
horse = "(abs(-1),)"

if re.match(r"[a-zA-Z]{4}", horse):
    print("4 letters", re.match(r"[a-zA-Z]{4}", horse))
    print("It has begun raining, so you return home.")

elif len(set(re.findall(r"[\W]", horse))) > 4:
    print("non words", set(re.findall(r"[\W]", horse)))
    print("A single horse cannot bear the weight of all those special characters. You return home.")

else:
    c = compile(horse, "<horse>", "eval")
    print("co_names:", c.co_names)
    c = c.replace(co_names=())
    e = eval(c)
    discovery = list(e)
    random.shuffle(discovery)
    print("You make it through the journey, but are severely dehydrated. This is all you can remember:", discovery)
