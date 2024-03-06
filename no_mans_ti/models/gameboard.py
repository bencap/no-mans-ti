from no_mans_ti.models.galaxy import Galaxy

TOP = "___________________"
BOTTOM = "___________________"
MIDDLE = ">----------------<"

class GameBoard:
    galaxy: Galaxy

    def __init__(self, galaxy: Galaxy) -> None:
        self.galaxy = galaxy

    def __str__(self) -> str:
        max_width = 33
        board_max_width = 189

        gb_str = ""
        idx = 0

        def buf_by_line(input: str, buf):
            return "\n".join([buf + s for s in input.split("\n")])
        
        def buf_and_pad_by_line(input: list[str], buf: str, pad: str):
            split_strs = [s.split("\n") for s in input]

            lines = []
            longest = max([len(s) for s in split_strs])
            for idx in range(longest):
                split_strs[0][idx] = buf + split_strs[0][idx]

                padded_line = ""
                for st in split_strs:
                    section = st[idx]
                    padded_line += section
                    additional_padding = 23 - len(padded_line)
                    padded_line += additional_padding * " "
                    padded_line += pad
                lines.append(padded_line)

            return "\n".join(lines)

        # XXX UGLY!!!
        for row in range(13):
            if row in (0,12):
                buf = " " * (board_max_width // 2)
                planet = self.galaxy.get(idx)
                idx+=1
                if planet:
                    gb_str += buf_by_line(planet.__compact_str__(), buf)
            elif row in (1, 11):
                buf = (" " * (board_max_width // 2))[:-max_width]
                pos1 = self.galaxy.get(idx)
                idx+=1
                pos2 = self.galaxy.get(idx)
                idx+=1
                if pos1 and pos2:
                    gb_str += buf_and_pad_by_line([pos1.__compact_str__(), pos2.__compact_str__()], buf, " " * max_width)
            elif row % 2 == 0:
                buf = (" " * (board_max_width // 2))[:-max_width-max_width]
                pos1 = self.galaxy.get(idx)
                idx+=1
                pos2 = self.galaxy.get(idx)
                idx+=1
                pos3 = self.galaxy.get(idx)
                idx+=1
                if pos1 and pos2 and pos3:
                    gb_str += buf_and_pad_by_line([pos1.__compact_str__(), pos2.__compact_str__(), pos3.__compact_str__()], buf, " " * max_width)
            elif row % 2 == 1:
                buf = (" " * (board_max_width // 2))[:-max_width-max_width-max_width]
                pos1 = self.galaxy.get(idx)
                idx+=1
                pos2 = self.galaxy.get(idx)
                idx+=1
                pos3 = self.galaxy.get(idx)
                idx+=1
                pos4 = self.galaxy.get(idx)
                idx+=1
                if pos1 and pos2 and pos3 and pos4:
                    gb_str += buf_and_pad_by_line([pos1.__compact_str__(), pos2.__compact_str__(), pos3.__compact_str__(), pos4.__compact_str__()], buf, " " * max_width)

            gb_str+="\n\n\n\n"
        return gb_str
    
    def export(self, fn: str) -> None:
        return
    

if __name__ == "__main__":
    gal = Galaxy()
    gal.randomize_galaxy()
    gb = GameBoard(gal)

    print(gb)