import mdtohtml, index, sys

def main():
    if len(sys.argv) == 2:
        mdtohtml.mdtohtml(md_path=sys.argv[1])
    elif len(sys.argv) > 2:
        sys.exit("usage: mdc optional[<markdown_file>]")
    index.make_index()

if __name__ == "__main__":
    main()