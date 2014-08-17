work = {1,1, "ok"}
print work
print 1 in work
print type(work)
lazy = {True, False, True, not True}
print lazy
print work.union(lazy)
print lazy | work
print work.union == lazy | work
print work | lazy == work.intersection(lazy)
work = lazy
work.clear()
print work, lazy
