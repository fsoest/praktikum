import sympy as sym


def error_calc(var_name, function_str, measurement):
    syst_error = 0
    stat_error = 0
    subs = []

    # Variableninitialisierung
    for key in measurement.keys():
        exec("{0} = sym.Symbol('{0}')".format(key))
        subs.append((key, measurement.get(key)[0]))

    # Berechnung Funktionswert
    function = eval(function_str)
    value = function.subs(subs)

    # Gausssche Fehlerfortpflanzung
    for val in measurement.keys():
        var = sym.Symbol(val)
        deriv = sym.diff(function, var).subs(subs)
        stat_error += (deriv * measurement.get(val)[1])**2
        syst_error += (deriv * measurement.get(val)[2])**2
    syst_error = sym.sqrt(syst_error)
    stat_error = sym.sqrt(stat_error)
    stat_rel = stat_error / value * 100
    syst_rel = syst_error / value * 100

    error = {
        'Name': var_name,
        'Value': value.evalf(),
        'stat': stat_error.evalf(),
        'stat_rel [%]': stat_rel.evalf(),
        'syst': syst_error.evalf(),
        'syst_rel [%]': syst_rel.evalf(),
    }

    for key in error.keys():
        print('{0}: {1}'.format(key, error.get(key)))
        print()
