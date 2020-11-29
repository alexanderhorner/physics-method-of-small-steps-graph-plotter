from matplotlib import pyplot
import subprocess as sp


class DataPoint:
  def __init__(self, t, v, s):
    self.t = t
    self.v = v
    self.s = s


sp.call('clear', shell=True)

class Calculation:
    def __init__(self):
        self.step_size = float(input("Schrittgröße (Dt in s): "))
        self.acceleration = float(input("Beschleunigung (a in m/s^2): "))
        self.step_ammount = int(input("Wie viele Schritte sollen gemacht werden: "))
        self.calculations = []


    def calculate_data(self):
        self.calculations.append(DataPoint(0, 0, 0)) # start with 0

        n = 0

        # Iterate 
        while n < self.step_ammount:
            # Calculate new data
            new_t = self.calculations[-1].t + self.step_size
            new_v = self.calculations[-1].v + self.acceleration * self.step_size
            new_s = self.calculations[-1].s + new_v * self.step_size

            # append new data
            self.calculations.append(DataPoint(new_t, new_v, new_s))

            n += 1

    def print_data(self):
        if (self.calculations == []):
            self.calculate_data()

        print('')
        print("| Zeit    | Geschw.    | Distanz  |")

        for row in self.calculations:
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

    def plot_graph(self):
        if (self.calculations == []):
            self.calculate_data()

        # Convert data for graph
        x = []
        y = []
        for row in self.calculations:
            x.append(row.t)
            y.append(row.s)


        # plot graph
        pyplot.plot(x, y, 'ro')
        pyplot.plot(x, y, 'b-')
        pyplot.xlabel('Distanz (s)')
        pyplot.ylabel('Zeit (t)')
        pyplot.show()

calc1 = Calculation()
calc1.print_data()
calc1.plot_graph()