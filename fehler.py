import sympy as sym


# Messgroessen: 'Variable': (Wert, stat_Fehler, syst_Fehler)
messgroessen = {
    'h_107': (0.5206033574481798, 0.009143772011737834, 0),
    'h_109': (0.4793966425518203, 0.009143772011737834, 0),
    'Z_108_m': (7328.748180429714, 135.36197889253683, 0),
    'Z_108_r': (7967.85020886897, 147.7239428724307, 0),
    'Z_110_m': (36346.38397421291, 1060.2240205277908, 0),
    'Z_110_r': (40967.32185647546, 1294.5673706646246, 0),
}


# Variableninitialisierung
for key in messgroessen.keys():
    exec("{0} = sym.Symbol('{0}')".format(key))

Ag = h_107 * (Z_108_m / Z_108_r) + h_109 * (Z_110_m / Z_110_r)

def fehler_berechnen(VarName, function, messgroessen):
    syst_fehler = 0
    stat_fehler = 0
    subs = []

    for key in messgroessen.keys():
        subs.append((key, messgroessen.get(key)[0]))

    Value = function.subs(subs)

    for val in messgroessen.keys():
        var = sym.Symbol(val)
        # print(var)
        # print(sym.diff(function, var))
        deriv = sym.diff(function, var).subs(subs)
        # print(deriv)
        # print(messgroessen.get(val)[1])
        # print()
        # print(messgroessen.get(key)[1]**2)
        stat_fehler += (deriv * messgroessen.get(val)[1])**2
        syst_fehler += (deriv * messgroessen.get(val)[2])**2
        # print(stat_fehler)
    syst_fehler = sym.sqrt(syst_fehler)
    stat_fehler = sym.sqrt(stat_fehler)


    fehler = {
        'Name': VarName,
        'Wert': Value,
        'stat': stat_fehler,
        'syst': syst_fehler
    }

    return fehler


print(fehler_berechnen("Silbergehalt", Ag, messgroessen))
