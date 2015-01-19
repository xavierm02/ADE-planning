default: all

all:

test:
	dev_appserver.py src

deploy:
	appcfg.py -A clean-trail-830 update appengine-try-python

.PHONY: default all test deploy
