import argparse
c=argparse.ArgumentParser()
c.add_argument("num1", type=int)
c.add_argument("num2", type=int)
args = c.parse_args()
print(args.num1 + args.num2)
