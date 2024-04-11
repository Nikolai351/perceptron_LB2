from random import random


class Perceptron:
    def __init__(self):

        self.v = {
            '01': 'A',
            '10': 'B',
        }

        self.patterns = [
            [
                0, 0, 0, 1, 1, 0, 0, 0,
                0, 0, 0, 1, 1, 0, 0, 0,
                0, 0, 1, 0, 0, 1, 0, 0,
                0, 0, 1, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 0, 1, 0,
                0, 1, 1, 1, 1, 1, 1, 0,
                1, 0, 0, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 0, 0, 1,
            ],
            [
                1, 1, 1, 1, 1, 1, 1, 0,
                1, 1, 0, 0, 0, 0, 0, 1,
                1, 1, 0, 0, 0, 0, 0, 1,
                1, 1, 1, 1, 1, 1, 1, 0,
                1, 1, 1, 1, 1, 1, 1, 0,
                1, 1, 0, 0, 0, 0, 0, 1,
                1, 1, 0, 0, 0, 0, 0, 1,
                1, 1, 1, 1, 1, 1, 1, 0,
            ]
                        ]

        self.broken = [
            [
                0, 0, 1, 1, 1, 1, 0, 0,
                0, 1, 0, 0, 0, 0, 1, 0,
                1, 0, 0, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 0, 0, 1,
                1, 1, 1, 1, 1, 1, 1, 1,
                1, 0, 0, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 0, 0, 1,
            ],
            [
                1, 1, 1, 1, 1, 1, 1, 0,
                1, 0, 0, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 0, 1, 0,
                1, 1, 1, 1, 1, 1, 1, 0,
                1, 0, 0, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 0, 0, 1,
                1, 1, 1, 1, 1, 1, 1, 0,
            ]
        ]

        self.answers = [
            [0, 1],
            [1, 0]
        ]

        self.neurons = [0 for _ in range(len(self.answers[0]))]

        self.synapses = [[random() * 0.2 + 0.0001 for _ in range(len(self.patterns[0]))]
                         for _ in range(len(self.neurons))]

        self.enters = []

    def count_neuron(self):
        for i, _ in enumerate(self.neurons):
            self.neurons[i] = 0
            for j, enter in enumerate(self.enters):
                self.neurons[i] += self.synapses[i][j] * enter
            self.neurons[i] = 1 if self.neurons[i] > 0.5 else 0

    def study(self):
        g_error = 1
        step = 0
        while g_error > 0:
            step += 1
            g_error = 0
            for i, pattern in enumerate(self.patterns):
                self.enters = pattern
                self.count_neuron()
                l_error = []
                for n, _ in enumerate(self.neurons):
                    local_error = self.answers[i][n] - self.neurons[n]
                    l_error.append(local_error)

                    g_error += abs(local_error)

                for n, _ in enumerate(self.neurons):
                    for j in range((len(self.enters))):
                        self.synapses[n][j] += 0.1 * l_error[n] * self.enters[j]
        return step


def main():
    p = Perceptron()
    print(p.study())

    for _, pattern in enumerate(p.patterns):
        p.enters = pattern
        p.count_neuron()
        print(p.v.get(''.join(str(n) for n in p.neurons), 'Буква не распознана!'))


if __name__ == '__main__':
    main()

