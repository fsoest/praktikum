import sympy as sym


def fehler_berechnen(VarName, function_str, messgroessen):
    syst_fehler = 0
    stat_fehler = 0
    subs = []

    # Variableninitialisierung
    for key in messgroessen.keys():
        exec("{0} = sym.Symbol('{0}')".format(key))
        subs.append((key, messgroessen.get(key)[0]))

    function = eval(function_str)
    Value = function.subs(subs)

    for val in messgroessen.keys():
        var = sym.Symbol(val)
        deriv = sym.diff(function, var).subs(subs)
        stat_fehler += (deriv * messgroessen.get(val)[1])**2
        syst_fehler += (deriv * messgroessen.get(val)[2])**2
    syst_fehler = sym.sqrt(syst_fehler)
    stat_fehler = sym.sqrt(stat_fehler)

    fehler = {
        'Name': VarName,
        'Wert': Value,
        'stat': stat_fehler,
        'syst': syst_fehler
    }

    return fehler
