import argparse

def main(args):
    # 在这里编写你的代码
    print("Hello, " + args.name + "!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="the name to greet")
    args = parser.parse_args()
    main(args)

