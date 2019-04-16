import sympy as sym

messgroessen = {
    "x": (x_val, x_stat, x_syst)
}

def fehler_berechnen(name, function, messgroessen):
    syst_fehler = 0
    stat_fehler = 0
    for val in messgroessen.keys():
        var = sym.Symbol(val)
        deriv = sym.diff(function, var)
