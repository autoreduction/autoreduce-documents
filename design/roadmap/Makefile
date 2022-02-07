%.pdf: %.md
	pandoc -f markdown -t pdf "$<" -o "$@"

all: autoreduction_roadmap.pdf

clean:
	rm -f autoreduction_roadmap.pdf
