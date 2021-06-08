import argparse
parser = argparse.ArgumentParser()
parser.add_argument('Square',help='display the square of a given number',type=int)
parser.add_argument('-v','--verbosity',help='decide on how the output should look',action='count')
args = parser.parse_args()
answer = args.Square**2
if args.verbosity==1:
    print(f'The square of {args.Square} is equal to {answer}')
elif args.verbosity==2:
    print(f'The value of {args.Square}^2 is equal to {answer}')
else:
    print(answer)