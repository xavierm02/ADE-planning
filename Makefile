default: all

all:

test:
	dev_appserver.py src

deploy:
	appcfg.py -A clean-trail-830 update src

.PHONY: default all test deploy
