'''demo for circle'''

import sys
import getopt
import circle  # pylint: disable=import-error,wrong-import-position

sys.path.insert(0, "..")


def main(argv):
    """Main function for circle code to process the file arguments """
    radius = 10
    try:
        opts, _args = getopt.getopt(argv, "r:", ["radius="])
    except getopt.GetoptError:
        print('demo -r <radius>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('demo -r <radius>')
            sys.exit()
        elif opt in ("-r", "--radius"):
            radius = arg
    if radius is None:
        print('demo -r <radius>')
    else:
        try:
            my_circle = circle.Circle(float(radius))
            print(my_circle.summary())
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


if __name__ == "__main__":
    main(sys.argv[1:])
