class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[" + self.start + "," + self.end + "]"

    def __repr__(self):
        return "[%s, %s]" % (self.start, self.end)




def insert(intervals, newInterval):
    merged = []
    for i in intervals:
        if newInterval is None or i.end < newInterval.start:
            merged += i,
        elif i.start > newInterval.end:
            merged += newInterval,
            merged += i,
            newInterval = None
        else:
            newInterval.start = min(newInterval.start, i.start)
            newInterval.end = max(newInterval.end, i.end)

    if newInterval is not None:
        merged += newInterval

    return merged




i1 = Interval(1, 3)
i2 = Interval(6, 9)
intervals = [i1, i2]
new = Interval(2, 5)
a = insert(intervals, new)
print(a)


def insert2(intervals, newInterval):
    left, right = [], []
    for i in intervals:
        if i.end < newInterval.start:
            left += i,
        elif i.start > newInterval.end:
            right += i,
        else:
            newInterval.start = min(newInterval.start, i.start)
            newInterval.end = max(newInterval.end, i.end)
    return left + [Interval(newInterval.start, newInterval.end)] + right

i1 = Interval(1,2)
i2 = Interval(3,5)
i3 = Interval(6,7)
i4 = Interval(8,10)
i5 = Interval(12,16)
intervals = [i1,i2,i3,i4,i5]
new = Interval(4,8)
b = insert2(intervals, new)
print(b)


def insert3(intervals, newInterval):
    if len(intervals) == 0:
        intervals += newInterval,

    startPos = searchPosition(intervals, newInterval.start)
    endPos = searchPosition(intervals, newInterval.end)

    newStart = 0

    # case 1:
    # startPos
    #           A
    # |____|    |____|    |____|
    #         <-
    #           startPos is less than A
    # and intervals[startPos].end >= newInterval.start
    # then
    #   new     A
    # |____|    |____|    |____|
    #     <-
    # newInterval starts within ONE interval
    # so newStart = intervals[startPos].start
    if (startPos >= 0 and intervals[startPos].end >= newInterval.start):
        newStart = intervals[startPos].start
    else:
        # case 2:
        # startPos = -1
        # A
        # |____|    |____|    |____|
        # newInterval starts before 1st interval
        # so newStart = newInterval.start

        # case 3:
        # startPos >= 0
        # A    B
        # |____|    |____|    |____|
        # newInterval starts between A and B
        # so NOT intervals[startPos].end >= newInterval.start
        # so newStart = newInterval.start
        newStart = newInterval.start
        startPos += 1

    newEnd = 0
    # case 1:
    # endPos >= 0
    # endPos
    #           A
    # |____|    |____|    |____|
    #         <-
    #           endPos is less than A
    # so newEnd = Math.max(newInterval.end, intervals.get(endPos).end)
    if (endPos >= 0):
        newEnd = max(newInterval.end, intervals[endPos].end)
    else:
        # case 2:
        # endPos < 0
        # endPos
        # A
        #     |____|    |____|    |____|
        #
        # endPos is before 1st interval
        # create a new interval
        newEnd = newInterval.end

    for i in range(startPos, endPos + 1):
        intervals.pop(startPos)  # note: NOT i, but startPos, since one element is removed.

    intervals.insert(startPos, Interval(newStart, newEnd))
    return intervals


# return (actual insertion position - 1)
def searchPosition(intervals, x):
    start = 0
    end = len(intervals) - 1
    while (start <= end):
        mid = start + (end - start) // 2
        if (intervals[mid].start == x):
            return mid
        if (intervals[mid].start < x):
            start = mid + 1
        else:
            end = mid - 1

    return end
