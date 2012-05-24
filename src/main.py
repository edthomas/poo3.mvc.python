#!/usr/bin/python2
# -*- encoding: utf-8 -*-
import controller
from model import Cd

if __name__ == "__main__":
    model = Cd(artist='artist', album='album', year='year')
    model.createDatabase()
    try:
        app = controller.Controller()
        print "Iniciando aplicação."
        app.main()
    except KeyboardInterrupt, e:
        pass

