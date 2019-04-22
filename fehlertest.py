from fehler import error_calc

# Messgroessen: 'Variable': (Wert, stat_Fehler, syst_Fehler)
messgroessen = {
    'x': (10, 3, 2),
    'y': (6, 1, 2)
}

Ag = "x / (x + y)"

error_calc("Silbergehalt", Ag, messgroessen)
