all: npm site

npm:
	npm install

site:
	python3 get_environment.py;kiln build

clean:
	rm -r ./public/*

publish: all
	tar -C public -cvz . > site.tar.gz

.PHONY: all npm site clean publish
