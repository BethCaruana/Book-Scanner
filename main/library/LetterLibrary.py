from PIL import Image
import numpy as np

class LetterLibrary:
    def __init__(this, alphabet):
        this.alphabet = alphabet

    #smaller letters will have more white space (bigger number)
    def get_letter_number(this, image):
        image = Image.open(image)
        height, width = image.size
        #print(height, width)
        image = np.array(image)

        #count all no zeros in the image
        pixel = np.count_nonzero(image)
        total = image.size
    
        #return the percent of non-zero
        percentage = pixel/total
        percentage = round(percentage,4)
        return percentage

    def add_percentage(this, percentage):
        this.alphabet = np.append(this.alphabet, percentage)

    def fill_array(this):
        this.add_percentage(this.get_letter_number("library/A.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_a.jpeg"))
        this.add_percentage(this.get_letter_number("library/B.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_b.jpeg"))
        this.add_percentage(this.get_letter_number("library/C.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_c.jpeg"))
        this.add_percentage(this.get_letter_number("library/D.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_d.jpeg"))
        this.add_percentage(this.get_letter_number("library/E.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_e.jpeg"))
        this.add_percentage(this.get_letter_number("library/F.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_f.jpeg"))
        this.add_percentage(this.get_letter_number("library/G.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_g.jpeg"))
        this.add_percentage(this.get_letter_number("library/H.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_h.jpeg"))
        this.add_percentage(this.get_letter_number("library/I.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_i.jpeg"))
        this.add_percentage(this.get_letter_number("library/J.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_j.jpeg"))
        this.add_percentage(this.get_letter_number("library/K.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_k.jpeg"))
        this.add_percentage(this.get_letter_number("library/L.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_l.jpeg"))
        this.add_percentage(this.get_letter_number("library/M.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_m.jpeg"))
        this.add_percentage(this.get_letter_number("library/N.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_n.jpeg"))
        this.add_percentage(this.get_letter_number("library/O.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_o.jpeg"))
        this.add_percentage(this.get_letter_number("library/P.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_p.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_m.jpeg"))
        this.add_percentage(this.get_letter_number("library/Q.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_q.jpeg"))
        this.add_percentage(this.get_letter_number("library/R.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_r.jpeg"))
        this.add_percentage(this.get_letter_number("library/S.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_s.jpeg"))
        this.add_percentage(this.get_letter_number("library/T.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_t.jpeg"))
        this.add_percentage(this.get_letter_number("library/U.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_u.jpeg"))
        this.add_percentage(this.get_letter_number("library/V.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_v.jpeg"))
        this.add_percentage(this.get_letter_number("library/W.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_w.jpeg"))
        this.add_percentage(this.get_letter_number("library/X.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_x.jpeg"))
        this.add_percentage(this.get_letter_number("library/Y.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_y.jpeg"))
        this.add_percentage(this.get_letter_number("library/Z.jpeg"))
        this.add_percentage(this.get_letter_number("library/little_z.jpeg"))


def main():
    library = LetterLibrary(alphabet=[])
    library.fill_array()
    print(library.alphabet)
    print(library.alphabet.min())
    print(library.alphabet.max())

main()




