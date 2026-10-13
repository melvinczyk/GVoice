import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int)
    parser.add_argument("-hs", "--host", default="0.0.0.0")
    parser.add_argument("-pl", "--preload", action="store_true")

    args = parser.parse_args()

    port = args.port
    host = args.host
    preload = args.preload
    print(port)