from fehler import error_calc


# Messgroessen: 'Variable': (Wert, stat_Fehler, syst_Fehler)
measurements = {
    'x_r': (80, 0, 0.3, 'mm'),
    'T': (295.75, 0, 0.5, 'K'),
    'p': (499.05483, 1.12423, 3, 'mbar'),
    'T_n': (293.15, 0, 0, 'K'),
    'p_n': (1013, 0, 0, 'mbar'),
    'R': (39.0655506251695, 0.0880036848442771, 0.284554869139582),
}

R = 'T_n * p * x_r / ( p_n * T)'
E = '(R/3.1)**(2/3)'



error_calc("Average range", R, measurements)
error_calc("Average energy", E, measurements)
