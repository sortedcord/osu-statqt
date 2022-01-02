#!/usr/bin/env python

import sys
import pyttanko as osu

p = osu.parser()
bmap = p.map('C:/d.osu')

stars = osu.diff_calc().calc(bmap)
print("%g stars" % stars.total)

pp, _, _, _, _ = osu.ppv2(stars.aim, stars.speed, bmap=bmap)
print("%g pp" % pp)