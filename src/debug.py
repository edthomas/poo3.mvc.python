# -*- encoding: utf-8 -*-

DebuggerAtivo=False

def Debugar(fn):
    global DebuggerAtivo
    import inspect
    varList, _, _, default = inspect.getargspec(fn)
    d = {}
    if default is not None:
        d = dict((varList[-len(default):][i], v) for i, v in enumerate(default))
    def f(*argt, **argd):
        if DebuggerAtivo:
            print ('\033[1;32mEntrando em %s\033[0m' % fn).center(100, '=')
            print d
        ret = fn(*argt, **argd)
        if DebuggerAtivo:
            try:
                print 'Retorno: %s' % ret
            except:
                pass
            print ('\033[1;34mExit %s\033[0m' % fn).center(100, '=')
        return ret
    return f

