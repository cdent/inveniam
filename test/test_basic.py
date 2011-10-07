from inveniam import Topospace

def test_2d_topo():
    t = Topospace()
    t.append((1.0, 1.0))
    t.append((1.0, 2.0))
    assert len(t) == 2
    assert t.nearest((0.0, 0.0)) == [((1.0, 1.0), 2.0)]
    assert t.nearest((0.0, 0.0), count=2) == [((1.0, 1.0), 2.0), ((1.0, 2.0), 5.0)]

def test_3d_topo():
    t = Topospace()
    t.append((1.0, 1.0, 1.0))
    t.append((1.0, 2.0, 2.0))
    t.append((2.0, 2.0, 2.0))
    assert len(t) == 3
    assert t.nearest((0.0, 0.0, 0.0)) == [((1.0, 1.0, 1.0), 3.0)]
