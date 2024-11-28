"""
Suite de Syracuce
"""

#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Code du professeur
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    # votre code ici
    l = []
    ind = 0
    l.insert(0,n)
    while n != 1:
        ind = ind + 1
        if n%2 == 0:
            n = n // 2
            l.insert(ind, n)
        else:
            n = n*3 +1
            l.insert(ind,n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    # votre code ici
    n = len(l) - 1
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    nb = l[0]
    tva = len(l)-1
    n=0
    for i in range (0,tva):
        n=i
        if l[i] < nb:
            return n-1
    return 0


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    # votre code ici
    n = max(l)

    return n


#### Fonction principale


def main():
    """
    Fonction main
    """

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
