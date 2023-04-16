def questions():
    while True:
        tags = ("16 bit","8 bit","64 bit","aaa","aa","2d","3d",
                "action","adventure","atmospheric","battle royale","beat em up",
                "city builder","classes","collectathon","comedy","competitive","cyberpunk","detective","fantasy",
                "first person","futuristic","horror","jumpscares","indie","linear","lore rich","metroidvania","mission based","moddable",
                "mmo","nostalgia","open world","platformer","point and click","post apocalypse","puzzle","rhythm",
                "roguelike","role playing","sandbox","scifi","shooter","shoot em up","side scroller","space"
                "stealth","survival","tactical","third person","turn based","walking simulator","zombies"
        )
        input_tags = input("input tags: ")
        if input_tags in tags:
            print("true")
questions()