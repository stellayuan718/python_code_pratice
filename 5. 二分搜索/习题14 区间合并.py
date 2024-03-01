

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[" + self.start + "," + self.end + "]"

    def __repr__(self):
        return "[%s, %s]" % (self.start, self.end)



def merge(intervals):
    intervals.sort(key=lambda x: x.start)

    merged = []
    for interval in intervals:
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.
        if not merged or merged[-1].end < interval.start:
            merged.append(interval)
        else:
        # otherwise, there is overlap, so we merge the current and previous
        # intervals.
            merged[-1].end = max(merged[-1].end, interval.end)

    return merged


i1 = Interval(1,3)
i2 = Interval(2,6)
i3 = Interval(8,10)
i4 = Interval(15,18)
intervals = [i1,i2,i3,i4]
print(merge(intervals))

i1 = Interval(1,9)
i2 = Interval(2,5)
i3 = Interval(19,20)
i4 = Interval(10,11)
i5 = Interval(12,20)
i6 = Interval(0,3)
i7 = Interval(0,1)
i8 = Interval(0,2)
intervals = [i1,i2,i3,i4,i5,i6,i7,i8]
print(merge(intervals))

intervals.sort(key=lambda x: x.start)
print(intervals)