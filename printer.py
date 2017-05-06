
class PsychPrinter:
    def __init__(self):
        self._NUM_SPACES = 45
        pass


    def _get_spacing(self, rank, name, time):
        return " " * (self._NUM_SPACES \
                - len(rank) - len(name) - len(time.text))


    def print_psych(self, event, psych):
        print("EVENT: " + event)

        for i, competitor in enumerate(psych):
            rank = str(i + 1)
            name = competitor["name"]
            time = competitor["time"]
            spacing = self._get_spacing(rank, name, time)
            print(rank + ". " + name + spacing + time.text)

        print()