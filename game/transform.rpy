transform idle:
    ease 2.0 yoffset 3
    ease 2.0 yoffset 0
    repeat

transform silhouette_in(duration=1.0):
    matrixcolor TintMatrix("#000000")
    ease duration matrixcolor TintMatrix("#ffffff")

transform take:
    ease 0.2 yoffset 40
    pause 0.2
    ease 0.5 yoffset -5
    ease 0.1 yoffset 0

transform jump(times=5):
    ease 0.2 yoffset -60
    pause 0.1
    ease 0.1 yoffset 5
    pause 0.1
    ease 0.2 yoffset 0
