from fehler import fehler_berechnen

# Messgroessen: 'Variable': (Wert, stat_Fehler, syst_Fehler)
messgroessen = {
    'h_107': (0.5206033574481798, 0.009143772011737834, 0),
    'h_109': (0.4793966425518203, 0.009143772011737834, 0),
    'Z_108_m': (7328.748180429714, 135.36197889253683, 0),
    'Z_108_r': (7967.85020886897, 147.7239428724307, 0),
    'Z_110_m': (36346.38397421291, 1060.2240205277908, 0),
    'Z_110_r': (40967.32185647546, 1294.5673706646246, 0),
}

Ag = "h_107 * (Z_108_m / Z_108_r) + h_109 * (Z_110_m / Z_110_r)"

print(fehler_berechnen("Silbergehalt", Ag, messgroessen))
