import sympy as sym

x_val = 1
x_stat = 1
x_syst = 0

# Messgroessen: 'Variable': (Wert, stat_Fehler, syst_Fehler)

messgroessen = {
    'x': (x_val, x_syst, x_stat),
    'y': (3, 0, 1)
}


# Variableninitialisierung
for key in messgroessen.keys():
    exec("{0} = sym.Symbol('{0}')".format(key))


def fehler_berechnen(name, function, messgroessen):
    syst_fehler = 0
    stat_fehler = 0
    subs = []
    for key in messgroessen.keys():
        subs.append((key, messgroessen.get(key)[0]))
    for val in messgroessen.keys():
        var = sym.Symbol(val)
        print(sym.diff(function, var))
        deriv = sym.diff(function, var).subs(subs)
        print(deriv)
        syst_fehler += deriv**2 * messgroessen.get(key)[1]**2
        stat_fehler += deriv**2 * messgroessen.get(key)[2]**2
    syst_fehler = sym.sqrt(syst_fehler)
    stat_fehler = sym.sqrt(stat_fehler)

    return (syst_fehler, stat_fehler)

fehler_berechnen("Test", x**2 + x**3*y, messgroessen)
