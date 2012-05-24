#!/usr/bin/python2
# -*- encoding: utf-8 -*-
import controller
from model import Cd

if __name__ == "__main__":
    ##print "==> Iniciando"
    model = Cd('artist', 'album', 'year')
    model.createDatabase()
    try:
        controller.Controller().main()
    except KeyboardInterrupt, e:
        pass

