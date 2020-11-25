from matplotlib import pyplot

class DataPoint:
  def __init__(self, t, v, s):
    self.t = t
    self.v = v
    self.s = s



# Get settings
step_size = float(input("Schrittgröße (Dt in s): "))
acceleration = float(input("Beschleunigung (a in m/s^2): "))
step_ammount = int(input("Wie viele Schritte sollen gemacht werden: "))

# Calculate data
calculations = []
calculations.append(DataPoint(0, 0, 0)) # start with 0

n = 0

# Iterate 
while n <= step_ammount:
    # Calculate new data
    new_t = calculations[-1].t + step_size
    new_v = calculations[-1].v + acceleration * step_size
    new_s = calculations[-1].s + new_v * step_size

    # append new data
    calculations.append(DataPoint(new_t, new_v, new_s))

    n += 1

# print
print('')

print("| Zeit    | Geschw.    | Distanz  |")
for row in calculations:
    text_t = str(round(row.t, 2)) + "s"
    while len(text_t) < 8:
        text_t += " "

    text_v = str(round(row.v, 2)) + "m/s"
    while len(text_v) < 11:
        text_v += " "

    text_s = str(round(row.s, 2)) + "m"
    while len(text_s) < 9:
        text_s += " "
    print("| " + text_t + "| " + text_v + "| " + text_s + "|")

# Convert data for graph
x = []
y = []
for row in calculations:
    x.append(row.t)
    y.append(row.s)


# plot graph
pyplot.plot(x, y, 'ro')
pyplot.plot(x, y, 'b-')
pyplot.xlabel('Distanz (s)')
pyplot.ylabel('Zeit (t)')
pyplot.show()