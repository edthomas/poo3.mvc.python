# -*- encoding: utf-8 -*-
DebuggerAtivo=True
Profundidade=''
''' Cada chamada de função decorada incrementa a profundidade '''
IncrementoDaProfundidade='  '

def Debugar(fn):
    ''''Mostra no terminal as chamadas de funções decoradas com @Debugar ''' 
    def f(*argt, **argd):
        global Profundidade, DebuggerAtivo
        if DebuggerAtivo:
            print Profundidade+'\033[1m==>\033[32m Entrando em %s\033[0m' % fn
        Profundidade += IncrementoDaProfundidade
        ret = fn(*argt, **argd)
        Profundidade = Profundidade[:-len(IncrementoDaProfundidade)]
        if DebuggerAtivo:
            print Profundidade+'\033[1m<==\033[34m Fim %s\033[0m' % fn
        return ret
    return f

